from collections import OrderedDict as OD

# file generated at 2020-08-24 20:06:04 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_hh.py -M

samples_2016 = OD()
samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 3.00004312e+05, 2.99995000e+05, 3.00045562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.05752375e+05, 3.00003969e+05, 2.92733281e+05, 3.05752375e+05, 3.00003969e+05, 2.92733281e+05, 3.05752375e+05, 3.00003969e+05, 2.92733281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.05752375e+05, 2.92733281e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.95862438e+05, 2.95851594e+05, 2.95897906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.95862438e+05, 2.94761375e+05, 2.96959375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01502969e+05, 2.95860938e+05, 2.88717438e+05, 3.01502969e+05, 2.95860938e+05, 2.88717438e+05, 3.01502969e+05, 2.95860938e+05, 2.88717438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01502969e+05, 2.88717438e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1053951813), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        11821300223), # 11.82GB, avg file size 2.96GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 294629, ],
    'CountWeighted'                                                                  : [ 2.94641469e+05, 2.94645906e+05, 2.94623750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.01126781e+05, 2.94639000e+05, 2.86779750e+05, 3.01126781e+05, 2.94639000e+05, 2.86779750e+05, 3.01126781e+05, 2.94639000e+05, 2.86779750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.01126781e+05, 2.86779750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90404500e+05, 2.90402156e+05, 2.90404219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90404500e+05, 2.89281719e+05, 2.91520438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.96771500e+05, 2.90401719e+05, 2.82689875e+05, 2.96771500e+05, 2.90401719e+05, 2.82689875e+05, 2.96771500e+05, 2.90401719e+05, 2.82689875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.96771500e+05, 2.82689875e+05, ],
  }),
  ("nof_tree_events",                 294629),
  ("nof_db_events",                   294629),
  ("fsize_local",                     1050428693), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        11694604529), # 11.69GB, avg file size 3.90GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99984219e+05, 2.99961438e+05, 3.00055781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08987844e+05, 2.99982750e+05, 2.90127500e+05, 3.08987844e+05, 2.99982750e+05, 2.90127500e+05, 3.08987844e+05, 2.99982750e+05, 2.90127500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08987844e+05, 2.90127500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.95358656e+05, 2.95339250e+05, 2.95414094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.95358656e+05, 2.94145344e+05, 2.96569000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.04182062e+05, 2.95356438e+05, 2.85679875e+05, 3.04182062e+05, 2.95356438e+05, 2.85679875e+05, 3.04182062e+05, 2.95356438e+05, 2.85679875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.04182062e+05, 2.85679875e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1115424215), # 1.12GB, avg file size 1.12GB
  ("fsize_db",                        12121761327), # 12.12GB, avg file size 3.03GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 295149, ],
    'CountWeighted'                                                                  : [ 2.95268000e+05, 2.95216344e+05, 2.95146438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.07329531e+05, 2.95247250e+05, 2.82815000e+05, 3.07329531e+05, 2.95247250e+05, 2.82815000e+05, 3.07329531e+05, 2.95247250e+05, 2.82815000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.07329531e+05, 2.82815000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90106719e+05, 2.90070750e+05, 2.90036281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90106719e+05, 2.88786750e+05, 2.91418594e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01960719e+05, 2.90093125e+05, 2.77947188e+05, 3.01960719e+05, 2.90093125e+05, 2.77947188e+05, 3.01960719e+05, 2.90093125e+05, 2.77947188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01960719e+05, 2.77947188e+05, ],
  }),
  ("nof_tree_events",                 295149),
  ("nof_db_events",                   295149),
  ("fsize_local",                     1165045302), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        12270587874), # 12.27GB, avg file size 2.45GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 3.00073906e+05, 2.99992969e+05, 3.00004125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15263062e+05, 3.00072094e+05, 2.85212906e+05, 3.15263062e+05, 3.00072094e+05, 2.85212906e+05, 3.15263062e+05, 3.00072094e+05, 2.85212906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15263062e+05, 2.85212906e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94387094e+05, 2.94336656e+05, 2.94357500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94387094e+05, 2.92946312e+05, 2.95825250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.09274875e+05, 2.94384312e+05, 2.79874625e+05, 3.09274875e+05, 2.94384312e+05, 2.79874625e+05, 3.09274875e+05, 2.94384312e+05, 2.79874625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.09274875e+05, 2.79874625e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1242562416), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        12763369067), # 12.76GB, avg file size 3.19GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 296256, ],
    'CountWeighted'                                                                  : [ 2.96242156e+05, 2.96282156e+05, 2.96272312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.13768094e+05, 2.96240062e+05, 2.79794219e+05, 3.13768094e+05, 2.96240062e+05, 2.79794219e+05, 3.13768094e+05, 2.96240062e+05, 2.79794219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.13768094e+05, 2.79794219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90340344e+05, 2.90359781e+05, 2.90358188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90340344e+05, 2.88850781e+05, 2.91824906e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.07458469e+05, 2.90337125e+05, 2.74248719e+05, 3.07458469e+05, 2.90337125e+05, 2.74248719e+05, 3.07458469e+05, 2.90337125e+05, 2.74248719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.07458469e+05, 2.74248719e+05, ],
  }),
  ("nof_tree_events",                 296256),
  ("nof_db_events",                   296256),
  ("fsize_local",                     1274438490), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        12817875328), # 12.82GB, avg file size 3.20GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99965375e+05, 2.99952188e+05, 2.99983125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.19918125e+05, 2.99964906e+05, 2.81656438e+05, 3.19918125e+05, 2.99964906e+05, 2.81656438e+05, 3.19918125e+05, 2.99964906e+05, 2.81656438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.19918125e+05, 2.81656438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93749344e+05, 2.93736375e+05, 2.93770844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93749344e+05, 2.92192750e+05, 2.95309469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.13223688e+05, 2.93747031e+05, 2.75848719e+05, 3.13223688e+05, 2.93747031e+05, 2.75848719e+05, 3.13223688e+05, 2.93747031e+05, 2.75848719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.13223688e+05, 2.75848719e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1330652144), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        13281765633), # 13.28GB, avg file size 2.66GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99980719e+05, 3.00020812e+05, 3.00061688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.21842312e+05, 2.99978250e+05, 2.80187062e+05, 3.21842312e+05, 2.99978250e+05, 2.80187062e+05, 3.21842312e+05, 2.99978250e+05, 2.80187062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.21842312e+05, 2.80187062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93496688e+05, 2.93505969e+05, 2.93556750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93496688e+05, 2.91884688e+05, 2.95106344e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.14824375e+05, 2.93493969e+05, 2.74162594e+05, 3.14824375e+05, 2.93493969e+05, 2.74162594e+05, 3.14824375e+05, 2.93493969e+05, 2.74162594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.14824375e+05, 2.74162594e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1368266220), # 1.37GB, avg file size 1.37GB
  ("fsize_db",                        13529956556), # 13.53GB, avg file size 2.71GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99979875e+05, 2.99991312e+05, 3.00034531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.23625906e+05, 2.99979031e+05, 2.78866250e+05, 3.23625906e+05, 2.99979031e+05, 2.78866250e+05, 3.23625906e+05, 2.99979031e+05, 2.78866250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.23625906e+05, 2.78866250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93315781e+05, 2.93319438e+05, 2.93347438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93315781e+05, 2.91665250e+05, 2.94968469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.16378406e+05, 2.93313594e+05, 2.72698812e+05, 3.16378406e+05, 2.93313594e+05, 2.72698812e+05, 3.16378406e+05, 2.93313594e+05, 2.72698812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.16378406e+05, 2.72698812e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1397954674), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        13674104858), # 13.67GB, avg file size 3.42GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299538, ],
    'CountWeighted'                                                                  : [ 2.99467250e+05, 2.99549562e+05, 2.99598281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.24726656e+05, 2.99465938e+05, 2.77246125e+05, 3.24726656e+05, 2.99465938e+05, 2.77246125e+05, 3.24726656e+05, 2.99465938e+05, 2.77246125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.24726656e+05, 2.77246125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92650719e+05, 2.92703125e+05, 2.92723188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92650719e+05, 2.90967719e+05, 2.94337250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.17254250e+05, 2.92648281e+05, 2.70942219e+05, 3.17254250e+05, 2.92648281e+05, 2.70942219e+05, 3.17254250e+05, 2.92648281e+05, 2.70942219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.17254250e+05, 2.70942219e+05, ],
  }),
  ("nof_tree_events",                 299538),
  ("nof_db_events",                   299538),
  ("fsize_local",                     1421666406), # 1.42GB, avg file size 1.42GB
  ("fsize_db",                        13997216210), # 14.00GB, avg file size 2.80GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 298727, ],
    'CountWeighted'                                                                  : [ 2.98779281e+05, 2.98723219e+05, 2.98728656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.26693844e+05, 2.98769156e+05, 2.74380875e+05, 3.26693844e+05, 2.98769156e+05, 2.74380875e+05, 3.26693844e+05, 2.98769156e+05, 2.74380875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.26693844e+05, 2.74380875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91624531e+05, 2.91585094e+05, 2.91608156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91624531e+05, 2.89879969e+05, 2.93370844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.18846156e+05, 2.91616750e+05, 2.67862344e+05, 3.18846156e+05, 2.91616750e+05, 2.67862344e+05, 3.18846156e+05, 2.91616750e+05, 2.67862344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.18846156e+05, 2.67862344e+05, ],
  }),
  ("nof_tree_events",                 298727),
  ("nof_db_events",                   298727),
  ("fsize_local",                     1450976496), # 1.45GB, avg file size 1.45GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299705, ],
    'CountWeighted'                                                                  : [ 2.99676531e+05, 2.99776062e+05, 2.99777406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.29028719e+05, 2.99674031e+05, 2.74337000e+05, 3.29028719e+05, 2.99674031e+05, 2.74337000e+05, 3.29028719e+05, 2.99674031e+05, 2.74337000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.29028719e+05, 2.74337000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92536938e+05, 2.92583844e+05, 2.92602562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92536938e+05, 2.90793438e+05, 2.94282219e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.21132750e+05, 2.92534250e+05, 2.67826156e+05, 3.21132750e+05, 2.92534250e+05, 2.67826156e+05, 3.21132750e+05, 2.92534250e+05, 2.67826156e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.21132750e+05, 2.67826156e+05, ],
  }),
  ("nof_tree_events",                 299705),
  ("nof_db_events",                   299705),
  ("fsize_local",                     1468642333), # 1.47GB, avg file size 1.47GB
  ("fsize_db",                        14140095303), # 14.14GB, avg file size 4.71GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 298733, ],
    'CountWeighted'                                                                  : [ 2.98741312e+05, 2.98820500e+05, 2.98715906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.30287250e+05, 2.98739438e+05, 2.71773594e+05, 3.30287250e+05, 2.98739438e+05, 2.71773594e+05, 3.30287250e+05, 2.98739438e+05, 2.71773594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.30287250e+05, 2.71773594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91480781e+05, 2.91511469e+05, 2.91477438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91480781e+05, 2.89717531e+05, 2.93247625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.22219406e+05, 2.91478250e+05, 2.65200688e+05, 3.22219406e+05, 2.91478250e+05, 2.65200688e+05, 3.22219406e+05, 2.91478250e+05, 2.65200688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.22219406e+05, 2.65200688e+05, ],
  }),
  ("nof_tree_events",                 298733),
  ("nof_db_events",                   298733),
  ("fsize_local",                     1484425010), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        14389658695), # 14.39GB, avg file size 4.80GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00033406e+05, 2.99943750e+05, 2.99983688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.33749781e+05, 3.00032531e+05, 2.71427219e+05, 3.33749781e+05, 3.00032531e+05, 2.71427219e+05, 3.33749781e+05, 3.00032531e+05, 2.71427219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.33749781e+05, 2.71427219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92565312e+05, 2.92501938e+05, 2.92546938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92565312e+05, 2.90762531e+05, 2.94373219e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.25422094e+05, 2.92563062e+05, 2.64712969e+05, 3.25422094e+05, 2.92563062e+05, 2.64712969e+05, 3.25422094e+05, 2.92563062e+05, 2.64712969e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.25422094e+05, 2.64712969e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1509477204), # 1.51GB, avg file size 1.51GB
  ("fsize_db",                        14685031472), # 14.69GB, avg file size 3.67GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99904312e+05, 3.00064625e+05, 3.00024375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.05770500e+05, 2.99904094e+05, 2.92706469e+05, 3.05770500e+05, 2.99904094e+05, 2.92706469e+05, 3.05770500e+05, 2.99904094e+05, 2.92706469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.05770500e+05, 2.92706469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.95626125e+05, 2.95715438e+05, 2.95712250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.95626125e+05, 2.94481812e+05, 2.96760562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01339312e+05, 2.95624531e+05, 2.88522062e+05, 3.01339312e+05, 2.95624531e+05, 2.88522062e+05, 3.01339312e+05, 2.95624531e+05, 2.88522062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01339312e+05, 2.88522062e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1077852692), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        12205401208), # 12.21GB, avg file size 4.07GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99993438e+05, 2.99992750e+05, 3.00024469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.06609812e+05, 2.99992000e+05, 2.92026438e+05, 3.06609812e+05, 2.99992000e+05, 2.92026438e+05, 3.06609812e+05, 2.99992000e+05, 2.92026438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.06609812e+05, 2.92026438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.95584219e+05, 2.95581625e+05, 2.95612688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.95584219e+05, 2.94420312e+05, 2.96743500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.02070594e+05, 2.95581812e+05, 2.87763062e+05, 3.02070594e+05, 2.95581812e+05, 2.87763062e+05, 3.02070594e+05, 2.95581812e+05, 2.87763062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02070594e+05, 2.87763062e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1095124879), # 1.10GB, avg file size 1.10GB
  ("fsize_db",                        12216222977), # 12.22GB, avg file size 4.07GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00074594e+05, 2.99970562e+05, 3.00036438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08996219e+05, 3.00053875e+05, 2.90111500e+05, 3.08996219e+05, 3.00053875e+05, 2.90111500e+05, 3.08996219e+05, 3.00053875e+05, 2.90111500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08996219e+05, 2.90111500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.95217906e+05, 2.95146750e+05, 2.95207625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.95217906e+05, 2.93962812e+05, 2.96471125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.03985438e+05, 2.95203531e+05, 2.85480719e+05, 3.03985438e+05, 2.95203531e+05, 2.85480719e+05, 3.03985438e+05, 2.95203531e+05, 2.85480719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03985438e+05, 2.85480719e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1149530164), # 1.15GB, avg file size 1.15GB
  ("fsize_db",                        12432044182), # 12.43GB, avg file size 4.14GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99952719e+05, 3.00004156e+05, 3.00078312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.12407719e+05, 2.99952094e+05, 2.87448531e+05, 3.12407719e+05, 2.99952094e+05, 2.87448531e+05, 3.12407719e+05, 2.99952094e+05, 2.87448531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.12407719e+05, 2.87448531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94675719e+05, 2.94706406e+05, 2.94755562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94675719e+05, 2.93320875e+05, 2.96027250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.06841875e+05, 2.94674125e+05, 2.82414750e+05, 3.06841875e+05, 2.94674125e+05, 2.82414750e+05, 3.06841875e+05, 2.94674125e+05, 2.82414750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.06841875e+05, 2.82414750e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1225345468), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        12931701996), # 12.93GB, avg file size 3.23GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00026156e+05, 2.99988875e+05, 2.99948219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15234594e+05, 3.00020031e+05, 2.85238375e+05, 3.15234594e+05, 3.00020031e+05, 2.85238375e+05, 3.15234594e+05, 3.00020031e+05, 2.85238375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15234594e+05, 2.85238375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94521938e+05, 2.94495719e+05, 2.94484219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94521938e+05, 2.93134219e+05, 2.95914000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.09407625e+05, 2.94516656e+05, 2.80059094e+05, 3.09407625e+05, 2.94516656e+05, 2.80059094e+05, 3.09407625e+05, 2.94516656e+05, 2.80059094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.09407625e+05, 2.80059094e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1286940127), # 1.29GB, avg file size 1.29GB
  ("fsize_db",                        13138610285), # 13.14GB, avg file size 4.38GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99960969e+05, 3.00059750e+05, 2.99987938e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17714094e+05, 2.99960594e+05, 2.83327188e+05, 3.17714094e+05, 2.99960594e+05, 2.83327188e+05, 3.17714094e+05, 2.99960594e+05, 2.83327188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17714094e+05, 2.83327188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94275250e+05, 2.94315625e+05, 2.94309344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94275250e+05, 2.92851562e+05, 2.95700188e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.11622188e+05, 2.94273812e+05, 2.77986219e+05, 3.11622188e+05, 2.94273812e+05, 2.77986219e+05, 3.11622188e+05, 2.94273812e+05, 2.77986219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.11622188e+05, 2.77986219e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1336940817), # 1.34GB, avg file size 1.34GB
  ("fsize_db",                        13501491108), # 13.50GB, avg file size 3.38GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00033312e+05, 2.99949812e+05, 2.99932156e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.19896938e+05, 3.00031000e+05, 2.81654250e+05, 3.19896938e+05, 3.00031000e+05, 2.81654250e+05, 3.19896938e+05, 3.00031000e+05, 2.81654250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.19896938e+05, 2.81654250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94236281e+05, 2.94175438e+05, 2.94179594e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94236281e+05, 2.92796656e+05, 2.95670375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.13672969e+05, 2.94233250e+05, 2.76265250e+05, 3.13672969e+05, 2.94233250e+05, 2.76265250e+05, 3.13672969e+05, 2.94233250e+05, 2.76265250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.13672969e+05, 2.76265250e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1382476002), # 1.38GB, avg file size 1.38GB
  ("fsize_db",                        13733577571), # 13.73GB, avg file size 4.58GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00016562e+05, 3.00028938e+05, 2.99979688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.21863594e+05, 3.00010125e+05, 2.80185562e+05, 3.21863594e+05, 3.00010125e+05, 2.80185562e+05, 3.21863594e+05, 3.00010125e+05, 2.80185562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.21863594e+05, 2.80185562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94118531e+05, 2.94114906e+05, 2.94102438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94118531e+05, 2.92662500e+05, 2.95570969e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.15485000e+05, 2.94113312e+05, 2.74719625e+05, 3.15485000e+05, 2.94113312e+05, 2.74719625e+05, 3.15485000e+05, 2.94113312e+05, 2.74719625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.15485000e+05, 2.74719625e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1422523815), # 1.42GB, avg file size 1.42GB
  ("fsize_db",                        13919729330), # 13.92GB, avg file size 4.64GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99968844e+05, 3.00035656e+05, 2.99992125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.23616750e+05, 2.99967844e+05, 2.78860406e+05, 3.23616750e+05, 2.99967844e+05, 2.78860406e+05, 3.23616750e+05, 2.99967844e+05, 2.78860406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.23616750e+05, 2.78860406e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94144750e+05, 2.94176344e+05, 2.94164969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94144750e+05, 2.92711438e+05, 2.95582094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.17272375e+05, 2.94142469e+05, 2.73470938e+05, 3.17272375e+05, 2.94142469e+05, 2.73470938e+05, 3.17272375e+05, 2.94142469e+05, 2.73470938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.17272375e+05, 2.73470938e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1449774082), # 1.45GB, avg file size 1.45GB
  ("fsize_db",                        14074430864), # 14.07GB, avg file size 4.69GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 298806, ],
    'CountWeighted'                                                                  : [ 2.98810188e+05, 2.98868625e+05, 2.98784125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.23945906e+05, 2.98799500e+05, 2.76575219e+05, 3.23945906e+05, 2.98799500e+05, 2.76575219e+05, 3.23945906e+05, 2.98799500e+05, 2.76575219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.23945906e+05, 2.76575219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92959469e+05, 2.92990219e+05, 2.92954906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92959469e+05, 2.91527438e+05, 2.94393312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.17558875e+05, 2.92951250e+05, 2.71188344e+05, 3.17558875e+05, 2.92951250e+05, 2.71188344e+05, 3.17558875e+05, 2.92951250e+05, 2.71188344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.17558875e+05, 2.71188344e+05, ],
  }),
  ("nof_tree_events",                 298806),
  ("nof_db_events",                   298806),
  ("fsize_local",                     1464171604), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        14346261466), # 14.35GB, avg file size 2.39GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00046531e+05, 2.99947094e+05, 2.99948406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.26704344e+05, 3.00039219e+05, 2.76566938e+05, 3.26704344e+05, 3.00039219e+05, 2.76566938e+05, 3.26704344e+05, 3.00039219e+05, 2.76566938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.26704344e+05, 2.76566938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94197344e+05, 2.94140094e+05, 2.94137344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94197344e+05, 2.92775250e+05, 2.95623438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.20316031e+05, 2.94191188e+05, 2.71220875e+05, 3.20316031e+05, 2.94191188e+05, 2.71220875e+05, 3.20316031e+05, 2.94191188e+05, 2.71220875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.20316031e+05, 2.71220875e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1483970886), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        14636315935), # 14.64GB, avg file size 4.88GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00030969e+05, 2.99921562e+05, 2.99915469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.29350906e+05, 3.00023844e+05, 2.74605719e+05, 3.29350906e+05, 3.00023844e+05, 2.74605719e+05, 3.29350906e+05, 3.00023844e+05, 2.74605719e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.29350906e+05, 2.74605719e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94262531e+05, 2.94188031e+05, 2.94190094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94262531e+05, 2.92859000e+05, 2.95664781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.23004250e+05, 2.94256406e+05, 2.69358844e+05, 3.23004250e+05, 2.94256406e+05, 2.69358844e+05, 3.23004250e+05, 2.94256406e+05, 2.69358844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.23004250e+05, 2.69358844e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1504938426), # 1.50GB, avg file size 1.50GB
  ("fsize_db",                        14673528101), # 14.67GB, avg file size 3.67GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99983531e+05, 2.99965125e+05, 3.00006344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.31709906e+05, 2.99978906e+05, 2.72939281e+05, 3.31709906e+05, 2.99978906e+05, 2.72939281e+05, 3.31709906e+05, 2.99978906e+05, 2.72939281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.31709906e+05, 2.72939281e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94245875e+05, 2.94229406e+05, 2.94266062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94245875e+05, 2.92850875e+05, 2.95642594e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.25332344e+05, 2.94241500e+05, 2.67727562e+05, 3.25332344e+05, 2.94241500e+05, 2.67727562e+05, 3.25332344e+05, 2.94241500e+05, 2.67727562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.25332344e+05, 2.67727562e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1521174910), # 1.52GB, avg file size 1.52GB
  ("fsize_db",                        15011560063), # 15.01GB, avg file size 5.00GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299118, ],
    'CountWeighted'                                                                  : [ 2.99112219e+05, 2.99137656e+05, 2.99189656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.32789188e+05, 2.99107594e+05, 2.70644531e+05, 3.32789188e+05, 2.99107594e+05, 2.70644531e+05, 3.32789188e+05, 2.99107594e+05, 2.70644531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.32789188e+05, 2.70644531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93385156e+05, 2.93387906e+05, 2.93456344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93385156e+05, 2.91998750e+05, 2.94775500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.26394125e+05, 2.93380594e+05, 2.65477031e+05, 3.26394125e+05, 2.93380594e+05, 2.65477031e+05, 3.26394125e+05, 2.93380594e+05, 2.65477031e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.26394125e+05, 2.65477031e+05, ],
  }),
  ("nof_tree_events",                 299118),
  ("nof_db_events",                   299118),
  ("fsize_local",                     1529501980), # 1.53GB, avg file size 1.53GB
  ("fsize_db",                        15065557472), # 15.07GB, avg file size 5.02GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00021312e+05, 3.00024844e+05, 2.99979000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.26212094e+05, 3.00020812e+05, 2.77736500e+05, 3.26212094e+05, 3.00020812e+05, 2.77736500e+05, 3.26212094e+05, 3.00020812e+05, 2.77736500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.28772562e+05, 2.75220875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.88364938e+05, 2.88364688e+05, 2.88355375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.88364938e+05, 2.85462219e+05, 2.91269438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.13352844e+05, 2.88362094e+05, 2.67104094e+05, 3.13352844e+05, 2.88362094e+05, 2.67104094e+05, 3.13352844e+05, 2.88362094e+05, 2.67104094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.15863688e+05, 2.64636469e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1260762042), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        12626803802), # 12.63GB, avg file size 4.21GB
  ("use_it",                          True),
  ("xsection",                        4.55695e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00041406e+05, 2.99893875e+05, 2.99992688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.24928250e+05, 3.00040656e+05, 2.78756031e+05, 3.24928250e+05, 3.00040656e+05, 2.78756031e+05, 3.24928250e+05, 3.00040656e+05, 2.78756031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.27206562e+05, 2.76515500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.85210750e+05, 2.85158875e+05, 2.85209875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.85210750e+05, 2.81652781e+05, 2.88787875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.08640000e+05, 2.85208188e+05, 2.65198719e+05, 3.08640000e+05, 2.85208188e+05, 2.65198719e+05, 3.08640000e+05, 2.85208188e+05, 2.65198719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.10865500e+05, 2.63009562e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1346391622), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        13505935893), # 13.51GB, avg file size 2.25GB
  ("use_it",                          True),
  ("xsection",                        3.75655e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99951000e+05, 2.99976906e+05, 2.99990625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.38115938e+05, 2.99950688e+05, 2.69639500e+05, 3.38115938e+05, 2.99950688e+05, 2.69639500e+05, 3.38115938e+05, 2.99950688e+05, 2.69639500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.39274219e+05, 2.68508500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.87335000e+05, 2.87331094e+05, 2.87364219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.87335000e+05, 2.84340781e+05, 2.90343906e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.23762062e+05, 2.87333062e+05, 2.58352688e+05, 3.23762062e+05, 2.87333062e+05, 2.58352688e+05, 3.23762062e+05, 2.87333062e+05, 2.58352688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.24897344e+05, 2.57244578e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1482047254), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        14484771487), # 14.48GB, avg file size 2.41GB
  ("use_it",                          True),
  ("xsection",                        0.0003753816),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_0_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00040094e+05, 2.99903719e+05, 2.99953656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22426000e+05, 3.00036625e+05, 2.80507250e+05, 3.22426000e+05, 3.00036625e+05, 2.80507250e+05, 3.22426000e+05, 3.00036625e+05, 2.80507250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.25874750e+05, 2.77108562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.89896281e+05, 2.89851000e+05, 2.89857812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.89896281e+05, 2.87341875e+05, 2.92448281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.11374125e+05, 2.89891812e+05, 2.71174750e+05, 3.11374125e+05, 2.89891812e+05, 2.71174750e+05, 3.11374125e+05, 2.89891812e+05, 2.71174750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.14760781e+05, 2.67835594e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1259665900), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        13033305340), # 13.03GB, avg file size 3.26GB
  ("use_it",                          True),
  ("xsection",                        0.0001216848),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_5_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299402, ],
    'CountWeighted'                                                                  : [ 2.99408219e+05, 2.99348500e+05, 2.99473969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.29954500e+05, 2.99404375e+05, 2.74211312e+05, 3.29954500e+05, 2.99404375e+05, 2.74211312e+05, 3.29954500e+05, 2.99404375e+05, 2.74211312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.32124188e+05, 2.72078875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.87828844e+05, 2.87800219e+05, 2.87858156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.87828844e+05, 2.84997375e+05, 2.90670250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.17006656e+05, 2.87825000e+05, 2.63748250e+05, 3.17006656e+05, 2.87825000e+05, 2.63748250e+05, 3.17006656e+05, 2.87825000e+05, 2.63748250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.19137188e+05, 2.61654312e+05, ],
  }),
  ("nof_tree_events",                 299402),
  ("nof_db_events",                   299402),
  ("fsize_local",                     1364979658), # 1.36GB, avg file size 1.36GB
  ("fsize_db",                        13628421160), # 13.63GB, avg file size 2.73GB
  ("use_it",                          True),
  ("xsection",                        0.001743038),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_0_5_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 297179, ],
    'CountWeighted'                                                                  : [ 2.97192375e+05, 2.97162000e+05, 2.97149625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.32159000e+05, 2.97189688e+05, 2.69009312e+05, 3.32159000e+05, 2.97189688e+05, 2.69009312e+05, 3.32159000e+05, 2.97189688e+05, 2.69009312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.33634125e+05, 2.67565562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.85149031e+05, 2.85125219e+05, 2.85143000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.85149031e+05, 2.82270062e+05, 2.88046312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.18568406e+05, 2.85145906e+05, 2.58219250e+05, 3.18568406e+05, 2.85145906e+05, 2.58219250e+05, 3.18568406e+05, 2.85145906e+05, 2.58219250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.20013625e+05, 2.56804859e+05, ],
  }),
  ("nof_tree_events",                 297179),
  ("nof_db_events",                   297179),
  ("fsize_local",                     1437048269), # 1.44GB, avg file size 1.44GB
  ("fsize_db",                        14044768795), # 14.04GB, avg file size 2.81GB
  ("use_it",                          True),
  ("xsection",                        0.0002857708),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00033156e+05, 3.00016156e+05, 3.00032188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84359875e+05, 3.62836188e+05, 3.42660594e+05, 3.17827906e+05, 3.00032594e+05, 2.83287406e+05, 2.67194531e+05, 2.52189453e+05, 2.38118875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.84359875e+05, 2.38118875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93946969e+05, 2.93930594e+05, 2.93954562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93946969e+05, 2.92418438e+05, 2.95475531e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.76518031e+05, 3.55501219e+05, 3.35784344e+05, 3.11339375e+05, 2.93945125e+05, 2.77599281e+05, 2.61737484e+05, 2.47082047e+05, 2.33335859e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76518031e+05, 2.33335859e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1312950107), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        13376661186), # 13.38GB, avg file size 2.68GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_box_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_box_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00021531e+05, 3.00043156e+05, 2.99975625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.82913000e+05, 3.63712719e+05, 3.45314875e+05, 3.15872562e+05, 3.00021062e+05, 2.84793188e+05, 2.65023594e+05, 2.51679875e+05, 2.38902969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.82913000e+05, 2.38902969e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94253594e+05, 2.94256844e+05, 2.94234031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94253594e+05, 2.92796250e+05, 2.95708094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.75496125e+05, 3.56735531e+05, 3.38742250e+05, 3.09750594e+05, 2.94251469e+05, 2.79369188e+05, 2.59882438e+05, 2.46844094e+05, 2.34350391e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.75496125e+05, 2.34350391e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1278580114), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        13225066454), # 13.23GB, avg file size 4.41GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_box_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_1_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99987500e+05, 2.99979469e+05, 2.99982875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.85629719e+05, 3.62179375e+05, 3.40639438e+05, 3.19539938e+05, 2.99985125e+05, 2.82078250e+05, 2.69129219e+05, 2.52596734e+05, 2.37448344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.85629719e+05, 2.37448344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93861500e+05, 2.93845406e+05, 2.93868125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93861500e+05, 2.92326094e+05, 2.95392469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.77670781e+05, 3.54789500e+05, 3.33758875e+05, 3.12930750e+05, 2.93858688e+05, 2.76369812e+05, 2.63552125e+05, 2.47423766e+05, 2.32635219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.77670781e+05, 2.32635219e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1336244412), # 1.34GB, avg file size 1.34GB
  ("fsize_db",                        13519407617), # 13.52GB, avg file size 3.38GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 8218, ],
    'CountWeighted'                                                                  : [ 8.21651660e+03, 8.21662793e+03, 8.21625977e+03, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.07527471e+04, 9.81205371e+03, 9.00235742e+03, 9.00789160e+03, 8.21634766e+03, 7.53584180e+03, 7.65699658e+03, 6.98195801e+03, 6.40169043e+03, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.07527471e+04, 6.40169043e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.03326221e+03, 8.03330664e+03, 8.03318701e+03, ],
    'CountWeightedL1Prefire'                                                         : [ 8.03326221e+03, 7.98848145e+03, 8.07807324e+03, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.05110645e+04, 9.59350977e+03, 8.80341406e+03, 8.80511328e+03, 8.03312158e+03, 7.36906396e+03, 7.48445752e+03, 6.82604980e+03, 6.25982812e+03, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.05110645e+04, 6.25982812e+03, ],
  }),
  ("nof_tree_events",                 8218),
  ("nof_db_events",                   300000),
  ("fsize_local",                     41546650), # 41.55MB, avg file size 41.55MB
  ("fsize_db",                        14649063726), # 14.65GB, avg file size 3.66GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 3.00064062e+05, 2.99963688e+05, 2.99935469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.85312312e+05, 3.62284062e+05, 3.40997656e+05, 3.19129938e+05, 3.00062938e+05, 2.82324812e+05, 2.68657531e+05, 2.52511719e+05, 2.37609062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.85312312e+05, 2.37609062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93906406e+05, 2.93840469e+05, 2.93838125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93906406e+05, 2.92368156e+05, 2.95441000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.77370906e+05, 3.54890625e+05, 3.34094875e+05, 3.12544906e+05, 2.93904219e+05, 2.76603688e+05, 2.63109375e+05, 2.47349250e+05, 2.32791109e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.77370906e+05, 2.32791109e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1332209180), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        13601999029), # 13.60GB, avg file size 4.53GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_4_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99998844e+05, 2.99997312e+05, 2.99937312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.83461062e+05, 3.63426281e+05, 3.44402062e+05, 3.16596844e+05, 2.99998594e+05, 2.84257438e+05, 2.65827969e+05, 2.51857094e+05, 2.38612359e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.83461062e+05, 2.38612359e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94120219e+05, 2.94113188e+05, 2.94088812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94120219e+05, 2.92636719e+05, 2.95604125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.75881844e+05, 3.56312031e+05, 3.37717344e+05, 3.10330781e+05, 2.94118281e+05, 2.78735406e+05, 2.60561703e+05, 2.46917703e+05, 2.33973203e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.75881844e+05, 2.33973203e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1289342003), # 1.29GB, avg file size 1.29GB
  ("fsize_db",                        13322107044), # 13.32GB, avg file size 4.44GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_5_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00070031e+05, 2.99941844e+05, 2.99966094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.89048875e+05, 3.60182219e+05, 3.34601312e+05, 3.24157688e+05, 3.00065688e+05, 2.78608438e+05, 2.74285031e+05, 2.53765594e+05, 2.35614438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.89048875e+05, 2.35614438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93482594e+05, 2.93412656e+05, 2.93417125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93482594e+05, 2.91863344e+05, 2.95104031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.80471906e+05, 3.52323781e+05, 3.27364906e+05, 3.16999688e+05, 2.93478500e+05, 2.72573656e+05, 2.68222469e+05, 2.48213359e+05, 2.30504469e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.80471906e+05, 2.30504469e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1402642987), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        14057961060), # 14.06GB, avg file size 3.51GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_5_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_6_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99981906e+05, 3.00014625e+05, 3.00051812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.82863719e+05, 3.63875875e+05, 3.45731812e+05, 3.15756750e+05, 2.99975312e+05, 2.84964375e+05, 2.64893031e+05, 2.51615797e+05, 2.38948891e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.82863719e+05, 2.38948891e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94383656e+05, 2.94395094e+05, 2.94438531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94383656e+05, 2.92963500e+05, 2.95801469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.75640781e+05, 3.57092906e+05, 3.39353594e+05, 3.09787344e+05, 2.94378062e+05, 2.79695719e+05, 2.59876359e+05, 2.46905938e+05, 2.34523375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.75640781e+05, 2.34523375e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1272739758), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        13143785774), # 13.14GB, avg file size 3.29GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 3.00015812e+05, 3.00034188e+05, 3.00044031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.79147094e+05, 3.66135469e+05, 3.52540250e+05, 3.10691188e+05, 3.00011406e+05, 2.88830250e+05, 2.59242109e+05, 2.50294281e+05, 2.40959188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.79147094e+05, 2.40959188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.95004062e+05, 2.95006844e+05, 2.95026531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.95004062e+05, 2.93709812e+05, 2.96293594e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.72764906e+05, 3.60032938e+05, 3.46711125e+05, 3.05458250e+05, 2.94999906e+05, 2.84050562e+05, 2.54870328e+05, 2.46115328e+05, 2.36968531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.72764906e+05, 2.36968531e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1180175740), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        12803480606), # 12.80GB, avg file size 3.20GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_8_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99935438e+05, 3.00001500e+05, 2.99949938e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.85549062e+05, 3.62239781e+05, 3.40803750e+05, 3.19406844e+05, 2.99933344e+05, 2.82171062e+05, 2.68970062e+05, 2.52555750e+05, 2.37495750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.85549062e+05, 2.37495750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93815594e+05, 2.93850906e+05, 2.93819375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93815594e+05, 2.92272125e+05, 2.95351375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.77569562e+05, 3.54829438e+05, 3.33899656e+05, 3.12786812e+05, 2.93812969e+05, 2.76444250e+05, 2.63384594e+05, 2.47371828e+05, 2.32668219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.77569562e+05, 2.32668219e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1332331952), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        13552950610), # 13.55GB, avg file size 4.52GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99947750e+05, 2.99999000e+05, 3.00000969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.87741312e+05, 3.60880531e+05, 3.36741781e+05, 3.22413000e+05, 2.99946812e+05, 2.79874125e+05, 2.72332562e+05, 2.53345906e+05, 2.36306906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.87741312e+05, 2.36306906e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93479469e+05, 2.93501562e+05, 2.93522625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93479469e+05, 2.91872125e+05, 2.95084438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.79281500e+05, 3.53084188e+05, 3.29528688e+05, 3.15368500e+05, 2.93477719e+05, 2.73870719e+05, 2.66377375e+05, 2.47859562e+05, 2.31233312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.79281500e+05, 2.31233312e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1382545617), # 1.38GB, avg file size 1.38GB
  ("fsize_db",                        13997106004), # 14.00GB, avg file size 4.67GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_10_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 3.00029719e+05, 3.00072625e+05, 2.99938781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.79915781e+05, 3.65712625e+05, 3.51256281e+05, 3.11717500e+05, 3.00016812e+05, 2.88078656e+05, 2.60389250e+05, 2.50542781e+05, 2.40548406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.79915781e+05, 2.40548406e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94893562e+05, 2.94911562e+05, 2.94836906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94893562e+05, 2.93571281e+05, 2.96205562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.73356750e+05, 3.59477344e+05, 3.45325000e+05, 3.06326688e+05, 2.94883938e+05, 2.83203906e+05, 2.55878672e+05, 2.46256422e+05, 2.36473547e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.73356750e+05, 2.36473547e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1196277603), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        12822566212), # 12.82GB, avg file size 3.21GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_11_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299364, ],
    'CountWeighted'                                                                  : [ 2.99374750e+05, 2.99295969e+05, 2.99376625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.82106719e+05, 3.63096906e+05, 3.44966062e+05, 3.15151594e+05, 2.99373750e+05, 2.84330219e+05, 2.64405969e+05, 2.51083812e+05, 2.38418906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.82106719e+05, 2.38418906e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93816438e+05, 2.93769531e+05, 2.93821281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93816438e+05, 2.92408906e+05, 2.95223219e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.74947875e+05, 3.56378562e+05, 3.38649188e+05, 3.09233312e+05, 2.93814438e+05, 2.79113844e+05, 2.59431625e+05, 2.46420328e+05, 2.34035438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.74947875e+05, 2.34035438e+05, ],
  }),
  ("nof_tree_events",                 299364),
  ("nof_db_events",                   299364),
  ("fsize_local",                     1266560870), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        13315340669), # 13.32GB, avg file size 2.66GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph-v2/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 3.00047906e+05, 3.00033719e+05, 3.00038562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.80853406e+05, 3.65028875e+05, 3.49246938e+05, 3.13042406e+05, 3.00046969e+05, 2.86992375e+05, 2.61865750e+05, 2.50922594e+05, 2.40024750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.80853406e+05, 2.40024750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94674719e+05, 2.94644938e+05, 2.94693031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94674719e+05, 2.93305094e+05, 2.96046188e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.73999000e+05, 3.58526562e+05, 3.43073062e+05, 3.07402406e+05, 2.94672562e+05, 2.81914125e+05, 2.57144031e+05, 2.46443234e+05, 2.35775172e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.73999000e+05, 2.35775172e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1226671172), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        13025018010), # 13.03GB, avg file size 3.26GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99973219e+05, 2.99945219e+05, 2.99933469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84329156e+05, 3.62832812e+05, 3.42671000e+05, 3.17803312e+05, 2.99970625e+05, 2.83298219e+05, 2.67178812e+05, 2.52180797e+05, 2.38129156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.84329156e+05, 2.38129156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93881094e+05, 2.93856781e+05, 2.93877406e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93881094e+05, 2.92339438e+05, 2.95424438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.76448969e+05, 3.55462125e+05, 3.35762156e+05, 3.11283156e+05, 2.93878219e+05, 2.77583438e+05, 2.61691859e+05, 2.47051984e+05, 2.33322797e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76448969e+05, 2.33322797e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1374546502), # 1.37GB, avg file size 1.37GB
  ("fsize_db",                        13758086324), # 13.76GB, avg file size 3.44GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node_box_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_box_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 3.00024500e+05, 3.00007875e+05, 2.99989094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.82905781e+05, 3.63725625e+05, 3.45344062e+05, 3.15856656e+05, 3.00022156e+05, 2.84809250e+05, 2.64999188e+05, 2.51669031e+05, 2.38904688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.82905781e+05, 2.38904688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94212406e+05, 2.94192281e+05, 2.94196219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94212406e+05, 2.92733031e+05, 2.95689594e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.75434188e+05, 3.56697938e+05, 3.38725562e+05, 3.09686812e+05, 2.94209344e+05, 2.79346094e+05, 2.59818984e+05, 2.46797594e+05, 2.34319781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.75434188e+05, 2.34319781e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1330503279), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        13554966138), # 13.55GB, avg file size 2.71GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_box_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 299994, ],
    'CountWeighted'                                                                  : [ 2.99977781e+05, 2.99938969e+05, 3.00004656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.85637094e+05, 3.62144812e+05, 3.40580188e+05, 3.19563375e+05, 2.99968188e+05, 2.82047281e+05, 2.69163438e+05, 2.52604422e+05, 2.37438297e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.85637094e+05, 2.37438297e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93771344e+05, 2.93741938e+05, 2.93797406e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93771344e+05, 2.92211781e+05, 2.95329094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.77570156e+05, 3.54662281e+05, 3.33614250e+05, 3.12865344e+05, 2.93764250e+05, 2.76265969e+05, 2.63510875e+05, 2.47364047e+05, 2.32562000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.77570156e+05, 2.32562000e+05, ],
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     1401598191), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        14226816913), # 14.23GB, avg file size 2.37GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_1_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99933062e+05, 2.99951281e+05, 3.00040969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.92377500e+05, 3.58370906e+05, 3.29047281e+05, 3.28594688e+05, 2.99932594e+05, 2.75354906e+05, 2.79230406e+05, 2.54841484e+05, 2.33845391e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.92377500e+05, 2.33845391e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93045906e+05, 2.93043594e+05, 2.93117844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93045906e+05, 2.91345906e+05, 2.94742062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.83257906e+05, 3.50123938e+05, 3.21538469e+05, 3.20944938e+05, 2.93044031e+05, 2.69060250e+05, 2.72719250e+05, 2.48960625e+05, 2.28492219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.83257906e+05, 2.28492219e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1528341828), # 1.53GB, avg file size 1.53GB
  ("fsize_db",                        15065193278), # 15.07GB, avg file size 3.01GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-3_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299201, ],
    'CountWeighted'                                                                  : [ 2.99174219e+05, 2.99201562e+05, 2.99284438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84292938e+05, 3.61320250e+05, 3.40087781e+05, 3.18284875e+05, 2.99173562e+05, 2.81574188e+05, 2.67947438e+05, 2.51842609e+05, 2.36972781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.84292938e+05, 2.36972781e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92998125e+05, 2.93000969e+05, 2.93075500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92998125e+05, 2.91435031e+05, 2.94556438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.76275688e+05, 3.53857344e+05, 3.33122250e+05, 3.11635625e+05, 2.92996250e+05, 2.75799188e+05, 2.62344938e+05, 2.46629094e+05, 2.32110188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76275688e+05, 2.32110188e+05, ],
  }),
  ("nof_tree_events",                 299201),
  ("nof_db_events",                   299201),
  ("fsize_local",                     1394546628), # 1.39GB, avg file size 1.39GB
  ("fsize_db",                        14042794496), # 14.04GB, avg file size 3.51GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-4_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99998906e+05, 3.00102281e+05, 2.99971656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.83459750e+05, 3.63429125e+05, 3.44409656e+05, 3.16587031e+05, 2.99991469e+05, 2.84261156e+05, 2.65816156e+05, 2.51845312e+05, 2.38615828e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.83459750e+05, 2.38615828e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94075031e+05, 2.94126594e+05, 2.94063938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94075031e+05, 2.92566875e+05, 2.95579094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.75816219e+05, 3.56257625e+05, 3.37673938e+05, 3.10269750e+05, 2.94069188e+05, 2.78695500e+05, 2.60506328e+05, 2.46868688e+05, 2.33938312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.75816219e+05, 2.33938312e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1345409191), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        13734345217), # 13.73GB, avg file size 2.75GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-5_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99939906e+05, 2.99978406e+05, 2.99994188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.89002969e+05, 3.60214562e+05, 3.34692344e+05, 3.24086594e+05, 2.99937625e+05, 2.78655906e+05, 2.74200438e+05, 2.53744562e+05, 2.35637141e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.89002969e+05, 2.35637141e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93315719e+05, 2.93330156e+05, 2.93358844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93315719e+05, 2.91665812e+05, 2.94965438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.80302656e+05, 3.52245031e+05, 3.27353844e+05, 3.16827094e+05, 2.93312500e+05, 2.72537031e+05, 2.68050156e+05, 2.48113391e+05, 2.30454844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.80302656e+05, 2.30454844e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1473633220), # 1.47GB, avg file size 1.47GB
  ("fsize_db",                        14660310040), # 14.66GB, avg file size 2.44GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_5_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-6_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99978188e+05, 2.99943781e+05, 2.99984875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.82838312e+05, 3.63872188e+05, 3.45748250e+05, 3.15736781e+05, 2.99977250e+05, 2.84979875e+05, 2.64878312e+05, 2.51607203e+05, 2.38963719e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.82838312e+05, 2.38963719e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94364781e+05, 2.94337969e+05, 2.94379281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94364781e+05, 2.92934281e+05, 2.95792656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.75589156e+05, 3.57070312e+05, 3.39354438e+05, 3.09742594e+05, 2.94362312e+05, 2.79697500e+05, 2.59842062e+05, 2.46883969e+05, 2.34524609e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.75589156e+05, 2.34524609e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1325766861), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        13255677867), # 13.26GB, avg file size 4.42GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-7_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99984438e+05, 2.99952531e+05, 2.99920562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.79174844e+05, 3.66134312e+05, 3.52515219e+05, 3.10721188e+05, 2.99976531e+05, 2.88811156e+05, 2.59266125e+05, 2.50295312e+05, 2.40945609e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.79174844e+05, 2.40945609e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94945344e+05, 2.94912438e+05, 2.94919656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94945344e+05, 2.93634938e+05, 2.96246625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.72740844e+05, 3.59981281e+05, 3.46636656e+05, 3.05442219e+05, 2.94939156e+05, 2.83991500e+05, 2.54859812e+05, 2.46082500e+05, 2.36921938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.72740844e+05, 2.36921938e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1217085467), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        12941536315), # 12.94GB, avg file size 3.24GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-8_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99985469e+05, 2.99970094e+05, 2.99951375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.85525969e+05, 3.62242875e+05, 3.40828500e+05, 3.19383562e+05, 2.99983531e+05, 2.82185500e+05, 2.68944250e+05, 2.52551234e+05, 2.37502938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.85525969e+05, 2.37502938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93809750e+05, 2.93797312e+05, 2.93791062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93809750e+05, 2.92255406e+05, 2.95360625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.77500625e+05, 3.54791062e+05, 3.33890562e+05, 3.12721562e+05, 2.93806875e+05, 2.76429250e+05, 2.63325312e+05, 2.47338031e+05, 2.32650359e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.77500625e+05, 2.32650359e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1394951318), # 1.39GB, avg file size 1.39GB
  ("fsize_db",                        14190505186), # 14.19GB, avg file size 2.84GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-9_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299591, ],
    'CountWeighted'                                                                  : [ 2.99525750e+05, 2.99557906e+05, 2.99611688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.87195062e+05, 3.60412000e+05, 3.36342969e+05, 3.21937438e+05, 2.99524688e+05, 2.79522344e+05, 2.71916062e+05, 2.52986594e+05, 2.35996188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.87195062e+05, 2.35996188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93025938e+05, 2.93033812e+05, 2.93080281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93025938e+05, 2.91396094e+05, 2.94646500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.78678562e+05, 3.52564688e+05, 3.29081125e+05, 3.14847219e+05, 2.93023750e+05, 2.73479969e+05, 2.65921688e+05, 2.47464406e+05, 2.30888812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.78678562e+05, 2.30888812e+05, ],
  }),
  ("nof_tree_events",                 299591),
  ("nof_db_events",                   299591),
  ("fsize_local",                     1452694846), # 1.45GB, avg file size 1.45GB
  ("fsize_db",                        14339474676), # 14.34GB, avg file size 2.87GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-10_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 3.00052000e+05, 3.00008562e+05, 2.99941500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.79837750e+05, 3.65749875e+05, 3.51367750e+05, 3.11636125e+05, 3.00049094e+05, 2.88144062e+05, 2.60296438e+05, 2.50528234e+05, 2.40588719e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.79837750e+05, 2.40588719e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94960500e+05, 2.94929812e+05, 2.94896938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94960500e+05, 2.93645906e+05, 2.96263969e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.73350844e+05, 3.59580188e+05, 3.45502031e+05, 3.06302281e+05, 2.94956562e+05, 2.83323438e+05, 2.55832781e+05, 2.46285625e+05, 2.36557031e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.73350844e+05, 2.36557031e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1233248720), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        13151222527), # 13.15GB, avg file size 2.63GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-11_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 299994, ],
    'CountWeighted'                                                                  : [ 3.00052312e+05, 2.99967781e+05, 2.99994375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.82924750e+05, 3.63852625e+05, 3.45678031e+05, 3.15830188e+05, 3.00051438e+05, 2.84920281e+05, 2.64976156e+05, 2.51617766e+05, 2.38913031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.82924750e+05, 2.38913031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94401156e+05, 2.94351031e+05, 2.94374219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94401156e+05, 2.92972531e+05, 2.95830969e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.75670188e+05, 3.57049875e+05, 3.39280938e+05, 3.09830312e+05, 2.94398719e+05, 2.79637938e+05, 2.59933750e+05, 2.46890219e+05, 2.34475016e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.75670188e+05, 2.34475016e+05, ],
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     1318499888), # 1.32GB, avg file size 1.32GB
  ("fsize_db",                        13676249855), # 13.68GB, avg file size 2.28GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_node-12_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299994, ],
    'CountWeighted'                                                                  : [ 2.99965812e+05, 2.99991188e+05, 2.99987562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.80877438e+05, 3.65020750e+05, 3.49211656e+05, 3.13068656e+05, 2.99965188e+05, 2.86967094e+05, 2.61891672e+05, 2.50924641e+05, 2.40010000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.80877438e+05, 2.40010000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94578250e+05, 2.94579344e+05, 2.94600594e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94578250e+05, 2.93184156e+05, 2.95960406e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.73958219e+05, 3.58456469e+05, 3.42983812e+05, 3.07376531e+05, 2.94576094e+05, 2.81844531e+05, 2.57125344e+05, 2.46404516e+05, 2.35721984e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.73958219e+05, 2.35721984e+05, ],
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     1270241759), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        13168943933), # 13.17GB, avg file size 3.29GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.99987375e+05, 3.00029938e+05, 3.00044438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.04877469e+05, 2.99986719e+05, 2.93425500e+05, 3.04877469e+05, 2.99986719e+05, 2.93425500e+05, 3.04877469e+05, 2.99986719e+05, 2.93425500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.04877469e+05, 2.93425500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.96017312e+05, 2.96035062e+05, 2.96063844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.96017312e+05, 2.94947938e+05, 2.97077500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.00808531e+05, 2.96015500e+05, 2.89562531e+05, 3.00808531e+05, 2.96015500e+05, 2.89562531e+05, 3.00808531e+05, 2.96015500e+05, 2.89562531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.00808531e+05, 2.89562531e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1051886754), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        12143344410), # 12.14GB, avg file size 2.43GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299402, ],
    'CountWeighted'                                                                  : [ 2.99421219e+05, 2.99326125e+05, 2.99383750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.05157156e+05, 2.99420031e+05, 2.92139625e+05, 3.05157156e+05, 2.99420031e+05, 2.92139625e+05, 3.05157156e+05, 2.99420031e+05, 2.92139625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.05157156e+05, 2.92139625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.95291562e+05, 2.95227000e+05, 2.95271125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.95291562e+05, 2.94183562e+05, 2.96381062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.00924938e+05, 2.95289062e+05, 2.88134281e+05, 3.00924938e+05, 2.95289062e+05, 2.88134281e+05, 3.00924938e+05, 2.95289062e+05, 2.88134281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.00924938e+05, 2.88134281e+05, ],
  }),
  ("nof_tree_events",                 299402),
  ("nof_db_events",                   299402),
  ("fsize_local",                     1067718502), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        12033567447), # 12.03GB, avg file size 2.41GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299995, ],
    'CountWeighted'                                                                  : [ 2.99992375e+05, 2.99997188e+05, 2.99973781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.06633094e+05, 2.99990906e+05, 2.91997531e+05, 3.06633094e+05, 2.99990906e+05, 2.91997531e+05, 3.06633094e+05, 2.99990906e+05, 2.91997531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.06633094e+05, 2.91997531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.95720844e+05, 2.95717844e+05, 2.95713000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.95720844e+05, 2.94582062e+05, 2.96852375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.02232281e+05, 2.95718562e+05, 2.87868312e+05, 3.02232281e+05, 2.95718562e+05, 2.87868312e+05, 3.02232281e+05, 2.95718562e+05, 2.87868312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02232281e+05, 2.87868312e+05, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1090206393), # 1.09GB, avg file size 1.09GB
  ("fsize_db",                        12073887370), # 12.07GB, avg file size 2.41GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99997000e+05, 3.00015875e+05, 2.99962969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08979312e+05, 2.99996375e+05, 2.90153812e+05, 3.08979312e+05, 2.99996375e+05, 2.90153812e+05, 3.08979312e+05, 2.99996375e+05, 2.90153812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08979312e+05, 2.90153812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.95355812e+05, 2.95367438e+05, 2.95329438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.95355812e+05, 2.94132812e+05, 2.96572844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.04158531e+05, 2.95353969e+05, 2.85690875e+05, 3.04158531e+05, 2.95353969e+05, 2.85690875e+05, 3.04158531e+05, 2.95353969e+05, 2.85690875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.04158531e+05, 2.85690875e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1144473979), # 1.14GB, avg file size 1.14GB
  ("fsize_db",                        12250780111), # 12.25GB, avg file size 3.06GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99962781e+05, 2.99966938e+05, 3.00027531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.12387094e+05, 2.99962500e+05, 2.87463031e+05, 3.12387094e+05, 2.99962500e+05, 2.87463031e+05, 3.12387094e+05, 2.99962500e+05, 2.87463031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.12387094e+05, 2.87463031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94710344e+05, 2.94695812e+05, 2.94771406e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94710344e+05, 2.93349719e+05, 2.96070938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.06855031e+05, 2.94708906e+05, 2.82451406e+05, 3.06855031e+05, 2.94708906e+05, 2.82451406e+05, 3.06855031e+05, 2.94708906e+05, 2.82451406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.06855031e+05, 2.82451406e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1225198034), # 1.23GB, avg file size 1.23GB
  ("fsize_db",                        12822147007), # 12.82GB, avg file size 2.56GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00043250e+05, 3.00016312e+05, 3.00048594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15243625e+05, 3.00042812e+05, 2.85255562e+05, 3.15243625e+05, 3.00042812e+05, 2.85255562e+05, 3.15243625e+05, 3.00042812e+05, 2.85255562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15243625e+05, 2.85255562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94366438e+05, 2.94338438e+05, 2.94382688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94366438e+05, 2.92913719e+05, 2.95812094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.09249719e+05, 2.94364719e+05, 2.79908469e+05, 3.09249719e+05, 2.94364719e+05, 2.79908469e+05, 3.09249719e+05, 2.94364719e+05, 2.79908469e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.09249719e+05, 2.79908469e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1293984527), # 1.29GB, avg file size 1.29GB
  ("fsize_db",                        13147855533), # 13.15GB, avg file size 2.63GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 292028, ],
    'CountWeighted'                                                                  : [ 2.92001938e+05, 2.92030562e+05, 2.92061031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09283125e+05, 2.92001469e+05, 2.75798438e+05, 3.09283125e+05, 2.92001469e+05, 2.75798438e+05, 3.09283125e+05, 2.92001469e+05, 2.75798438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09283125e+05, 2.75798438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.86163719e+05, 2.86169719e+05, 2.86206250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.86163719e+05, 2.84680062e+05, 2.87649312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.03034250e+05, 2.86162000e+05, 2.70308125e+05, 3.03034250e+05, 2.86162000e+05, 2.70308125e+05, 3.03034250e+05, 2.86162000e+05, 2.70308125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03034250e+05, 2.70308125e+05, ],
  }),
  ("nof_tree_events",                 292028),
  ("nof_db_events",                   292028),
  ("fsize_local",                     1317629915), # 1.32GB, avg file size 1.32GB
  ("fsize_db",                        13118198421), # 13.12GB, avg file size 3.28GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.99986000e+05, 3.00030219e+05, 2.99912562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.19912969e+05, 2.99985875e+05, 2.81667938e+05, 3.19912969e+05, 2.99985875e+05, 2.81667938e+05, 3.19912969e+05, 2.99985875e+05, 2.81667938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.19912969e+05, 2.81667938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93637688e+05, 2.93659875e+05, 2.93591500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93637688e+05, 2.92040094e+05, 2.95231656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.13081438e+05, 2.93636625e+05, 2.75737000e+05, 3.13081438e+05, 2.93636625e+05, 2.75737000e+05, 3.13081438e+05, 2.93636625e+05, 2.75737000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.13081438e+05, 2.75737000e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1408216758), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        13799384403), # 13.80GB, avg file size 2.76GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 3.00055281e+05, 2.99982438e+05, 2.99984812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.21847531e+05, 3.00055094e+05, 2.80185031e+05, 3.21847531e+05, 3.00055094e+05, 2.80185031e+05, 3.21847531e+05, 3.00055094e+05, 2.80185031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.21847531e+05, 2.80185031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93490250e+05, 2.93446812e+05, 2.93453812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93490250e+05, 2.91852438e+05, 2.95126312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.14776906e+05, 2.93488438e+05, 2.74117406e+05, 3.14776906e+05, 2.93488438e+05, 2.74117406e+05, 3.14776906e+05, 2.93488438e+05, 2.74117406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.14776906e+05, 2.74117406e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1453233058), # 1.45GB, avg file size 1.45GB
  ("fsize_db",                        13970691602), # 13.97GB, avg file size 3.49GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00036156e+05, 3.00028000e+05, 3.00050844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.23625344e+05, 3.00027938e+05, 2.78845469e+05, 3.23625344e+05, 3.00027938e+05, 2.78845469e+05, 3.23625344e+05, 3.00027938e+05, 2.78845469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.23625344e+05, 2.78845469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93188875e+05, 2.93184594e+05, 2.93202875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93188875e+05, 2.91493531e+05, 2.94888812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.16203531e+05, 2.93182406e+05, 2.72542219e+05, 3.16203531e+05, 2.93182406e+05, 2.72542219e+05, 3.16203531e+05, 2.93182406e+05, 2.72542219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.16203531e+05, 2.72542219e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1489188811), # 1.49GB, avg file size 1.49GB
  ("fsize_db",                        14217239886), # 14.22GB, avg file size 2.84GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-700_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99993156e+05, 2.99939844e+05, 3.00040438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.26693250e+05, 2.99991844e+05, 2.76553344e+05, 3.26693250e+05, 2.99991844e+05, 2.76553344e+05, 3.26693250e+05, 2.99991844e+05, 2.76553344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.26693250e+05, 2.76553344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92891719e+05, 2.92857875e+05, 2.92921312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92891719e+05, 2.91137875e+05, 2.94642344e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.18912406e+05, 2.92889625e+05, 2.70042156e+05, 3.18912406e+05, 2.92889625e+05, 2.70042156e+05, 3.18912406e+05, 2.92889625e+05, 2.70042156e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.18912406e+05, 2.70042156e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1537468981), # 1.54GB, avg file size 1.54GB
  ("fsize_db",                        14467187735), # 14.47GB, avg file size 3.62GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_700_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00038781e+05, 2.99921438e+05, 2.99937406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.29331188e+05, 3.00037312e+05, 2.74610031e+05, 3.29331188e+05, 3.00037312e+05, 2.74610031e+05, 3.29331188e+05, 3.00037312e+05, 2.74610031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.29331188e+05, 2.74610031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92683500e+05, 2.92615562e+05, 2.92634219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92683500e+05, 2.90889719e+05, 2.94485219e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.21237719e+05, 2.92681000e+05, 2.67932125e+05, 3.21237719e+05, 2.92681000e+05, 2.67932125e+05, 3.21237719e+05, 2.92681000e+05, 2.67932125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.21237719e+05, 2.67932125e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1567182785), # 1.57GB, avg file size 1.57GB
  ("fsize_db",                        14975865562), # 14.98GB, avg file size 3.00GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99925688e+05, 2.99943000e+05, 3.00017750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.31701594e+05, 2.99925156e+05, 2.72913281e+05, 3.31701594e+05, 2.99925156e+05, 2.72913281e+05, 3.31701594e+05, 2.99925156e+05, 2.72913281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.31701594e+05, 2.72913281e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92412844e+05, 2.92421656e+05, 2.92467969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92412844e+05, 2.90576031e+05, 2.94250312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.23309469e+05, 2.92410844e+05, 2.66087125e+05, 3.23309469e+05, 2.92410844e+05, 2.66087125e+05, 3.23309469e+05, 2.92410844e+05, 2.66087125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.23309469e+05, 2.66087125e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1586339116), # 1.59GB, avg file size 1.59GB
  ("fsize_db",                        15010963358), # 15.01GB, avg file size 3.75GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2WToLNu2J_M-1000_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299469, ],
    'CountWeighted'                                                                  : [ 2.99440719e+05, 2.99493031e+05, 2.99481500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.33191812e+05, 2.99439312e+05, 2.70988562e+05, 3.33191812e+05, 2.99439312e+05, 2.70988562e+05, 3.33191812e+05, 2.99439312e+05, 2.70988562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.33191812e+05, 2.70988562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91879375e+05, 2.91900500e+05, 2.91908812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91879375e+05, 2.90037562e+05, 2.93720438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.24709625e+05, 2.91876812e+05, 2.64156406e+05, 3.24709625e+05, 2.91876812e+05, 2.64156406e+05, 3.24709625e+05, 2.91876812e+05, 2.64156406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.24709625e+05, 2.64156406e+05, ],
  }),
  ("nof_tree_events",                 299469),
  ("nof_db_events",                   299469),
  ("fsize_local",                     1595907094), # 1.60GB, avg file size 1.60GB
  ("fsize_db",                        15303436616), # 15.30GB, avg file size 3.06GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_1000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99981875e+05, 3.00053719e+05, 3.00018938e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.04802969e+05, 2.99966844e+05, 2.93478531e+05, 3.04802969e+05, 2.99966844e+05, 2.93478531e+05, 3.04802969e+05, 2.99966844e+05, 2.93478531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.04802969e+05, 2.93478531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.95870062e+05, 2.95908031e+05, 2.95903125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.95870062e+05, 2.94769656e+05, 2.96963094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.00589812e+05, 2.95859125e+05, 2.89472094e+05, 3.00589812e+05, 2.95859125e+05, 2.89472094e+05, 3.00589812e+05, 2.95859125e+05, 2.89472094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.00589812e+05, 2.89472094e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1074362254), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        12270543882), # 12.27GB, avg file size 2.45GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00001250e+05, 3.00018719e+05, 3.00031750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.05778031e+05, 2.99997812e+05, 2.92707406e+05, 3.05778031e+05, 2.99997812e+05, 2.92707406e+05, 3.05778031e+05, 2.99997812e+05, 2.92707406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.05778031e+05, 2.92707406e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.95710844e+05, 2.95717031e+05, 2.95736156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.95710844e+05, 2.94570594e+05, 2.96844750e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01374875e+05, 2.95707344e+05, 2.88549438e+05, 3.01374875e+05, 2.95707344e+05, 2.88549438e+05, 3.01374875e+05, 2.95707344e+05, 2.88549438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01374875e+05, 2.88549438e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1098016909), # 1.10GB, avg file size 1.10GB
  ("fsize_db",                        12407686965), # 12.41GB, avg file size 3.10GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299231, ],
    'CountWeighted'                                                                  : [ 2.99186156e+05, 2.99233688e+05, 2.99213062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.05821656e+05, 2.99183969e+05, 2.91287875e+05, 3.05821656e+05, 2.99183969e+05, 2.91287875e+05, 3.05821656e+05, 2.99183969e+05, 2.91287875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.05821656e+05, 2.91287875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94792750e+05, 2.94811469e+05, 2.94816156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94792750e+05, 2.93624000e+05, 2.95955562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01279281e+05, 2.94789875e+05, 2.87022656e+05, 3.01279281e+05, 2.94789875e+05, 2.87022656e+05, 3.01279281e+05, 2.94789875e+05, 2.87022656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01279281e+05, 2.87022656e+05, ],
  }),
  ("nof_tree_events",                 299231),
  ("nof_db_events",                   299231),
  ("fsize_local",                     1117533847), # 1.12GB, avg file size 1.12GB
  ("fsize_db",                        12387077839), # 12.39GB, avg file size 2.48GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 3.00016312e+05, 3.00022750e+05, 3.00035281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08977375e+05, 3.00016031e+05, 2.90135406e+05, 3.08977375e+05, 3.00016031e+05, 2.90135406e+05, 3.08977375e+05, 3.00016031e+05, 2.90135406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08977375e+05, 2.90135406e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.95190500e+05, 2.95189500e+05, 2.95218219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.95190500e+05, 2.93933812e+05, 2.96448312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.03980250e+05, 2.95189000e+05, 2.85510906e+05, 3.03980250e+05, 2.95189000e+05, 2.85510906e+05, 3.03980250e+05, 2.95189000e+05, 2.85510906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03980250e+05, 2.85510906e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1182854646), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        12692339481), # 12.69GB, avg file size 3.17GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299402, ],
    'CountWeighted'                                                                  : [ 2.99391000e+05, 2.99360938e+05, 2.99427781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11775438e+05, 2.99390688e+05, 2.86878094e+05, 3.11775438e+05, 2.99390688e+05, 2.86878094e+05, 3.11775438e+05, 2.99390688e+05, 2.86878094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11775438e+05, 2.86878094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94080938e+05, 2.94057156e+05, 2.94104781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94080938e+05, 2.92709312e+05, 2.95446656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.06188719e+05, 2.94079438e+05, 2.81822875e+05, 3.06188719e+05, 2.94079438e+05, 2.81822875e+05, 3.06188719e+05, 2.94079438e+05, 2.81822875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.06188719e+05, 2.81822875e+05, ],
  }),
  ("nof_tree_events",                 299402),
  ("nof_db_events",                   299402),
  ("fsize_local",                     1270497671), # 1.27GB, avg file size 1.27GB
  ("fsize_db",                        13215909741), # 13.22GB, avg file size 3.30GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299993, ],
    'CountWeighted'                                                                  : [ 3.00003250e+05, 2.99966906e+05, 3.00004000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15254750e+05, 3.00003094e+05, 2.85218906e+05, 3.15254750e+05, 3.00003094e+05, 2.85218906e+05, 3.15254750e+05, 3.00003094e+05, 2.85218906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15254750e+05, 2.85218906e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94440531e+05, 2.94422719e+05, 2.94439312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94440531e+05, 2.93025656e+05, 2.95853219e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.09351969e+05, 2.94439219e+05, 2.79978844e+05, 3.09351969e+05, 2.94439219e+05, 2.79978844e+05, 3.09351969e+05, 2.94439219e+05, 2.79978844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.09351969e+05, 2.79978844e+05, ],
  }),
  ("nof_tree_events",                 299993),
  ("nof_db_events",                   299993),
  ("fsize_local",                     1347999215), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        13636388128), # 13.64GB, avg file size 3.41GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 3.00060719e+05, 3.00089719e+05, 3.00008875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17722062e+05, 3.00059969e+05, 2.83331844e+05, 3.17722062e+05, 3.00059969e+05, 2.83331844e+05, 3.17722062e+05, 3.00059969e+05, 2.83331844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17722062e+05, 2.83331844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94234438e+05, 2.94247375e+05, 2.94201031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94234438e+05, 2.92772156e+05, 2.95691844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.11517031e+05, 2.94232594e+05, 2.77892812e+05, 3.11517031e+05, 2.94232594e+05, 2.77892812e+05, 3.11517031e+05, 2.94232594e+05, 2.77892812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.11517031e+05, 2.77892812e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1413733232), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        13995682190), # 14.00GB, avg file size 2.80GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00073406e+05, 2.99948406e+05, 2.99979094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.19929594e+05, 3.00053406e+05, 2.81658125e+05, 3.19929594e+05, 3.00053406e+05, 2.81658125e+05, 3.19929594e+05, 3.00053406e+05, 2.81658125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.19929594e+05, 2.81658125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94141500e+05, 2.94063875e+05, 2.94085125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94141500e+05, 2.92662812e+05, 2.95618156e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.13567938e+05, 2.94126938e+05, 2.76157906e+05, 3.13567938e+05, 2.94126938e+05, 2.76157906e+05, 3.13567938e+05, 2.94126938e+05, 2.76157906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.13567938e+05, 2.76157906e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1471806109), # 1.47GB, avg file size 1.47GB
  ("fsize_db",                        14208882340), # 14.21GB, avg file size 3.55GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299995, ],
    'CountWeighted'                                                                  : [ 3.00071938e+05, 3.00041562e+05, 3.00024844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.21859812e+05, 3.00070312e+05, 2.80175781e+05, 3.21859812e+05, 3.00070312e+05, 2.80175781e+05, 3.21859812e+05, 3.00070312e+05, 2.80175781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.21859812e+05, 2.80175781e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94072812e+05, 2.94047938e+05, 2.94054562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94072812e+05, 2.92591625e+05, 2.95552062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.15398219e+05, 2.94070531e+05, 2.74641188e+05, 3.15398219e+05, 2.94070531e+05, 2.74641188e+05, 3.15398219e+05, 2.94070531e+05, 2.74641188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.15398219e+05, 2.74641188e+05, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1516104546), # 1.52GB, avg file size 1.52GB
  ("fsize_db",                        14478664969), # 14.48GB, avg file size 3.62GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299995, ],
    'CountWeighted'                                                                  : [ 2.99952375e+05, 3.00020656e+05, 2.99984062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.23629375e+05, 2.99949281e+05, 2.78843625e+05, 3.23629375e+05, 2.99949281e+05, 2.78843625e+05, 3.23629375e+05, 2.99949281e+05, 2.78843625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.23629375e+05, 2.78843625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94022125e+05, 2.94056844e+05, 2.94044188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94022125e+05, 2.92552469e+05, 2.95488469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.17155719e+05, 2.94018656e+05, 2.73354062e+05, 3.17155719e+05, 2.94018656e+05, 2.73354062e+05, 3.17155719e+05, 2.94018656e+05, 2.73354062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.17155719e+05, 2.73354062e+05, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1550329113), # 1.55GB, avg file size 1.55GB
  ("fsize_db",                        14654413374), # 14.65GB, avg file size 3.66GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.99998656e+05, 2.99968875e+05, 3.00002031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.25219812e+05, 2.99989969e+05, 2.77677969e+05, 3.25219812e+05, 2.99989969e+05, 2.77677969e+05, 3.25219812e+05, 2.99989969e+05, 2.77677969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.25219812e+05, 2.77677969e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94116031e+05, 2.94075500e+05, 2.94140312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94116031e+05, 2.92669594e+05, 2.95565125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.18794250e+05, 2.94109312e+05, 2.72263125e+05, 3.18794250e+05, 2.94109312e+05, 2.72263125e+05, 3.18794250e+05, 2.94109312e+05, 2.72263125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.18794250e+05, 2.72263125e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1573528484), # 1.57GB, avg file size 1.57GB
  ("fsize_db",                        14989654961), # 14.99GB, avg file size 3.00GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-700_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299995, ],
    'CountWeighted'                                                                  : [ 2.99979156e+05, 2.99989594e+05, 2.99944562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.26708906e+05, 2.99978844e+05, 2.76575938e+05, 3.26708906e+05, 2.99978844e+05, 2.76575938e+05, 3.26708906e+05, 2.99978844e+05, 2.76575938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.26708906e+05, 2.76575938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93984156e+05, 2.93985500e+05, 2.93973531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93984156e+05, 2.92512375e+05, 2.95453562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.20129250e+05, 2.93982375e+05, 2.71068000e+05, 3.20129250e+05, 2.93982375e+05, 2.71068000e+05, 3.20129250e+05, 2.93982375e+05, 2.71068000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.20129250e+05, 2.71068000e+05, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1588405658), # 1.59GB, avg file size 1.59GB
  ("fsize_db",                        15100949761), # 15.10GB, avg file size 3.02GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_700_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99962188e+05, 3.00054312e+05, 2.99991156e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.29359500e+05, 2.99961125e+05, 2.74621219e+05, 3.29359500e+05, 2.99961125e+05, 2.74621219e+05, 3.29359500e+05, 2.99961125e+05, 2.74621219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.29359500e+05, 2.74621219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94051312e+05, 2.94101688e+05, 2.94072000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94051312e+05, 2.92604250e+05, 2.95494969e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.22816906e+05, 2.94049406e+05, 2.69222125e+05, 3.22816906e+05, 2.94049406e+05, 2.69222125e+05, 3.22816906e+05, 2.94049406e+05, 2.69222125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.22816906e+05, 2.69222125e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1607007027), # 1.61GB, avg file size 1.61GB
  ("fsize_db",                        15643527631), # 15.64GB, avg file size 2.61GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00046625e+05, 2.99967750e+05, 3.00037344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.31688500e+05, 3.00041594e+05, 2.72952344e+05, 3.31688500e+05, 3.00041594e+05, 2.72952344e+05, 3.31688500e+05, 3.00041594e+05, 2.72952344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.31688500e+05, 2.72952344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94209031e+05, 2.94158844e+05, 2.94203188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94209031e+05, 2.92794875e+05, 2.95625781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.25221188e+05, 2.94204125e+05, 2.67670656e+05, 3.25221188e+05, 2.94204125e+05, 2.67670656e+05, 3.25221188e+05, 2.94204125e+05, 2.67670656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.25221188e+05, 2.67670656e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1616754115), # 1.62GB, avg file size 1.62GB
  ("fsize_db",                        15836490873), # 15.84GB, avg file size 2.64GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_900_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1000_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 3.00051812e+05, 2.99918875e+05, 3.00028562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.33739375e+05, 3.00051375e+05, 2.71428781e+05, 3.33739375e+05, 3.00051375e+05, 2.71428781e+05, 3.33739375e+05, 3.00051375e+05, 2.71428781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.33739375e+05, 2.71428781e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94227094e+05, 2.94130219e+05, 2.94224438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94227094e+05, 2.92820812e+05, 2.95638250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.27264938e+05, 2.94225344e+05, 2.66193812e+05, 3.27264938e+05, 2.94225344e+05, 2.66193812e+05, 3.27264938e+05, 2.94225344e+05, 2.66193812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.27264938e+05, 2.66193812e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1620757264), # 1.62GB, avg file size 1.62GB
  ("fsize_db",                        15848133420), # 15.85GB, avg file size 3.17GB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_1000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 5.00004961e+04, 4.99962109e+04, 4.99960508e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.08067930e+04, 5.00004961e+04, 4.89079375e+04, 5.08067930e+04, 5.00004961e+04, 4.89079375e+04, 5.08067930e+04, 5.00004961e+04, 4.89079375e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.08067930e+04, 4.89079375e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.92945859e+04, 4.92879219e+04, 4.92960781e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.92945859e+04, 4.91051836e+04, 4.94820195e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.00841094e+04, 4.92945859e+04, 4.82226328e+04, 5.00841094e+04, 4.92945859e+04, 4.82226328e+04, 5.00841094e+04, 4.92945859e+04, 4.82226328e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.00841094e+04, 4.82226328e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     177837984), # 177.84MB, avg file size 177.84MB
  ("fsize_db",                        1962681716), # 1.96GB, avg file size 1.96GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99985625e+04, 4.99957734e+04, 5.00009102e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09554883e+04, 4.99985625e+04, 4.87873086e+04, 5.09554883e+04, 4.99985625e+04, 4.87873086e+04, 5.09554883e+04, 4.99985625e+04, 4.87873086e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09554883e+04, 4.87873086e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.92794922e+04, 4.92754492e+04, 4.92835352e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.92794922e+04, 4.90874609e+04, 4.94703203e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.02159102e+04, 4.92794922e+04, 4.80905195e+04, 5.02159102e+04, 4.92794922e+04, 4.80905195e+04, 5.02159102e+04, 4.92794922e+04, 4.80905195e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.02159102e+04, 4.80905195e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     180616405), # 180.62MB, avg file size 180.62MB
  ("fsize_db",                        1978376178), # 1.98GB, avg file size 1.98GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99956719e+04, 5.00031836e+04, 4.99969922e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.11025000e+04, 4.99956719e+04, 4.86689102e+04, 5.11025000e+04, 4.99956719e+04, 4.86689102e+04, 5.11025000e+04, 4.99956719e+04, 4.86689102e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.11025000e+04, 4.86689102e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.92400820e+04, 4.92459883e+04, 4.92392891e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.92400820e+04, 4.90385781e+04, 4.94400156e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.03224766e+04, 4.92400820e+04, 4.79375117e+04, 5.03224766e+04, 4.92400820e+04, 4.79375117e+04, 5.03224766e+04, 4.92400820e+04, 4.79375117e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.03224766e+04, 4.79375117e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     183385152), # 183.39MB, avg file size 183.39MB
  ("fsize_db",                        1992599467), # 1.99GB, avg file size 1.99GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 49600, ],
    'CountWeighted'                                                                  : [ 4.96062617e+04, 4.95981367e+04, 4.96031719e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.08284336e+04, 4.96062617e+04, 4.81748672e+04, 5.08284336e+04, 4.96062617e+04, 4.81748672e+04, 5.08284336e+04, 4.96062617e+04, 4.81748672e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.08284336e+04, 4.81748672e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.88458828e+04, 4.88360000e+04, 4.88483164e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.88458828e+04, 4.86452031e+04, 4.90454922e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.00450977e+04, 4.88458828e+04, 4.74442500e+04, 5.00450977e+04, 4.88458828e+04, 4.74442500e+04, 5.00450977e+04, 4.88458828e+04, 4.74442500e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.00450977e+04, 4.74442500e+04, ],
  }),
  ("nof_tree_events",                 49600),
  ("nof_db_events",                   49600),
  ("fsize_local",                     184735035), # 184.74MB, avg file size 184.74MB
  ("fsize_db",                        1985262651), # 1.99GB, avg file size 1.99GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 450000, ],
    'CountWeighted'                                                                  : [ 4.50044156e+05, 4.50015906e+05, 4.49953688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.63471656e+05, 4.50044156e+05, 4.35231219e+05, 4.63471656e+05, 4.50044156e+05, 4.35231219e+05, 4.63471656e+05, 4.50044156e+05, 4.35231219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.63471656e+05, 4.35231219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.42707812e+05, 4.42677562e+05, 4.42675844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 4.42707812e+05, 4.40789750e+05, 4.44624156e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.55872031e+05, 4.42707812e+05, 4.28202094e+05, 4.55872031e+05, 4.42707812e+05, 4.28202094e+05, 4.55872031e+05, 4.42707812e+05, 4.28202094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.55872031e+05, 4.28202094e+05, ],
  }),
  ("nof_tree_events",                 450000),
  ("nof_db_events",                   450000),
  ("fsize_local",                     1711626676), # 1.71GB, avg file size 1.71GB
  ("fsize_db",                        18335508201), # 18.34GB, avg file size 2.62GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99961641e+04, 5.00030859e+04, 4.99990508e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.17312656e+04, 4.99961641e+04, 4.81711562e+04, 5.17312656e+04, 4.99961641e+04, 4.81711562e+04, 5.17312656e+04, 4.99961641e+04, 4.81711562e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.17312656e+04, 4.81711562e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.91457734e+04, 4.91503203e+04, 4.91465000e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.91457734e+04, 4.89240000e+04, 4.93671328e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.08421758e+04, 4.91457734e+04, 4.73565430e+04, 5.08421758e+04, 4.91457734e+04, 4.73565430e+04, 5.08421758e+04, 4.91457734e+04, 4.73565430e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.08421758e+04, 4.73565430e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     196546883), # 196.55MB, avg file size 196.55MB
  ("fsize_db",                        2102297139), # 2.10GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-340_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_340_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_340_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 48000, ],
    'CountWeighted'                                                                  : [ 4.79970547e+04, 4.80009297e+04, 4.79989375e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.98809844e+04, 4.79970547e+04, 4.60727812e+04, 4.98809844e+04, 4.79970547e+04, 4.60727812e+04, 4.98809844e+04, 4.79970547e+04, 4.60727812e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.98809844e+04, 4.60727812e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.71319570e+04, 4.71350977e+04, 4.71318750e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.71319570e+04, 4.69077852e+04, 4.73555195e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.89730781e+04, 4.71319570e+04, 4.52472578e+04, 4.89730781e+04, 4.71319570e+04, 4.52472578e+04, 4.89730781e+04, 4.71319570e+04, 4.52472578e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.89730781e+04, 4.52472578e+04, ],
  }),
  ("nof_tree_events",                 48000),
  ("nof_db_events",                   48000),
  ("fsize_local",                     192759782), # 192.76MB, avg file size 192.76MB
  ("fsize_db",                        1955847184), # 1.96GB, avg file size 1.96GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99891992e+04, 4.99920312e+04, 5.00018867e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.20619336e+04, 4.99891992e+04, 4.79127891e+04, 5.20619336e+04, 4.99891992e+04, 4.79127891e+04, 5.20619336e+04, 4.99891992e+04, 4.79127891e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.20619336e+04, 4.79127891e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.90911133e+04, 4.90906133e+04, 4.91003945e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.90911133e+04, 4.88578320e+04, 4.93234805e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.11141680e+04, 4.90911133e+04, 4.70537344e+04, 5.11141680e+04, 4.90911133e+04, 4.70537344e+04, 5.11141680e+04, 4.90911133e+04, 4.70537344e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.11141680e+04, 4.70537344e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     203493121), # 203.49MB, avg file size 203.49MB
  ("fsize_db",                        2167356346), # 2.17GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 250000, ],
    'CountWeighted'                                                                  : [ 2.49983250e+05, 2.50019750e+05, 2.49980344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.62684344e+05, 2.49983250e+05, 2.37709219e+05, 2.62684344e+05, 2.49983250e+05, 2.37709219e+05, 2.62684344e+05, 2.49983250e+05, 2.37709219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.62684344e+05, 2.37709219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.45060859e+05, 2.45069422e+05, 2.45069125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.45060859e+05, 2.43804891e+05, 2.46311797e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.57459078e+05, 2.45060859e+05, 2.33055625e+05, 2.57459078e+05, 2.45060859e+05, 2.33055625e+05, 2.57459078e+05, 2.45060859e+05, 2.33055625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.57459078e+05, 2.33055625e+05, ],
  }),
  ("nof_tree_events",                 250000),
  ("nof_db_events",                   250000),
  ("fsize_local",                     1061832745), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        10749996877), # 10.75GB, avg file size 3.58GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 99600, ],
    'CountWeighted'                                                                  : [ 9.96111719e+04, 9.95947578e+04, 9.96359531e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.05484711e+05, 9.96111719e+04, 9.40629688e+04, 1.05484711e+05, 9.96111719e+04, 9.40629688e+04, 1.05484711e+05, 9.96111719e+04, 9.40629688e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.05484711e+05, 9.40629688e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.75119219e+04, 9.75100781e+04, 9.75207266e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.75119219e+04, 9.69857578e+04, 9.80388672e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.03246703e+05, 9.75119219e+04, 9.21012734e+04, 1.03246703e+05, 9.75119219e+04, 9.21012734e+04, 1.03246703e+05, 9.75119219e+04, 9.21012734e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.03246703e+05, 9.21012734e+04, ],
  }),
  ("nof_tree_events",                 99600),
  ("nof_db_events",                   99600),
  ("fsize_local",                     441757756), # 441.76MB, avg file size 441.76MB
  ("fsize_db",                        4411305292), # 4.41GB, avg file size 2.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 99200, ],
    'CountWeighted'                                                                  : [ 9.92069922e+04, 9.91855625e+04, 9.92116562e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.05773242e+05, 9.92069922e+04, 9.31336406e+04, 1.05773242e+05, 9.92069922e+04, 9.31336406e+04, 1.05773242e+05, 9.92069922e+04, 9.31336406e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.05773242e+05, 9.31336406e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70280234e+04, 9.70142734e+04, 9.70355469e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70280234e+04, 9.64839609e+04, 9.75723359e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.03436820e+05, 9.70280234e+04, 9.11060938e+04, 1.03436820e+05, 9.70280234e+04, 9.11060938e+04, 1.03436820e+05, 9.70280234e+04, 9.11060938e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.03436820e+05, 9.11060938e+04, ],
  }),
  ("nof_tree_events",                 99200),
  ("nof_db_events",                   99200),
  ("fsize_local",                     455567820), # 455.57MB, avg file size 455.57MB
  ("fsize_db",                        4435751146), # 4.44GB, avg file size 2.22GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 1.00021023e+05, 1.00010656e+05, 9.99742578e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.07278258e+05, 1.00021023e+05, 9.34015859e+04, 1.07278258e+05, 1.00021023e+05, 9.34015859e+04, 1.07278258e+05, 1.00021023e+05, 9.34015859e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.07278258e+05, 9.34015859e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.77679297e+04, 9.77588516e+04, 9.77447500e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.77679297e+04, 9.72088281e+04, 9.83279766e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.04851039e+05, 9.77679297e+04, 9.13202734e+04, 1.04851039e+05, 9.77679297e+04, 9.13202734e+04, 1.04851039e+05, 9.77679297e+04, 9.13202734e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.04851039e+05, 9.13202734e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     474005400), # 474.01MB, avg file size 474.01MB
  ("fsize_db",                        4499327267), # 4.50GB, avg file size 2.25GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 1.00009977e+05, 9.99968438e+04, 1.00000633e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.07866102e+05, 1.00009977e+05, 9.29560312e+04, 1.07866102e+05, 1.00009977e+05, 9.29560312e+04, 1.07866102e+05, 1.00009977e+05, 9.29560312e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.07866102e+05, 9.29560312e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.76527422e+04, 9.76457188e+04, 9.76474141e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.76527422e+04, 9.70713594e+04, 9.82351484e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.05311211e+05, 9.76527422e+04, 9.07827031e+04, 1.05311211e+05, 9.76527422e+04, 9.07827031e+04, 1.05311211e+05, 9.76527422e+04, 9.07827031e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.05311211e+05, 9.07827031e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     485611003), # 485.61MB, avg file size 485.61MB
  ("fsize_db",                        4581235338), # 4.58GB, avg file size 2.29GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99918203e+04, 9.99976797e+04, 1.00029984e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.08412891e+05, 9.99918203e+04, 9.25538125e+04, 1.08412891e+05, 9.99918203e+04, 9.25538125e+04, 1.08412891e+05, 9.99918203e+04, 9.25538125e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.08412891e+05, 9.25538125e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.76226719e+04, 9.76226328e+04, 9.76459609e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.76226719e+04, 9.70387109e+04, 9.82078125e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.05820281e+05, 9.76226719e+04, 9.03716797e+04, 1.05820281e+05, 9.76226719e+04, 9.03716797e+04, 1.05820281e+05, 9.76226719e+04, 9.03716797e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.05820281e+05, 9.03716797e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     495478356), # 495.48MB, avg file size 495.48MB
  ("fsize_db",                        4742625025), # 4.74GB, avg file size 2.37GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99930547e+04, 9.99925781e+04, 1.00006227e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.09795266e+05, 9.99930547e+04, 9.15391016e+04, 1.09795266e+05, 9.99930547e+04, 9.15391016e+04, 1.09795266e+05, 9.99930547e+04, 9.15391016e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.09795266e+05, 9.15391016e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.74896953e+04, 9.74847266e+04, 9.75003516e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.74896953e+04, 9.68792578e+04, 9.80996172e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07022219e+05, 9.74896953e+04, 8.92561719e+04, 1.07022219e+05, 9.74896953e+04, 8.92561719e+04, 1.07022219e+05, 9.74896953e+04, 8.92561719e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07022219e+05, 8.92561719e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     515974652), # 515.97MB, avg file size 515.97MB
  ("fsize_db",                        4845795202), # 4.85GB, avg file size 2.42GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99923672e+04, 9.99841641e+04, 9.99723906e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.10555406e+05, 9.99923672e+04, 9.09830391e+04, 1.10555406e+05, 9.99923672e+04, 9.09830391e+04, 1.10555406e+05, 9.99923672e+04, 9.09830391e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10555406e+05, 9.09830391e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.74546953e+04, 9.74455391e+04, 9.74496016e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.74546953e+04, 9.68374531e+04, 9.80725625e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07729617e+05, 9.74546953e+04, 8.86819922e+04, 1.07729617e+05, 9.74546953e+04, 8.86819922e+04, 1.07729617e+05, 9.74546953e+04, 8.86819922e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07729617e+05, 8.86819922e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     526084675), # 526.08MB, avg file size 526.08MB
  ("fsize_db",                        4858199935), # 4.86GB, avg file size 2.43GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99999336e+04, 4.99944219e+04, 4.99981328e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.08095352e+04, 4.99999336e+04, 4.89053164e+04, 5.08095352e+04, 4.99999336e+04, 4.89053164e+04, 5.08095352e+04, 4.99999336e+04, 4.89053164e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.08095352e+04, 4.89053164e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.92780391e+04, 4.92742031e+04, 4.92777969e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.92780391e+04, 4.90855234e+04, 4.94693320e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.00710156e+04, 4.92780391e+04, 4.82042695e+04, 5.00710156e+04, 4.92780391e+04, 4.82042695e+04, 5.00710156e+04, 4.92780391e+04, 4.82042695e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.00710156e+04, 4.82042695e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     180561425), # 180.56MB, avg file size 180.56MB
  ("fsize_db",                        1970267888), # 1.97GB, avg file size 1.97GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99954844e+04, 5.00047188e+04, 5.00029883e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09536797e+04, 4.99954844e+04, 4.87904492e+04, 5.09536797e+04, 4.99954844e+04, 4.87904492e+04, 5.09536797e+04, 4.99954844e+04, 4.87904492e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09536797e+04, 4.87904492e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.92452383e+04, 4.92512617e+04, 4.92497070e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.92452383e+04, 4.90461016e+04, 4.94431055e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.01811914e+04, 4.92452383e+04, 4.80618047e+04, 5.01811914e+04, 4.92452383e+04, 4.80618047e+04, 5.01811914e+04, 4.92452383e+04, 4.80618047e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.01811914e+04, 4.80618047e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     183747367), # 183.75MB, avg file size 183.75MB
  ("fsize_db",                        2021288641), # 2.02GB, avg file size 2.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99971992e+04, 5.00016445e+04, 5.00007305e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10999062e+04, 4.99971992e+04, 4.86721484e+04, 5.10999062e+04, 4.99971992e+04, 4.86721484e+04, 5.10999062e+04, 4.99971992e+04, 4.86721484e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10999062e+04, 4.86721484e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.92104258e+04, 4.92121289e+04, 4.92133594e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.92104258e+04, 4.90023867e+04, 4.94171289e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.02881211e+04, 4.92104258e+04, 4.79104570e+04, 5.02881211e+04, 4.92104258e+04, 4.79104570e+04, 5.02881211e+04, 4.92104258e+04, 4.79104570e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.02881211e+04, 4.79104570e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     187401636), # 187.40MB, avg file size 187.40MB
  ("fsize_db",                        2049006927), # 2.05GB, avg file size 2.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99960508e+04, 4.99992852e+04, 4.99952617e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12384922e+04, 4.99960508e+04, 4.85585898e+04, 5.12384922e+04, 4.99960508e+04, 4.85585898e+04, 5.12384922e+04, 4.99960508e+04, 4.85585898e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12384922e+04, 4.85585898e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.91884648e+04, 4.91908125e+04, 4.91879375e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.91884648e+04, 4.89765742e+04, 4.93989180e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.04028008e+04, 4.91884648e+04, 4.77795352e+04, 5.04028008e+04, 4.91884648e+04, 4.77795352e+04, 5.04028008e+04, 4.91884648e+04, 4.77795352e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.04028008e+04, 4.77795352e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     190601763), # 190.60MB, avg file size 190.60MB
  ("fsize_db",                        2024724980), # 2.02GB, avg file size 2.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 447400, ],
    'CountWeighted'                                                                  : [ 4.47443719e+05, 4.47397625e+05, 4.47345062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.60789500e+05, 4.47443719e+05, 4.32711750e+05, 4.60789500e+05, 4.47443719e+05, 4.32711750e+05, 4.60789500e+05, 4.47443719e+05, 4.32711750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.60789500e+05, 4.32711750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.39952000e+05, 4.39915438e+05, 4.39905562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 4.39952000e+05, 4.38008688e+05, 4.41888656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.53023656e+05, 4.39952000e+05, 4.25540469e+05, 4.53023656e+05, 4.39952000e+05, 4.25540469e+05, 4.53023656e+05, 4.39952000e+05, 4.25540469e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.53023656e+05, 4.25540469e+05, ],
  }),
  ("nof_tree_events",                 447400),
  ("nof_db_events",                   447400),
  ("fsize_local",                     1750238552), # 1.75GB, avg file size 1.75GB
  ("fsize_db",                        18368864093), # 18.37GB, avg file size 3.67GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99915234e+04, 4.99942266e+04, 5.00011406e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.17288398e+04, 4.99915234e+04, 4.81685195e+04, 5.17288398e+04, 4.99915234e+04, 4.81685195e+04, 5.17288398e+04, 4.99915234e+04, 4.81685195e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.17288398e+04, 4.81685195e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.91310938e+04, 4.91300859e+04, 4.91400508e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.91310938e+04, 4.89079258e+04, 4.93539102e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.08283086e+04, 4.91310938e+04, 4.73442734e+04, 5.08283086e+04, 4.91310938e+04, 4.73442734e+04, 5.08283086e+04, 4.91310938e+04, 4.73442734e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.08283086e+04, 4.73442734e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     202655291), # 202.66MB, avg file size 202.66MB
  ("fsize_db",                        2056109122), # 2.06GB, avg file size 2.06GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-340_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_340_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_340_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99961758e+04, 5.00096484e+04, 5.00004766e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19581250e+04, 4.99961758e+04, 4.79925508e+04, 5.19581250e+04, 4.99961758e+04, 4.79925508e+04, 5.19581250e+04, 4.99961758e+04, 4.79925508e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19581250e+04, 4.79925508e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.91060898e+04, 4.91118633e+04, 4.91102969e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.91060898e+04, 4.88775195e+04, 4.93344102e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.10231953e+04, 4.91060898e+04, 4.71435391e+04, 5.10231953e+04, 4.91060898e+04, 4.71435391e+04, 5.10231953e+04, 4.91060898e+04, 4.71435391e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.10231953e+04, 4.71435391e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     207559742), # 207.56MB, avg file size 207.56MB
  ("fsize_db",                        2082210498), # 2.08GB, avg file size 2.08GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 5.00016406e+04, 4.99961367e+04, 5.00056016e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.20605820e+04, 5.00016406e+04, 4.79117656e+04, 5.20605820e+04, 5.00016406e+04, 4.79117656e+04, 5.20605820e+04, 5.00016406e+04, 4.79117656e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.20605820e+04, 4.79117656e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.91023047e+04, 4.90967148e+04, 4.91073945e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.91023047e+04, 4.88718555e+04, 4.93318633e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.11161172e+04, 4.91023047e+04, 4.70577461e+04, 5.11161172e+04, 4.91023047e+04, 4.70577461e+04, 5.11161172e+04, 4.91023047e+04, 4.70577461e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.11161172e+04, 4.70577461e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     210472148), # 210.47MB, avg file size 210.47MB
  ("fsize_db",                        2097870831), # 2.10GB, avg file size 2.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 250000, ],
    'CountWeighted'                                                                  : [ 2.50027125e+05, 2.49951172e+05, 2.50000734e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.62681656e+05, 2.50027125e+05, 2.37713906e+05, 2.62681656e+05, 2.50027125e+05, 2.37713906e+05, 2.62681656e+05, 2.50027125e+05, 2.37713906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.62681656e+05, 2.37713906e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.45201328e+05, 2.45153141e+05, 2.45191844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.45201328e+05, 2.43987516e+05, 2.46417047e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.57573375e+05, 2.45201328e+05, 2.33171484e+05, 2.57573375e+05, 2.45201328e+05, 2.33171484e+05, 2.57573375e+05, 2.45201328e+05, 2.33171484e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.57573375e+05, 2.33171484e+05, ],
  }),
  ("nof_tree_events",                 250000),
  ("nof_db_events",                   250000),
  ("fsize_local",                     1100085725), # 1.10GB, avg file size 1.10GB
  ("fsize_db",                        10695129460), # 10.70GB, avg file size 3.57GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99972891e+04, 9.99744609e+04, 1.00015586e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.05905758e+05, 9.99972891e+04, 9.44473203e+04, 1.05905758e+05, 9.99972891e+04, 9.44473203e+04, 1.05905758e+05, 9.99972891e+04, 9.44473203e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.05905758e+05, 9.44473203e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.80261719e+04, 9.80090938e+04, 9.80415469e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.80261719e+04, 9.75327188e+04, 9.85195547e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.03795883e+05, 9.80261719e+04, 9.25991484e+04, 1.03795883e+05, 9.80261719e+04, 9.25991484e+04, 1.03795883e+05, 9.80261719e+04, 9.25991484e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.03795883e+05, 9.25991484e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     460627321), # 460.63MB, avg file size 460.63MB
  ("fsize_db",                        4416939298), # 4.42GB, avg file size 2.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99935312e+04, 1.00014188e+05, 9.99858359e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.06625219e+05, 9.99935312e+04, 9.38950156e+04, 1.06625219e+05, 9.99935312e+04, 9.38950156e+04, 1.06625219e+05, 9.99935312e+04, 9.38950156e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.06625219e+05, 9.38950156e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.79867422e+04, 9.79939688e+04, 9.79885234e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.79867422e+04, 9.74888672e+04, 9.84857656e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.04462570e+05, 9.79867422e+04, 9.20234531e+04, 1.04462570e+05, 9.79867422e+04, 9.20234531e+04, 1.04462570e+05, 9.79867422e+04, 9.20234531e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.04462570e+05, 9.20234531e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     478071536), # 478.07MB, avg file size 478.07MB
  ("fsize_db",                        4450805287), # 4.45GB, avg file size 4.45GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99967656e+04, 1.00035820e+05, 9.99863516e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.07293383e+05, 9.99967656e+04, 9.33919844e+04, 1.07293383e+05, 9.99967656e+04, 9.33919844e+04, 1.07293383e+05, 9.99967656e+04, 9.33919844e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.07293383e+05, 9.33919844e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.79527500e+04, 9.79741562e+04, 9.79499766e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.79527500e+04, 9.74483047e+04, 9.84558750e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.05076859e+05, 9.79527500e+04, 9.14967422e+04, 1.05076859e+05, 9.79527500e+04, 9.14967422e+04, 1.05076859e+05, 9.79527500e+04, 9.14967422e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.05076859e+05, 9.14967422e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     492609060), # 492.61MB, avg file size 492.61MB
  ("fsize_db",                        4675550080), # 4.68GB, avg file size 2.34GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 1.00041055e+05, 9.99771094e+04, 1.00006789e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.07871703e+05, 1.00041055e+05, 9.29544219e+04, 1.07871703e+05, 1.00041055e+05, 9.29544219e+04, 1.07871703e+05, 1.00041055e+05, 9.29544219e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.07871703e+05, 9.29544219e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.79873906e+04, 9.79416641e+04, 9.79710078e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.79873906e+04, 9.74874531e+04, 9.84877188e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.05652469e+05, 9.79873906e+04, 9.10731797e+04, 1.05652469e+05, 9.79873906e+04, 9.10731797e+04, 1.05652469e+05, 9.79873906e+04, 9.10731797e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.05652469e+05, 9.10731797e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     504409487), # 504.41MB, avg file size 504.41MB
  ("fsize_db",                        4653469892), # 4.65GB, avg file size 2.33GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99853281e+04, 1.00024391e+05, 1.00008180e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.08412062e+05, 9.99853281e+04, 9.25504297e+04, 1.08412062e+05, 9.99853281e+04, 9.25504297e+04, 1.08412062e+05, 9.99853281e+04, 9.25504297e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.08412062e+05, 9.25504297e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.79658750e+04, 9.79881172e+04, 9.79812656e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.79658750e+04, 9.74688125e+04, 9.84608984e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06198688e+05, 9.79658750e+04, 9.06885391e+04, 1.06198688e+05, 9.79658750e+04, 9.06885391e+04, 1.06198688e+05, 9.79658750e+04, 9.06885391e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06198688e+05, 9.06885391e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     513893860), # 513.89MB, avg file size 513.89MB
  ("fsize_db",                        4740249400), # 4.74GB, avg file size 2.37GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 1.00009148e+05, 1.00004688e+05, 1.00022508e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.09360562e+05, 1.00009148e+05, 9.18487500e+04, 1.09360562e+05, 1.00009148e+05, 9.18487500e+04, 1.09360562e+05, 1.00009148e+05, 9.18487500e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.09360562e+05, 9.18487500e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.80299297e+04, 9.80268516e+04, 9.80409844e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.80299297e+04, 9.75494922e+04, 9.85133047e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07185125e+05, 9.80299297e+04, 9.00460859e+04, 1.07185125e+05, 9.80299297e+04, 9.00460859e+04, 1.07185125e+05, 9.80299297e+04, 9.00460859e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07185125e+05, 9.00460859e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     525309896), # 525.31MB, avg file size 525.31MB
  ("fsize_db",                        4895097500), # 4.90GB, avg file size 2.45GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 1.00006203e+05, 9.99863516e+04, 9.99906953e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.09784930e+05, 1.00006203e+05, 9.15392500e+04, 1.09784930e+05, 1.00006203e+05, 9.15392500e+04, 1.09784930e+05, 1.00006203e+05, 9.15392500e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.09784930e+05, 9.15392500e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.80317578e+04, 9.80146328e+04, 9.80262422e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.80317578e+04, 9.75494922e+04, 9.85127969e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07606008e+05, 9.80317578e+04, 8.97425547e+04, 1.07606008e+05, 9.80317578e+04, 8.97425547e+04, 1.07606008e+05, 9.80317578e+04, 8.97425547e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07606008e+05, 8.97425547e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     530507513), # 530.51MB, avg file size 530.51MB
  ("fsize_db",                        4784663508), # 4.78GB, avg file size 4.78GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_spin2_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 296060, ],
    'CountWeighted'                                                                  : [ 2.96005125e+05, 2.96109406e+05, 2.96123500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.18163375e+05, 2.96004031e+05, 2.76840125e+05, 3.18163375e+05, 2.96004031e+05, 2.76840125e+05, 3.18163375e+05, 2.96004031e+05, 2.76840125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.21592000e+05, 2.73454875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.85769625e+05, 2.85792812e+05, 2.85815344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.85769625e+05, 2.83175500e+05, 2.88360781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.06933719e+05, 2.85766688e+05, 2.67372750e+05, 3.06933719e+05, 2.85766688e+05, 2.67372750e+05, 3.06933719e+05, 2.85766688e+05, 2.67372750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.10302188e+05, 2.64048375e+05, ],
  }),
  ("nof_tree_events",                 296060),
  ("nof_db_events",                   296060),
  ("fsize_local",                     1259707994), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        12663197291), # 12.66GB, avg file size 2.53GB
  ("use_it",                          True),
  ("xsection",                        0.0003364547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00036250e+05, 2.99989750e+05, 3.00041156e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.26180250e+05, 3.00035406e+05, 2.77762656e+05, 3.26180250e+05, 3.00035406e+05, 2.77762656e+05, 3.26180250e+05, 3.00035406e+05, 2.77762656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.28762719e+05, 2.75224281e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.87829562e+05, 2.87814688e+05, 2.87834875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.87829562e+05, 2.84799438e+05, 2.90877062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.12727750e+05, 2.87826750e+05, 2.66641281e+05, 3.12727750e+05, 2.87826750e+05, 2.66641281e+05, 3.12727750e+05, 2.87826750e+05, 2.66641281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.15260188e+05, 2.64151281e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1278158916), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        12708206493), # 12.71GB, avg file size 3.18GB
  ("use_it",                          True),
  ("xsection",                        0.0001260006),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 257175, ],
    'CountWeighted'                                                                  : [ 2.57203594e+05, 2.57167406e+05, 2.57150234e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.78651250e+05, 2.57201547e+05, 2.38891000e+05, 2.78651250e+05, 2.57201547e+05, 2.38891000e+05, 2.78651250e+05, 2.57201547e+05, 2.38891000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.80627688e+05, 2.36948172e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.44167672e+05, 2.44161406e+05, 2.44146453e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.44167672e+05, 2.41033578e+05, 2.47318625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.64317125e+05, 2.44164797e+05, 2.26976656e+05, 2.64317125e+05, 2.44164797e+05, 2.26976656e+05, 2.64317125e+05, 2.44164797e+05, 2.26976656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.66244469e+05, 2.25080688e+05, ],
  }),
  ("nof_tree_events",                 257175),
  ("nof_db_events",                   257175),
  ("fsize_local",                     1168747990), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        11297192364), # 11.30GB, avg file size 2.82GB
  ("use_it",                          True),
  ("xsection",                        0.0001038674),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00020875e+05, 2.99917594e+05, 3.00019844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.38031156e+05, 3.00018625e+05, 2.69697312e+05, 3.38031156e+05, 3.00018625e+05, 2.69697312e+05, 3.38031156e+05, 3.00018625e+05, 2.69697312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.39162156e+05, 2.68595719e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.87115406e+05, 2.87069562e+05, 2.87124719e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.87115406e+05, 2.84056375e+05, 2.90193125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.23403219e+05, 2.87112156e+05, 2.58189422e+05, 3.23403219e+05, 2.87112156e+05, 2.58189422e+05, 3.23403219e+05, 2.87112156e+05, 2.58189422e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.24509531e+05, 2.57110953e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1539664115), # 1.54GB, avg file size 1.54GB
  ("fsize_db",                        14237299312), # 14.24GB, avg file size 2.85GB
  ("use_it",                          True),
  ("xsection",                        0.001037918),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 299322, ],
    'CountWeighted'                                                                  : [ 2.99228031e+05, 2.99337969e+05, 2.99323875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.30039406e+05, 2.99227594e+05, 2.74011812e+05, 3.30039406e+05, 2.99227594e+05, 2.74011812e+05, 3.30039406e+05, 2.99227594e+05, 2.74011812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.32139062e+05, 2.71947438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.87288031e+05, 2.87319938e+05, 2.87320031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.87288031e+05, 2.84353875e+05, 2.90226531e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.16611281e+05, 2.87285312e+05, 2.63163281e+05, 3.16611281e+05, 2.87285312e+05, 2.63163281e+05, 3.16611281e+05, 2.87285312e+05, 2.63163281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.18667375e+05, 2.61143219e+05, ],
  }),
  ("nof_tree_events",                 299322),
  ("nof_db_events",                   299322),
  ("fsize_local",                     1400669895), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        13394462193), # 13.39GB, avg file size 3.35GB
  ("use_it",                          True),
  ("xsection",                        0.004819446),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_0_5_C2V_1_C3_1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00034500e+05, 3.00021000e+05, 2.99998000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.35097906e+05, 3.00027344e+05, 2.71700719e+05, 3.35097906e+05, 3.00027344e+05, 2.71700719e+05, 3.35097906e+05, 3.00027344e+05, 2.71700719e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.36636375e+05, 2.70192969e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.87483562e+05, 2.87473625e+05, 2.87475656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.87483562e+05, 2.84486969e+05, 2.90502406e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.20954594e+05, 2.87479000e+05, 2.60466875e+05, 3.20954594e+05, 2.87479000e+05, 2.60466875e+05, 3.20954594e+05, 2.87479000e+05, 2.60466875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.22460844e+05, 2.58990547e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1501775869), # 1.50GB, avg file size 1.50GB
  ("fsize_db",                        13698968263), # 13.70GB, avg file size 3.42GB
  ("use_it",                          True),
  ("xsection",                        0.0007901474),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00009855e+05, 2.99984129e+05, 3.00018383e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84326191e+05, 3.62835328e+05, 3.42679230e+05, 3.17798965e+05, 3.00007219e+05, 2.83309699e+05, 2.67174258e+05, 2.52189598e+05, 2.38142633e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.84326191e+05, 2.38142633e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93734160e+05, 2.93720980e+05, 2.93734172e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93734160e+05, 2.92155684e+05, 2.95309945e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.76219406e+05, 3.55255117e+05, 3.35576066e+05, 3.11092043e+05, 2.93730012e+05, 2.77433609e+05, 2.61532566e+05, 2.46914969e+05, 2.33200543e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76219406e+05, 2.33200543e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1358045386), # 1.36GB, avg file size 679.02MB
  ("fsize_db",                        13013254769), # 13.01GB, avg file size 4.34GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_box_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_box_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 277140, ],
    'CountWeighted'                                                                  : [ 2.77140590e+05, 2.77151885e+05, 2.77124283e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.53745441e+05, 3.36001254e+05, 3.18998883e+05, 2.91807490e+05, 2.77136961e+05, 2.63092311e+05, 2.44831062e+05, 2.32503594e+05, 2.20699826e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.53745441e+05, 2.20699826e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.71541035e+05, 2.71531453e+05, 2.71544484e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.71541035e+05, 2.70120414e+05, 2.72956055e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.46528340e+05, 3.29216074e+05, 3.12611199e+05, 2.85849463e+05, 2.71535980e+05, 2.57819482e+05, 2.39829305e+05, 2.27802072e+05, 2.16274070e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.46528340e+05, 2.16274070e+05, ],
  }),
  ("nof_tree_events",                 277140),
  ("nof_db_events",                   277140),
  ("fsize_local",                     1219481122), # 1.22GB, avg file size 609.74MB
  ("fsize_db",                        11969129912), # 11.97GB, avg file size 3.99GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_box_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 291000, ],
    'CountWeighted'                                                                  : [ 2.91008246e+05, 2.91000305e+05, 2.90997836e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.71669500e+05, 3.52735605e+05, 3.34726289e+05, 3.06701090e+05, 2.91006809e+05, 2.76077809e+05, 2.57423551e+05, 2.44188344e+05, 2.31621119e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.71669500e+05, 2.31621119e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.85180441e+05, 2.85165547e+05, 2.85176910e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.85180441e+05, 2.83704289e+05, 2.86649520e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.64148367e+05, 3.45687270e+05, 3.28106520e+05, 3.00483805e+05, 2.85178305e+05, 2.70608027e+05, 2.52196781e+05, 2.39292113e+05, 2.27024965e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.64148367e+05, 2.27024965e+05, ],
  }),
  ("nof_tree_events",                 291000),
  ("nof_db_events",                   291000),
  ("fsize_local",                     1286695871), # 1.29GB, avg file size 643.35MB
  ("fsize_db",                        12693181737), # 12.69GB, avg file size 4.23GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_9_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99988395e+05, 2.99993926e+05, 3.00008098e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.80809645e+05, 3.65080324e+05, 3.49381168e+05, 3.12974965e+05, 2.99965500e+05, 2.87063031e+05, 2.61793902e+05, 2.50908867e+05, 2.40060152e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.80809645e+05, 2.40060152e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94390555e+05, 2.94388719e+05, 2.94411023e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94390555e+05, 2.92959910e+05, 2.95821332e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.73631551e+05, 3.58271508e+05, 3.42922406e+05, 3.07070438e+05, 2.94375469e+05, 2.81750473e+05, 2.56850094e+05, 2.46220008e+05, 2.35613262e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.73631551e+05, 2.35613262e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1263896368), # 1.26GB, avg file size 631.95MB
  ("fsize_db",                        12554774019), # 12.55GB, avg file size 4.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_10_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00014758e+05, 3.00000059e+05, 2.99985949e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.82021031e+05, 3.64307328e+05, 3.47067004e+05, 3.14636973e+05, 3.00006988e+05, 2.85766551e+05, 2.63646410e+05, 2.51348559e+05, 2.39399191e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.82021031e+05, 2.39399191e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94150617e+05, 2.94134770e+05, 2.94142090e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94150617e+05, 2.92662375e+05, 2.95636047e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.74490988e+05, 3.57201105e+05, 3.40357652e+05, 3.08428828e+05, 2.94144273e+05, 2.80237391e+05, 2.58440012e+05, 2.46437305e+05, 2.34763191e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.74490988e+05, 2.34763191e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1295417865), # 1.30GB, avg file size 647.71MB
  ("fsize_db",                        12953354252), # 12.95GB, avg file size 3.24GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_10_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_11_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00003137e+05, 2.99983141e+05, 2.99961707e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84467074e+05, 3.62940531e+05, 3.42915199e+05, 3.17930188e+05, 3.00001211e+05, 2.83344258e+05, 2.67335531e+05, 2.52166582e+05, 2.38092922e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.84467074e+05, 2.38092922e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93844629e+05, 2.93835773e+05, 2.93817730e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93844629e+05, 2.92300461e+05, 2.95389664e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.76488418e+05, 3.55511574e+05, 3.35976590e+05, 3.11316055e+05, 2.93840926e+05, 2.77596645e+05, 2.61762195e+05, 2.46980488e+05, 2.33252746e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76488418e+05, 2.33252746e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1355666889), # 1.36GB, avg file size 677.83MB
  ("fsize_db",                        13042878478), # 13.04GB, avg file size 4.35GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_11_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_12_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 298800, ],
    'CountWeighted'                                                                  : [ 2.98741004e+05, 2.98815723e+05, 2.98793379e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.85318441e+05, 3.59966273e+05, 3.36994387e+05, 3.19936535e+05, 2.98735629e+05, 2.79662875e+05, 2.69922891e+05, 2.52028113e+05, 2.35837453e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.85318441e+05, 2.35837453e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92410918e+05, 2.92449008e+05, 2.92446500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92410918e+05, 2.90830789e+05, 2.93991027e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.77046566e+05, 3.52321172e+05, 3.29902883e+05, 3.13058758e+05, 2.92405262e+05, 2.73769316e+05, 2.64114094e+05, 2.46663121e+05, 2.30862242e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.77046566e+05, 2.30862242e+05, ],
  }),
  ("nof_tree_events",                 298800),
  ("nof_db_events",                   298800),
  ("fsize_local",                     1422975428), # 1.42GB, avg file size 711.49MB
  ("fsize_db",                        13370108309), # 13.37GB, avg file size 4.46GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_13_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_13_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99962816e+05, 3.00001543e+05, 2.99985906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.88568023e+05, 3.60322930e+05, 3.35113594e+05, 3.23568066e+05, 2.99957883e+05, 2.78971047e+05, 2.73631391e+05, 2.53665559e+05, 2.35855688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.88568023e+05, 2.35855688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93102461e+05, 2.93120418e+05, 2.93116426e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93102461e+05, 2.91399562e+05, 2.94802504e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.79586375e+05, 3.52067523e+05, 3.27492797e+05, 3.16083367e+05, 2.93098363e+05, 2.72622699e+05, 2.67298352e+05, 2.47846816e+05, 2.30485504e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.79586375e+05, 2.30485504e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1466522087), # 1.47GB, avg file size 733.26MB
  ("fsize_db",                        13600771777), # 13.60GB, avg file size 4.53GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_13_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2t',          'signal_ggf_nonresonant_node_box_hh_2b2t',         'signal_ggf_nonresonant_node_2_hh_2b2t',           'signal_ggf_nonresonant_node_9_hh_2b2t',           'signal_ggf_nonresonant_node_10_hh_2b2t',          'signal_ggf_nonresonant_node_11_hh_2b2t',          'signal_ggf_nonresonant_node_12_hh_2b2t',          'signal_ggf_nonresonant_node_13_hh_2b2t',           ],
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2v',          'signal_ggf_nonresonant_node_box_hh_2b2v',         'signal_ggf_nonresonant_node_1_hh_2b2v',           'signal_ggf_nonresonant_node_2_hh_2b2v',           'signal_ggf_nonresonant_node_3_hh_2b2v',           'signal_ggf_nonresonant_node_4_hh_2b2v',           'signal_ggf_nonresonant_node_5_hh_2b2v',           'signal_ggf_nonresonant_node_6_hh_2b2v',           'signal_ggf_nonresonant_node_7_hh_2b2v',           'signal_ggf_nonresonant_node_8_hh_2b2v',           'signal_ggf_nonresonant_node_9_hh_2b2v',           'signal_ggf_nonresonant_node_10_hh_2b2v',          'signal_ggf_nonresonant_node_11_hh_2b2v',          'signal_ggf_nonresonant_node_12_hh_2b2v',           ],
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2v_sl',       'signal_ggf_nonresonant_node_box_hh_2b2v_sl',      'signal_ggf_nonresonant_node_1_hh_2b2v_sl',        'signal_ggf_nonresonant_node_2_hh_2b2v_sl',        'signal_ggf_nonresonant_node_3_hh_2b2v_sl',        'signal_ggf_nonresonant_node_4_hh_2b2v_sl',        'signal_ggf_nonresonant_node_5_hh_2b2v_sl',        'signal_ggf_nonresonant_node_6_hh_2b2v_sl',        'signal_ggf_nonresonant_node_7_hh_2b2v_sl',        'signal_ggf_nonresonant_node_8_hh_2b2v_sl',        'signal_ggf_nonresonant_node_9_hh_2b2v_sl',        'signal_ggf_nonresonant_node_10_hh_2b2v_sl',       'signal_ggf_nonresonant_node_11_hh_2b2v_sl',       'signal_ggf_nonresonant_node_12_hh_2b2v_sl',        ],
]

