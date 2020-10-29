from collections import OrderedDict as OD

# file generated at 2020-10-29 20:46:42 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh.py -p python/samples/sampleLocations_2016_hh_bbww.txt -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_hh.py -M

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

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       5),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 398999, ],
    'CountWeighted'                                                                  : [ 3.97556572e+05, 3.97604340e+05, 3.97604117e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97556572e+05, 3.97556572e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97540144e+06, 3.97540144e+06, 3.97540144e+06, 3.97540144e+06, 3.97540144e+06, 3.97540144e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.98980643e+05, 3.99385807e+05, 5.89739523e+05, 3.98996328e+05, 3.98132133e+05, 2.28737695e+05, ],
    'CountWeightedFull'                                                              : [ 3.97379105e+05, 3.97424209e+05, 3.97425480e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97379105e+05, 3.97379105e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97364445e+06, 3.97364445e+06, 3.97364445e+06, 3.97364445e+06, 3.97364445e+06, 3.97364445e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98802109e+05, 3.99206852e+05, 5.89472867e+05, 3.98817195e+05, 3.97953055e+05, 2.28636254e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.82396396e+05, 3.82413410e+05, 3.82404221e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.82396396e+05, 3.78595629e+05, 3.86201594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.82396396e+05, 3.82396396e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.82391111e+06, 3.82391111e+06, 3.82391111e+06, 3.82391111e+06, 3.82391111e+06, 3.82391111e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.83769098e+05, 3.83940676e+05, 5.67044828e+05, 3.83713859e+05, 3.83194861e+05, 2.20218338e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.82226408e+05, 3.82242832e+05, 3.82234244e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.82226408e+05, 3.78427855e+05, 3.86029512e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.82226408e+05, 3.82226408e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.82221533e+06, 3.82221533e+06, 3.82221533e+06, 3.82221533e+06, 3.82221533e+06, 3.82221533e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.83599055e+05, 3.83770326e+05, 5.66791445e+05, 3.83543250e+05, 3.83023996e+05, 2.20121588e+05, ],
  }),
  ("nof_tree_events",                 398999),
  ("nof_db_events",                   398999),
  ("fsize_local",                     1590324896), # 1.59GB, avg file size 318.06MB
  ("fsize_db",                        18513625499), # 18.51GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        4.55695e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       6),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 396799, ],
    'CountWeighted'                                                                  : [ 3.95403127e+05, 3.95429871e+05, 3.95394537e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95403127e+05, 3.95403127e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95388766e+06, 3.95388766e+06, 3.95388766e+06, 3.95388766e+06, 3.95388766e+06, 3.95388766e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96835820e+05, 3.96572715e+05, 5.89944809e+05, 3.96740744e+05, 3.95665992e+05, 2.24042495e+05, ],
    'CountWeightedFull'                                                              : [ 3.95213000e+05, 3.95241240e+05, 3.95205619e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95213000e+05, 3.95213000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95200553e+06, 3.95200553e+06, 3.95200553e+06, 3.95200553e+06, 3.95200553e+06, 3.95200553e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96647123e+05, 3.96384850e+05, 5.89661098e+05, 3.96550234e+05, 3.95474865e+05, 2.23936164e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.76588838e+05, 3.76590170e+05, 3.76587637e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.76588838e+05, 3.72032557e+05, 3.81165168e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76588838e+05, 3.76588838e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.76584267e+06, 3.76584267e+06, 3.76584267e+06, 3.76584267e+06, 3.76584267e+06, 3.76584267e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.78004014e+05, 3.77539883e+05, 5.61663070e+05, 3.77756746e+05, 3.77049992e+05, 2.13593353e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.76410836e+05, 3.76412775e+05, 3.76409477e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.76410836e+05, 3.71857166e+05, 3.80984445e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.76410836e+05, 3.76410836e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.76406425e+06, 3.76406425e+06, 3.76406425e+06, 3.76406425e+06, 3.76406425e+06, 3.76406425e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.77826342e+05, 3.77362836e+05, 5.61395836e+05, 3.77577523e+05, 3.76869920e+05, 2.13493193e+05, ],
  }),
  ("nof_tree_events",                 396799),
  ("nof_db_events",                   396799),
  ("fsize_local",                     1692766496), # 1.69GB, avg file size 282.13MB
  ("fsize_db",                        19203455679), # 19.20GB, avg file size 738.59MB
  ("use_it",                          True),
  ("xsection",                        3.75655e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       5),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 399200, ],
    'CountWeighted'                                                                  : [ 3.97047879e+05, 3.97063488e+05, 3.97048516e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97047879e+05, 3.97047879e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97045200e+06, 3.97045200e+06, 3.97045200e+06, 3.97045200e+06, 3.97045200e+06, 3.97045200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99080602e+05, 3.99500598e+05, 5.91679508e+05, 3.99371777e+05, 3.98283789e+05, 2.27272697e+05, ],
    'CountWeightedFull'                                                              : [ 3.96856418e+05, 3.96872152e+05, 3.96855668e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96856418e+05, 3.96856418e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96853519e+06, 3.96853519e+06, 3.96853519e+06, 3.96853519e+06, 3.96853519e+06, 3.96853519e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98889109e+05, 3.99307785e+05, 5.91392539e+05, 3.99178707e+05, 3.98091953e+05, 2.27164492e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.80849684e+05, 3.80853344e+05, 3.80855855e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.80849684e+05, 3.76985070e+05, 3.84733184e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.80849684e+05, 3.80849684e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.80846941e+06, 3.80846941e+06, 3.80846941e+06, 3.80846941e+06, 3.80846941e+06, 3.80846941e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.82821012e+05, 3.83028352e+05, 5.67323875e+05, 3.82975715e+05, 3.82254199e+05, 2.18213449e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.80667965e+05, 3.80671340e+05, 3.80673125e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.80667965e+05, 3.76805605e+05, 3.84549039e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.80667965e+05, 3.80667965e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.80664962e+06, 3.80664962e+06, 3.80664962e+06, 3.80664962e+06, 3.80664962e+06, 3.80664962e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.82639062e+05, 3.82845047e+05, 5.67051660e+05, 3.82792449e+05, 3.82071930e+05, 2.18110523e+05, ],
  }),
  ("nof_tree_events",                 399200),
  ("nof_db_events",                   399200),
  ("fsize_local",                     1893441002), # 1.89GB, avg file size 378.69MB
  ("fsize_db",                        20560010155), # 20.56GB, avg file size 822.40MB
  ("use_it",                          True),
  ("xsection",                        0.0003753816),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       6),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.98673123e+05, 3.98693091e+05, 3.98663076e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.98673123e+05, 3.98673123e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.98659077e+06, 3.98659077e+06, 3.98659077e+06, 3.98659077e+06, 3.98659077e+06, 3.98659077e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00039611e+05, 3.99914470e+05, 5.89801396e+05, 3.99929341e+05, 3.98916007e+05, 2.30073469e+05, ],
    'CountWeightedFull'                                                              : [ 3.98500597e+05, 3.98520020e+05, 3.98492489e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.98500597e+05, 3.98500597e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.98486962e+06, 3.98486962e+06, 3.98486962e+06, 3.98486962e+06, 3.98486962e+06, 3.98486962e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99867490e+05, 3.99741670e+05, 5.89549074e+05, 3.99757763e+05, 3.98747865e+05, 2.29975356e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.85426233e+05, 3.85426288e+05, 3.85427654e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.85426233e+05, 3.82077931e+05, 3.88775507e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.85426233e+05, 3.85426233e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.85418541e+06, 3.85418541e+06, 3.85418541e+06, 3.85418541e+06, 3.85418541e+06, 3.85418541e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.86778498e+05, 3.86487396e+05, 5.70028215e+05, 3.86589603e+05, 3.85831198e+05, 2.22605021e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.85261377e+05, 3.85261511e+05, 3.85263408e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.85261377e+05, 3.81914928e+05, 3.88608961e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.85261377e+05, 3.85261377e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.85253971e+06, 3.85253971e+06, 3.85253971e+06, 3.85253971e+06, 3.85253971e+06, 3.85253971e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.86613616e+05, 3.86321812e+05, 5.69786232e+05, 3.86425268e+05, 3.85669675e+05, 2.22510904e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1594631688), # 1.59GB, avg file size 265.77MB
  ("fsize_db",                        18665186777), # 18.67GB, avg file size 777.72MB
  ("use_it",                          True),
  ("xsection",                        0.0001216848),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 398799, ],
    'CountWeighted'                                                                  : [ 3.97056007e+05, 3.97116667e+05, 3.97093491e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97056007e+05, 3.97056007e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97091370e+06, 3.97091370e+06, 3.97091370e+06, 3.97091370e+06, 3.97091370e+06, 3.97091370e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.98828824e+05, 3.98403803e+05, 5.89212216e+05, 3.98745035e+05, 3.98372451e+05, 2.28467879e+05, ],
    'CountWeightedFull'                                                              : [ 3.96875582e+05, 3.96932133e+05, 3.96909688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96875582e+05, 3.96875582e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96909771e+06, 3.96909771e+06, 3.96909771e+06, 3.96909771e+06, 3.96909771e+06, 3.96909771e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98646695e+05, 3.98221620e+05, 5.88942998e+05, 3.98562415e+05, 3.98191311e+05, 2.28363948e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81992743e+05, 3.82013257e+05, 3.82010332e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81992743e+05, 3.78287117e+05, 3.85708700e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81992743e+05, 3.81992743e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.82008898e+06, 3.82008898e+06, 3.82008898e+06, 3.82008898e+06, 3.82008898e+06, 3.82008898e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.83698223e+05, 3.83078927e+05, 5.66732827e+05, 3.83540287e+05, 3.83566770e+05, 2.19983557e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81819783e+05, 3.81838883e+05, 3.81835922e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81819783e+05, 3.78116093e+05, 3.85533798e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81819783e+05, 3.81819783e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81835418e+06, 3.81835418e+06, 3.81835418e+06, 3.81835418e+06, 3.81835418e+06, 3.81835418e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.83524814e+05, 3.82905431e+05, 5.66476319e+05, 3.83366189e+05, 3.83394009e+05, 2.19884351e+05, ],
  }),
  ("nof_tree_events",                 398799),
  ("nof_db_events",                   398799),
  ("fsize_local",                     1730683689), # 1.73GB, avg file size 432.67MB
  ("fsize_db",                        19328505325), # 19.33GB, avg file size 1.29GB
  ("use_it",                          True),
  ("xsection",                        0.001743038),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       6),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 399097, ],
    'CountWeighted'                                                                  : [ 3.97024629e+05, 3.97012924e+05, 3.97038277e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97024629e+05, 3.97024629e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97029048e+06, 3.97029048e+06, 3.97029048e+06, 3.97029048e+06, 3.97029048e+06, 3.97029048e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.98944853e+05, 3.99761904e+05, 5.89342828e+05, 3.99287955e+05, 3.96196020e+05, 2.27711817e+05, ],
    'CountWeightedFull'                                                              : [ 3.96833244e+05, 3.96823559e+05, 3.96846747e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96833244e+05, 3.96833244e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96838945e+06, 3.96838945e+06, 3.96838945e+06, 3.96838945e+06, 3.96838945e+06, 3.96838945e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98754908e+05, 3.99570324e+05, 5.89061178e+05, 3.99096012e+05, 3.96008325e+05, 2.27603730e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81186766e+05, 3.81172170e+05, 3.81202094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81186766e+05, 3.77375407e+05, 3.85009783e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81186766e+05, 3.81186766e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81187520e+06, 3.81187520e+06, 3.81187520e+06, 3.81187520e+06, 3.81187520e+06, 3.81187520e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.83057312e+05, 3.83615607e+05, 5.65602115e+05, 3.83267778e+05, 3.80631729e+05, 2.18854626e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81005738e+05, 3.80992044e+05, 3.81021008e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81005738e+05, 3.77196922e+05, 3.84826656e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81005738e+05, 3.81005738e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81007006e+06, 3.81007006e+06, 3.81007006e+06, 3.81007006e+06, 3.81007006e+06, 3.81007006e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.82876883e+05, 3.83433942e+05, 5.65334666e+05, 3.83085334e+05, 3.80453125e+05, 2.18751944e+05, ],
  }),
  ("nof_tree_events",                 399097),
  ("nof_db_events",                   399097),
  ("fsize_local",                     1851861930), # 1.85GB, avg file size 308.64MB
  ("fsize_db",                        20226758825), # 20.23GB, avg file size 842.78MB
  ("use_it",                          True),
  ("xsection",                        0.0002857708),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_2b2v_dipoleRecoilOff"),
  ("nof_files",                       6),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 396800, ],
    'CountWeighted'                                                                  : [ 3.94914545e+05, 3.94933857e+05, 3.94925298e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94914545e+05, 3.94914545e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94891681e+06, 3.94891681e+06, 3.94891681e+06, 3.94891681e+06, 3.94891681e+06, 3.94891681e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96868158e+05, 3.96727243e+05, 5.85768518e+05, 3.96697160e+05, 3.95530756e+05, 2.27334529e+05, ],
    'CountWeightedFull'                                                              : [ 3.94732689e+05, 3.94752831e+05, 3.94739942e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.94732689e+05, 3.94732689e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.94710561e+06, 3.94710561e+06, 3.94710561e+06, 3.94710561e+06, 3.94710561e+06, 3.94710561e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96684745e+05, 3.96543576e+05, 5.85494764e+05, 3.96512536e+05, 3.95346173e+05, 2.27230359e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.79473455e+05, 3.79474703e+05, 3.79479566e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.79473455e+05, 3.75716175e+05, 3.83244337e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.79473455e+05, 3.79473455e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.79463213e+06, 3.79463213e+06, 3.79463213e+06, 3.79463213e+06, 3.79463213e+06, 3.79463213e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.81377292e+05, 3.81009804e+05, 5.62658750e+05, 3.81105797e+05, 3.80311363e+05, 2.18655397e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.79299692e+05, 3.79301719e+05, 3.79304562e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.79299692e+05, 3.75544798e+05, 3.83068402e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.79299692e+05, 3.79299692e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.79289696e+06, 3.79289696e+06, 3.79289696e+06, 3.79289696e+06, 3.79289696e+06, 3.79289696e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.81203251e+05, 3.80835157e+05, 5.62398753e+05, 3.80930451e+05, 3.80136029e+05, 2.18556325e+05, ],
  }),
  ("nof_tree_events",                 396800),
  ("nof_db_events",                   396800),
  ("fsize_local",                     1772427700), # 1.77GB, avg file size 295.40MB
  ("fsize_db",                        19702706677), # 19.70GB, avg file size 820.95MB
  ("use_it",                          True),
  ("xsection",                        0.0007149609),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2b2v"),
  ("nof_files",                       6),
  ("nof_db_files",                    89),
  ("nof_events",                      {
    'Count'                                                                          : [ 396798, ],
    'CountWeighted'                                                                  : [ 3.55736574e+05, 3.55707389e+05, 3.55764760e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.05001197e+05, 3.98537168e+05, 3.94274119e+05, 3.63937197e+05, 3.55725326e+05, 3.49300668e+05, 3.26635002e+05, 3.17715840e+05, 3.10243771e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.22376043e+05, 3.00800631e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.55645881e+05, 3.55454420e+05, 5.39986148e+05, 3.55857449e+05, 3.54755107e+05, 1.93727782e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.18724734e+04, 1.18694053e+04, 1.80651335e+04, 1.18778771e+04, 1.18854304e+04, 6.47055219e+03, ],
    'CountWeightedFull'                                                              : [ 1.06224902e+04, 1.06224637e+04, 1.06232863e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.20936473e+04, 1.19004885e+04, 1.17731055e+04, 1.08677789e+04, 1.06224074e+04, 1.04305055e+04, 9.75339697e+03, 9.48698929e+03, 9.26381067e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.26128879e+04, 8.98185352e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.06201564e+04, 1.06143069e+04, 1.61248008e+04, 1.06262802e+04, 1.05935679e+04, 5.78497220e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.55950256e+02, 3.55960144e+02, 5.41120646e+02, 3.56162571e+02, 3.56111809e+02, 1.94318829e+02, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.50235848e+05, 3.50202439e+05, 3.50265342e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.50235848e+05, 3.48806586e+05, 3.51663021e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98637785e+05, 3.92333984e+05, 3.88189598e+05, 3.58255334e+05, 3.50224850e+05, 3.43944560e+05, 3.21558364e+05, 3.12824955e+05, 3.05508012e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.15747205e+05, 2.96212842e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.50191379e+05, 3.49887947e+05, 5.31575738e+05, 3.50295771e+05, 3.49366246e+05, 1.90801307e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.16892429e+04, 1.16827186e+04, 1.77821975e+04, 1.16911255e+04, 1.17034462e+04, 6.37208060e+03, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.04582793e+04, 1.04578377e+04, 1.04591639e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.04582793e+04, 1.04155540e+04, 1.05008691e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.19035327e+04, 1.17151744e+04, 1.15913394e+04, 1.06980413e+04, 1.04581021e+04, 1.02705106e+04, 9.60174716e+03, 9.34090695e+03, 9.12238281e+03, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.24148420e+04, 8.84483771e+03, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.04572163e+04, 1.04480490e+04, 1.58735436e+04, 1.04601338e+04, 1.04325491e+04, 5.69756293e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.50441504e+02, 3.50343225e+02, 5.32619553e+02, 3.50545959e+02, 3.50649830e+02, 1.91356227e+02, ],
  }),
  ("nof_tree_events",                 396798),
  ("nof_db_events",                   396798),
  ("fsize_local",                     1627345264), # 1.63GB, avg file size 271.22MB
  ("fsize_db",                        17674000555), # 17.67GB, avg file size 198.58MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 398400, ],
    'CountWeighted'                                                                  : [ 3.43460812e+05, 3.43474219e+05, 3.43457047e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.91843500e+05, 3.86327562e+05, 3.82795250e+05, 3.50528828e+05, 3.43455844e+05, 3.37916453e+05, 3.13714766e+05, 3.05950609e+05, 2.99419500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.12573625e+05, 2.86767289e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.43666016e+05, 3.43842141e+05, 5.22053828e+05, 3.43215547e+05, 3.41542250e+05, 1.86092242e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.23530542e+03, 5.23623340e+03, 7.97928467e+03, 5.22924609e+03, 5.23097437e+03, 2.83538855e+03, ],
    'CountWeightedFull'                                                              : [ 4.50374548e+03, 4.50377515e+03, 4.50395410e+03, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.13858154e+03, 5.06611768e+03, 5.01971240e+03, 4.59679126e+03, 4.50366101e+03, 4.43124036e+03, 4.11391565e+03, 4.01203821e+03, 3.92634802e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.41045361e+03, 3.76043896e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.50674475e+03, 4.50910107e+03, 6.84590015e+03, 4.50071155e+03, 4.47866650e+03, 2.44033826e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 6.87947388e+01, 6.88183041e+01, 1.04847874e+02, 6.87095051e+01, 6.87173176e+01, 3.72528305e+01, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.38092406e+05, 3.38093484e+05, 3.38099953e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.38092406e+05, 3.36699188e+05, 3.39480125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.85627375e+05, 3.80258922e+05, 3.76835594e+05, 3.44996078e+05, 3.38085406e+05, 3.32682969e+05, 3.08779828e+05, 3.01187672e+05, 2.94800266e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.06035797e+05, 2.82349188e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.38347281e+05, 3.38411859e+05, 5.13829922e+05, 3.37788781e+05, 3.36292000e+05, 1.83261312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 5.15338208e+03, 5.15249634e+03, 7.85263599e+03, 5.14563306e+03, 5.15013867e+03, 2.79164917e+03, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 4.43339563e+03, 4.43334802e+03, 4.43366797e+03, ],
    'CountWeightedFullL1Prefire'                                                     : [ 4.43339563e+03, 4.41513245e+03, 4.45162866e+03, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 5.05701685e+03, 4.98649854e+03, 4.94153345e+03, 4.52420337e+03, 4.43329614e+03, 4.36259131e+03, 4.04917676e+03, 3.94956055e+03, 3.86575610e+03, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 5.32467920e+03, 3.70248840e+03, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 4.43697351e+03, 4.43785999e+03, 6.73803906e+03, 4.42952844e+03, 4.40982202e+03, 2.40320544e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 6.77159519e+01, 6.77156277e+01, 1.03180611e+02, 6.76086292e+01, 6.76534653e+01, 3.66769104e+01, ],
  }),
  ("nof_tree_events",                 398400),
  ("nof_db_events",                   398400),
  ("fsize_local",                     1631954007), # 1.63GB, avg file size 815.98MB
  ("fsize_db",                        16864768372), # 16.86GB, avg file size 674.59MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VTo2L2Nu_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_2b2v"),
  ("nof_files",                       5),
  ("nof_db_files",                    42),
  ("nof_events",                      {
    'Count'                                                                          : [ 394800, ],
    'CountWeighted'                                                                  : [ 3.88464885e+05, 3.88493750e+05, 3.88421145e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.65392602e+05, 4.56639844e+05, 4.49907943e+05, 3.96175004e+05, 3.88462230e+05, 3.81931154e+05, 3.41108666e+05, 3.34279438e+05, 3.28102152e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.79520076e+05, 3.21512998e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.88558633e+05, 3.88751832e+05, 5.87666457e+05, 3.88355418e+05, 3.86219355e+05, 2.12480475e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.16907865e+04, 3.17101527e+04, 4.80682717e+04, 3.16724545e+04, 3.16381195e+04, 1.73320940e+04, ],
    'CountWeightedFull'                                                              : [ 3.11534175e+04, 3.11543116e+04, 3.11511079e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.73219004e+04, 3.66196736e+04, 3.60795571e+04, 3.17712280e+04, 3.11529524e+04, 3.06284714e+04, 2.73547760e+04, 2.68069302e+04, 2.63114951e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.84551125e+04, 2.57830505e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.11601758e+04, 3.11753905e+04, 4.71285093e+04, 3.11437076e+04, 3.09736746e+04, 1.70395579e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.54405319e+03, 2.54557901e+03, 3.85786589e+03, 2.54258841e+03, 2.53986682e+03, 1.39220656e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.83062305e+05, 3.83079727e+05, 3.83034566e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.83062305e+05, 3.81623455e+05, 3.84492506e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.58791783e+05, 4.50230576e+05, 4.43651867e+05, 3.90605840e+05, 3.83056602e+05, 3.76666178e+05, 3.36346355e+05, 3.29660766e+05, 3.23609941e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.72739594e+05, 3.17103691e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.83201195e+05, 3.83259348e+05, 5.79400730e+05, 3.82890211e+05, 3.80961650e+05, 2.09617563e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.12514419e+04, 3.12594280e+04, 4.73889741e+04, 3.12245708e+04, 3.12057443e+04, 1.70974230e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.07196458e+04, 3.07203196e+04, 3.07181912e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.07196458e+04, 3.06042268e+04, 3.08342139e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 3.67922827e+04, 3.61054502e+04, 3.55776931e+04, 3.13243646e+04, 3.07190399e+04, 3.02061031e+04, 2.69727302e+04, 2.64364200e+04, 2.59510977e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.79110957e+04, 2.54293202e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.07303790e+04, 3.07348070e+04, 4.64654094e+04, 3.07052880e+04, 3.05518463e+04, 1.68099108e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.50878998e+03, 2.50939548e+03, 3.80333775e+03, 2.50663516e+03, 2.50515945e+03, 1.37337138e+03, ],
  }),
  ("nof_tree_events",                 394800),
  ("nof_db_events",                   394800),
  ("fsize_local",                     1478753967), # 1.48GB, avg file size 295.75MB
  ("fsize_db",                        16232250597), # 16.23GB, avg file size 386.48MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2WToLNu2J_node_SM_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v_sl_PSWeights"),
  ("nof_files",                       6),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99977836e+05, 2.99975159e+05, 2.99971660e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99977836e+05, 2.99977836e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99950388e+06, 2.99950388e+06, 2.99950388e+06, 2.99950388e+06, 2.99950388e+06, 2.99950388e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00004765e+05, 3.00014397e+05, 4.67898060e+05, 2.99984813e+05, 2.98216677e+05, 1.54086293e+05, ],
    'CountWeightedFull'                                                              : [ 2.99913667e+05, 2.99911357e+05, 2.99907511e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99913667e+05, 2.99913667e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99886872e+06, 2.99886872e+06, 2.99886872e+06, 2.99886872e+06, 2.99886872e+06, 2.99886872e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99942956e+05, 2.99950755e+05, 4.67797809e+05, 2.99918074e+05, 2.98152804e+05, 1.54053556e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93702024e+05, 2.93692146e+05, 2.93704109e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93702024e+05, 2.92119676e+05, 2.95281889e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93702024e+05, 2.93702024e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.93686259e+06, 2.93686259e+06, 2.93686259e+06, 2.93686259e+06, 2.93686259e+06, 2.93686259e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.94002631e+05, 2.93665937e+05, 4.58021910e+05, 2.93359816e+05, 2.92072935e+05, 1.50924340e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.93639890e+05, 2.93630136e+05, 2.93641761e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.93639890e+05, 2.92057953e+05, 2.95219285e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.93639890e+05, 2.93639890e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.93624330e+06, 2.93624330e+06, 2.93624330e+06, 2.93624330e+06, 2.93624330e+06, 2.93624330e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.93942501e+05, 2.93604160e+05, 4.57924517e+05, 2.93295092e+05, 2.92010885e+05, 1.50892497e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1308089844), # 1.31GB, avg file size 218.01MB
  ("fsize_db",                        13854390389), # 13.85GB, avg file size 532.86MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2WToLNu2J_node_1_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_2b2v_sl_PSWeights"),
  ("nof_files",                       4),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 297895, ],
    'CountWeighted'                                                                  : [ 2.97839379e+05, 2.97861537e+05, 2.97843674e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.97839379e+05, 2.97839379e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.33926623e+06, 2.10582581e+06, 2.83364345e+06, 2.31685845e+06, 1.77908584e+06, 1.21065962e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.97768797e+05, 2.97535756e+05, 4.64419570e+05, 2.98084799e+05, 2.96860697e+05, 1.53495368e+05, ],
    'CountWeightedFull'                                                              : [ 2.97778984e+05, 2.97801537e+05, 2.97783215e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.97778984e+05, 2.97778984e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.33880622e+06, 2.10540238e+06, 2.83307042e+06, 2.31637283e+06, 1.77872453e+06, 1.21041488e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.97710488e+05, 2.97475957e+05, 4.64325293e+05, 2.98022199e+05, 2.96800438e+05, 1.53464367e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91869570e+05, 2.91878031e+05, 2.91873670e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91869570e+05, 2.90352947e+05, 2.93381898e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.91869570e+05, 2.91869570e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.29426702e+06, 2.06341158e+06, 2.77677541e+06, 2.26809378e+06, 1.74424342e+06, 1.18688117e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.92050271e+05, 2.91473654e+05, 4.55081219e+05, 2.91774221e+05, 2.91082609e+05, 1.50478977e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.91810826e+05, 2.91819654e+05, 2.91814857e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.91810826e+05, 2.90294705e+05, 2.93322797e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.91810826e+05, 2.91810826e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.29381909e+06, 2.06299973e+06, 2.77621716e+06, 2.26762261e+06, 1.74389059e+06, 1.18664288e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.91993479e+05, 2.91415697e+05, 4.54989633e+05, 2.91713357e+05, 2.91023908e+05, 1.50448802e+05, ],
  }),
  ("nof_tree_events",                 297895),
  ("nof_db_events",                   297895),
  ("fsize_local",                     1261705032), # 1.26GB, avg file size 315.43MB
  ("fsize_db",                        13390936467), # 13.39GB, avg file size 704.79MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_1_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2WToLNu2J_node_2_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2v_sl_PSWeights"),
  ("nof_files",                       5),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 298398, ],
    'CountWeighted'                                                                  : [ 2.98344718e+05, 2.98319827e+05, 2.98345007e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98344718e+05, 2.98344718e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98349122e+06, 2.98349122e+06, 2.98349122e+06, 2.98349122e+06, 2.98349122e+06, 2.98349122e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98416135e+05, 2.98598403e+05, 4.68638717e+05, 2.98405959e+05, 2.95418479e+05, 1.49715871e+05, ],
    'CountWeightedFull'                                                              : [ 2.98274195e+05, 2.98249857e+05, 2.98275591e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98274195e+05, 2.98274195e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98278437e+06, 2.98278437e+06, 2.98278437e+06, 2.98278437e+06, 2.98278437e+06, 2.98278437e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98348585e+05, 2.98529222e+05, 4.68528430e+05, 2.98332573e+05, 2.95348572e+05, 1.49680974e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91174178e+05, 2.91154770e+05, 2.91176938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91174178e+05, 2.89424115e+05, 2.92925320e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.91174178e+05, 2.91174178e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.91176791e+06, 2.91176791e+06, 2.91176791e+06, 2.91176791e+06, 2.91176791e+06, 2.91176791e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.91529097e+05, 2.91338595e+05, 4.57291740e+05, 2.90857751e+05, 2.88398424e+05, 1.46175296e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.91106056e+05, 2.91087055e+05, 2.91109496e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.91106056e+05, 2.89356523e+05, 2.92856736e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.91106056e+05, 2.91106056e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.91108666e+06, 2.91108666e+06, 2.91108666e+06, 2.91108666e+06, 2.91108666e+06, 2.91108666e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.91463580e+05, 2.91271651e+05, 4.57184969e+05, 2.90786864e+05, 2.88330714e+05, 1.46141505e+05, ],
  }),
  ("nof_tree_events",                 298398),
  ("nof_db_events",                   298398),
  ("fsize_local",                     1455278091), # 1.46GB, avg file size 291.06MB
  ("fsize_db",                        14956599323), # 14.96GB, avg file size 679.85MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2WToLNu2J_node_4_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2v_sl_PSWeights"),
  ("nof_files",                       5),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 293698, ],
    'CountWeighted'                                                                  : [ 2.93651488e+05, 2.93665787e+05, 2.93648504e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.93651488e+05, 2.93651488e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.93653658e+06, 2.93609341e+06, 2.93653658e+06, 2.93653658e+06, 2.92294645e+06, 2.92250347e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.93829627e+05, 2.93270682e+05, 4.57721572e+05, 2.93565223e+05, 2.92629238e+05, 1.51250875e+05, ],
    'CountWeightedFull'                                                              : [ 2.93590680e+05, 2.93604723e+05, 2.93588020e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.93590680e+05, 2.93590680e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.93592766e+06, 2.93548453e+06, 2.93592766e+06, 2.93592766e+06, 2.92234062e+06, 2.92189752e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.93770900e+05, 2.93211400e+05, 4.57626098e+05, 2.93501592e+05, 2.92567234e+05, 1.51219657e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.87805594e+05, 2.87811844e+05, 2.87807307e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.87805594e+05, 2.86319412e+05, 2.89288654e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.87805594e+05, 2.87805594e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.87807753e+06, 2.87764288e+06, 2.87807753e+06, 2.87807753e+06, 2.86481628e+06, 2.86438156e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.88226230e+05, 2.87357551e+05, 4.48598328e+05, 2.87403410e+05, 2.86961322e+05, 1.48294302e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.87746482e+05, 2.87752668e+05, 2.87748408e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.87746482e+05, 2.86260793e+05, 2.89229141e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.87746482e+05, 2.87746482e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.87748570e+06, 2.87705122e+06, 2.87748570e+06, 2.87748570e+06, 2.86422731e+06, 2.86379259e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.88169170e+05, 2.87299996e+05, 4.48505410e+05, 2.87341627e+05, 2.86901002e+05, 1.48263891e+05, ],
  }),
  ("nof_tree_events",                 293698),
  ("nof_db_events",                   293698),
  ("fsize_local",                     1245818720), # 1.25GB, avg file size 249.16MB
  ("fsize_db",                        13281373082), # 13.28GB, avg file size 664.07MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2WToLNu2J_node_5_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99939906e+05, 2.99978406e+05, 2.99994188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.89002969e+05, 2.35637141e+05, ],
    'CountWeightedPSWeight'                                                          : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedFull'                                                              : [ 0., 0., 0., ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 0., 0., ],
    'CountWeightedFullPSWeight'                                                      : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93315719e+05, 2.93330156e+05, 2.93358844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93315719e+05, 2.91665812e+05, 2.94965438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.80302656e+05, 2.30454844e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 0., 0., 0., ],
    'CountWeightedFullL1Prefire'                                                     : [ 0., 0., 0., ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 0., 0., ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 0., 0., 0., 0., 0., 0., ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299098),
  ("fsize_local",                     1473633220), # 1.47GB, avg file size 1.47GB
  ("fsize_db",                        14447245371), # 14.45GB, avg file size 760.38MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
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

samples_2016["/GluGluToHHTo2B2WToLNu2J_node_6_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_2b2v_sl_PSWeights"),
  ("nof_files",                       4),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 298896, ],
    'CountWeighted'                                                                  : [ 2.98865935e+05, 2.98846628e+05, 2.98861815e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98865935e+05, 2.98865935e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98886928e+06, 2.98886928e+06, 2.98886928e+06, 2.98886928e+06, 2.98886928e+06, 2.98886928e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98890494e+05, 2.98870488e+05, 4.66457342e+05, 2.98931771e+05, 2.97604838e+05, 1.53640100e+05, ],
    'CountWeightedFull'                                                              : [ 2.98804530e+05, 2.98786756e+05, 2.98800033e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98804530e+05, 2.98804530e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98824814e+06, 2.98824814e+06, 2.98824814e+06, 2.98824814e+06, 2.98824814e+06, 2.98824814e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98831592e+05, 2.98809616e+05, 4.66359598e+05, 2.98867425e+05, 2.97542251e+05, 1.53608996e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92814132e+05, 2.92790180e+05, 2.92825982e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92814132e+05, 2.91280521e+05, 2.94344453e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.92814132e+05, 2.92814132e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.92826402e+06, 2.92826402e+06, 2.92826402e+06, 2.92826402e+06, 2.92826402e+06, 2.92826402e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.93094883e+05, 2.92723515e+05, 4.56974331e+05, 2.92546439e+05, 2.91737974e+05, 1.50587410e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.92754414e+05, 2.92731400e+05, 2.92766141e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.92754414e+05, 2.91221318e+05, 2.94284377e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.92754414e+05, 2.92754414e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.92766412e+06, 2.92766412e+06, 2.92766412e+06, 2.92766412e+06, 2.92766412e+06, 2.92766412e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.93037643e+05, 2.92664371e+05, 4.56879592e+05, 2.92484025e+05, 2.91677240e+05, 1.50557191e+05, ],
  }),
  ("nof_tree_events",                 298896),
  ("nof_db_events",                   298896),
  ("fsize_local",                     1279150948), # 1.28GB, avg file size 319.79MB
  ("fsize_db",                        13518884270), # 13.52GB, avg file size 844.93MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2WToLNu2J_node_7_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2v_sl"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99984438e+05, 2.99952531e+05, 2.99920562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.79174844e+05, 2.40945609e+05, ],
    'CountWeightedPSWeight'                                                          : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedFull'                                                              : [ 0., 0., 0., ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 0., 0., ],
    'CountWeightedFullPSWeight'                                                      : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94945344e+05, 2.94912438e+05, 2.94919656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94945344e+05, 2.93634938e+05, 2.96246625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.72740844e+05, 2.36921938e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 0., 0., 0., ],
    'CountWeightedFullL1Prefire'                                                     : [ 0., 0., 0., ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 0., 0., ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 0., 0., 0., 0., 0., 0., ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 0., 0., 0., 0., 0., 0., ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   298398),
  ("fsize_local",                     1217085467), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        13451681242), # 13.45GB, avg file size 747.32MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
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

samples_2016["/GluGluToHHTo2B2WToLNu2J_node_8_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2b2v_sl_PSWeights"),
  ("nof_files",                       5),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 298899, ],
    'CountWeighted'                                                                  : [ 2.98876560e+05, 2.98884931e+05, 2.98907990e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98876560e+05, 2.98876560e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.37148263e+05, 2.37471886e+05, 3.69380624e+05, 2.37102795e+05, 2.35315103e+05, 1.22093105e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98912433e+05, 2.99315385e+05, 4.64865841e+05, 2.98860721e+05, 2.95888963e+05, 1.53895762e+05, ],
    'CountWeightedFull'                                                              : [ 2.98815034e+05, 2.98823565e+05, 2.98845801e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98815034e+05, 2.98815034e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.37101141e+05, 2.37424053e+05, 3.69304155e+05, 2.37052236e+05, 2.35265737e+05, 1.22068173e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98852972e+05, 2.99255231e+05, 4.64769558e+05, 2.98796957e+05, 2.95826650e+05, 1.53864304e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92902186e+05, 2.92901782e+05, 2.92925793e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92902186e+05, 2.91385078e+05, 2.94415754e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.92902186e+05, 2.92902186e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.32605664e+05, 2.32675951e+05, 3.61936792e+05, 2.32109470e+05, 2.30680502e+05, 1.19699700e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.93186191e+05, 2.93270480e+05, 4.55494175e+05, 2.92565926e+05, 2.90058425e+05, 1.50878807e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.92842540e+05, 2.92842153e+05, 2.92865732e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.92842540e+05, 2.91325742e+05, 2.94355719e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.92842540e+05, 2.92842540e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.32559817e+05, 2.32629459e+05, 3.61862456e+05, 2.32060509e+05, 2.30632427e+05, 1.19675477e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.93128299e+05, 2.93211990e+05, 4.55400691e+05, 2.92504192e+05, 2.89997885e+05, 1.50848200e+05, ],
  }),
  ("nof_tree_events",                 298899),
  ("nof_db_events",                   298899),
  ("fsize_local",                     1262932171), # 1.26GB, avg file size 252.59MB
  ("fsize_db",                        13370755539), # 13.37GB, avg file size 703.72MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2WToLNu2J_node_9_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
  ("nof_files",                       5),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99941105e+05, 2.99947921e+05, 2.99939812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99941105e+05, 2.99941105e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99934944e+06, 2.99934944e+06, 2.99934944e+06, 2.99934944e+06, 2.99934944e+06, 2.99934944e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99915402e+05, 2.99795689e+05, 4.69221176e+05, 3.00058387e+05, 2.97834183e+05, 1.52438251e+05, ],
    'CountWeightedFull'                                                              : [ 2.99876053e+05, 2.99882605e+05, 2.99874833e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99876053e+05, 2.99876053e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99869638e+06, 2.99869638e+06, 2.99869638e+06, 2.99869638e+06, 2.99869638e+06, 2.99869638e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99853038e+05, 2.99731874e+05, 4.69118773e+05, 2.99990752e+05, 2.97768734e+05, 1.52405613e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93195133e+05, 2.93189148e+05, 2.93203774e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93195133e+05, 2.91519769e+05, 2.94870561e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93195133e+05, 2.93195133e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.93192339e+06, 2.93192339e+06, 2.93192339e+06, 2.93192339e+06, 2.93192339e+06, 2.93192339e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.93445266e+05, 2.92944469e+05, 4.58630992e+05, 2.92952693e+05, 2.91303463e+05, 1.49069376e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.93132255e+05, 2.93126259e+05, 2.93140867e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.93132255e+05, 2.91457388e+05, 2.94807213e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.93132255e+05, 2.93132255e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.93129364e+06, 2.93129364e+06, 2.93129364e+06, 2.93129364e+06, 2.93129364e+06, 2.93129364e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.93384879e+05, 2.92882645e+05, 4.58531949e+05, 2.92887389e+05, 2.91240165e+05, 1.49037784e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1390737110), # 1.39GB, avg file size 278.15MB
  ("fsize_db",                        14367121107), # 14.37GB, avg file size 684.15MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2WToLNu2J_node_10_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2b2v_sl_PSWeights"),
  ("nof_files",                       4),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99945746e+05, 2.99933742e+05, 2.99945672e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99945746e+05, 2.99945746e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.00513014e+06, 1.00248430e+06, 1.50093800e+06, 1.00649950e+06, 9.37024484e+05, 5.17499164e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99837902e+05, 2.99908254e+05, 4.67766613e+05, 3.00249465e+05, 2.98692121e+05, 1.54378059e+05, ],
    'CountWeightedFull'                                                              : [ 2.99883395e+05, 2.99871393e+05, 2.99883031e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99883395e+05, 2.99883395e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.00492830e+06, 1.00227381e+06, 1.50062377e+06, 1.00628067e+06, 9.36831898e+05, 5.17392664e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99777670e+05, 2.99845293e+05, 4.67668695e+05, 3.00184240e+05, 2.98630674e+05, 1.54346271e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93855572e+05, 2.93837564e+05, 2.93866324e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93855572e+05, 2.92311582e+05, 2.95395920e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93855572e+05, 2.93855572e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.85616477e+05, 9.81860219e+05, 1.47033005e+06, 9.84913438e+05, 9.18509828e+05, 5.07206125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.94009277e+05, 2.93724141e+05, 4.58208863e+05, 2.93802148e+05, 2.92767857e+05, 1.51302650e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.93794906e+05, 2.93776855e+05, 2.93805354e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.93794906e+05, 2.92251348e+05, 2.95334807e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.93794906e+05, 2.93794906e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.85419922e+05, 9.81655609e+05, 1.47002452e+06, 9.84700781e+05, 9.18322625e+05, 5.07102531e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.93950617e+05, 2.93662883e+05, 4.58113652e+05, 2.93738703e+05, 2.92708074e+05, 1.51271764e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1270187958), # 1.27GB, avg file size 317.55MB
  ("fsize_db",                        13467941180), # 13.47GB, avg file size 792.23MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2WToLNu2J_node_11_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2b2v_sl_PSWeights"),
  ("nof_files",                       2),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 298398, ],
    'CountWeighted'                                                                  : [ 2.98354969e+05, 2.98384828e+05, 2.98361172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98354969e+05, 2.98354969e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98320388e+06, 2.98320388e+06, 2.98320388e+06, 2.98320388e+06, 2.98320388e+06, 2.98320388e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98360727e+05, 2.98498281e+05, 4.65090953e+05, 2.98415406e+05, 2.96183125e+05, 1.53199512e+05, ],
    'CountWeightedFull'                                                              : [ 2.98292648e+05, 2.98321906e+05, 2.98299906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98292648e+05, 2.98292648e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98258688e+06, 2.98258688e+06, 2.98258688e+06, 2.98258688e+06, 2.98258688e+06, 2.98258688e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98300680e+05, 2.98436547e+05, 4.64993812e+05, 2.98350516e+05, 2.96121312e+05, 1.53167930e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92133125e+05, 2.92144367e+05, 2.92140188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92133125e+05, 2.90563516e+05, 2.93701547e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.92133125e+05, 2.92133125e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.92114688e+06, 2.92114688e+06, 2.92114688e+06, 2.92114688e+06, 2.92114688e+06, 2.92114688e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.92395781e+05, 2.92174055e+05, 4.55309344e+05, 2.91844656e+05, 2.90126609e+05, 1.50070297e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.92072641e+05, 2.92083453e+05, 2.92080352e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.92072641e+05, 2.90503562e+05, 2.93640625e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.92072641e+05, 2.92072641e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.92054500e+06, 2.92054500e+06, 2.92054500e+06, 2.92054500e+06, 2.92054500e+06, 2.92054500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.92337484e+05, 2.92114172e+05, 4.55215078e+05, 2.91781734e+05, 2.90066586e+05, 1.50039594e+05, ],
  }),
  ("nof_tree_events",                 298398),
  ("nof_db_events",                   298398),
  ("fsize_local",                     1293109005), # 1.29GB, avg file size 646.55MB
  ("fsize_db",                        13629128068), # 13.63GB, avg file size 757.17MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2WToLNu2J_node_12_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2v_sl_PSWeights"),
  ("nof_files",                       4),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 295397, ],
    'CountWeighted'                                                                  : [ 2.95409550e+05, 2.95402146e+05, 2.95408417e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.95409550e+05, 2.95409550e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.18421640e+05, 2.18504597e+05, 3.40209973e+05, 2.18491205e+05, 2.17117470e+05, 1.12494320e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.95348202e+05, 2.95458956e+05, 4.59179556e+05, 2.95441632e+05, 2.92736747e+05, 1.52114937e+05, ],
    'CountWeightedFull'                                                              : [ 2.95348677e+05, 2.95341556e+05, 2.95347662e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.95348677e+05, 2.95348677e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.18378437e+05, 2.18460411e+05, 3.40138499e+05, 2.18444431e+05, 2.17071453e+05, 1.12471672e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.95289786e+05, 2.95399051e+05, 4.59083416e+05, 2.95378501e+05, 2.92674822e+05, 1.52084338e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.89484902e+05, 2.89473186e+05, 2.89490744e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.89484902e+05, 2.87984074e+05, 2.90981915e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.89484902e+05, 2.89484902e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.14234260e+05, 2.14076352e+05, 3.33332832e+05, 2.13875346e+05, 2.12835650e+05, 1.10289818e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.89684990e+05, 2.89470664e+05, 4.49896207e+05, 2.89198137e+05, 2.86962435e+05, 1.49133059e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.89425798e+05, 2.89414149e+05, 2.89431813e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.89425798e+05, 2.87925340e+05, 2.90922431e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.89425798e+05, 2.89425798e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.14192201e+05, 2.14033364e+05, 3.33263210e+05, 2.13829834e+05, 2.12790772e+05, 1.10267782e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.89628057e+05, 2.89412417e+05, 4.49802480e+05, 2.89136774e+05, 2.86902036e+05, 1.49103292e+05, ],
  }),
  ("nof_tree_events",                 295397),
  ("nof_db_events",                   295397),
  ("fsize_local",                     1248302431), # 1.25GB, avg file size 312.08MB
  ("fsize_db",                        13215460281), # 13.22GB, avg file size 734.19MB
  ("use_it",                          True),
  ("xsection",                        0.109352),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VLNu2J_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2b2v_sl"),
  ("nof_files",                       3),
  ("nof_db_files",                    43),
  ("nof_events",                      {
    'Count'                                                                          : [ 398998, ],
    'CountWeighted'                                                                  : [ 3.57598895e+05, 3.57530383e+05, 3.57620441e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06886098e+05, 4.00472336e+05, 3.96251836e+05, 3.65771586e+05, 3.57562258e+05, 3.51154191e+05, 3.28400688e+05, 3.19468922e+05, 3.11981398e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.24594184e+05, 3.02261277e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.57620781e+05, 3.57689070e+05, 5.52594816e+05, 3.57509773e+05, 3.55817773e+05, 1.86020602e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.19199854e+04, 1.19198445e+04, 1.84904180e+04, 1.19202471e+04, 1.19314828e+04, 6.20109839e+03, ],
    'CountWeightedFull'                                                              : [ 1.06774369e+04, 1.06760803e+04, 1.06781409e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.21494513e+04, 1.19578247e+04, 1.18317330e+04, 1.09218042e+04, 1.06761145e+04, 1.04852063e+04, 9.80583582e+03, 9.53902539e+03, 9.31542676e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.26782515e+04, 9.02520734e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.06783191e+04, 1.06806427e+04, 1.64999508e+04, 1.06750759e+04, 1.06240801e+04, 5.55442249e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.56106968e+02, 3.56095879e+02, 5.52491474e+02, 3.56234116e+02, 3.56572258e+02, 1.85271296e+02, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.52075172e+05, 3.52005852e+05, 3.52115074e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.52075172e+05, 3.50627668e+05, 3.53519508e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.00519848e+05, 3.94259348e+05, 3.90151594e+05, 3.60078984e+05, 3.52049000e+05, 3.45779496e+05, 3.23308297e+05, 3.14561016e+05, 3.07226477e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.17966008e+05, 2.97649186e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.52150973e+05, 3.52082051e+05, 5.44079398e+05, 3.51934020e+05, 3.50502852e+05, 1.83203459e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.17356707e+04, 1.17313562e+04, 1.82026154e+04, 1.17324071e+04, 1.17510375e+04, 6.10606653e+03, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.05126484e+04, 1.05109528e+04, 1.05137614e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.05126484e+04, 1.04693474e+04, 1.05557552e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.19593030e+04, 1.17722671e+04, 1.16495497e+04, 1.07517858e+04, 1.05117184e+04, 1.03246909e+04, 9.65376465e+03, 9.39245605e+03, 9.17344232e+03, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.24802693e+04, 8.88748596e+03, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.05149346e+04, 1.05131862e+04, 1.62456488e+04, 1.05085299e+04, 1.04653586e+04, 5.47028156e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.50594124e+02, 3.50459610e+02, 5.43876404e+02, 3.50606453e+02, 3.51165482e+02, 1.82427414e+02, ],
  }),
  ("nof_tree_events",                 398998),
  ("nof_db_events",                   398998),
  ("fsize_local",                     1706320345), # 1.71GB, avg file size 568.77MB
  ("fsize_db",                        17448307042), # 17.45GB, avg file size 405.77MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2VLNu2J_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2b2v_sl"),
  ("nof_files",                       5),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 391395, ],
    'CountWeighted'                                                                  : [ 3.37001594e+05, 3.36914891e+05, 3.37102047e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84151305e+05, 3.78848701e+05, 3.75483164e+05, 3.43880035e+05, 3.36997230e+05, 3.31619693e+05, 3.07904434e+05, 3.00332145e+05, 2.93960119e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04670523e+05, 2.81380336e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.37087254e+05, 3.37110670e+05, 5.21428812e+05, 3.36887816e+05, 3.34943609e+05, 1.74612111e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.14020319e+03, 5.14185519e+03, 7.99240515e+03, 5.14106848e+03, 5.14740158e+03, 2.66314557e+03, ],
    'CountWeightedFull'                                                              : [ 4.41910852e+03, 4.41802435e+03, 4.42039633e+03, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.03751538e+03, 4.96790756e+03, 4.92369891e+03, 4.50942957e+03, 4.41904639e+03, 4.34854462e+03, 4.03762274e+03, 3.93826672e+03, 3.85467398e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.30659787e+03, 3.68973279e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.42032233e+03, 4.42068988e+03, 6.83775519e+03, 4.41761469e+03, 4.39221851e+03, 2.28968372e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 6.75434999e+01, 6.75634556e+01, 1.05029072e+02, 6.75533848e+01, 6.76452436e+01, 3.49931216e+01, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.31647211e+05, 3.31554814e+05, 3.31753031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.31647211e+05, 3.30251686e+05, 3.33039004e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.77955424e+05, 3.72796719e+05, 3.69535660e+05, 3.38363512e+05, 3.31640820e+05, 3.26397975e+05, 3.02983234e+05, 2.95581164e+05, 2.89350637e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98156895e+05, 2.76968479e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.31785705e+05, 3.31695883e+05, 5.13083805e+05, 3.31466631e+05, 3.29711738e+05, 1.71907350e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 5.05864478e+03, 5.05842432e+03, 7.86325195e+03, 5.05766385e+03, 5.06622125e+03, 2.62151253e+03, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 4.34891968e+03, 4.34772794e+03, 4.35028882e+03, ],
    'CountWeightedFullL1Prefire'                                                     : [ 4.34891968e+03, 4.33061224e+03, 4.36716891e+03, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.95625720e+03, 4.88853564e+03, 4.84569916e+03, 4.43707935e+03, 4.34883392e+03, 4.28006470e+03, 3.97307727e+03, 3.87595770e+03, 3.79423145e+03, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 5.22116452e+03, 3.63187589e+03, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 4.35079532e+03, 4.34966916e+03, 6.72829132e+03, 4.34650742e+03, 4.32359915e+03, 2.25421671e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 6.64693432e+01, 6.64647112e+01, 1.03328353e+02, 6.64550800e+01, 6.65763073e+01, 3.44447861e+01, ],
  }),
  ("nof_tree_events",                 391395),
  ("nof_db_events",                   391395),
  ("fsize_local",                     1674728124), # 1.67GB, avg file size 334.95MB
  ("fsize_db",                        16836087533), # 16.84GB, avg file size 732.00MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2016["/GluGluToRadionToHHTo2B2VToLNu2J_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbvv_sl"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2v_sl"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.99972664e+05, 2.99988484e+05, 3.00024086e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.25221219e+05, 2.99953078e+05, 2.77657852e+05, 3.25221219e+05, 2.99953078e+05, 2.77657852e+05, 3.25221219e+05, 2.99953078e+05, 2.77657852e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.25221219e+05, 2.77657852e+05, ],
    'CountWeightedFull'                                                              : [ 2.99972664e+05, 2.99988484e+05, 3.00024086e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.25221219e+05, 2.99953078e+05, 2.77657852e+05, 3.25221219e+05, 2.99953078e+05, 2.77657852e+05, 3.25221219e+05, 2.99953078e+05, 2.77657852e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.25221219e+05, 2.77657852e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93001801e+05, 2.93002289e+05, 2.93041754e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93001801e+05, 2.91275934e+05, 2.94731242e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.17600500e+05, 2.92989293e+05, 2.71234844e+05, 3.17600500e+05, 2.92989293e+05, 2.71234844e+05, 3.17600500e+05, 2.92989293e+05, 2.71234844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.17600500e+05, 2.71234844e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.93001801e+05, 2.93002289e+05, 2.93041754e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.93001801e+05, 2.91275934e+05, 2.94731242e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 3.17600500e+05, 2.92989293e+05, 2.71234844e+05, 3.17600500e+05, 2.92989293e+05, 2.71234844e+05, 3.17600500e+05, 2.92989293e+05, 2.71234844e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.17600500e+05, 2.71234844e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1518042143), # 1.52GB, avg file size 759.02MB
  ("fsize_db",                        14421548407), # 14.42GB, avg file size 2.88GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_650_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2016["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 398999, ],
    'CountWeighted'                                                                  : [ 3.97651627e+05, 3.97671891e+05, 3.97656934e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97651627e+05, 3.97651627e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97660127e+06, 3.97660127e+06, 3.97660127e+06, 3.97660127e+06, 3.97660127e+06, 3.97660127e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99031887e+05, 3.98957385e+05, 5.99661270e+05, 3.98934428e+05, 3.96935143e+05, 2.19056273e+05, ],
    'CountWeightedFull'                                                              : [ 3.97476289e+05, 3.97494154e+05, 3.97480830e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97476289e+05, 3.97476289e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97483541e+06, 3.97483541e+06, 3.97483541e+06, 3.97483541e+06, 3.97483541e+06, 3.97483541e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98855598e+05, 3.98780760e+05, 5.99396605e+05, 3.98756824e+05, 3.96760664e+05, 2.18959883e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.84569414e+05, 3.84567766e+05, 3.84581207e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.84569414e+05, 3.81239625e+05, 3.87898096e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.84569414e+05, 3.84569414e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.84570798e+06, 3.84570798e+06, 3.84570798e+06, 3.84570798e+06, 3.84570798e+06, 3.84570798e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.85934104e+05, 3.85617871e+05, 5.79828133e+05, 3.85742277e+05, 3.84186639e+05, 2.12019094e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.84400500e+05, 3.84397811e+05, 3.84411920e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.84400500e+05, 3.81072490e+05, 3.87727299e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.84400500e+05, 3.84400500e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.84401550e+06, 3.84401550e+06, 3.84401550e+06, 3.84401550e+06, 3.84401550e+06, 3.84401550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.85765133e+05, 3.85448682e+05, 5.79574250e+05, 3.85572061e+05, 3.84019146e+05, 2.11926603e+05, ],
  }),
  ("nof_tree_events",                 398999),
  ("nof_db_events",                   398999),
  ("fsize_local",                     1631271752), # 1.63GB, avg file size 407.82MB
  ("fsize_db",                        18635165335), # 18.64GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.0005036125),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       6),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.98606771e+05, 3.98628370e+05, 3.98610643e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.98606771e+05, 3.98606771e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.98617255e+06, 3.98617255e+06, 3.98617255e+06, 3.98617255e+06, 3.98617255e+06, 3.98617255e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00087408e+05, 3.99754181e+05, 6.02205502e+05, 3.99850235e+05, 3.98716130e+05, 2.19123517e+05, ],
    'CountWeightedFull'                                                              : [ 3.98424966e+05, 3.98445284e+05, 3.98428224e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.98424966e+05, 3.98424966e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.98434214e+06, 3.98434214e+06, 3.98434214e+06, 3.98434214e+06, 3.98434214e+06, 3.98434214e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99904090e+05, 3.99570194e+05, 6.01929410e+05, 3.99666394e+05, 3.98534909e+05, 2.19023526e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.83425151e+05, 3.83441564e+05, 3.83413383e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.83425151e+05, 3.79606329e+05, 3.87251957e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.83425151e+05, 3.83425151e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.83429062e+06, 3.83429062e+06, 3.83429062e+06, 3.83429062e+06, 3.83429062e+06, 3.83429062e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.84882968e+05, 3.84351985e+05, 5.79064814e+05, 3.84546050e+05, 3.83729383e+05, 2.10969866e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.83251319e+05, 3.83267095e+05, 3.83239261e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.83251319e+05, 3.79434400e+05, 3.87075802e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.83251319e+05, 3.83251319e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.83254864e+06, 3.83254864e+06, 3.83254864e+06, 3.83254864e+06, 3.83254864e+06, 3.83254864e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.84708411e+05, 3.84176857e+05, 5.78801639e+05, 3.84370924e+05, 3.83556490e+05, 2.10874435e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1637723452), # 1.64GB, avg file size 272.95MB
  ("fsize_db",                        18828525571), # 18.83GB, avg file size 818.63MB
  ("use_it",                          True),
  ("xsection",                        0.0001886003),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 395494, ],
    'CountWeighted'                                                                  : [ 3.94065688e+05, 3.94075891e+05, 3.94063250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94065688e+05, 3.94065688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94136175e+06, 3.94136175e+06, 3.94136175e+06, 3.94136175e+06, 3.94136175e+06, 3.94136175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95626609e+05, 3.95388047e+05, 5.99343000e+05, 3.95347312e+05, 3.93732797e+05, 2.13440000e+05, ],
    'CountWeightedFull'                                                              : [ 3.93872172e+05, 3.93882688e+05, 3.93871453e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.93872172e+05, 3.93872172e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.93940250e+06, 3.93940250e+06, 3.93940250e+06, 3.93940250e+06, 3.93940250e+06, 3.93940250e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95437891e+05, 3.95199859e+05, 5.99053312e+05, 3.95158266e+05, 3.93541750e+05, 2.13339352e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.75191375e+05, 3.75190297e+05, 3.75189391e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.75191375e+05, 3.70609438e+05, 3.79792344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.75191375e+05, 3.75191375e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.75213625e+06, 3.75213625e+06, 3.75213625e+06, 3.75213625e+06, 3.75213625e+06, 3.75213625e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.76705234e+05, 3.76193250e+05, 5.70502078e+05, 3.76319594e+05, 3.75227422e+05, 2.03408664e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.75010250e+05, 3.75008828e+05, 3.75008938e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.75010250e+05, 3.70430906e+05, 3.79608266e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.75010250e+05, 3.75010250e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.75031400e+06, 3.75031400e+06, 3.75031400e+06, 3.75031400e+06, 3.75031400e+06, 3.75031400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.76527469e+05, 3.76016250e+05, 5.70229469e+05, 3.76141797e+05, 3.75047484e+05, 2.03313867e+05, ],
  }),
  ("nof_tree_events",                 395494),
  ("nof_db_events",                   395494),
  ("fsize_local",                     1720411863), # 1.72GB, avg file size 860.21MB
  ("fsize_db",                        19284295734), # 19.28GB, avg file size 803.51MB
  ("use_it",                          True),
  ("xsection",                        0.0001554708),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2WToLNu2J_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 398193, ],
    'CountWeighted'                                                                  : [ 3.95900953e+05, 3.95966250e+05, 3.95883422e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95900953e+05, 3.95900953e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95878362e+06, 3.95878362e+06, 3.95878362e+06, 3.95878362e+06, 3.95878362e+06, 3.95878362e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.98323922e+05, 3.98286266e+05, 6.00835625e+05, 3.97998625e+05, 3.96097844e+05, 2.16490125e+05, ],
    'CountWeightedFull'                                                              : [ 3.95702453e+05, 3.95762844e+05, 3.95683953e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95702453e+05, 3.95702453e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95679700e+06, 3.95679700e+06, 3.95679700e+06, 3.95679700e+06, 3.95679700e+06, 3.95679700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98125406e+05, 3.98088109e+05, 6.00534094e+05, 3.97799250e+05, 3.95899219e+05, 2.16382852e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.79365875e+05, 3.79383922e+05, 3.79364578e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.79365875e+05, 3.75422922e+05, 3.83325578e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.79365875e+05, 3.79365875e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.79355750e+06, 3.79355750e+06, 3.79355750e+06, 3.79355750e+06, 3.79355750e+06, 3.79355750e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.81715266e+05, 3.81461594e+05, 5.75600750e+05, 3.81303844e+05, 3.79865359e+05, 2.07651672e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.79177953e+05, 3.79194156e+05, 3.79176203e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.79177953e+05, 3.75237500e+05, 3.83135406e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.79177953e+05, 3.79177953e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.79168012e+06, 3.79168012e+06, 3.79168012e+06, 3.79168012e+06, 3.79168012e+06, 3.79168012e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.81526781e+05, 3.81273734e+05, 5.75314891e+05, 3.81115203e+05, 3.79676797e+05, 2.07549828e+05, ],
  }),
  ("nof_tree_events",                 398193),
  ("nof_db_events",                   398193),
  ("fsize_local",                     1973262058), # 1.97GB, avg file size 986.63MB
  ("fsize_db",                        20938124623), # 20.94GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.001553578),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2WToLNu2J_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       3),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.97938067e+05, 3.97989016e+05, 3.97977265e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97938067e+05, 3.97938067e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97993407e+06, 3.97993407e+06, 3.97993407e+06, 3.97993407e+06, 3.97993407e+06, 3.97993407e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00060996e+05, 4.00606238e+05, 6.03050965e+05, 3.99899435e+05, 3.97167134e+05, 2.17715072e+05, ],
    'CountWeightedFull'                                                              : [ 3.97743126e+05, 3.97794634e+05, 3.97782775e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97743126e+05, 3.97743126e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97799325e+06, 3.97799325e+06, 3.97799325e+06, 3.97799325e+06, 3.97799325e+06, 3.97799325e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99866026e+05, 4.00409986e+05, 6.02755318e+05, 3.99702910e+05, 3.96973647e+05, 2.17609643e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81969998e+05, 3.81987425e+05, 3.81983162e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81969998e+05, 3.78113219e+05, 3.85842085e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81969998e+05, 3.81969998e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81987594e+06, 3.81987594e+06, 3.81987594e+06, 3.81987594e+06, 3.81987594e+06, 3.81987594e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.83999089e+05, 3.84310562e+05, 5.78629213e+05, 3.83741000e+05, 3.81451243e+05, 2.09164595e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81784940e+05, 3.81802195e+05, 3.81798650e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81784940e+05, 3.77930440e+05, 3.85654548e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81784940e+05, 3.81784940e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81802916e+06, 3.81802916e+06, 3.81802916e+06, 3.81802916e+06, 3.81802916e+06, 3.81802916e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.83813880e+05, 3.84124413e+05, 5.78348517e+05, 3.83554701e+05, 3.81267183e+05, 2.09064259e+05, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     1933077333), # 1.93GB, avg file size 644.36MB
  ("fsize_db",                        20402821916), # 20.40GB, avg file size 2.55GB
  ("use_it",                          True),
  ("xsection",                        0.001182709),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2WToLNu2J_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_bbvv_sl"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_2b2v_sl_dipoleRecoilOff"),
  ("nof_files",                       6),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                                          : [ 399096, ],
    'CountWeighted'                                                                  : [ 3.97141691e+05, 3.97171062e+05, 3.97125342e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97141691e+05, 3.97141691e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97136620e+06, 3.97136620e+06, 3.97136620e+06, 3.97136620e+06, 3.97136620e+06, 3.97136620e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99108283e+05, 3.99136061e+05, 6.00630688e+05, 3.99070510e+05, 3.96841809e+05, 2.18205685e+05, ],
    'CountWeightedFull'                                                              : [ 3.96954867e+05, 3.96982545e+05, 3.96938578e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96954867e+05, 3.96954867e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96949855e+06, 3.96949855e+06, 3.96949855e+06, 3.96949855e+06, 3.96949855e+06, 3.96949855e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98920154e+05, 3.98947410e+05, 6.00345109e+05, 3.98881525e+05, 3.96653986e+05, 2.18103620e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81566738e+05, 3.81567367e+05, 3.81564076e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81566738e+05, 3.77761049e+05, 3.85385379e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81566738e+05, 3.81566738e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81563225e+06, 3.81563225e+06, 3.81563225e+06, 3.81563225e+06, 3.81563225e+06, 3.81563225e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.83476441e+05, 3.83279158e+05, 5.76912045e+05, 3.83335293e+05, 3.81547957e+05, 2.09843333e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81387988e+05, 3.81388273e+05, 3.81385508e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81387988e+05, 3.77584713e+05, 3.85204475e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81387988e+05, 3.81387988e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81384741e+06, 3.81384741e+06, 3.81384741e+06, 3.81384741e+06, 3.81384741e+06, 3.81384741e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.83297354e+05, 3.83099648e+05, 5.76640301e+05, 3.83155426e+05, 3.81369059e+05, 2.09745938e+05, ],
  }),
  ("nof_tree_events",                 399096),
  ("nof_db_events",                   399096),
  ("fsize_local",                     1858418722), # 1.86GB, avg file size 309.74MB
  ("fsize_db",                        20236728193), # 20.24GB, avg file size 749.51MB
  ("use_it",                          True),
  ("xsection",                        0.002959034),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_250_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 399200, ],
    'CountWeighted'                                                                  : [ 3.99153422e+05, 3.99141078e+05, 3.99158000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99153422e+05, 3.99153422e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99168138e+06, 3.99168138e+06, 3.99168138e+06, 3.99168138e+06, 3.99168138e+06, 3.99168138e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99116562e+05, 3.98877125e+05, 6.46680906e+05, 3.99323266e+05, 3.94030672e+05, 1.83652219e+05, ],
    'CountWeightedFull'                                                              : [ 3.99109938e+05, 3.99098219e+05, 3.99114297e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99109938e+05, 3.99109938e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99125025e+06, 3.99125025e+06, 3.99125025e+06, 3.99125025e+06, 3.99125025e+06, 3.99125025e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99076297e+05, 3.98835922e+05, 6.46609844e+05, 3.99276469e+05, 3.93986500e+05, 1.83633039e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.90983781e+05, 3.90970766e+05, 3.90987031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.90983781e+05, 3.88888734e+05, 3.93069047e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.90983781e+05, 3.90983781e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.90989500e+06, 3.90989500e+06, 3.90989500e+06, 3.90989500e+06, 3.90989500e+06, 3.90989500e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.91313375e+05, 3.90616328e+05, 6.33344859e+05, 3.90686312e+05, 3.86137922e+05, 1.80012266e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.90941969e+05, 3.90929203e+05, 3.90945125e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.90941969e+05, 3.88847406e+05, 3.93027031e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.90941969e+05, 3.90941969e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.90948000e+06, 3.90948000e+06, 3.90948000e+06, 3.90948000e+06, 3.90948000e+06, 3.90948000e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.91274625e+05, 3.90576656e+05, 6.33276531e+05, 3.90641359e+05, 3.86095453e+05, 1.79993758e+05, ],
  }),
  ("nof_tree_events",                 399200),
  ("nof_db_events",                   399200),
  ("fsize_local",                     1979515577), # 1.98GB, avg file size 989.76MB
  ("fsize_db",                        21299446883), # 21.30GB, avg file size 3.55GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_260_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_260_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 395000, ],
    'CountWeighted'                                                                  : [ 3.94950688e+05, 3.94955625e+05, 3.94933047e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94950688e+05, 3.94950688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94913725e+06, 3.94913725e+06, 3.94913725e+06, 3.94913725e+06, 3.94913725e+06, 3.94913725e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95156422e+05, 3.95237688e+05, 6.40830281e+05, 3.94816969e+05, 3.89340188e+05, 1.80847672e+05, ],
    'CountWeightedFull'                                                              : [ 3.94908547e+05, 3.94913062e+05, 3.94891312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.94908547e+05, 3.94908547e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.94872512e+06, 3.94872512e+06, 3.94872512e+06, 3.94872512e+06, 3.94872512e+06, 3.94872512e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95117312e+05, 3.95197797e+05, 6.40759531e+05, 3.94771281e+05, 3.89295625e+05, 1.80829031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86742266e+05, 3.86734297e+05, 3.86745578e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86742266e+05, 3.84639703e+05, 3.88838078e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.86742266e+05, 3.86742266e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.86721562e+06, 3.86721562e+06, 3.86721562e+06, 3.86721562e+06, 3.86721562e+06, 3.86721562e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.87301500e+05, 3.86922656e+05, 6.27475578e+05, 3.86155234e+05, 3.81470547e+05, 1.77188160e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.86701594e+05, 3.86693531e+05, 3.86705203e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.86701594e+05, 3.84599500e+05, 3.88797188e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.86701594e+05, 3.86701594e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.86681362e+06, 3.86681362e+06, 3.86681362e+06, 3.86681362e+06, 3.86681362e+06, 3.86681362e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.87263656e+05, 3.86884250e+05, 6.27407344e+05, 3.86111109e+05, 3.81427562e+05, 1.77170160e+05, ],
  }),
  ("nof_tree_events",                 395000),
  ("nof_db_events",                   395000),
  ("fsize_local",                     1988004979), # 1.99GB, avg file size 994.00MB
  ("fsize_db",                        21209489911), # 21.21GB, avg file size 4.24GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_270_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_270_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 395700, ],
    'CountWeighted'                                                                  : [ 3.95613203e+05, 3.95619641e+05, 3.95612938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95613203e+05, 3.95613203e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95634088e+06, 3.95634088e+06, 3.95634088e+06, 3.95634088e+06, 3.95634088e+06, 3.95634088e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95740484e+05, 3.96221938e+05, 6.43525938e+05, 3.95708719e+05, 3.90266266e+05, 1.80465305e+05, ],
    'CountWeightedFull'                                                              : [ 3.95568859e+05, 3.95576219e+05, 3.95568391e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95568859e+05, 3.95568859e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95589575e+06, 3.95589575e+06, 3.95589575e+06, 3.95589575e+06, 3.95589575e+06, 3.95589575e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95699609e+05, 3.96180438e+05, 6.43452609e+05, 3.95660672e+05, 3.90220016e+05, 1.80445797e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87235750e+05, 3.87233391e+05, 3.87238828e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87235750e+05, 3.85097016e+05, 3.89373250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.87235750e+05, 3.87235750e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.87249188e+06, 3.87249188e+06, 3.87249188e+06, 3.87249188e+06, 3.87249188e+06, 3.87249188e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.87710062e+05, 3.87680812e+05, 6.29769125e+05, 3.86851422e+05, 3.82191766e+05, 1.76750574e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.87193109e+05, 3.87191344e+05, 3.87196188e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.87193109e+05, 3.85054844e+05, 3.89330250e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.87193109e+05, 3.87193109e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.87206362e+06, 3.87206362e+06, 3.87206362e+06, 3.87206362e+06, 3.87206362e+06, 3.87206362e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.87670562e+05, 3.87640703e+05, 6.29698359e+05, 3.86805141e+05, 3.82146906e+05, 1.76731781e+05, ],
  }),
  ("nof_tree_events",                 395700),
  ("nof_db_events",                   395700),
  ("fsize_local",                     2019732413), # 2.02GB, avg file size 1.01GB
  ("fsize_db",                        21337721793), # 21.34GB, avg file size 3.05GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_280_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_280_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 396400, ],
    'CountWeighted'                                                                  : [ 3.96297797e+05, 3.96331016e+05, 3.96291156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96297797e+05, 3.96297797e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96319700e+06, 3.96319700e+06, 3.96319700e+06, 3.96319700e+06, 3.96319700e+06, 3.96319700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96364797e+05, 3.96612422e+05, 6.45074641e+05, 3.96415359e+05, 3.91253500e+05, 1.80343727e+05, ],
    'CountWeightedFull'                                                              : [ 3.96253156e+05, 3.96285953e+05, 3.96246781e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96253156e+05, 3.96253156e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96274538e+06, 3.96274538e+06, 3.96274538e+06, 3.96274538e+06, 3.96274538e+06, 3.96274538e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96322891e+05, 3.96569094e+05, 6.44999094e+05, 3.96366625e+05, 3.91206219e+05, 1.80323891e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87849484e+05, 3.87863484e+05, 3.87849078e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87849484e+05, 3.85692344e+05, 3.90001578e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.87849484e+05, 3.87849484e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.87861025e+06, 3.87861025e+06, 3.87861025e+06, 3.87861025e+06, 3.87861025e+06, 3.87861025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.88252812e+05, 3.88012391e+05, 6.31149562e+05, 3.87479984e+05, 3.83042453e+05, 1.76594383e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.87806281e+05, 3.87820156e+05, 3.87806062e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.87806281e+05, 3.85649547e+05, 3.89957984e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.87806281e+05, 3.87806281e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.87817775e+06, 3.87817775e+06, 3.87817775e+06, 3.87817775e+06, 3.87817775e+06, 3.87817775e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.88212375e+05, 3.87970781e+05, 6.31076812e+05, 3.87432969e+05, 3.82996938e+05, 1.76575164e+05, ],
  }),
  ("nof_tree_events",                 396400),
  ("nof_db_events",                   396400),
  ("fsize_local",                     2049989896), # 2.05GB, avg file size 1.02GB
  ("fsize_db",                        21531514022), # 21.53GB, avg file size 4.31GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99958469e+05, 2.99975273e+05, 2.99948789e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99958469e+05, 2.99958469e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99982353e+06, 2.99982353e+06, 2.99982353e+06, 2.99982353e+06, 2.99982353e+06, 2.99982353e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00055430e+05, 3.00166680e+05, 4.89148188e+05, 2.99982035e+05, 2.95856547e+05, 1.35547697e+05, ],
    'CountWeightedFull'                                                              : [ 2.99922297e+05, 2.99939227e+05, 2.99912680e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99922297e+05, 2.99922297e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99946359e+06, 2.99946359e+06, 2.99946359e+06, 2.99946359e+06, 2.99946359e+06, 2.99946359e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00021672e+05, 3.00132039e+05, 4.89087180e+05, 2.99943281e+05, 2.95818238e+05, 1.35531934e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93329371e+05, 2.93337066e+05, 2.93324152e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93329371e+05, 2.91643785e+05, 2.95010672e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93329371e+05, 2.93329371e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.93340562e+06, 2.93340562e+06, 2.93340562e+06, 2.93340562e+06, 2.93340562e+06, 2.93340562e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.93695906e+05, 2.93447004e+05, 4.78240438e+05, 2.92984875e+05, 2.89416656e+05, 1.32631182e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.93294656e+05, 2.93302477e+05, 2.93289461e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.93294656e+05, 2.91609320e+05, 2.94975602e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.93294656e+05, 2.93294656e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.93306016e+06, 2.93306016e+06, 2.93306016e+06, 2.93306016e+06, 2.93306016e+06, 2.93306016e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.93663465e+05, 2.93413750e+05, 4.78181719e+05, 2.92947547e+05, 2.89379855e+05, 1.32615973e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1592623049), # 1.59GB, avg file size 796.31MB
  ("fsize_db",                        16521214810), # 16.52GB, avg file size 3.30GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_320_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_320_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299200, ],
    'CountWeighted'                                                                  : [ 2.99167691e+05, 2.99160328e+05, 2.99151355e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99167691e+05, 2.99167691e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99155531e+06, 2.99155531e+06, 2.99155531e+06, 2.99155531e+06, 2.99155397e+06, 2.99155397e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99338629e+05, 2.99148844e+05, 4.88454648e+05, 2.99016164e+05, 2.95277680e+05, 1.34737488e+05, ],
    'CountWeightedFull'                                                              : [ 2.99131898e+05, 2.99124547e+05, 2.99115969e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99131898e+05, 2.99131898e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99119931e+06, 2.99119931e+06, 2.99119931e+06, 2.99119931e+06, 2.99119794e+06, 2.99119794e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99305152e+05, 2.99114852e+05, 4.88395062e+05, 2.98977723e+05, 2.95240516e+05, 1.34721932e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92394336e+05, 2.92387227e+05, 2.92389797e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92394336e+05, 2.90682840e+05, 2.94104016e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.92394336e+05, 2.92394336e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.92389184e+06, 2.92389184e+06, 2.92389184e+06, 2.92389184e+06, 2.92389053e+06, 2.92389053e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.92849266e+05, 2.92272211e+05, 4.77368477e+05, 2.91870242e+05, 2.88785105e+05, 1.31756738e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.92360008e+05, 2.92352875e+05, 2.92355570e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.92360008e+05, 2.90648977e+05, 2.94069297e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.92360008e+05, 2.92360008e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.92354981e+06, 2.92354981e+06, 2.92354981e+06, 2.92354981e+06, 2.92354850e+06, 2.92354850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.92817141e+05, 2.92239430e+05, 4.77310969e+05, 2.91833398e+05, 2.88749273e+05, 1.31741816e+05, ],
  }),
  ("nof_tree_events",                 299200),
  ("nof_db_events",                   299200),
  ("fsize_local",                     1622477156), # 1.62GB, avg file size 811.24MB
  ("fsize_db",                        16662151278), # 16.66GB, avg file size 3.33GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_350_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_350_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 298000, ],
    'CountWeighted'                                                                  : [ 2.97964590e+05, 2.97966875e+05, 2.97969227e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.97964590e+05, 2.97964590e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.97968028e+06, 2.97968028e+06, 2.97968028e+06, 2.97968028e+06, 2.97968028e+06, 2.97968028e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98120453e+05, 2.97761070e+05, 4.88112492e+05, 2.97819621e+05, 2.94498109e+05, 1.33026395e+05, ],
    'CountWeightedFull'                                                              : [ 2.97927465e+05, 2.97929738e+05, 2.97931879e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.97927465e+05, 2.97927465e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.97930581e+06, 2.97930581e+06, 2.97930581e+06, 2.97930581e+06, 2.97930581e+06, 2.97930581e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98085422e+05, 2.97724871e+05, 4.88050125e+05, 2.97779164e+05, 2.94459637e+05, 1.33010057e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91029574e+05, 2.91026387e+05, 2.91033520e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91029574e+05, 2.89282566e+05, 2.92772629e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.91029574e+05, 2.91029574e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.91032722e+06, 2.91032722e+06, 2.91032722e+06, 2.91032722e+06, 2.91032722e+06, 2.91032722e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.91468324e+05, 2.90679543e+05, 4.76661906e+05, 2.90513977e+05, 2.87815805e+05, 1.30012004e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.90993777e+05, 2.90990508e+05, 2.90997754e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.90993777e+05, 2.89247125e+05, 2.92736520e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.90993777e+05, 2.90993777e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.90996650e+06, 2.90996650e+06, 2.90996650e+06, 2.90996650e+06, 2.90996650e+06, 2.90996650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.91434629e+05, 2.90644797e+05, 4.76601828e+05, 2.90475102e+05, 2.87778879e+05, 1.29996297e+05, ],
  }),
  ("nof_tree_events",                 298000),
  ("nof_db_events",                   298000),
  ("fsize_local",                     1665077427), # 1.67GB, avg file size 832.54MB
  ("fsize_db",                        16908533930), # 16.91GB, avg file size 2.11GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_400_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_400_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 298400, ],
    'CountWeighted'                                                                  : [ 2.98328066e+05, 2.98320816e+05, 2.98313215e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98328066e+05, 2.98328066e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98313859e+06, 2.98313859e+06, 2.98313859e+06, 2.98313859e+06, 2.98313859e+06, 2.98313859e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98147828e+05, 2.98057156e+05, 4.89610523e+05, 2.98749445e+05, 2.93934152e+05, 1.31910182e+05, ],
    'CountWeightedFull'                                                              : [ 2.98288352e+05, 2.98281125e+05, 2.98273609e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98288352e+05, 2.98288352e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98274275e+06, 2.98274275e+06, 2.98274275e+06, 2.98274275e+06, 2.98274275e+06, 2.98274275e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98110340e+05, 2.98018723e+05, 4.89544133e+05, 2.98706504e+05, 2.93893797e+05, 1.31893090e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91132945e+05, 2.91118043e+05, 2.91130348e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91132945e+05, 2.89331488e+05, 2.92931590e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.91132945e+05, 2.91132945e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.91125069e+06, 2.91125069e+06, 2.91125069e+06, 2.91125069e+06, 2.91125069e+06, 2.91125069e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.91246102e+05, 2.90781043e+05, 4.77787164e+05, 2.91161223e+05, 2.87013629e+05, 1.28783371e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.91094699e+05, 2.91079781e+05, 2.91092355e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.91094699e+05, 2.89293699e+05, 2.92892988e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.91094699e+05, 2.91094699e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.91086959e+06, 2.91086959e+06, 2.91086959e+06, 2.91086959e+06, 2.91086959e+06, 2.91086959e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.91210137e+05, 2.90744262e+05, 4.77723531e+05, 2.91120051e+05, 2.86974957e+05, 1.28766980e+05, ],
  }),
  ("nof_tree_events",                 298400),
  ("nof_db_events",                   298400),
  ("fsize_local",                     1732708063), # 1.73GB, avg file size 866.35MB
  ("fsize_db",                        17255325259), # 17.26GB, avg file size 3.45GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_450_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_450_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 298400, ],
    'CountWeighted'                                                                  : [ 2.98346012e+05, 2.98329758e+05, 2.98260758e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98346012e+05, 2.98346012e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98365416e+06, 2.98365416e+06, 2.98365416e+06, 2.98365416e+06, 2.98365416e+06, 2.98365416e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98457297e+05, 2.98590488e+05, 4.91953109e+05, 2.98349438e+05, 2.94009977e+05, 1.30501514e+05, ],
    'CountWeightedFull'                                                              : [ 2.98304277e+05, 2.98288645e+05, 2.98220445e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98304277e+05, 2.98304277e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98323016e+06, 2.98323016e+06, 2.98323016e+06, 2.98323016e+06, 2.98323016e+06, 2.98323016e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98418156e+05, 2.98550051e+05, 4.91883312e+05, 2.98304664e+05, 2.93967559e+05, 1.30483768e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90963672e+05, 2.90946477e+05, 2.90926867e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90963672e+05, 2.89121684e+05, 2.92805336e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.90963672e+05, 2.90963672e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.90973844e+06, 2.90973844e+06, 2.90973844e+06, 2.90973844e+06, 2.90973844e+06, 2.90973844e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.91369438e+05, 2.91050066e+05, 4.79742109e+05, 2.90584238e+05, 2.86939379e+05, 1.27334994e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.90923633e+05, 2.90906766e+05, 2.90887391e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.90923633e+05, 2.89082086e+05, 2.92764984e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.90923633e+05, 2.90923633e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.90933506e+06, 2.90933506e+06, 2.90933506e+06, 2.90933506e+06, 2.90933506e+06, 2.90933506e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.91331832e+05, 2.91011238e+05, 4.79675078e+05, 2.90541324e+05, 2.86898418e+05, 1.27317945e+05, ],
  }),
  ("nof_tree_events",                 298400),
  ("nof_db_events",                   298400),
  ("fsize_local",                     1790622229), # 1.79GB, avg file size 895.31MB
  ("fsize_db",                        17580406855), # 17.58GB, avg file size 5.86GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_500_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99946520e+05, 2.99962430e+05, 3.00006277e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99946520e+05, 2.99946520e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99932522e+06, 2.99932522e+06, 2.99932522e+06, 2.99932522e+06, 2.99932522e+06, 2.99932522e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00056789e+05, 3.00089332e+05, 4.94773188e+05, 2.99977688e+05, 2.94463383e+05, 1.30089283e+05, ],
    'CountWeightedFull'                                                              : [ 2.99903621e+05, 2.99918680e+05, 2.99962180e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99903621e+05, 2.99903621e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99890112e+06, 2.99890112e+06, 2.99890112e+06, 2.99890112e+06, 2.99890112e+06, 2.99890112e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00016352e+05, 3.00047797e+05, 4.94700609e+05, 2.99931293e+05, 2.94419027e+05, 1.30070852e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92368641e+05, 2.92366465e+05, 2.92407445e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92368641e+05, 2.90482883e+05, 2.94256203e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.92368641e+05, 2.92368641e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.92361181e+06, 2.92361181e+06, 2.92361181e+06, 2.92361181e+06, 2.92361181e+06, 2.92361181e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.92775004e+05, 2.92401508e+05, 4.82243391e+05, 2.92007992e+05, 2.87187121e+05, 1.26852414e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.92327438e+05, 2.92324797e+05, 2.92365816e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.92327438e+05, 2.90442109e+05, 2.94214559e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.92327438e+05, 2.92327438e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.92320144e+06, 2.92320144e+06, 2.92320144e+06, 2.92320144e+06, 2.92320144e+06, 2.92320144e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.92736207e+05, 2.92361699e+05, 4.82173859e+05, 2.91963582e+05, 2.87144527e+05, 1.26834676e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1848705835), # 1.85GB, avg file size 924.35MB
  ("fsize_db",                        17956939093), # 17.96GB, avg file size 5.99GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_550_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_550_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 299300, ],
    'CountWeighted'                                                                  : [ 2.99209961e+05, 2.99252695e+05, 2.99242656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99209961e+05, 2.99209961e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99232300e+06, 2.99232300e+06, 2.99232300e+06, 2.99232300e+06, 2.99232300e+06, 2.99232300e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99428695e+05, 2.99103688e+05, 4.94978164e+05, 2.99128504e+05, 2.94362074e+05, 1.28983824e+05, ],
    'CountWeightedFull'                                                              : [ 2.99166535e+05, 2.99208922e+05, 2.99199594e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99166535e+05, 2.99166535e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99188847e+06, 2.99188847e+06, 2.99188847e+06, 2.99188847e+06, 2.99188847e+06, 2.99188847e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99387750e+05, 2.99061535e+05, 4.94905734e+05, 2.99081746e+05, 2.94318504e+05, 1.28965428e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91524328e+05, 2.91544730e+05, 2.91544133e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91524328e+05, 2.89613945e+05, 2.93433766e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.91524328e+05, 2.91524328e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.91537103e+06, 2.91537103e+06, 2.91537103e+06, 2.91537103e+06, 2.91537103e+06, 2.91537103e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.92035242e+05, 2.91312543e+05, 4.82225523e+05, 2.91022613e+05, 2.86943805e+05, 1.25709689e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.91482719e+05, 2.91502809e+05, 2.91502621e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.91482719e+05, 2.89572809e+05, 2.93391590e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.91482719e+05, 2.91482719e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.91495438e+06, 2.91495438e+06, 2.91495438e+06, 2.91495438e+06, 2.91495438e+06, 2.91495438e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.91995965e+05, 2.91272121e+05, 4.82156516e+05, 2.90977824e+05, 2.86902105e+05, 1.25692053e+05, ],
  }),
  ("nof_tree_events",                 299300),
  ("nof_db_events",                   299300),
  ("fsize_local",                     1883776896), # 1.88GB, avg file size 941.89MB
  ("fsize_db",                        18237199185), # 18.24GB, avg file size 3.04GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_600_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99944719e+05, 1.99936750e+05, 1.99956375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99944719e+05, 1.99944719e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99943875e+06, 1.99943875e+06, 1.99943875e+06, 1.99943875e+06, 1.99943875e+06, 1.99943875e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00028156e+05, 1.99954391e+05, 3.31567188e+05, 1.99949922e+05, 1.96481109e+05, 8.54491250e+04, ],
    'CountWeightedFull'                                                              : [ 1.99913188e+05, 1.99905656e+05, 1.99924391e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99913188e+05, 1.99913188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99912300e+06, 1.99912300e+06, 1.99912300e+06, 1.99912300e+06, 1.99912300e+06, 1.99912300e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99998594e+05, 1.99924438e+05, 3.31513438e+05, 1.99916344e+05, 1.96447703e+05, 8.54359219e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94745062e+05, 1.94733062e+05, 1.94759438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94745062e+05, 1.93459516e+05, 1.96029875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.94745062e+05, 1.94745062e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.94744525e+06, 1.94744525e+06, 1.94744525e+06, 1.94744525e+06, 1.94744525e+06, 1.94744525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.95030953e+05, 1.94665734e+05, 3.22916344e+05, 1.94480812e+05, 1.91492172e+05, 8.32566016e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.94714891e+05, 1.94703188e+05, 1.94728938e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.94714891e+05, 1.93429609e+05, 1.95999438e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.94714891e+05, 1.94714891e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.94714362e+06, 1.94714362e+06, 1.94714362e+06, 1.94714362e+06, 1.94714362e+06, 1.94714362e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.95002438e+05, 1.94637000e+05, 3.22864781e+05, 1.94448750e+05, 1.91460094e+05, 8.32439531e+04, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1282009507), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        12377694096), # 12.38GB, avg file size 2.48GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_650_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99943859e+05, 1.99967703e+05, 1.99946312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99943859e+05, 1.99943859e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99959125e+06, 1.99959125e+06, 1.99959125e+06, 1.99959125e+06, 1.99959125e+06, 1.99959125e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99920500e+05, 2.00334750e+05, 3.30976188e+05, 2.00077641e+05, 1.94732328e+05, 8.49533906e+04, ],
    'CountWeightedFull'                                                              : [ 1.99911812e+05, 1.99934750e+05, 1.99914031e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99911812e+05, 1.99911812e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99926362e+06, 1.99926362e+06, 1.99926362e+06, 1.99926362e+06, 1.99926362e+06, 1.99926362e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99890125e+05, 2.00303438e+05, 3.30922094e+05, 2.00042344e+05, 1.94699844e+05, 8.49397500e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94687984e+05, 1.94692656e+05, 1.94698281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94687984e+05, 1.93387281e+05, 1.95990500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.94687984e+05, 1.94687984e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.94694375e+06, 1.94694375e+06, 1.94694375e+06, 1.94694375e+06, 1.94694375e+06, 1.94694375e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.94864203e+05, 1.94985281e+05, 3.22262938e+05, 1.94535000e+05, 1.89736766e+05, 8.27450078e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.94656859e+05, 1.94661188e+05, 1.94667109e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.94656859e+05, 1.93356484e+05, 1.95959062e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.94656859e+05, 1.94656859e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.94663012e+06, 1.94663012e+06, 1.94663012e+06, 1.94663012e+06, 1.94663012e+06, 1.94663012e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.94834891e+05, 1.94955234e+05, 3.22210875e+05, 1.94501172e+05, 1.89705375e+05, 8.27319453e+04, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1302597429), # 1.30GB, avg file size 1.30GB
  ("fsize_db",                        12477486812), # 12.48GB, avg file size 3.12GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_700_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_700_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99926922e+05, 1.99937594e+05, 1.99934375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99926922e+05, 1.99926922e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99925550e+06, 1.99925550e+06, 1.99925550e+06, 1.99925550e+06, 1.99925550e+06, 1.99925550e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00001844e+05, 2.00041828e+05, 3.32202938e+05, 2.00001734e+05, 1.95760812e+05, 8.44283594e+04, ],
    'CountWeightedFull'                                                              : [ 1.99893359e+05, 1.99904484e+05, 1.99900969e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99893359e+05, 1.99893359e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99891838e+06, 1.99891838e+06, 1.99891838e+06, 1.99891838e+06, 1.99891838e+06, 1.99891838e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99970344e+05, 2.00009750e+05, 3.32147156e+05, 1.99966047e+05, 1.95727031e+05, 8.44143281e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94591750e+05, 1.94600469e+05, 1.94594141e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94591750e+05, 1.93279578e+05, 1.95906031e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.94591750e+05, 1.94591750e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.94593012e+06, 1.94593012e+06, 1.94593012e+06, 1.94593012e+06, 1.94593012e+06, 1.94593012e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.94874188e+05, 1.94616188e+05, 3.23328500e+05, 1.94382219e+05, 1.90659516e+05, 8.22053359e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.94559641e+05, 1.94568641e+05, 1.94561984e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.94559641e+05, 1.93247719e+05, 1.95873562e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.94559641e+05, 1.94559641e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.94560800e+06, 1.94560800e+06, 1.94560800e+06, 1.94560800e+06, 1.94560800e+06, 1.94560800e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.94843969e+05, 1.94585359e+05, 3.23275125e+05, 1.94348000e+05, 1.90627125e+05, 8.21918828e+04, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1318897073), # 1.32GB, avg file size 1.32GB
  ("fsize_db",                        12617931333), # 12.62GB, avg file size 4.21GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99906375e+05, 1.99871125e+05, 1.99911828e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99906375e+05, 1.99906375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99882675e+06, 1.99882675e+06, 1.99882675e+06, 1.99882675e+06, 1.99882675e+06, 1.99882675e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00015797e+05, 2.00371594e+05, 3.33303094e+05, 2.00020953e+05, 1.95808062e+05, 8.38819219e+04, ],
    'CountWeightedFull'                                                              : [ 1.99873516e+05, 1.99838812e+05, 1.99879062e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99873516e+05, 1.99873516e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99850325e+06, 1.99850325e+06, 1.99850325e+06, 1.99850325e+06, 1.99850325e+06, 1.99850325e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99985141e+05, 2.00340047e+05, 3.33248531e+05, 1.99985891e+05, 1.95775156e+05, 8.38684219e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94594938e+05, 1.94564750e+05, 1.94611594e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94594938e+05, 1.93290109e+05, 1.95902969e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.94594938e+05, 1.94594938e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.94584212e+06, 1.94584212e+06, 1.94584212e+06, 1.94584212e+06, 1.94584212e+06, 1.94584212e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.94905312e+05, 1.94995109e+05, 3.24436562e+05, 1.94423344e+05, 1.90691953e+05, 8.16731875e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.94563594e+05, 1.94533656e+05, 1.94580172e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.94563594e+05, 1.93259062e+05, 1.95871312e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.94563594e+05, 1.94563594e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.94553075e+06, 1.94553075e+06, 1.94553075e+06, 1.94553075e+06, 1.94553075e+06, 1.94553075e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.94875891e+05, 1.94964906e+05, 3.24384281e+05, 1.94389750e+05, 1.90660391e+05, 8.16602656e+04, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1333382291), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        12763317309), # 12.76GB, avg file size 3.19GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_800_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_800_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 199300, ],
    'CountWeighted'                                                                  : [ 1.99173828e+05, 1.99187453e+05, 1.99181766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99173828e+05, 1.99173828e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99187275e+06, 1.99187275e+06, 1.99187275e+06, 1.99187275e+06, 1.99187275e+06, 1.99187275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99385875e+05, 1.99089203e+05, 3.31565062e+05, 1.99183875e+05, 1.94954750e+05, 8.34869688e+04, ],
    'CountWeightedFull'                                                              : [ 1.99140656e+05, 1.99154641e+05, 1.99148750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99140656e+05, 1.99140656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99153625e+06, 1.99153625e+06, 1.99153625e+06, 1.99153625e+06, 1.99153625e+06, 1.99153625e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99354312e+05, 1.99057094e+05, 3.31508500e+05, 1.99148031e+05, 1.94920469e+05, 8.34731719e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93821500e+05, 1.93829500e+05, 1.93819984e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93821500e+05, 1.92502938e+05, 1.95141203e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.93821500e+05, 1.93821500e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.93828125e+06, 1.93828125e+06, 1.93828125e+06, 1.93828125e+06, 1.93828125e+06, 1.93828125e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.94211375e+05, 1.93648219e+05, 3.22641406e+05, 1.93538922e+05, 1.89824562e+05, 8.12480156e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.93789609e+05, 1.93797750e+05, 1.93788219e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.93789609e+05, 1.92471344e+05, 1.95108906e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.93789609e+05, 1.93789609e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.93796062e+06, 1.93796062e+06, 1.93796062e+06, 1.93796062e+06, 1.93796062e+06, 1.93796062e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.94181172e+05, 1.93617438e+05, 3.22587375e+05, 1.93504719e+05, 1.89791625e+05, 8.12348125e+04, ],
  }),
  ("nof_tree_events",                 199300),
  ("nof_db_events",                   199300),
  ("fsize_local",                     1341260675), # 1.34GB, avg file size 1.34GB
  ("fsize_db",                        12855127044), # 12.86GB, avg file size 3.21GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_850_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_850_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 199400, ],
    'CountWeighted'                                                                  : [ 1.99288281e+05, 1.99266469e+05, 1.99279469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99288281e+05, 1.99288281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99314925e+06, 1.99314925e+06, 1.99314925e+06, 1.99314925e+06, 1.99314925e+06, 1.99314925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99353656e+05, 1.99281047e+05, 3.32071844e+05, 1.99437625e+05, 1.94764031e+05, 8.31513750e+04, ],
    'CountWeightedFull'                                                              : [ 1.99253672e+05, 1.99231891e+05, 1.99245094e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99253672e+05, 1.99253672e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99279500e+06, 1.99279500e+06, 1.99279500e+06, 1.99279500e+06, 1.99279500e+06, 1.99279500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99321266e+05, 1.99248125e+05, 3.32012562e+05, 1.99400516e+05, 1.94727641e+05, 8.31373047e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93883812e+05, 1.93864719e+05, 1.93886469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93883812e+05, 1.92555938e+05, 1.95211938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.93883812e+05, 1.93883812e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.93895450e+06, 1.93895450e+06, 1.93895450e+06, 1.93895450e+06, 1.93895450e+06, 1.93895450e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.94150688e+05, 1.93780719e+05, 3.23071188e+05, 1.93744375e+05, 1.89623172e+05, 8.09221172e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.93850719e+05, 1.93831594e+05, 1.93853469e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.93850719e+05, 1.92523156e+05, 1.95178453e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.93850719e+05, 1.93850719e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.93862000e+06, 1.93862000e+06, 1.93862000e+06, 1.93862000e+06, 1.93862000e+06, 1.93862000e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.94119688e+05, 1.93749031e+05, 3.23014375e+05, 1.93708719e+05, 1.89588062e+05, 8.09085859e+04, ],
  }),
  ("nof_tree_events",                 199400),
  ("nof_db_events",                   199400),
  ("fsize_local",                     1352430279), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        12962982116), # 12.96GB, avg file size 2.59GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_900_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 199600, ],
    'CountWeighted'                                                                  : [ 1.99478125e+05, 1.99477703e+05, 1.99467375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99478125e+05, 1.99478125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99485288e+06, 1.99485288e+06, 1.99485288e+06, 1.99485288e+06, 1.99485288e+06, 1.99485288e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99560562e+05, 1.99218109e+05, 3.33548906e+05, 1.99659812e+05, 1.95966125e+05, 8.28689141e+04, ],
    'CountWeightedFull'                                                              : [ 1.99442422e+05, 1.99442953e+05, 1.99432000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99442422e+05, 1.99442422e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99450175e+06, 1.99450175e+06, 1.99450175e+06, 1.99450175e+06, 1.99450175e+06, 1.99450175e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99527312e+05, 1.99183812e+05, 3.33488750e+05, 1.99621844e+05, 1.95930094e+05, 8.28545625e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94051359e+05, 1.94051297e+05, 1.94047094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94051359e+05, 1.92718688e+05, 1.95383875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.94051359e+05, 1.94051359e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.94054575e+06, 1.94054575e+06, 1.94054575e+06, 1.94054575e+06, 1.94054575e+06, 1.94054575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.94328578e+05, 1.93709562e+05, 3.24407219e+05, 1.93935219e+05, 1.90695844e+05, 8.06365156e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.94017188e+05, 1.94017719e+05, 1.94013062e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.94017188e+05, 1.92684969e+05, 1.95349406e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.94017188e+05, 1.94017188e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.94020700e+06, 1.94020700e+06, 1.94020700e+06, 1.94020700e+06, 1.94020700e+06, 1.94020700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.94296594e+05, 1.93676656e+05, 3.24349469e+05, 1.93898844e+05, 1.90661406e+05, 8.06227891e+04, ],
  }),
  ("nof_tree_events",                 199600),
  ("nof_db_events",                   199600),
  ("fsize_local",                     1363642284), # 1.36GB, avg file size 1.36GB
  ("fsize_db",                        13038158901), # 13.04GB, avg file size 3.26GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99105078e+04, 9.99185938e+04, 9.99192812e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99105078e+04, 9.99105078e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99085062e+05, 9.99085062e+05, 9.99085062e+05, 9.99085062e+05, 9.99085062e+05, 9.99085062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00014359e+05, 9.99514531e+04, 1.67215141e+05, 1.00004797e+05, 9.77043047e+04, 4.12206055e+04, ],
    'CountWeightedFull'                                                              : [ 9.98915078e+04, 9.98994375e+04, 9.98998359e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98915078e+04, 9.98915078e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.98896375e+05, 9.98896375e+05, 9.98896375e+05, 9.98896375e+05, 9.98896375e+05, 9.98896375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99961641e+04, 9.99328828e+04, 1.67182438e+05, 9.99842422e+04, 9.76846250e+04, 4.12127031e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.72076172e+04, 9.72068750e+04, 9.72183516e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.72076172e+04, 9.65440391e+04, 9.78729453e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.72076172e+04, 9.72076172e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.72075312e+05, 9.72075312e+05, 9.72075312e+05, 9.72075312e+05, 9.72075312e+05, 9.72075312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.73974375e+04, 9.72032656e+04, 1.62647234e+05, 9.71541250e+04, 9.50681875e+04, 4.01095664e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.71892031e+04, 9.71883281e+04, 9.71997812e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.71892031e+04, 9.65257578e+04, 9.78544375e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.71892031e+04, 9.71892031e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.71891750e+05, 9.71891750e+05, 9.71891750e+05, 9.71891750e+05, 9.71891750e+05, 9.71891750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.73798750e+04, 9.71854375e+04, 1.62615812e+05, 9.71344297e+04, 9.50492656e+04, 4.01019727e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     691321756), # 691.32MB, avg file size 691.32MB
  ("fsize_db",                        6644043956), # 6.64GB, avg file size 2.21GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99112812e+04, 9.99244297e+04, 9.99172500e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99112812e+04, 9.99112812e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99240250e+05, 9.99240250e+05, 9.99240250e+05, 9.99240250e+05, 9.99240250e+05, 9.99240250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.98958672e+04, 1.00113578e+05, 1.67603391e+05, 1.00125727e+05, 9.72279844e+04, 4.07415625e+04, ],
    'CountWeightedFull'                                                              : [ 9.98923125e+04, 9.99050078e+04, 9.98978984e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98923125e+04, 9.98923125e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99045500e+05, 9.99045500e+05, 9.99045500e+05, 9.99045500e+05, 9.99045500e+05, 9.99045500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.98777344e+04, 1.00095312e+05, 1.67571266e+05, 1.00105070e+05, 9.72087891e+04, 4.07336914e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71661797e+04, 9.71790781e+04, 9.71627734e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71661797e+04, 9.64952266e+04, 9.78386641e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.71661797e+04, 9.71661797e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.71724750e+05, 9.71724750e+05, 9.71724750e+05, 9.71724750e+05, 9.71724750e+05, 9.71724750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72494922e+04, 9.72983203e+04, 1.62979281e+05, 9.72190547e+04, 9.46222109e+04, 3.96243438e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.71478828e+04, 9.71606016e+04, 9.71442266e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.71478828e+04, 9.64770078e+04, 9.78201719e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.71478828e+04, 9.71478828e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.71539062e+05, 9.71539062e+05, 9.71539062e+05, 9.71539062e+05, 9.71539062e+05, 9.71539062e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72320078e+04, 9.72807031e+04, 1.62948344e+05, 9.71992578e+04, 9.46037031e+04, 3.96167969e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     700628539), # 700.63MB, avg file size 700.63MB
  ("fsize_db",                        6799676332), # 6.80GB, avg file size 2.27GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 99700, ],
    'CountWeighted'                                                                  : [ 9.95497656e+04, 9.95326719e+04, 9.95519688e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.95497656e+04, 9.95497656e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.95520500e+05, 9.95520500e+05, 9.95520500e+05, 9.95520500e+05, 9.95520500e+05, 9.95520500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.96680469e+04, 9.94345938e+04, 1.68676531e+05, 9.97348438e+04, 9.84811641e+04, 4.01266836e+04, ],
    'CountWeightedFull'                                                              : [ 9.95294219e+04, 9.95126875e+04, 9.95317344e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.95294219e+04, 9.95294219e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.95318500e+05, 9.95318500e+05, 9.95318500e+05, 9.95318500e+05, 9.95318500e+05, 9.95318500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.96488203e+04, 9.94151094e+04, 1.68640375e+05, 9.97132422e+04, 9.84590000e+04, 4.01187812e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.67963281e+04, 9.67842578e+04, 9.68003438e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.67963281e+04, 9.61255625e+04, 9.74686250e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.67963281e+04, 9.67963281e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.67975500e+05, 9.67975500e+05, 9.67975500e+05, 9.67975500e+05, 9.67975500e+05, 9.67975500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.70062109e+04, 9.65987344e+04, 1.63965922e+05, 9.68298359e+04, 9.58141797e+04, 3.90246953e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.67768203e+04, 9.67648906e+04, 9.67809531e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.67768203e+04, 9.61061719e+04, 9.74489453e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.67768203e+04, 9.67768203e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.67781375e+05, 9.67781375e+05, 9.67781375e+05, 9.67781375e+05, 9.67781375e+05, 9.67781375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.69877344e+04, 9.65801406e+04, 1.63931469e+05, 9.68091328e+04, 9.57930469e+04, 3.90170938e+04, ],
  }),
  ("nof_tree_events",                 99700),
  ("nof_db_events",                   99700),
  ("fsize_local",                     700538329), # 700.54MB, avg file size 700.54MB
  ("fsize_db",                        6898339776), # 6.90GB, avg file size 1.72GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 99500, ],
    'CountWeighted'                                                                  : [ 9.93223750e+04, 9.93284844e+04, 9.93135156e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.93223750e+04, 9.93223750e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.93321500e+05, 9.93321500e+05, 9.93321500e+05, 9.93321500e+05, 9.93321500e+05, 9.93321500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.95270469e+04, 9.95643594e+04, 1.67672422e+05, 9.94569375e+04, 9.70046562e+04, 3.98785625e+04, ],
    'CountWeightedFull'                                                              : [ 9.93024688e+04, 9.93082109e+04, 9.92939062e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.93024688e+04, 9.93024688e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.93118875e+05, 9.93118875e+05, 9.93118875e+05, 9.93118875e+05, 9.93118875e+05, 9.93118875e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.95082109e+04, 9.95448438e+04, 1.67639375e+05, 9.94356016e+04, 9.69853203e+04, 3.98706328e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.66133047e+04, 9.66106094e+04, 9.66146016e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.66133047e+04, 9.59535234e+04, 9.72738438e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.66133047e+04, 9.66133047e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.66186312e+05, 9.66186312e+05, 9.66186312e+05, 9.66186312e+05, 9.66186312e+05, 9.66186312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.69049922e+04, 9.67906562e+04, 1.63061500e+05, 9.65924688e+04, 9.43942969e+04, 3.87965586e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.65942031e+04, 9.65912891e+04, 9.65956562e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.65942031e+04, 9.59345391e+04, 9.72545625e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.65942031e+04, 9.65942031e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.65993312e+05, 9.65993312e+05, 9.65993312e+05, 9.65993312e+05, 9.65993312e+05, 9.65993312e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.68868125e+04, 9.67719766e+04, 1.63029812e+05, 9.65720078e+04, 9.43757188e+04, 3.87889375e+04, ],
  }),
  ("nof_tree_events",                 99500),
  ("nof_db_events",                   99500),
  ("fsize_local",                     699046269), # 699.05MB, avg file size 699.05MB
  ("fsize_db",                        6898552202), # 6.90GB, avg file size 6.90GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_2000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 99600, ],
    'CountWeighted'                                                                  : [ 9.93862969e+04, 9.93902969e+04, 9.93726406e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.93862969e+04, 9.93862969e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.93767500e+05, 9.93767500e+05, 9.93767500e+05, 9.93767500e+05, 9.93767500e+05, 9.93767500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.95790312e+04, 9.95471250e+04, 1.68454281e+05, 9.96331719e+04, 9.76065469e+04, 3.97180312e+04, ],
    'CountWeightedFull'                                                              : [ 9.93650312e+04, 9.93689688e+04, 9.93516562e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.93650312e+04, 9.93650312e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.93558062e+05, 9.93558062e+05, 9.93558062e+05, 9.93558062e+05, 9.93558062e+05, 9.93558062e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.95589688e+04, 9.95265547e+04, 1.68417719e+05, 9.96107500e+04, 9.75845234e+04, 3.97097969e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.66647031e+04, 9.66619922e+04, 9.66601406e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.66647031e+04, 9.60035625e+04, 9.73265781e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.66647031e+04, 9.66647031e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.66589125e+05, 9.66589125e+05, 9.66589125e+05, 9.66589125e+05, 9.66589125e+05, 9.66589125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.69488750e+04, 9.67911250e+04, 1.63848812e+05, 9.67631250e+04, 9.49835469e+04, 3.86362188e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.66444375e+04, 9.66417031e+04, 9.66400312e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.66444375e+04, 9.59834844e+04, 9.73060391e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.66444375e+04, 9.66444375e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.66387750e+05, 9.66387750e+05, 9.66387750e+05, 9.66387750e+05, 9.66387750e+05, 9.66387750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.69296641e+04, 9.67714688e+04, 1.63813625e+05, 9.67416406e+04, 9.49623828e+04, 3.86283281e+04, ],
  }),
  ("nof_tree_events",                 99600),
  ("nof_db_events",                   99600),
  ("fsize_local",                     699386034), # 699.39MB, avg file size 699.39MB
  ("fsize_db",                        6975912136), # 6.98GB, avg file size 6.98GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToRadionToHHTo2B2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_3000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_3000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 99600, ],
    'CountWeighted'                                                                  : [ 9.85973984e+04, 9.85891875e+04, 9.86071406e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.85973984e+04, 9.85973984e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.86026438e+05, 9.86026438e+05, 9.86026438e+05, 9.86026438e+05, 9.86026438e+05, 9.86026438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.95575312e+04, 9.91544375e+04, 1.68271406e+05, 9.96528281e+04, 9.79060156e+04, 3.96837109e+04, ],
    'CountWeightedFull'                                                              : [ 9.85747344e+04, 9.85664609e+04, 9.85843281e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.85747344e+04, 9.85747344e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.85797125e+05, 9.85797125e+05, 9.85797125e+05, 9.85797125e+05, 9.85797125e+05, 9.85797125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.95357344e+04, 9.91326953e+04, 1.68231438e+05, 9.96282344e+04, 9.78812031e+04, 3.96746250e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.58959219e+04, 9.58836797e+04, 9.59091875e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.58959219e+04, 9.52460547e+04, 9.65478047e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.58959219e+04, 9.58959219e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.58986625e+05, 9.58986625e+05, 9.58986625e+05, 9.58986625e+05, 9.58986625e+05, 9.58986625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.69086641e+04, 9.63796875e+04, 1.63649000e+05, 9.67764062e+04, 9.52808281e+04, 3.85929648e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.58740859e+04, 9.58617344e+04, 9.58873438e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.58740859e+04, 9.52244219e+04, 9.65257422e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.58740859e+04, 9.58740859e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.58766625e+05, 9.58766625e+05, 9.58766625e+05, 9.58766625e+05, 9.58766625e+05, 9.58766625e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.68876562e+04, 9.63587812e+04, 1.63610438e+05, 9.67527734e+04, 9.52570391e+04, 3.85842305e+04, ],
  }),
  ("nof_tree_events",                 99600),
  ("nof_db_events",                   99600),
  ("fsize_local",                     695825077), # 695.83MB, avg file size 695.83MB
  ("fsize_db",                        7186439272), # 7.19GB, avg file size 2.40GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin0_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_250_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 399300, ],
    'CountWeighted'                                                                  : [ 3.97513375e+05, 3.97584891e+05, 3.97620500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97513375e+05, 3.97513375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97627475e+06, 3.97627475e+06, 3.97627475e+06, 3.97627475e+06, 3.97627475e+06, 3.97627475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99200391e+05, 3.99161297e+05, 6.10473000e+05, 3.99439734e+05, 3.96856719e+05, 2.10797820e+05, ],
    'CountWeightedFull'                                                              : [ 3.97323844e+05, 3.97389609e+05, 3.97425359e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97323844e+05, 3.97323844e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97431950e+06, 3.97431950e+06, 3.97431950e+06, 3.97431950e+06, 3.97431950e+06, 3.97431950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99005953e+05, 3.98966156e+05, 6.10171422e+05, 3.99243516e+05, 3.96661688e+05, 2.10696453e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.79038250e+05, 3.79058375e+05, 3.79092953e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.79038250e+05, 3.74757422e+05, 3.83346875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.79038250e+05, 3.79038250e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.79090350e+06, 3.79090350e+06, 3.79090350e+06, 3.79090350e+06, 3.79090350e+06, 3.79090350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.80643031e+05, 3.80349688e+05, 5.82072125e+05, 3.80651719e+05, 3.78598078e+05, 2.00954617e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.78856766e+05, 3.78874641e+05, 3.78909062e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.78856766e+05, 3.74578344e+05, 3.83162891e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.78856766e+05, 3.78856766e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.78906200e+06, 3.78906200e+06, 3.78906200e+06, 3.78906200e+06, 3.78906200e+06, 3.78906200e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.80459656e+05, 3.80165594e+05, 5.81787453e+05, 3.80466797e+05, 3.78413828e+05, 2.00859055e+05, ],
  }),
  ("nof_tree_events",                 399300),
  ("nof_db_events",                   399300),
  ("fsize_local",                     2039620956), # 2.04GB, avg file size 1.02GB
  ("fsize_db",                        21665085461), # 21.67GB, avg file size 4.33GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_260_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_260_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 399000, ],
    'CountWeighted'                                                                  : [ 3.97775062e+05, 3.97749828e+05, 3.97718984e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97775062e+05, 3.97775062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97740025e+06, 3.97740025e+06, 3.97740025e+06, 3.97740025e+06, 3.97740025e+06, 3.97740025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99053922e+05, 3.98727406e+05, 6.00791906e+05, 3.98936141e+05, 3.97259703e+05, 2.18876188e+05, ],
    'CountWeightedFull'                                                              : [ 3.97615984e+05, 3.97590266e+05, 3.97561141e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97615984e+05, 3.97615984e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97581488e+06, 3.97581488e+06, 3.97581488e+06, 3.97581488e+06, 3.97581488e+06, 3.97581488e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98894000e+05, 3.98567188e+05, 6.00549344e+05, 3.98775016e+05, 3.97100188e+05, 2.18789453e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81472625e+05, 3.81441406e+05, 3.81460422e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81472625e+05, 3.77571609e+05, 3.85386250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81472625e+05, 3.81472625e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81454825e+06, 3.81454825e+06, 3.81454825e+06, 3.81454825e+06, 3.81454825e+06, 3.81454825e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.82757312e+05, 3.82284719e+05, 5.76045781e+05, 3.82467172e+05, 3.81103453e+05, 2.10023430e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81321094e+05, 3.81290141e+05, 3.81309656e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81321094e+05, 3.77422203e+05, 3.85232828e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81321094e+05, 3.81321094e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81303562e+06, 3.81303562e+06, 3.81303562e+06, 3.81303562e+06, 3.81303562e+06, 3.81303562e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.82605953e+05, 3.82133109e+05, 5.75815703e+05, 3.82314359e+05, 3.80952406e+05, 2.09941312e+05, ],
  }),
  ("nof_tree_events",                 399000),
  ("nof_db_events",                   399000),
  ("fsize_local",                     1835029987), # 1.84GB, avg file size 917.51MB
  ("fsize_db",                        19965168763), # 19.97GB, avg file size 3.33GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_270_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_270_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 399100, ],
    'CountWeighted'                                                                  : [ 3.97803766e+05, 3.97836094e+05, 3.97781047e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97803766e+05, 3.97803766e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97778925e+06, 3.97778925e+06, 3.97778925e+06, 3.97778925e+06, 3.97778925e+06, 3.97778925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99000953e+05, 3.99067391e+05, 6.01369484e+05, 3.99218734e+05, 3.97602469e+05, 2.18766875e+05, ],
    'CountWeightedFull'                                                              : [ 3.97645609e+05, 3.97675688e+05, 3.97619688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97645609e+05, 3.97645609e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97621850e+06, 3.97621850e+06, 3.97621850e+06, 3.97621850e+06, 3.97621850e+06, 3.97621850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98842375e+05, 3.98909109e+05, 6.01127250e+05, 3.99058531e+05, 3.97442094e+05, 2.18681188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81536344e+05, 3.81530234e+05, 3.81540047e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81536344e+05, 3.77642859e+05, 3.85445062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81536344e+05, 3.81536344e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81526150e+06, 3.81526150e+06, 3.81526150e+06, 3.81526150e+06, 3.81526150e+06, 3.81526150e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.82719781e+05, 3.82496859e+05, 5.76686484e+05, 3.82753453e+05, 3.81661000e+05, 2.09950305e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81386188e+05, 3.81379188e+05, 3.81389031e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81386188e+05, 3.77494641e+05, 3.85292828e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81386188e+05, 3.81386188e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81376475e+06, 3.81376475e+06, 3.81376475e+06, 3.81376475e+06, 3.81376475e+06, 3.81376475e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.82569672e+05, 3.82347266e+05, 5.76457094e+05, 3.82602000e+05, 3.81509094e+05, 2.09869211e+05, ],
  }),
  ("nof_tree_events",                 399100),
  ("nof_db_events",                   399100),
  ("fsize_local",                     1839529733), # 1.84GB, avg file size 919.76MB
  ("fsize_db",                        19965470447), # 19.97GB, avg file size 2.85GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_280_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_280_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 399200, ],
    'CountWeighted'                                                                  : [ 3.97924625e+05, 3.97876875e+05, 3.97874359e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97924625e+05, 3.97924625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97831100e+06, 3.97831100e+06, 3.97831100e+06, 3.97831100e+06, 3.97831100e+06, 3.97831100e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99346266e+05, 3.99065344e+05, 6.00973312e+05, 3.99033469e+05, 3.97589609e+05, 2.19157953e+05, ],
    'CountWeightedFull'                                                              : [ 3.97766250e+05, 3.97717172e+05, 3.97715969e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97766250e+05, 3.97766250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97673125e+06, 3.97673125e+06, 3.97673125e+06, 3.97673125e+06, 3.97673125e+06, 3.97673125e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99187719e+05, 3.98906859e+05, 6.00730375e+05, 3.98873453e+05, 3.97428984e+05, 2.19072195e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81435781e+05, 3.81399781e+05, 3.81433953e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81435781e+05, 3.77493031e+05, 3.85394234e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81435781e+05, 3.81435781e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81400112e+06, 3.81400112e+06, 3.81400112e+06, 3.81400112e+06, 3.81400112e+06, 3.81400112e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.82848500e+05, 3.82345672e+05, 5.75947172e+05, 3.82376891e+05, 3.81330641e+05, 2.10218070e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81285609e+05, 3.81249141e+05, 3.81283781e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81285609e+05, 3.77344938e+05, 3.85242125e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81285609e+05, 3.81285609e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81249975e+06, 3.81249975e+06, 3.81249975e+06, 3.81249975e+06, 3.81249975e+06, 3.81249975e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.82698500e+05, 3.82195422e+05, 5.75717000e+05, 3.82225375e+05, 3.81178859e+05, 2.10136797e+05, ],
  }),
  ("nof_tree_events",                 399200),
  ("nof_db_events",                   399200),
  ("fsize_local",                     1841621669), # 1.84GB, avg file size 920.81MB
  ("fsize_db",                        19918920031), # 19.92GB, avg file size 3.32GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_300_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_300_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.98974375e+05, 2.98946699e+05, 2.98993043e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98974375e+05, 2.98974375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98977847e+06, 2.98977847e+06, 2.98977847e+06, 2.98977847e+06, 2.98977847e+06, 2.98977847e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99913297e+05, 3.00239133e+05, 4.51423500e+05, 3.00116285e+05, 2.98696816e+05, 1.65132521e+05, ],
    'CountWeightedFull'                                                              : [ 2.98859344e+05, 2.98833281e+05, 2.98874594e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98859344e+05, 2.98859344e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98862178e+06, 2.98862178e+06, 2.98862178e+06, 2.98862178e+06, 2.98862178e+06, 2.98862178e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99797133e+05, 3.00123328e+05, 4.51246961e+05, 2.99998438e+05, 2.98580332e+05, 1.65069062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.86600730e+05, 2.86574609e+05, 2.86616738e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.86600730e+05, 2.83630254e+05, 2.89583410e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.86600730e+05, 2.86600730e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.86600234e+06, 2.86600234e+06, 2.86600234e+06, 2.86600234e+06, 2.86600234e+06, 2.86600234e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.87522496e+05, 2.87649305e+05, 4.32560547e+05, 2.87570984e+05, 2.86435293e+05, 1.58388988e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.86490883e+05, 2.86465281e+05, 2.86505730e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.86490883e+05, 2.83521812e+05, 2.89471855e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.86490883e+05, 2.86490883e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.86490241e+06, 2.86490241e+06, 2.86490241e+06, 2.86490241e+06, 2.86490241e+06, 2.86490241e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.87412359e+05, 2.87539598e+05, 4.32393656e+05, 2.87459691e+05, 2.86324777e+05, 1.58328805e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1385660571), # 1.39GB, avg file size 692.83MB
  ("fsize_db",                        14933126905), # 14.93GB, avg file size 2.99GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_320_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_320_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299000, ],
    'CountWeighted'                                                                  : [ 2.98041734e+05, 2.98033680e+05, 2.98040312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98041734e+05, 2.98041734e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98022350e+06, 2.98022350e+06, 2.98022350e+06, 2.98022350e+06, 2.98022350e+06, 2.98022350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98962207e+05, 2.99271379e+05, 4.49779992e+05, 2.99059340e+05, 2.97960676e+05, 1.64797068e+05, ],
    'CountWeightedFull'                                                              : [ 2.97924406e+05, 2.97917699e+05, 2.97923715e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.97924406e+05, 2.97924406e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.97905997e+06, 2.97905997e+06, 2.97905997e+06, 2.97905997e+06, 2.97905997e+06, 2.97905997e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98844945e+05, 2.99153250e+05, 4.49602242e+05, 2.98941281e+05, 2.97844555e+05, 1.64733225e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.85711445e+05, 2.85688211e+05, 2.85730422e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.85711445e+05, 2.82747172e+05, 2.88687828e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.85711445e+05, 2.85711445e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.85704534e+06, 2.85704534e+06, 2.85704534e+06, 2.85704534e+06, 2.85704534e+06, 2.85704534e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.86608125e+05, 2.86748445e+05, 4.31072859e+05, 2.86605121e+05, 2.85795785e+05, 1.58079375e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.85600387e+05, 2.85577797e+05, 2.85619895e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.85600387e+05, 2.82637910e+05, 2.88575414e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.85600387e+05, 2.85600387e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.85594256e+06, 2.85594256e+06, 2.85594256e+06, 2.85594256e+06, 2.85594256e+06, 2.85594256e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.86497367e+05, 2.86637086e+05, 4.30905227e+05, 2.86493590e+05, 2.85686059e+05, 1.58019059e+05, ],
  }),
  ("nof_tree_events",                 299000),
  ("nof_db_events",                   299000),
  ("fsize_local",                     1382440605), # 1.38GB, avg file size 691.22MB
  ("fsize_db",                        14844734816), # 14.84GB, avg file size 2.97GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_350_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_350_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99005414e+05, 2.99071059e+05, 2.99067414e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99005414e+05, 2.99005414e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99042556e+06, 2.99042556e+06, 2.99042556e+06, 2.99042556e+06, 2.99042556e+06, 2.99042556e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99938695e+05, 3.00066164e+05, 4.50259875e+05, 3.00094516e+05, 2.98814473e+05, 1.66018473e+05, ],
    'CountWeightedFull'                                                              : [ 2.98890887e+05, 2.98955574e+05, 2.98949820e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98890887e+05, 2.98890887e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98927350e+06, 2.98927350e+06, 2.98927350e+06, 2.98927350e+06, 2.98927350e+06, 2.98927350e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99822797e+05, 2.99949777e+05, 4.50086055e+05, 2.99978305e+05, 2.98700641e+05, 1.65955062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.86601824e+05, 2.86613391e+05, 2.86635633e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.86601824e+05, 2.83608938e+05, 2.89609648e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.86601824e+05, 2.86601824e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.86614525e+06, 2.86614525e+06, 2.86614525e+06, 2.86614525e+06, 2.86614525e+06, 2.86614525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.87503297e+05, 2.87476422e+05, 4.31316531e+05, 2.87495688e+05, 2.86417484e+05, 1.59215830e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.86492750e+05, 2.86504152e+05, 2.86525203e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.86492750e+05, 2.83501465e+05, 2.89498965e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.86492750e+05, 2.86492750e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.86505281e+06, 2.86505281e+06, 2.86505281e+06, 2.86505281e+06, 2.86505281e+06, 2.86505281e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.87393559e+05, 2.87366391e+05, 4.31151898e+05, 2.87385586e+05, 2.86309617e+05, 1.59155686e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1388963433), # 1.39GB, avg file size 694.48MB
  ("fsize_db",                        14849340648), # 14.85GB, avg file size 2.12GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_400_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_400_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.98878488e+05, 2.98892504e+05, 2.98921355e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98878488e+05, 2.98878488e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98911353e+06, 2.98911353e+06, 2.98911353e+06, 2.98911353e+06, 2.98911353e+06, 2.98911353e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00022043e+05, 3.00494363e+05, 4.48917273e+05, 2.99960605e+05, 2.97712363e+05, 1.66478492e+05, ],
    'CountWeightedFull'                                                              : [ 2.98763199e+05, 2.98777168e+05, 2.98804535e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98763199e+05, 2.98763199e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98795578e+06, 2.98795578e+06, 2.98795578e+06, 2.98795578e+06, 2.98795578e+06, 2.98795578e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99906016e+05, 3.00378695e+05, 4.48741578e+05, 2.99843273e+05, 2.97595414e+05, 1.66414836e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.86213098e+05, 2.86222938e+05, 2.86227332e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.86213098e+05, 2.83160707e+05, 2.89281953e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.86213098e+05, 2.86213098e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.86226812e+06, 2.86226812e+06, 2.86226812e+06, 2.86226812e+06, 2.86226812e+06, 2.86226812e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.87305641e+05, 2.87565398e+05, 4.29676000e+05, 2.87133332e+05, 2.85202699e+05, 1.59534648e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.86103465e+05, 2.86113348e+05, 2.86117145e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.86103465e+05, 2.83052469e+05, 2.89170602e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.86103465e+05, 2.86103465e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.86116941e+06, 2.86116941e+06, 2.86116941e+06, 2.86116941e+06, 2.86116941e+06, 2.86116941e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.87195949e+05, 2.87455973e+05, 4.29509672e+05, 2.87022406e+05, 2.85092090e+05, 1.59474299e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1397214824), # 1.40GB, avg file size 698.61MB
  ("fsize_db",                        14759908108), # 14.76GB, avg file size 4.92GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_450_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_450_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 295800, ],
    'CountWeighted'                                                                  : [ 2.94629262e+05, 2.94629539e+05, 2.94591938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.94629262e+05, 2.94629262e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.94661753e+06, 2.94661753e+06, 2.94661753e+06, 2.94661753e+06, 2.94661753e+06, 2.94661753e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.95741359e+05, 2.96115469e+05, 4.41608859e+05, 2.95877562e+05, 2.93459957e+05, 1.64825389e+05, ],
    'CountWeightedFull'                                                              : [ 2.94517012e+05, 2.94519039e+05, 2.94482109e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.94517012e+05, 2.94517012e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.94549334e+06, 2.94549334e+06, 2.94549334e+06, 2.94549334e+06, 2.94549334e+06, 2.94549334e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.95629734e+05, 2.96003895e+05, 4.41439234e+05, 2.95764926e+05, 2.93346855e+05, 1.64764082e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.81958699e+05, 2.81945309e+05, 2.81960094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.81958699e+05, 2.78900062e+05, 2.85028363e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.81958699e+05, 2.81958699e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.81971656e+06, 2.81971656e+06, 2.81971656e+06, 2.81971656e+06, 2.81971656e+06, 2.81971656e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.83040875e+05, 2.83245133e+05, 4.22481086e+05, 2.83066957e+05, 2.80969801e+05, 1.57851402e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.81853316e+05, 2.81840340e+05, 2.81855469e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.81853316e+05, 2.78796215e+05, 2.84921602e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.81853316e+05, 2.81853316e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.81866069e+06, 2.81866069e+06, 2.81866069e+06, 2.81866069e+06, 2.81866069e+06, 2.81866069e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.82935629e+05, 2.83140055e+05, 4.22321109e+05, 2.82960855e+05, 2.80863262e+05, 1.57793480e+05, ],
  }),
  ("nof_tree_events",                 295800),
  ("nof_db_events",                   295800),
  ("fsize_local",                     1383460613), # 1.38GB, avg file size 691.73MB
  ("fsize_db",                        14543528828), # 14.54GB, avg file size 4.85GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_500_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299100, ],
    'CountWeighted'                                                                  : [ 2.97948211e+05, 2.97923480e+05, 2.97931039e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.97948211e+05, 2.97948211e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.97943081e+06, 2.97943081e+06, 2.97943081e+06, 2.97943081e+06, 2.97943081e+06, 2.97943081e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98984281e+05, 2.99165520e+05, 4.46855266e+05, 2.99249785e+05, 2.97621367e+05, 1.66935941e+05, ],
    'CountWeightedFull'                                                              : [ 2.97834766e+05, 2.97810129e+05, 2.97817891e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.97834766e+05, 2.97834766e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.97829609e+06, 2.97829609e+06, 2.97829609e+06, 2.97829609e+06, 2.97829609e+06, 2.97829609e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98870492e+05, 2.99051547e+05, 4.46683875e+05, 2.99135594e+05, 2.97508250e+05, 1.66873393e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.84815148e+05, 2.84800656e+05, 2.84820297e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.84815148e+05, 2.81657551e+05, 2.87989637e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.84815148e+05, 2.84815148e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.84813825e+06, 2.84813825e+06, 2.84813825e+06, 2.84813825e+06, 2.84813825e+06, 2.84813825e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.85840543e+05, 2.85846891e+05, 4.27016836e+05, 2.85981355e+05, 2.84649582e+05, 1.59703832e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.84707617e+05, 2.84693102e+05, 2.84712797e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.84707617e+05, 2.81551602e+05, 2.87880496e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.84707617e+05, 2.84707617e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.84706453e+06, 2.84706453e+06, 2.84706453e+06, 2.84706453e+06, 2.84706453e+06, 2.84706453e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.85732961e+05, 2.85738941e+05, 4.26854586e+05, 2.85873453e+05, 2.84542469e+05, 1.59644744e+05, ],
  }),
  ("nof_tree_events",                 299100),
  ("nof_db_events",                   299100),
  ("fsize_local",                     1411718101), # 1.41GB, avg file size 705.86MB
  ("fsize_db",                        14761989473), # 14.76GB, avg file size 2.95GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_600_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_600_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99190750e+05, 1.99176094e+05, 1.99154016e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99190750e+05, 1.99190750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99168025e+06, 1.99168025e+06, 1.99168025e+06, 1.99168025e+06, 1.99168025e+06, 1.99168025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99992906e+05, 1.99976062e+05, 2.98543031e+05, 2.00020375e+05, 1.99575094e+05, 1.12102852e+05, ],
    'CountWeightedFull'                                                              : [ 1.99113547e+05, 1.99099672e+05, 1.99078719e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99113547e+05, 1.99113547e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99091388e+06, 1.99091388e+06, 1.99091388e+06, 1.99091388e+06, 1.99091388e+06, 1.99091388e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99916719e+05, 1.99899938e+05, 2.98429125e+05, 1.99943688e+05, 1.99499594e+05, 1.12060461e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.89984562e+05, 1.89974281e+05, 1.89977484e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.89984562e+05, 1.87775359e+05, 1.92204234e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.89984562e+05, 1.89984562e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.89977225e+06, 1.89977225e+06, 1.89977225e+06, 1.89977225e+06, 1.89977225e+06, 1.89977225e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.90785250e+05, 1.90676000e+05, 2.84713031e+05, 1.90734156e+05, 1.90482125e+05, 1.07007156e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.89912844e+05, 1.89902531e+05, 1.89906469e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.89912844e+05, 1.87704844e+05, 1.92131594e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.89912844e+05, 1.89912844e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.89905738e+06, 1.89905738e+06, 1.89905738e+06, 1.89905738e+06, 1.89905738e+06, 1.89905738e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.90713875e+05, 1.90604344e+05, 2.84606312e+05, 1.90662203e+05, 1.90411219e+05, 1.06967328e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     956236341), # 956.24MB, avg file size 956.24MB
  ("fsize_db",                        9898141934), # 9.90GB, avg file size 2.47GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_650_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_650_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 197300, ],
    'CountWeighted'                                                                  : [ 1.96407625e+05, 1.96405844e+05, 1.96426641e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.96407625e+05, 1.96407625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.96426238e+06, 1.96426238e+06, 1.96426238e+06, 1.96426238e+06, 1.96426238e+06, 1.96426238e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.97205094e+05, 1.97198094e+05, 2.94420875e+05, 1.97421094e+05, 1.96945000e+05, 1.10597703e+05, ],
    'CountWeightedFull'                                                              : [ 1.96331656e+05, 1.96328984e+05, 1.96348922e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.96331656e+05, 1.96331656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.96347925e+06, 1.96347925e+06, 1.96347925e+06, 1.96347925e+06, 1.96347925e+06, 1.96347925e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.97127812e+05, 1.97121359e+05, 2.94304312e+05, 1.97343531e+05, 1.96866594e+05, 1.10554922e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.87181516e+05, 1.87186188e+05, 1.87181234e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.87181516e+05, 1.84965828e+05, 1.89409859e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.87181516e+05, 1.87181516e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.87186700e+06, 1.87186700e+06, 1.87186700e+06, 1.87186700e+06, 1.87186700e+06, 1.87186700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.87946828e+05, 1.87844312e+05, 2.80502875e+05, 1.88097562e+05, 1.87786344e+05, 1.05482375e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.87109406e+05, 1.87113484e+05, 1.87108484e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.87109406e+05, 1.84894797e+05, 1.89336609e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.87109406e+05, 1.87109406e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.87113762e+06, 1.87113762e+06, 1.87113762e+06, 1.87113762e+06, 1.87113762e+06, 1.87113762e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.87874094e+05, 1.87771953e+05, 2.80392938e+05, 1.88024562e+05, 1.87712547e+05, 1.05442023e+05, ],
  }),
  ("nof_tree_events",                 197300),
  ("nof_db_events",                   197300),
  ("fsize_local",                     949367883), # 949.37MB, avg file size 949.37MB
  ("fsize_db",                        9750259439), # 9.75GB, avg file size 3.25GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_700_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_700_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99107484e+05, 1.99105422e+05, 1.99094969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99107484e+05, 1.99107484e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99116375e+06, 1.99116375e+06, 1.99116375e+06, 1.99116375e+06, 1.99116375e+06, 1.99116375e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00027812e+05, 2.00322297e+05, 2.97545438e+05, 1.99988109e+05, 1.98583062e+05, 1.12452469e+05, ],
    'CountWeightedFull'                                                              : [ 1.99028875e+05, 1.99027406e+05, 1.99016484e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99028875e+05, 1.99028875e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99036088e+06, 1.99036088e+06, 1.99036088e+06, 1.99036088e+06, 1.99036088e+06, 1.99036088e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99949891e+05, 2.00243656e+05, 2.97427219e+05, 1.99909406e+05, 1.98504812e+05, 1.12409227e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.89522891e+05, 1.89531641e+05, 1.89507766e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.89522891e+05, 1.87230484e+05, 1.91830500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.89522891e+05, 1.89522891e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.89527088e+06, 1.89527088e+06, 1.89527088e+06, 1.89527088e+06, 1.89527088e+06, 1.89527088e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.90419672e+05, 1.90584328e+05, 2.83164500e+05, 1.90321062e+05, 1.89173922e+05, 1.07132445e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.89449656e+05, 1.89458359e+05, 1.89434375e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.89449656e+05, 1.87158125e+05, 1.91756016e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.89449656e+05, 1.89449656e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.89453212e+06, 1.89453212e+06, 1.89453212e+06, 1.89453212e+06, 1.89453212e+06, 1.89453212e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.90346438e+05, 1.90510531e+05, 2.83053656e+05, 1.90247000e+05, 1.89100516e+05, 1.07091898e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     968307245), # 968.31MB, avg file size 968.31MB
  ("fsize_db",                        9931172424), # 9.93GB, avg file size 1.99GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 198000, ],
    'CountWeighted'                                                                  : [ 1.97008141e+05, 1.97009062e+05, 1.96985688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.97008141e+05, 1.97008141e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.97022025e+06, 1.97022025e+06, 1.97022025e+06, 1.97022025e+06, 1.97022025e+06, 1.97022025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.97974844e+05, 1.97936516e+05, 2.95449906e+05, 1.98033062e+05, 1.97907672e+05, 1.11215219e+05, ],
    'CountWeightedFull'                                                              : [ 1.96933266e+05, 1.96933766e+05, 1.96910891e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.96933266e+05, 1.96933266e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.96946300e+06, 1.96946300e+06, 1.96946300e+06, 1.96946300e+06, 1.96946300e+06, 1.96946300e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.97899344e+05, 1.97860953e+05, 2.95335625e+05, 1.97957031e+05, 1.97831453e+05, 1.11173211e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.87442500e+05, 1.87441172e+05, 1.87438750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.87442500e+05, 1.85154094e+05, 1.89744281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.87442500e+05, 1.87442500e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.87447238e+06, 1.87447238e+06, 1.87447238e+06, 1.87447238e+06, 1.87447238e+06, 1.87447238e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.88368016e+05, 1.88226469e+05, 2.81020094e+05, 1.88369141e+05, 1.88416266e+05, 1.05899375e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.87371766e+05, 1.87370125e+05, 1.87367984e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.87371766e+05, 1.85084469e+05, 1.89672500e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.87371766e+05, 1.87371766e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.87376275e+06, 1.87376275e+06, 1.87376275e+06, 1.87376275e+06, 1.87376275e+06, 1.87376275e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.88297078e+05, 1.88155625e+05, 2.80912688e+05, 1.88297797e+05, 1.88344562e+05, 1.05859867e+05, ],
  }),
  ("nof_tree_events",                 198000),
  ("nof_db_events",                   198000),
  ("fsize_local",                     962567269), # 962.57MB, avg file size 962.57MB
  ("fsize_db",                        9850444030), # 9.85GB, avg file size 1.97GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_850_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_850_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 197200, ],
    'CountWeighted'                                                                  : [ 1.96018938e+05, 1.96029609e+05, 1.96039031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.96018938e+05, 1.96018938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.96048875e+06, 1.96048875e+06, 1.96048875e+06, 1.96048875e+06, 1.96048875e+06, 1.96048875e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.97218125e+05, 1.96780922e+05, 2.93348250e+05, 1.97165641e+05, 1.97151797e+05, 1.11255422e+05, ],
    'CountWeightedFull'                                                              : [ 1.95942094e+05, 1.95951906e+05, 1.95962094e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.95942094e+05, 1.95942094e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.95970088e+06, 1.95970088e+06, 1.95970088e+06, 1.95970088e+06, 1.95970088e+06, 1.95970088e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.97140859e+05, 1.96703812e+05, 2.93233062e+05, 1.97088234e+05, 1.97075250e+05, 1.11212344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.86132312e+05, 1.86122125e+05, 1.86151750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.86132312e+05, 1.83769266e+05, 1.88508609e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.86132312e+05, 1.86132312e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.86142612e+06, 1.86142612e+06, 1.86142612e+06, 1.86142612e+06, 1.86142612e+06, 1.86142612e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.87285453e+05, 1.86716031e+05, 2.78496156e+05, 1.87163688e+05, 1.87401531e+05, 1.05735547e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.86060266e+05, 1.86049703e+05, 1.86079812e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.86060266e+05, 1.83698359e+05, 1.88435328e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.86060266e+05, 1.86060266e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.86069962e+06, 1.86069962e+06, 1.86069962e+06, 1.86069962e+06, 1.86069962e+06, 1.86069962e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.87213109e+05, 1.86643812e+05, 2.78388031e+05, 1.87091234e+05, 1.87329469e+05, 1.05695180e+05, ],
  }),
  ("nof_tree_events",                 197200),
  ("nof_db_events",                   197200),
  ("fsize_local",                     965935687), # 965.94MB, avg file size 965.94MB
  ("fsize_db",                        9850192498), # 9.85GB, avg file size 1.97GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_900_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 199100, ],
    'CountWeighted'                                                                  : [ 1.97943844e+05, 1.97932609e+05, 1.97941188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.97943844e+05, 1.97943844e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.97961575e+06, 1.97961575e+06, 1.97961575e+06, 1.97961575e+06, 1.97961575e+06, 1.97961575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99176281e+05, 1.98933156e+05, 2.95319344e+05, 1.99001562e+05, 1.98185031e+05, 1.12501914e+05, ],
    'CountWeightedFull'                                                              : [ 1.97866734e+05, 1.97855500e+05, 1.97863781e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.97866734e+05, 1.97866734e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.97882900e+06, 1.97882900e+06, 1.97882900e+06, 1.97882900e+06, 1.97882900e+06, 1.97882900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99098281e+05, 1.98854938e+05, 2.95202500e+05, 1.98923781e+05, 1.98107031e+05, 1.12458461e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.87760062e+05, 1.87759281e+05, 1.87762359e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.87760062e+05, 1.85335828e+05, 1.90202766e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.87760062e+05, 1.87760062e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.87766775e+06, 1.87766775e+06, 1.87766775e+06, 1.87766775e+06, 1.87766775e+06, 1.87766775e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.88932625e+05, 1.88599203e+05, 2.80080438e+05, 1.88708656e+05, 1.88141125e+05, 1.06791008e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.87687688e+05, 1.87686859e+05, 1.87689875e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.87687688e+05, 1.85264703e+05, 1.90129172e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.87687688e+05, 1.87687688e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.87693962e+06, 1.87693962e+06, 1.87693962e+06, 1.87693962e+06, 1.87693962e+06, 1.87693962e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.88859750e+05, 1.88526109e+05, 2.79971188e+05, 1.88636016e+05, 1.88068359e+05, 1.06750344e+05, ],
  }),
  ("nof_tree_events",                 199100),
  ("nof_db_events",                   199100),
  ("fsize_local",                     977706813), # 977.71MB, avg file size 977.71MB
  ("fsize_db",                        9914302589), # 9.91GB, avg file size 2.48GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 99200, ],
    'CountWeighted'                                                                  : [ 9.86611250e+04, 9.86578984e+04, 9.86377969e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.86611250e+04, 9.86611250e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.86501375e+05, 9.86501375e+05, 9.86501375e+05, 9.86501375e+05, 9.86501375e+05, 9.86501375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.91007422e+04, 9.91644297e+04, 1.47386625e+05, 9.93342812e+04, 9.89975938e+04, 5.60592344e+04, ],
    'CountWeightedFull'                                                              : [ 9.86203203e+04, 9.86180781e+04, 9.85976719e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.86203203e+04, 9.86203203e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.86099875e+05, 9.86099875e+05, 9.86099875e+05, 9.86099875e+05, 9.86099875e+05, 9.86099875e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.90609922e+04, 9.91250000e+04, 1.47326812e+05, 9.92941250e+04, 9.89572578e+04, 5.60368477e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.33900547e+04, 9.33877109e+04, 9.33841094e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.33900547e+04, 9.21402344e+04, 9.46463281e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.33900547e+04, 9.33900547e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.33856625e+05, 9.33856625e+05, 9.33856625e+05, 9.33856625e+05, 9.33856625e+05, 9.33856625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.38241016e+04, 9.38324844e+04, 1.39453844e+05, 9.40114141e+04, 9.37433906e+04, 5.31160703e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.33524844e+04, 9.33504922e+04, 9.33467500e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.33524844e+04, 9.21033594e+04, 9.46082266e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.33524844e+04, 9.33524844e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.33483688e+05, 9.33483688e+05, 9.33483688e+05, 9.33483688e+05, 9.33483688e+05, 9.33483688e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.37869688e+04, 9.37955938e+04, 1.39397906e+05, 9.39738906e+04, 9.37056875e+04, 5.30951797e+04, ],
  }),
  ("nof_tree_events",                 99200),
  ("nof_db_events",                   99200),
  ("fsize_local",                     490801192), # 490.80MB, avg file size 490.80MB
  ("fsize_db",                        4992199922), # 4.99GB, avg file size 1.66GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-1200_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1200_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_1200_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.92524453e+04, 9.92579531e+04, 9.92525312e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.92524453e+04, 9.92524453e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.92449875e+05, 9.92449875e+05, 9.92449875e+05, 9.92449875e+05, 9.92449875e+05, 9.92449875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99536953e+04, 9.97716016e+04, 1.48099156e+05, 1.00049320e+05, 9.99479141e+04, 5.68218750e+04, ],
    'CountWeightedFull'                                                              : [ 9.92125625e+04, 9.92178281e+04, 9.92128516e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.92125625e+04, 9.92125625e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.92058250e+05, 9.92058250e+05, 9.92058250e+05, 9.92058250e+05, 9.92058250e+05, 9.92058250e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99136406e+04, 9.97312422e+04, 1.48039922e+05, 1.00009102e+05, 9.99087656e+04, 5.67993945e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.36616094e+04, 9.36537812e+04, 9.36729062e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.36616094e+04, 9.23454766e+04, 9.49888594e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.36616094e+04, 9.36616094e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.36596438e+05, 9.36596438e+05, 9.36596438e+05, 9.36596438e+05, 9.36596438e+05, 9.36596438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.43179531e+04, 9.41088438e+04, 1.39727750e+05, 9.43858750e+04, 9.43839688e+04, 5.36572188e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.36243750e+04, 9.36164688e+04, 9.36357500e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.36243750e+04, 9.23088906e+04, 9.49510391e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.36243750e+04, 9.36243750e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.36226812e+05, 9.36226812e+05, 9.36226812e+05, 9.36226812e+05, 9.36226812e+05, 9.36226812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.42805547e+04, 9.40713047e+04, 1.39672531e+05, 9.43485234e+04, 9.43472500e+04, 5.36362656e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     497088300), # 497.09MB, avg file size 497.09MB
  ("fsize_db",                        5054132277), # 5.05GB, avg file size 1.68GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_1200_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.90066641e+04, 9.90089766e+04, 9.90043984e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.90066641e+04, 9.90066641e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.90005125e+05, 9.90005125e+05, 9.90005125e+05, 9.90005125e+05, 9.90005125e+05, 9.90005125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99491094e+04, 1.00004219e+05, 1.47720562e+05, 1.00060977e+05, 9.99140938e+04, 5.72522422e+04, ],
    'CountWeightedFull'                                                              : [ 9.89659375e+04, 9.89684844e+04, 9.89633750e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.89659375e+04, 9.89659375e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.89602312e+05, 9.89602312e+05, 9.89602312e+05, 9.89602312e+05, 9.89602312e+05, 9.89602312e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99082969e+04, 9.99631406e+04, 1.47660031e+05, 1.00020016e+05, 9.98735312e+04, 5.72291406e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.28079922e+04, 9.28006250e+04, 9.28133984e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.28079922e+04, 9.13787109e+04, 9.42522891e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.28079922e+04, 9.28079922e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.28060438e+05, 9.28060438e+05, 9.28060438e+05, 9.28060438e+05, 9.28060438e+05, 9.28060438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.36836875e+04, 9.36698438e+04, 1.38362344e+05, 9.37730469e+04, 9.36776406e+04, 5.37161836e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.27702344e+04, 9.27632734e+04, 9.27755312e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.27702344e+04, 9.13417578e+04, 9.42139609e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.27702344e+04, 9.27702344e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.27685500e+05, 9.27685500e+05, 9.27685500e+05, 9.27685500e+05, 9.27685500e+05, 9.27685500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.36459297e+04, 9.36320234e+04, 1.38306328e+05, 9.37352109e+04, 9.36400234e+04, 5.36947305e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     486119469), # 486.12MB, avg file size 486.12MB
  ("fsize_db",                        5078291014), # 5.08GB, avg file size 1.69GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_2000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 99300, ],
    'CountWeighted'                                                                  : [ 9.81870312e+04, 9.81681250e+04, 9.81801641e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.81870312e+04, 9.81870312e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.81785875e+05, 9.81785875e+05, 9.81785875e+05, 9.81785875e+05, 9.81785875e+05, 9.81785875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.93226328e+04, 9.95713438e+04, 1.46262844e+05, 9.92575000e+04, 9.87423516e+04, 5.70078398e+04, ],
    'CountWeightedFull'                                                              : [ 9.81465000e+04, 9.81284453e+04, 9.81400000e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.81465000e+04, 9.81465000e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.81378375e+05, 9.81378375e+05, 9.81378375e+05, 9.81378375e+05, 9.81378375e+05, 9.81378375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.92820312e+04, 9.95303672e+04, 1.46202984e+05, 9.92171719e+04, 9.87024844e+04, 5.69850898e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.18803828e+04, 9.18734297e+04, 9.18793750e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.18803828e+04, 9.04394531e+04, 9.33392031e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.18803828e+04, 9.18803828e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.18785562e+05, 9.18785562e+05, 9.18785562e+05, 9.18785562e+05, 9.18785562e+05, 9.18785562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.29438281e+04, 9.31294297e+04, 1.36841625e+05, 9.28735391e+04, 9.24718906e+04, 5.33925781e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.18431641e+04, 9.18365391e+04, 9.18421719e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.18431641e+04, 9.04029922e+04, 9.33012188e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.18431641e+04, 9.18431641e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.18412438e+05, 9.18412438e+05, 9.18412438e+05, 9.18412438e+05, 9.18412438e+05, 9.18412438e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.29064141e+04, 9.30916797e+04, 1.36786375e+05, 9.28363672e+04, 9.24351250e+04, 5.33715312e+04, ],
  }),
  ("nof_tree_events",                 99300),
  ("nof_db_events",                   99300),
  ("fsize_local",                     479048622), # 479.05MB, avg file size 479.05MB
  ("fsize_db",                        5051593636), # 5.05GB, avg file size 1.68GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_spin2_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 199000, ],
    'CountWeighted'                                                                  : [ 1.98985781e+05, 1.99002594e+05, 1.98959750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.98985781e+05, 1.98985781e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.39925391e+05, 1.39886594e+05, 2.16231766e+05, 1.39972594e+05, 1.39576531e+05, 7.38046641e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.98954391e+05, 1.98899094e+05, 3.06951156e+05, 1.99021203e+05, 1.97959375e+05, 1.04940688e+05, ],
    'CountWeightedFull'                                                              : [ 1.98964719e+05, 1.98981656e+05, 1.98939234e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.98964719e+05, 1.98964719e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.39911906e+05, 1.39871906e+05, 2.16208703e+05, 1.39956375e+05, 1.39562125e+05, 7.37970781e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.98935188e+05, 1.98878109e+05, 3.06918344e+05, 1.98998156e+05, 1.97938734e+05, 1.04929875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94040078e+05, 1.94039781e+05, 1.94032391e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94040078e+05, 1.92828062e+05, 1.95252719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.94040078e+05, 1.94040078e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.36580859e+05, 1.36381766e+05, 2.10832062e+05, 1.36320609e+05, 1.36141188e+05, 7.19861094e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.94197266e+05, 1.93914219e+05, 2.99288500e+05, 1.93827312e+05, 1.93089812e+05, 1.02353562e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.94019891e+05, 1.94019766e+05, 1.94012625e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.94019891e+05, 1.92808203e+05, 1.95232391e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.94019891e+05, 1.94019891e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.36567875e+05, 1.36367656e+05, 2.10810000e+05, 1.36305094e+05, 1.36127312e+05, 7.19788594e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.94178844e+05, 1.93894109e+05, 2.99257156e+05, 1.93805266e+05, 1.93070125e+05, 1.02343219e+05, ],
  }),
  ("nof_tree_events",                 199000),
  ("nof_db_events",                   199000),
  ("fsize_local",                     945357262), # 945.36MB, avg file size 945.36MB
  ("fsize_db",                        9589956271), # 9.59GB, avg file size 3.20GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 198200, ],
    'CountWeighted'                                                                  : [ 1.98157219e+05, 1.98168656e+05, 1.98157391e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.98157219e+05, 1.98157219e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.27655227e+05, 1.27721422e+05, 1.97675500e+05, 1.27930594e+05, 1.27384500e+05, 6.72174375e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.98013672e+05, 1.98109625e+05, 3.05982750e+05, 1.98442719e+05, 1.96963766e+05, 1.04269141e+05, ],
    'CountWeightedFull'                                                              : [ 1.98136266e+05, 1.98147562e+05, 1.98136594e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.98136266e+05, 1.98136266e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.27642836e+05, 1.27708391e+05, 1.97653688e+05, 1.27915719e+05, 1.27370047e+05, 6.72106094e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.97994453e+05, 1.98089406e+05, 3.05949031e+05, 1.98419625e+05, 1.96941469e+05, 1.04258570e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93127625e+05, 1.93131125e+05, 1.93128641e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93127625e+05, 1.91899672e+05, 1.94356703e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.93127625e+05, 1.93127625e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.24538938e+05, 1.24456062e+05, 1.92651125e+05, 1.24525797e+05, 1.24201133e+05, 6.55270312e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.93170188e+05, 1.93038281e+05, 2.98192938e+05, 1.93153156e+05, 1.92029562e+05, 1.01642547e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.93107688e+05, 1.93111078e+05, 1.93108734e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.93107688e+05, 1.91879922e+05, 1.94336484e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.93107688e+05, 1.93107688e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.24527094e+05, 1.24443609e+05, 1.92630141e+05, 1.24511656e+05, 1.24187273e+05, 6.55204844e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.93151828e+05, 1.93018953e+05, 2.98160719e+05, 1.93131125e+05, 1.92008234e+05, 1.01632430e+05, ],
  }),
  ("nof_tree_events",                 198200),
  ("nof_db_events",                   198200),
  ("fsize_local",                     954390048), # 954.39MB, avg file size 954.39MB
  ("fsize_db",                        9653223921), # 9.65GB, avg file size 2.41GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 199100, ],
    'CountWeighted'                                                                  : [ 1.99060693e+05, 1.99043302e+05, 1.99053572e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99060693e+05, 1.99060693e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.34727667e+05, 1.34888707e+05, 2.08639213e+05, 1.34684449e+05, 1.33894577e+05, 7.03756720e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99112974e+05, 1.99347414e+05, 3.07748889e+05, 1.99049385e+05, 1.97293208e+05, 1.04014964e+05, ],
    'CountWeightedFull'                                                              : [ 1.99039418e+05, 1.99022228e+05, 1.99032501e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99039418e+05, 1.99039418e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.34714421e+05, 1.34874576e+05, 2.08616694e+05, 1.34668767e+05, 1.33880055e+05, 7.03683217e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99093410e+05, 1.99326607e+05, 3.07715773e+05, 1.99026152e+05, 1.97271924e+05, 1.04004115e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93788374e+05, 1.93773469e+05, 1.93786480e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93788374e+05, 1.92512767e+05, 1.95065776e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.93788374e+05, 1.93788374e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.31300481e+05, 1.31298997e+05, 2.03095808e+05, 1.30941728e+05, 1.30381665e+05, 6.85280073e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.94042735e+05, 1.94036845e+05, 2.99569596e+05, 1.93511840e+05, 1.92115717e+05, 1.01280250e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.93768096e+05, 1.93753128e+05, 1.93766314e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.93768096e+05, 1.92492729e+05, 1.95045304e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.93768096e+05, 1.93768096e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.31287802e+05, 1.31285499e+05, 2.03074253e+05, 1.30926763e+05, 1.30367779e+05, 6.85209874e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.94024027e+05, 1.94016906e+05, 2.99537919e+05, 1.93489704e+05, 1.92095499e+05, 1.01269883e+05, ],
  }),
  ("nof_tree_events",                 199100),
  ("nof_db_events",                   199100),
  ("fsize_local",                     980557879), # 980.56MB, avg file size 490.28MB
  ("fsize_db",                        9884082889), # 9.88GB, avg file size 1.65GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99965453e+05, 1.99967156e+05, 1.99960047e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99965453e+05, 1.99965453e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.23875086e+05, 1.23880617e+05, 1.92106672e+05, 1.23904484e+05, 1.23370938e+05, 6.46131523e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99979766e+05, 1.99994359e+05, 3.09413719e+05, 2.00026688e+05, 1.98444688e+05, 1.04310508e+05, ],
    'CountWeightedFull'                                                              : [ 1.99942234e+05, 1.99943859e+05, 1.99937062e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99942234e+05, 1.99942234e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.23861828e+05, 1.23866312e+05, 1.92083953e+05, 1.23888711e+05, 1.23356516e+05, 6.46059062e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99958422e+05, 1.99971281e+05, 3.09377250e+05, 2.00001281e+05, 1.98421625e+05, 1.04298805e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94608828e+05, 1.94610672e+05, 1.94603281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94608828e+05, 1.93315312e+05, 1.95904125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.94608828e+05, 1.94608828e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.20682445e+05, 1.20513047e+05, 1.86928469e+05, 1.20428023e+05, 1.20117766e+05, 6.29070625e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.94818406e+05, 1.94548750e+05, 3.01065938e+05, 1.94407031e+05, 1.93210109e+05, 1.01552039e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.94586719e+05, 1.94588422e+05, 1.94581281e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.94586719e+05, 1.93293438e+05, 1.95881719e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.94586719e+05, 1.94586719e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.20669766e+05, 1.20499391e+05, 1.86906859e+05, 1.20412977e+05, 1.20104000e+05, 6.29001406e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.94798031e+05, 1.94526750e+05, 3.01031125e+05, 1.94382703e+05, 1.93188062e+05, 1.01540859e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     992657291), # 992.66MB, avg file size 992.66MB
  ("fsize_db",                        9988346129), # 9.99GB, avg file size 2.00GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_900_hh_2b2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99944375e+04, 9.99770000e+04, 9.99786250e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99944375e+04, 9.99944375e+04, ],
    'CountWeightedPSWeight'                                                          : [ 6.60222500e+04, 6.59111875e+04, 1.03176484e+05, 6.61249375e+04, 6.64353750e+04, 3.42832109e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99309062e+04, 9.97623594e+04, 1.55752656e+05, 1.00083906e+05, 1.00144641e+05, 5.18917812e+04, ],
    'CountWeightedFull'                                                              : [ 9.99831094e+04, 9.99657422e+04, 9.99673125e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99831094e+04, 9.99831094e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.60153906e+04, 6.59041016e+04, 1.03164609e+05, 6.61167656e+04, 6.64274844e+04, 3.42794219e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99205234e+04, 9.97515938e+04, 1.55734672e+05, 1.00071453e+05, 1.00132750e+05, 5.18860312e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.72405078e+04, 9.72272500e+04, 9.72364688e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.72405078e+04, 9.65806484e+04, 9.79017578e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.72405078e+04, 9.72405078e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 6.42774023e+04, 6.40747070e+04, 1.00337844e+05, 6.42217188e+04, 6.46486719e+04, 3.33510039e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72842109e+04, 9.69787500e+04, 1.51459047e+05, 9.71990234e+04, 9.74433594e+04, 5.04772227e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.72297344e+04, 9.72165000e+04, 9.72256562e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.72297344e+04, 9.65699688e+04, 9.78908750e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.72297344e+04, 9.72297344e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 6.42708750e+04, 6.40679609e+04, 1.00326500e+05, 6.42139141e+04, 6.46411562e+04, 3.33473672e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72743203e+04, 9.69684219e+04, 1.51441875e+05, 9.71871406e+04, 9.74320156e+04, 5.04717188e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     505346937), # 505.35MB, avg file size 505.35MB
  ("fsize_db",                        5075552784), # 5.08GB, avg file size 1.69GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99806797e+04, 9.99640312e+04, 9.99596484e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99806797e+04, 9.99806797e+04, ],
    'CountWeightedPSWeight'                                                          : [ 6.98908281e+04, 6.97063125e+04, 1.09152109e+05, 6.99025859e+04, 7.00205469e+04, 3.60230273e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99863281e+04, 9.97208516e+04, 1.55822344e+05, 1.00001805e+05, 9.98452109e+04, 5.15372266e+04, ],
    'CountWeightedFull'                                                              : [ 9.99670312e+04, 9.99506250e+04, 9.99463906e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99670312e+04, 9.99670312e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 6.98820859e+04, 6.96970000e+04, 1.09137195e+05, 6.98922188e+04, 7.00110469e+04, 3.60181758e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99739062e+04, 9.97074922e+04, 1.55801094e+05, 9.99869609e+04, 9.98317031e+04, 5.15303320e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71932109e+04, 9.71834297e+04, 9.71814922e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71932109e+04, 9.65266719e+04, 9.78602969e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.71932109e+04, 9.71932109e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 6.80182969e+04, 6.77451484e+04, 1.06111430e+05, 6.78629609e+04, 6.81050859e+04, 3.50308516e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.73025156e+04, 9.69110312e+04, 1.51470656e+05, 9.70795469e+04, 9.71048203e+04, 5.01151562e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.71801875e+04, 9.71705625e+04, 9.71687266e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.71801875e+04, 9.65138516e+04, 9.78471562e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.71801875e+04, 9.71801875e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 6.80099453e+04, 6.77362812e+04, 1.06097172e+05, 6.78530156e+04, 6.80959453e+04, 3.50262109e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72905859e+04, 9.68982891e+04, 1.51450391e+05, 9.70654141e+04, 9.70917656e+04, 5.01085430e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     515229501), # 515.23MB, avg file size 515.23MB
  ("fsize_db",                        5140097093), # 5.14GB, avg file size 5.14GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99648047e+04, 9.99569766e+04, 9.99761094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99648047e+04, 9.99648047e+04, ],
    'CountWeightedPSWeight'                                                          : [ 8.73582109e+04, 8.73013047e+04, 1.36710328e+05, 8.73394922e+04, 8.72769141e+04, 4.46689023e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00009375e+05, 9.99529766e+04, 1.56362141e+05, 9.99873828e+04, 9.97613125e+04, 5.11372422e+04, ],
    'CountWeightedFull'                                                              : [ 9.99512812e+04, 9.99434141e+04, 9.99622812e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99512812e+04, 9.99512812e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 8.73472344e+04, 8.72898281e+04, 1.36692016e+05, 8.73265781e+04, 8.72650078e+04, 4.46628047e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99967188e+04, 9.99398594e+04, 1.56341109e+05, 9.99725312e+04, 9.97477656e+04, 5.11302656e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71509141e+04, 9.71416953e+04, 9.71614219e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71509141e+04, 9.64805547e+04, 9.78225000e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.71509141e+04, 9.71509141e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.49915547e+04, 8.48183125e+04, 1.32800156e+05, 8.47659141e+04, 8.48087109e+04, 4.34278789e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72939688e+04, 9.71036250e+04, 1.51882891e+05, 9.70350312e+04, 9.69373594e+04, 4.97135156e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.71379531e+04, 9.71287266e+04, 9.71483359e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.71379531e+04, 9.64677344e+04, 9.78094766e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.71379531e+04, 9.71379531e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 8.49810000e+04, 8.48073281e+04, 1.32782594e+05, 8.47535859e+04, 8.47973281e+04, 4.34220586e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72819062e+04, 9.70911328e+04, 1.51862938e+05, 9.70208906e+04, 9.69244453e+04, 4.97068672e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     512027669), # 512.03MB, avg file size 512.03MB
  ("fsize_db",                        5315508364), # 5.32GB, avg file size 1.77GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99599219e+04, 9.99556406e+04, 9.99586406e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99599219e+04, 9.99599219e+04, ],
    'CountWeightedPSWeight'                                                          : [ 1.11641781e+05, 1.11971477e+05, 1.74186406e+05, 1.11486102e+05, 1.10180664e+05, 5.67052617e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00053750e+05, 1.00353703e+05, 1.56273875e+05, 9.99166094e+04, 9.89092188e+04, 5.08225664e+04, ],
    'CountWeightedFull'                                                              : [ 9.99455625e+04, 9.99413594e+04, 9.99444922e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99455625e+04, 9.99455625e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.11627117e+05, 1.11956039e+05, 1.74161172e+05, 1.11469062e+05, 1.10164359e+05, 5.66974570e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00040609e+05, 1.00339938e+05, 1.56251172e+05, 9.99012891e+04, 9.88945703e+04, 5.08155898e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71281875e+04, 9.71246797e+04, 9.71281875e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71281875e+04, 9.64566875e+04, 9.78011875e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.71281875e+04, 9.71281875e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.08600859e+05, 1.08766211e+05, 1.69235406e+05, 1.08181938e+05, 1.07102625e+05, 5.51205391e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.73212031e+04, 9.74723828e+04, 1.51823625e+05, 9.69493984e+04, 9.61425625e+04, 4.93986641e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.71146172e+04, 9.71112500e+04, 9.71148516e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.71146172e+04, 9.64432969e+04, 9.77874844e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.71146172e+04, 9.71146172e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.08586844e+05, 1.08751586e+05, 1.69211453e+05, 1.08165711e+05, 1.07087148e+05, 5.51131211e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.73086641e+04, 9.74592734e+04, 1.51802172e+05, 9.69349141e+04, 9.61286562e+04, 4.93920430e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     509246131), # 509.25MB, avg file size 509.25MB
  ("fsize_db",                        5358389208), # 5.36GB, avg file size 5.36GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99355547e+04, 9.99583438e+04, 9.99445391e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99355547e+04, 9.99355547e+04, ],
    'CountWeightedPSWeight'                                                          : [ 1.23934320e+05, 1.23953312e+05, 1.93439594e+05, 1.24119047e+05, 1.22761508e+05, 6.30219531e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99333359e+04, 9.99506406e+04, 1.56386141e+05, 1.00082406e+05, 9.93956953e+04, 5.08193711e+04, ],
    'CountWeightedFull'                                                              : [ 9.99207578e+04, 9.99432109e+04, 9.99296094e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99207578e+04, 9.99207578e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.23917016e+05, 1.23934719e+05, 1.93411141e+05, 1.24098969e+05, 1.22743773e+05, 6.30125352e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99193672e+04, 9.99357109e+04, 1.56363188e+05, 1.00066258e+05, 9.93813203e+04, 5.08118047e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70873438e+04, 9.70996094e+04, 9.70928281e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70873438e+04, 9.64127266e+04, 9.77648203e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70873438e+04, 9.70873438e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.20524156e+05, 1.20379344e+05, 1.87912703e+05, 1.20409266e+05, 1.19318312e+05, 6.12385430e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.71796719e+04, 9.70670938e+04, 1.51909641e+05, 9.70871875e+04, 9.66000156e+04, 4.93787461e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70731484e+04, 9.70852812e+04, 9.70785234e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70731484e+04, 9.63986484e+04, 9.77504531e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70731484e+04, 9.70731484e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.20507641e+05, 1.20361703e+05, 1.87885594e+05, 1.20390180e+05, 1.19301492e+05, 6.12295547e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.71663672e+04, 9.70528984e+04, 1.51887875e+05, 9.70717266e+04, 9.65863594e+04, 4.93715508e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     507598452), # 507.60MB, avg file size 507.60MB
  ("fsize_db",                        5409168825), # 5.41GB, avg file size 2.70GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98769688e+04, 9.98774844e+04, 9.98870391e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98769688e+04, 9.98769688e+04, ],
    'CountWeightedPSWeight'                                                          : [ 2.53011562e+05, 2.53273797e+05, 3.86798688e+05, 2.52816516e+05, 2.41719469e+05, 1.28030969e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00037938e+05, 1.00217578e+05, 1.56927969e+05, 9.99665312e+04, 9.94954141e+04, 5.06284688e+04, ],
    'CountWeightedFull'                                                              : [ 9.98603750e+04, 9.98612656e+04, 9.98704141e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98603750e+04, 9.98603750e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.52972922e+05, 2.53232391e+05, 3.86735500e+05, 2.52771453e+05, 2.41680281e+05, 1.28009844e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00022656e+05, 1.00201172e+05, 1.56902359e+05, 9.99486875e+04, 9.94792188e+04, 5.06201328e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70673672e+04, 9.70609062e+04, 9.70789219e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70673672e+04, 9.64048359e+04, 9.77324062e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70673672e+04, 9.70673672e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.46175703e+05, 2.46092016e+05, 3.75954406e+05, 2.45353016e+05, 2.35051266e+05, 1.24438859e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.73250859e+04, 9.73649062e+04, 1.52520438e+05, 9.70041328e+04, 9.67467812e+04, 4.92021289e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70516094e+04, 9.70453984e+04, 9.70631172e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70516094e+04, 9.63892578e+04, 9.77165156e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70516094e+04, 9.70516094e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.46138734e+05, 2.46052641e+05, 3.75894031e+05, 2.45309984e+05, 2.35013812e+05, 1.24418719e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.73104609e+04, 9.73492656e+04, 1.52495922e+05, 9.69871797e+04, 9.67313281e+04, 4.91941719e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     505604971), # 505.60MB, avg file size 505.60MB
  ("fsize_db",                        5464121471), # 5.46GB, avg file size 5.46GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_2500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2B2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.97915469e+04, 9.97975312e+04, 9.97985625e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.97915469e+04, 9.97915469e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.95619812e+05, 3.92440875e+05, 5.80880125e+05, 3.95036969e+05, 3.58204688e+05, 2.00469234e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00065609e+05, 9.99874531e+04, 1.56942156e+05, 9.99211094e+04, 9.99004609e+04, 5.07137344e+04, ],
    'CountWeightedFull'                                                              : [ 9.97757031e+04, 9.97813828e+04, 9.97828047e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.97757031e+04, 9.97757031e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95561562e+05, 3.92380375e+05, 5.80788625e+05, 3.94970156e+05, 3.58147250e+05, 2.00437828e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00050875e+05, 9.99720000e+04, 1.56917625e+05, 9.99041953e+04, 9.98846406e+04, 5.07058125e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69691016e+04, 9.69688125e+04, 9.69791719e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69691016e+04, 9.63092891e+04, 9.76325938e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.69691016e+04, 9.69691016e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.84855938e+05, 3.81233281e+05, 5.64447500e+05, 3.83340562e+05, 3.48229000e+05, 1.94834844e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.73377969e+04, 9.71255312e+04, 1.52498297e+05, 9.69561250e+04, 9.71140156e+04, 4.92850859e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.69539531e+04, 9.69534609e+04, 9.69641562e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.69539531e+04, 9.62943281e+04, 9.76173438e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.69539531e+04, 9.69539531e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.84800000e+05, 3.81175188e+05, 5.64359438e+05, 3.83276562e+05, 3.48174156e+05, 1.94804844e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.73236562e+04, 9.71107344e+04, 1.52474719e+05, 9.69399219e+04, 9.70988438e+04, 4.92775195e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     503156721), # 503.16MB, avg file size 503.16MB
  ("fsize_db",                        5545454639), # 5.55GB, avg file size 1.85GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 2.00009656e+05, 1.99971078e+05, 2.00006406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.00009656e+05, 2.00009656e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99980112e+06, 1.99980112e+06, 1.99980112e+06, 1.99980112e+06, 1.99980112e+06, 1.99980112e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00000922e+05, 2.00052453e+05, 3.08761500e+05, 1.99972609e+05, 1.98605500e+05, 1.05107547e+05, ],
    'CountWeightedFull'                                                              : [ 1.99987391e+05, 1.99949172e+05, 1.99984188e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99987391e+05, 1.99987391e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99958362e+06, 1.99958362e+06, 1.99958362e+06, 1.99958362e+06, 1.99958362e+06, 1.99958362e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99980703e+05, 2.00031406e+05, 3.08726812e+05, 1.99948594e+05, 1.98582516e+05, 1.05096148e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.95801156e+05, 1.95776219e+05, 1.95802656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.95801156e+05, 1.94778500e+05, 1.96825312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.95801156e+05, 1.95801156e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.95783612e+06, 1.95783612e+06, 1.95783612e+06, 1.95783612e+06, 1.95783612e+06, 1.95783612e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.95998625e+05, 1.95804359e+05, 3.02239156e+05, 1.95519938e+05, 1.94501406e+05, 1.02934445e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.95779953e+05, 1.95755203e+05, 1.95781422e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.95779953e+05, 1.94757484e+05, 1.96803938e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.95779953e+05, 1.95779953e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.95762638e+06, 1.95762638e+06, 1.95762638e+06, 1.95762638e+06, 1.95762638e+06, 1.95762638e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.95979125e+05, 1.95784219e+05, 3.02205969e+05, 1.95496953e+05, 1.94479344e+05, 1.02923516e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     985595551), # 985.60MB, avg file size 985.60MB
  ("fsize_db",                        10228456255), # 10.23GB, avg file size 2.56GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99967359e+05, 1.99963062e+05, 1.99953109e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99967359e+05, 1.99967359e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99983600e+06, 1.99983600e+06, 1.99983600e+06, 1.99983600e+06, 1.99983600e+06, 1.99983600e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99920484e+05, 1.99663516e+05, 3.09748625e+05, 2.00090094e+05, 1.99065109e+05, 1.04279195e+05, ],
    'CountWeightedFull'                                                              : [ 1.99944406e+05, 1.99940328e+05, 1.99930641e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99944406e+05, 1.99944406e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99960612e+06, 1.99960612e+06, 1.99960612e+06, 1.99960612e+06, 1.99960612e+06, 1.99960612e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99899328e+05, 1.99640922e+05, 3.09712281e+05, 2.00065125e+05, 1.99041906e+05, 1.04267594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.95856578e+05, 1.95846438e+05, 1.95854359e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.95856578e+05, 1.94860031e+05, 1.96853531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.95856578e+05, 1.95856578e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.95866162e+06, 1.95866162e+06, 1.95866162e+06, 1.95866162e+06, 1.95866162e+06, 1.95866162e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.96013875e+05, 1.95511109e+05, 3.03344875e+05, 1.95701375e+05, 1.95042688e+05, 1.02167406e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.95834594e+05, 1.95824594e+05, 1.95832609e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.95834594e+05, 1.94838250e+05, 1.96831312e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.95834594e+05, 1.95834594e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.95844175e+06, 1.95844175e+06, 1.95844175e+06, 1.95844175e+06, 1.95844175e+06, 1.95844175e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.95993562e+05, 1.95489406e+05, 3.03309844e+05, 1.95677469e+05, 1.95020281e+05, 1.02156281e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1013218847), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        10438711009), # 10.44GB, avg file size 2.61GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99953188e+05, 1.99966688e+05, 1.99963297e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99953188e+05, 1.99953188e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99960475e+06, 1.99960475e+06, 1.99960475e+06, 1.99960475e+06, 1.99960475e+06, 1.99960475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99971406e+05, 1.99915062e+05, 3.09854062e+05, 2.00019406e+05, 1.98646547e+05, 1.04047898e+05, ],
    'CountWeightedFull'                                                              : [ 1.99930875e+05, 1.99943953e+05, 1.99940859e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99930875e+05, 1.99930875e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.99938100e+06, 1.99938100e+06, 1.99938100e+06, 1.99938100e+06, 1.99938100e+06, 1.99938100e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99950531e+05, 1.99893219e+05, 3.09818938e+05, 1.99994750e+05, 1.98623625e+05, 1.04036258e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.95911844e+05, 1.95916656e+05, 1.95920328e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.95911844e+05, 1.94929953e+05, 1.96892625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.95911844e+05, 1.95911844e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.95915900e+06, 1.95915900e+06, 1.95915900e+06, 1.95915900e+06, 1.95915900e+06, 1.95915900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.96137656e+05, 1.95810594e+05, 3.03534781e+05, 1.95687406e+05, 1.94699938e+05, 1.01979266e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.95890281e+05, 1.95894859e+05, 1.95898719e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.95890281e+05, 1.94908656e+05, 1.96870891e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.95890281e+05, 1.95890281e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.95894338e+06, 1.95894338e+06, 1.95894338e+06, 1.95894338e+06, 1.95894338e+06, 1.95894338e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.96117641e+05, 1.95789562e+05, 3.03500906e+05, 1.95663719e+05, 1.94677891e+05, 1.01968055e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1020388088), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        10490939882), # 10.49GB, avg file size 2.62GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99752734e+04, 9.99754844e+04, 9.99637109e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99752734e+04, 9.99752734e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99759188e+05, 9.99759188e+05, 9.99759188e+05, 9.99759188e+05, 9.99759188e+05, 9.99759188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99052422e+04, 1.00014297e+05, 1.55311969e+05, 1.00120312e+05, 9.93284375e+04, 5.17695508e+04, ],
    'CountWeightedFull'                                                              : [ 9.99628281e+04, 9.99629922e+04, 9.99515312e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99628281e+04, 9.99628281e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99634500e+05, 9.99634500e+05, 9.99634500e+05, 9.99634500e+05, 9.99634500e+05, 9.99634500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.98936562e+04, 1.00001875e+05, 1.55292203e+05, 1.00106711e+05, 9.93159688e+04, 5.17632461e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.79862969e+04, 9.79841562e+04, 9.79829062e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.79862969e+04, 9.75052891e+04, 9.84674062e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.79862969e+04, 9.79862969e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.79867750e+05, 9.79867750e+05, 9.79867750e+05, 9.79867750e+05, 9.79867750e+05, 9.79867750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.80245703e+04, 9.79766172e+04, 1.52196281e+05, 9.79836328e+04, 9.74121953e+04, 5.07639102e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.79743125e+04, 9.79721328e+04, 9.79711562e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.79743125e+04, 9.74934609e+04, 9.84553672e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.79743125e+04, 9.79743125e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.79748062e+05, 9.79748062e+05, 9.79748062e+05, 9.79748062e+05, 9.79748062e+05, 9.79748062e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.80134375e+04, 9.79647500e+04, 1.52177391e+05, 9.79706094e+04, 9.74002188e+04, 5.07578750e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     517063645), # 517.06MB, avg file size 517.06MB
  ("fsize_db",                        5306653973), # 5.31GB, avg file size 1.77GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99757266e+04, 9.99788359e+04, 9.99725781e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99757266e+04, 9.99757266e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99727688e+05, 9.99727688e+05, 9.99727688e+05, 9.99727688e+05, 9.99727688e+05, 9.99727688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99987422e+04, 9.99102422e+04, 1.56156141e+05, 9.99841094e+04, 9.98118438e+04, 5.13212148e+04, ],
    'CountWeightedFull'                                                              : [ 9.99628125e+04, 9.99655000e+04, 9.99597188e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99628125e+04, 9.99628125e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99595750e+05, 9.99595750e+05, 9.99595750e+05, 9.99595750e+05, 9.99595750e+05, 9.99595750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99866094e+04, 9.98972656e+04, 1.56135906e+05, 9.99698828e+04, 9.97991172e+04, 5.13145195e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.80086562e+04, 9.80063438e+04, 9.80105938e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.80086562e+04, 9.75338203e+04, 9.84834688e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.80086562e+04, 9.80086562e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.80067000e+05, 9.80067000e+05, 9.80067000e+05, 9.80067000e+05, 9.80067000e+05, 9.80067000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.81451094e+04, 9.79124375e+04, 1.53052078e+05, 9.78628828e+04, 9.78868516e+04, 5.03331523e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.79962031e+04, 9.79936172e+04, 9.79981953e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.79962031e+04, 9.75214141e+04, 9.84708906e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.79962031e+04, 9.79962031e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.79941125e+05, 9.79941125e+05, 9.79941125e+05, 9.79941125e+05, 9.79941125e+05, 9.79941125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.81334922e+04, 9.78999375e+04, 1.53032688e+05, 9.78492422e+04, 9.78746406e+04, 5.03266992e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     521758050), # 521.76MB, avg file size 521.76MB
  ("fsize_db",                        5407629175), # 5.41GB, avg file size 1.80GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99741406e+04, 9.99638359e+04, 9.99656484e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99741406e+04, 9.99741406e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99659812e+05, 9.99659812e+05, 9.99659812e+05, 9.99659812e+05, 9.99659812e+05, 9.99659812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99323359e+04, 1.00100852e+05, 1.55752000e+05, 1.00058953e+05, 9.89567891e+04, 5.11826797e+04, ],
    'CountWeightedFull'                                                              : [ 9.99600703e+04, 9.99500078e+04, 9.99516797e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99600703e+04, 9.99600703e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99523375e+05, 9.99523375e+05, 9.99523375e+05, 9.99523375e+05, 9.99523375e+05, 9.99523375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99194219e+04, 1.00087047e+05, 1.55729828e+05, 1.00043812e+05, 9.89426719e+04, 5.11757070e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.80639141e+04, 9.80532734e+04, 9.80614766e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.80639141e+04, 9.76022734e+04, 9.85258359e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.80639141e+04, 9.80639141e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.80584500e+05, 9.80584500e+05, 9.80584500e+05, 9.80584500e+05, 9.80584500e+05, 9.80584500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.81340156e+04, 9.81692266e+04, 1.52758484e+05, 9.80044531e+04, 9.70978047e+04, 5.02225078e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.80504297e+04, 9.80399141e+04, 9.80480781e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.80504297e+04, 9.75889062e+04, 9.85121797e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.80504297e+04, 9.80504297e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.80452062e+05, 9.80452062e+05, 9.80452062e+05, 9.80452062e+05, 9.80452062e+05, 9.80452062e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.81215859e+04, 9.81560156e+04, 1.52737109e+05, 9.79899297e+04, 9.70841641e+04, 5.02157891e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     511115784), # 511.12MB, avg file size 511.12MB
  ("fsize_db",                        5408366589), # 5.41GB, avg file size 5.41GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99520000e+04, 9.99370078e+04, 9.99321562e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99520000e+04, 9.99520000e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99292688e+05, 9.99292688e+05, 9.99292688e+05, 9.99292688e+05, 9.99292688e+05, 9.99292688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99569062e+04, 9.97030859e+04, 1.56234484e+05, 1.00048906e+05, 9.96796250e+04, 5.09889688e+04, ],
    'CountWeightedFull'                                                              : [ 9.99364531e+04, 9.99216953e+04, 9.99169375e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99364531e+04, 9.99364531e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99141812e+05, 9.99141812e+05, 9.99141812e+05, 9.99141812e+05, 9.99141812e+05, 9.99141812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99425781e+04, 9.96883203e+04, 1.56210469e+05, 1.00032320e+05, 9.96639219e+04, 5.09811602e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.80586875e+04, 9.80467656e+04, 9.80460703e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.80586875e+04, 9.76008828e+04, 9.85156562e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.80586875e+04, 9.80586875e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.80439312e+05, 9.80439312e+05, 9.80439312e+05, 9.80439312e+05, 9.80439312e+05, 9.80439312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.81800859e+04, 9.77721875e+04, 1.53214672e+05, 9.80047969e+04, 9.78162500e+04, 5.00544141e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.80437656e+04, 9.80319844e+04, 9.80314219e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.80437656e+04, 9.75861875e+04, 9.85006406e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.80437656e+04, 9.80437656e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.80292500e+05, 9.80292500e+05, 9.80292500e+05, 9.80292500e+05, 9.80292500e+05, 9.80292500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.81662734e+04, 9.77579453e+04, 1.53191672e+05, 9.79887969e+04, 9.78010078e+04, 5.00468867e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     504170019), # 504.17MB, avg file size 504.17MB
  ("fsize_db",                        5424783618), # 5.42GB, avg file size 5.42GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99405234e+04, 9.99443984e+04, 9.99426016e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99405234e+04, 9.99405234e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99259812e+05, 9.99259812e+05, 9.99259812e+05, 9.99259812e+05, 9.99259812e+05, 9.99259812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99606484e+04, 9.99360781e+04, 1.56406406e+05, 1.00076328e+05, 9.93496328e+04, 5.08461836e+04, ],
    'CountWeightedFull'                                                              : [ 9.99255625e+04, 9.99294531e+04, 9.99275547e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99255625e+04, 9.99255625e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99113312e+05, 9.99113312e+05, 9.99113312e+05, 9.99113312e+05, 9.99113312e+05, 9.99113312e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99467812e+04, 9.99210000e+04, 1.56382406e+05, 1.00060117e+05, 9.93346797e+04, 5.08387227e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.80738438e+04, 9.80731172e+04, 9.80780938e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.80738438e+04, 9.76216562e+04, 9.85260000e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.80738438e+04, 9.80738438e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.80646062e+05, 9.80646062e+05, 9.80646062e+05, 9.80646062e+05, 9.80646062e+05, 9.80646062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.82094531e+04, 9.80234297e+04, 1.53491578e+05, 9.80535156e+04, 9.75785469e+04, 4.99132812e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.80593438e+04, 9.80586328e+04, 9.80635234e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.80593438e+04, 9.76072812e+04, 9.85113594e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.80593438e+04, 9.80593438e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.80503188e+05, 9.80503188e+05, 9.80503188e+05, 9.80503188e+05, 9.80503188e+05, 9.80503188e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.81960234e+04, 9.80089219e+04, 1.53468422e+05, 9.80378594e+04, 9.75640469e+04, 4.99060742e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     500663192), # 500.66MB, avg file size 500.66MB
  ("fsize_db",                        5460445376), # 5.46GB, avg file size 5.46GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99047500e+04, 9.98998906e+04, 9.99032969e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99047500e+04, 9.99047500e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99041750e+05, 9.99041750e+05, 9.99041750e+05, 9.99041750e+05, 9.99041750e+05, 9.99041750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00039859e+05, 9.96024609e+04, 1.56664531e+05, 9.99428281e+04, 9.99341094e+04, 5.07109766e+04, ],
    'CountWeightedFull'                                                              : [ 9.98890312e+04, 9.98840859e+04, 9.98876641e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98890312e+04, 9.98890312e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.98883750e+05, 9.98883750e+05, 9.98883750e+05, 9.98883750e+05, 9.98883750e+05, 9.98883750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00025109e+05, 9.95870625e+04, 1.56640281e+05, 9.99260078e+04, 9.99186094e+04, 5.07030156e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.80810703e+04, 9.80741250e+04, 9.80828125e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.80810703e+04, 9.76367031e+04, 9.85248672e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.80810703e+04, 9.80810703e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.80801750e+05, 9.80801750e+05, 9.80801750e+05, 9.80801750e+05, 9.80801750e+05, 9.80801750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.83246875e+04, 9.77547578e+04, 1.53797938e+05, 9.79780469e+04, 9.81587500e+04, 4.98035508e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.80659062e+04, 9.80588594e+04, 9.80677422e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.80659062e+04, 9.76216641e+04, 9.85096016e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.80659062e+04, 9.80659062e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.80649562e+05, 9.80649562e+05, 9.80649562e+05, 9.80649562e+05, 9.80649562e+05, 9.80649562e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.83104141e+04, 9.77398594e+04, 1.53774547e+05, 9.79617812e+04, 9.81437422e+04, 4.97958281e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     498683530), # 498.68MB, avg file size 498.68MB
  ("fsize_db",                        5576170410), # 5.58GB, avg file size 1.86GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_2500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2B2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98347734e+04, 9.98402656e+04, 9.98279766e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98347734e+04, 9.98347734e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.98198938e+05, 9.98198938e+05, 9.98198938e+05, 9.98198938e+05, 9.98198938e+05, 9.98198938e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00073797e+05, 1.00190789e+05, 1.56124562e+05, 9.99093828e+04, 9.89021797e+04, 5.07265156e+04, ],
    'CountWeightedFull'                                                              : [ 9.98172734e+04, 9.98225000e+04, 9.98103672e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98172734e+04, 9.98172734e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.98025750e+05, 9.98025750e+05, 9.98025750e+05, 9.98025750e+05, 9.98025750e+05, 9.98025750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00057445e+05, 1.00173484e+05, 1.56096688e+05, 9.98905312e+04, 9.88842266e+04, 5.07177578e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.80642812e+04, 9.80612891e+04, 9.80663984e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.80642812e+04, 9.76304844e+04, 9.84968359e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.80642812e+04, 9.80642812e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.80553062e+05, 9.80553062e+05, 9.80553062e+05, 9.80553062e+05, 9.80553062e+05, 9.80553062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.84123047e+04, 9.83904844e+04, 1.53373500e+05, 9.80016172e+04, 9.72179844e+04, 4.98414180e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.80473984e+04, 9.80442969e+04, 9.80494609e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.80473984e+04, 9.76137500e+04, 9.84797656e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.80473984e+04, 9.80473984e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.80385062e+05, 9.80385062e+05, 9.80385062e+05, 9.80385062e+05, 9.80385062e+05, 9.80385062e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.83965156e+04, 9.83737812e+04, 1.53346547e+05, 9.79833828e+04, 9.72006250e+04, 4.98329570e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     498259414), # 498.26MB, avg file size 498.26MB
  ("fsize_db",                        5581992893), # 5.58GB, avg file size 5.58GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       5),
  ("nof_db_files",                    39),
  ("nof_events",                      {
    'Count'                                                                          : [ 993600, ],
    'CountWeighted'                                                                  : [ 9.90312889e+05, 9.90210570e+05, 9.90250035e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.90312889e+05, 9.90312889e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.90029775e+06, 9.90029775e+06, 9.90029775e+06, 9.90029775e+06, 9.90029775e+06, 9.90029775e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.93655641e+05, 9.94692883e+05, 1.46434675e+06, 9.93585773e+05, 9.88654006e+05, 5.71410657e+05, ],
    'CountWeightedFull'                                                              : [ 9.89994043e+05, 9.89894232e+05, 9.89932686e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.89994043e+05, 9.89994043e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.89723012e+06, 9.89723012e+06, 9.89723012e+06, 9.89723012e+06, 9.89723012e+06, 9.89723012e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.93339096e+05, 9.94377467e+05, 1.46387496e+06, 9.93266611e+05, 9.88333953e+05, 5.71229743e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.56131451e+05, 9.56084283e+05, 9.56117812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.56131451e+05, 9.47522742e+05, 9.64755594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.56131451e+05, 9.56131451e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.56033622e+06, 9.56033622e+06, 9.56033622e+06, 9.56033622e+06, 9.56033622e+06, 9.56033622e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.59481402e+05, 9.59924588e+05, 1.41354178e+06, 9.59188748e+05, 9.55266910e+05, 5.52168441e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.55827854e+05, 9.55781508e+05, 9.55814699e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.55827854e+05, 9.47222098e+05, 9.64448588e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.55827854e+05, 9.55827854e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.55733742e+06, 9.55733742e+06, 9.55733742e+06, 9.55733742e+06, 9.55733742e+06, 9.55733742e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.59178828e+05, 9.59623195e+05, 1.41309145e+06, 9.58883707e+05, 9.54961311e+05, 5.51995157e+05, ],
  }),
  ("nof_tree_events",                 993600),
  ("nof_db_events",                   993600),
  ("fsize_local",                     3980473977), # 3.98GB, avg file size 796.09MB
  ("fsize_db",                        45541341311), # 45.54GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.0003364547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       9),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 1996000, ],
    'CountWeighted'                                                                  : [ 1.98887862e+06, 1.98851766e+06, 1.98858810e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.98887862e+06, 1.98887862e+06, ],
    'CountWeightedPSWeight'                                                          : [ 1.98856143e+07, 1.98856143e+07, 1.98856143e+07, 1.98856143e+07, 1.98856143e+07, 1.98856143e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99607153e+06, 1.99581821e+06, 2.94593471e+06, 1.99600773e+06, 1.99021948e+06, 1.14518554e+06, ],
    'CountWeightedFull'                                                              : [ 1.98819730e+06, 1.98786317e+06, 1.98791735e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.98819730e+06, 1.98819730e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.98790088e+07, 1.98790088e+07, 1.98790088e+07, 1.98790088e+07, 1.98790088e+07, 1.98790088e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99540090e+06, 1.99514716e+06, 2.94493646e+06, 1.99533272e+06, 1.98954791e+06, 1.14480432e+06, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.90976165e+06, 1.90957449e+06, 1.90972395e+06, ],
    'CountWeightedL1Prefire'                                                         : [ 1.90976165e+06, 1.89000980e+06, 1.92955309e+06, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.90976165e+06, 1.90976165e+06, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.90965115e+07, 1.90965115e+07, 1.90965115e+07, 1.90965115e+07, 1.90965115e+07, 1.90965115e+07, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.91696030e+06, 1.91562863e+06, 2.82814627e+06, 1.91640516e+06, 1.91252693e+06, 1.10074604e+06, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.90912339e+06, 1.90894378e+06, 1.90908907e+06, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.90912339e+06, 1.88938025e+06, 1.92890619e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.90912339e+06, 1.90912339e+06, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.90901807e+07, 1.90901807e+07, 1.90901807e+07, 1.90901807e+07, 1.90901807e+07, 1.90901807e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.91632454e+06, 1.91499307e+06, 2.82719969e+06, 1.91576505e+06, 1.91189009e+06, 1.10038425e+06, ],
  }),
  ("nof_tree_events",                 1996000),
  ("nof_db_events",                   1996000),
  ("fsize_local",                     7999213739), # 8.00GB, avg file size 888.80MB
  ("fsize_db",                        90436757989), # 90.44GB, avg file size 5.32GB
  ("use_it",                          True),
  ("xsection",                        0.0001260006),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 998000, ],
    'CountWeighted'                                                                  : [ 9.94452594e+05, 9.94457844e+05, 9.94364875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.94452594e+05, 9.94452594e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.94441000e+06, 9.94441000e+06, 9.94441000e+06, 9.94441000e+06, 9.94441000e+06, 9.94441000e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.98007719e+05, 9.97984750e+05, 1.48432753e+06, 9.98019188e+05, 9.94833875e+05, 5.63277547e+05, ],
    'CountWeightedFull'                                                              : [ 9.94085156e+05, 9.94090750e+05, 9.94002672e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.94085156e+05, 9.94085156e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.94076225e+06, 9.94076225e+06, 9.94076225e+06, 9.94076225e+06, 9.94076225e+06, 9.94076225e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.97641328e+05, 9.97618328e+05, 1.48377922e+06, 9.97650031e+05, 9.94468422e+05, 5.63073297e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.45699328e+05, 9.45672156e+05, 9.45679078e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.45699328e+05, 9.33897156e+05, 9.57556750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.45699328e+05, 9.45699328e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.45683675e+06, 9.45683675e+06, 9.45683675e+06, 9.45683675e+06, 9.45683675e+06, 9.45683675e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.49196328e+05, 9.48488703e+05, 1.41121081e+06, 9.48863531e+05, 9.46924453e+05, 5.36209719e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.45355469e+05, 9.45328203e+05, 9.45337562e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.45355469e+05, 9.33559000e+05, 9.57207250e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.45355469e+05, 9.45355469e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.45340700e+06, 9.45340700e+06, 9.45340700e+06, 9.45340700e+06, 9.45340700e+06, 9.45340700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.48852734e+05, 9.48145359e+05, 1.41069622e+06, 9.48517625e+05, 9.46580766e+05, 5.36018000e+05, ],
  }),
  ("nof_tree_events",                 998000),
  ("nof_db_events",                   998000),
  ("fsize_local",                     4276698412), # 4.28GB, avg file size 1.07GB
  ("fsize_db",                        46741447242), # 46.74GB, avg file size 5.19GB
  ("use_it",                          True),
  ("xsection",                        0.0001038674),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       8),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 1996000, ],
    'CountWeighted'                                                                  : [ 1.98489217e+06, 1.98486727e+06, 1.98477411e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.98489217e+06, 1.98489217e+06, ],
    'CountWeightedPSWeight'                                                          : [ 1.98466625e+07, 1.98466625e+07, 1.98466625e+07, 1.98466625e+07, 1.98466625e+07, 1.98466625e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99613944e+06, 1.99572089e+06, 2.95504297e+06, 1.99578250e+06, 1.99054636e+06, 1.13674511e+06, ],
    'CountWeightedFull'                                                              : [ 1.98414178e+06, 1.98411247e+06, 1.98401958e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.98414178e+06, 1.98414178e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.98391278e+07, 1.98391278e+07, 1.98391278e+07, 1.98391278e+07, 1.98391278e+07, 1.98391278e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99538991e+06, 1.99496977e+06, 2.95392225e+06, 1.99502956e+06, 1.98979575e+06, 1.13632266e+06, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.90187534e+06, 1.90179478e+06, 1.90189053e+06, ],
    'CountWeightedL1Prefire'                                                         : [ 1.90187534e+06, 1.88213184e+06, 1.92172180e+06, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.90187534e+06, 1.90187534e+06, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.90178700e+07, 1.90178700e+07, 1.90178700e+07, 1.90178700e+07, 1.90178700e+07, 1.90178700e+07, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.91287583e+06, 1.91149466e+06, 2.83048478e+06, 1.91199727e+06, 1.90849692e+06, 1.09038230e+06, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.90116742e+06, 1.90108600e+06, 1.90118031e+06, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.90116742e+06, 1.88143353e+06, 1.92100453e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.90116742e+06, 1.90116742e+06, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.90107745e+07, 1.90107745e+07, 1.90107745e+07, 1.90107745e+07, 1.90107745e+07, 1.90107745e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.91216641e+06, 1.91078456e+06, 2.82942541e+06, 1.91128541e+06, 1.90778702e+06, 1.08998239e+06, ],
  }),
  ("nof_tree_events",                 1996000),
  ("nof_db_events",                   1996000),
  ("fsize_local",                     9740640961), # 9.74GB, avg file size 1.22GB
  ("fsize_db",                        99308407017), # 99.31GB, avg file size 5.23GB
  ("use_it",                          True),
  ("xsection",                        0.001037918),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 995500, ],
    'CountWeighted'                                                                  : [ 9.90985297e+05, 9.91072109e+05, 9.91083438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.90985297e+05, 9.90985297e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.91071475e+06, 9.91071475e+06, 9.91071475e+06, 9.91071475e+06, 9.91071475e+06, 9.91071475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.95582016e+05, 9.95669750e+05, 1.47079084e+06, 9.95399062e+05, 9.93059922e+05, 5.70219062e+05, ],
    'CountWeightedFull'                                                              : [ 9.90644906e+05, 9.90724859e+05, 9.90744453e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.90644906e+05, 9.90644906e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.90732875e+06, 9.90732875e+06, 9.90732875e+06, 9.90732875e+06, 9.90732875e+06, 9.90732875e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.95242156e+05, 9.95330000e+05, 1.47028244e+06, 9.95057547e+05, 9.92716875e+05, 5.70026875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.52178703e+05, 9.52160312e+05, 9.52269703e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.52178703e+05, 9.42643875e+05, 9.61741594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.52178703e+05, 9.52178703e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.52199200e+06, 9.52199200e+06, 9.52199200e+06, 9.52199200e+06, 9.52199200e+06, 9.52199200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.56609375e+05, 9.56126328e+05, 1.41284031e+06, 9.56203688e+05, 9.54920172e+05, 5.48336750e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.51856172e+05, 9.51835625e+05, 9.51947484e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.51856172e+05, 9.42325688e+05, 9.61414688e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.51856172e+05, 9.51856172e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.51877775e+06, 9.51877775e+06, 9.51877775e+06, 9.51877775e+06, 9.51877775e+06, 9.51877775e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.56287094e+05, 9.55804469e+05, 1.41235831e+06, 9.55879859e+05, 9.54594438e+05, 5.48154266e+05, ],
  }),
  ("nof_tree_events",                 995500),
  ("nof_db_events",                   995500),
  ("fsize_local",                     4393569516), # 4.39GB, avg file size 1.10GB
  ("fsize_db",                        47063460066), # 47.06GB, avg file size 4.28GB
  ("use_it",                          True),
  ("xsection",                        0.004819446),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       6),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 999000, ],
    'CountWeighted'                                                                  : [ 9.94030388e+05, 9.94064525e+05, 9.93901366e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.94030388e+05, 9.94030388e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.93909652e+06, 9.93909652e+06, 9.93909652e+06, 9.93909652e+06, 9.93909652e+06, 9.93909652e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.98827095e+05, 9.99072081e+05, 1.47716684e+06, 9.99216131e+05, 9.95442590e+05, 5.70228533e+05, ],
    'CountWeightedFull'                                                              : [ 9.93667020e+05, 9.93700969e+05, 9.93538866e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.93667020e+05, 9.93667020e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.93546077e+06, 9.93546077e+06, 9.93546077e+06, 9.93546077e+06, 9.93546077e+06, 9.93546077e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.98464980e+05, 9.98708360e+05, 1.47662899e+06, 9.98851946e+05, 9.95083039e+05, 5.70023768e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.53478191e+05, 9.53499749e+05, 9.53419475e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.53478191e+05, 9.43738735e+05, 9.63264395e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.53478191e+05, 9.53478191e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.53433550e+06, 9.53433550e+06, 9.53433550e+06, 9.53433550e+06, 9.53433550e+06, 9.53433550e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.58165157e+05, 9.57797381e+05, 1.41640607e+06, 9.58281322e+05, 9.55535710e+05, 5.47560362e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.53135339e+05, 9.53156431e+05, 9.53076726e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.53135339e+05, 9.43400342e+05, 9.62916841e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.53135339e+05, 9.53135339e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.53090778e+06, 9.53090778e+06, 9.53090778e+06, 9.53090778e+06, 9.53090778e+06, 9.53090778e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.57822423e+05, 9.57453437e+05, 1.41589683e+06, 9.57936481e+05, 9.55195120e+05, 5.47366162e+05, ],
  }),
  ("nof_tree_events",                 999000),
  ("nof_db_events",                   999000),
  ("fsize_local",                     4748000510), # 4.75GB, avg file size 791.33MB
  ("fsize_db",                        49082808579), # 49.08GB, avg file size 2.89GB
  ("use_it",                          True),
  ("xsection",                        0.0007901474),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff"),
  ("nof_files",                       9),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 1998600, ],
    'CountWeighted'                                                                  : [ 1.98914721e+06, 1.98941292e+06, 1.98909515e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.98914721e+06, 1.98914721e+06, ],
    'CountWeightedPSWeight'                                                          : [ 1.98894132e+07, 1.98894132e+07, 1.98894132e+07, 1.98894132e+07, 1.98894132e+07, 1.98894132e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99873006e+06, 1.99935029e+06, 2.95187499e+06, 1.99846339e+06, 1.99167685e+06, 1.14402811e+06, ],
    'CountWeightedFull'                                                              : [ 1.98843859e+06, 1.98869137e+06, 1.98838768e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.98843859e+06, 1.98843859e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.98823637e+07, 1.98823637e+07, 1.98823637e+07, 1.98823637e+07, 1.98823637e+07, 1.98823637e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99802357e+06, 1.99864204e+06, 2.95082366e+06, 1.99775173e+06, 1.99097135e+06, 1.14362727e+06, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.90929418e+06, 1.90934837e+06, 1.90935057e+06, ],
    'CountWeightedL1Prefire'                                                         : [ 1.90929418e+06, 1.88989374e+06, 1.92877876e+06, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.90929418e+06, 1.90929418e+06, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.90921313e+07, 1.90921313e+07, 1.90921313e+07, 1.90921313e+07, 1.90921313e+07, 1.90921313e+07, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.91868183e+06, 1.91824010e+06, 2.83253754e+06, 1.91792038e+06, 1.91297085e+06, 1.09915829e+06, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.90862471e+06, 1.90867394e+06, 1.90868096e+06, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.90862471e+06, 1.88923269e+06, 1.92810010e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.90862471e+06, 1.90862471e+06, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.90854520e+07, 1.90854520e+07, 1.90854520e+07, 1.90854520e+07, 1.90854520e+07, 1.90854520e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.91801281e+06, 1.91756899e+06, 2.83154235e+06, 1.91724698e+06, 1.91230306e+06, 1.09877816e+06, ],
  }),
  ("nof_tree_events",                 1998600),
  ("nof_db_events",                   1998600),
  ("fsize_local",                     9107176787), # 9.11GB, avg file size 1.01GB
  ("fsize_db",                        95935612009), # 95.94GB, avg file size 5.05GB
  ("use_it",                          True),
  ("xsection",                        0.001976886),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff_ext1"),
  ("nof_files",                       3),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                                          : [ 496500, ],
    'CountWeighted'                                                                  : [ 4.94130934e+05, 4.94151633e+05, 4.94151988e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.94130934e+05, 4.94130934e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.94145572e+06, 4.94145572e+06, 4.94145572e+06, 4.94145572e+06, 4.94145572e+06, 4.94145572e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.96553266e+05, 4.96093922e+05, 7.33790586e+05, 4.96419168e+05, 4.95949641e+05, 2.84281680e+05, ],
    'CountWeightedFull'                                                              : [ 4.93958711e+05, 4.93978996e+05, 4.93976953e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.93958711e+05, 4.93958711e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.93971794e+06, 4.93971794e+06, 4.93971794e+06, 4.93971794e+06, 4.93971794e+06, 4.93971794e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.96380188e+05, 4.95920203e+05, 7.33533773e+05, 4.96244402e+05, 4.95778336e+05, 2.84183250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.74460734e+05, 4.74466141e+05, 4.74473164e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 4.74460734e+05, 4.69669730e+05, 4.79272465e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.74460734e+05, 4.74460734e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 4.74468438e+06, 4.74468438e+06, 4.74468438e+06, 4.74468438e+06, 4.74468438e+06, 4.74468438e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 4.76817891e+05, 4.76095547e+05, 7.04357223e+05, 4.76552648e+05, 4.76534934e+05, 2.73208668e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 4.74297016e+05, 4.74302250e+05, 4.74308160e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 4.74297016e+05, 4.69508027e+05, 4.79106223e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.74297016e+05, 4.74297016e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 4.74303844e+06, 4.74303844e+06, 4.74303844e+06, 4.74303844e+06, 4.74303844e+06, 4.74303844e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 4.76653785e+05, 4.75930750e+05, 7.04113562e+05, 4.76387168e+05, 4.76371891e+05, 2.73115264e+05, ],
  }),
  ("nof_tree_events",                 496500),
  ("nof_db_events",                   496500),
  ("fsize_local",                     2264836264), # 2.26GB, avg file size 754.95MB
  ("fsize_db",                        24277893809), # 24.28GB, avg file size 899.18MB
  ("use_it",                          True),
  ("xsection",                        0.001976886),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2016["/GluGluToHHTo2B2Tau_node_1_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99923094e+05, 3.99971734e+05, 3.99925578e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99923094e+05, 3.99923094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.98699162e+06, 3.65965625e+06, 3.99810750e+06, 3.97392700e+06, 3.20732800e+06, 2.86001712e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00089406e+05, 3.99662484e+05, 6.12934781e+05, 3.99880562e+05, 3.99153234e+05, 2.15061289e+05, ],
    'CountWeightedFull'                                                              : [ 3.99888172e+05, 3.99936906e+05, 3.99890828e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99888172e+05, 3.99888172e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.98664675e+06, 3.65934488e+06, 3.99776112e+06, 3.97358062e+06, 3.20705350e+06, 2.85977800e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00057422e+05, 3.99628391e+05, 6.12879469e+05, 3.99841953e+05, 3.99117359e+05, 2.15043297e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91566266e+05, 3.91594281e+05, 3.91562500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91566266e+05, 3.89456688e+05, 3.93673578e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.91566266e+05, 3.91566266e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.90363400e+06, 3.58328788e+06, 3.91442988e+06, 3.89050662e+06, 3.14111300e+06, 2.80120975e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.92053031e+05, 3.91238375e+05, 5.99969906e+05, 3.91064828e+05, 3.90865078e+05, 2.10638977e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.91532797e+05, 3.91560766e+05, 3.91529047e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.91532797e+05, 3.89423516e+05, 3.93639688e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.91532797e+05, 3.91532797e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.90330262e+06, 3.58298838e+06, 3.91409700e+06, 3.89017425e+06, 3.14084900e+06, 2.80097962e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.92022328e+05, 3.91205438e+05, 5.99916891e+05, 3.91027875e+05, 3.90830594e+05, 2.10621641e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1647544542), # 1.65GB, avg file size 823.77MB
  ("fsize_db",                        17178531370), # 17.18GB, avg file size 2.45GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2016["/GluGluToHHTo2B2Tau_node_3_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 396700, ],
    'CountWeighted'                                                                  : [ 3.96679312e+05, 3.96596234e+05, 3.96660672e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96679312e+05, 3.96679312e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96637338e+06, 3.96637338e+06, 3.96637338e+06, 3.96637338e+06, 3.96637338e+06, 3.96637338e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96801625e+05, 3.96589031e+05, 6.08824453e+05, 3.96598781e+05, 3.95240109e+05, 2.12263141e+05, ],
    'CountWeightedFull'                                                              : [ 3.96642969e+05, 3.96560625e+05, 3.96624812e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96642969e+05, 3.96642969e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96601425e+06, 3.96601425e+06, 3.96601425e+06, 3.96601425e+06, 3.96601425e+06, 3.96601425e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96768406e+05, 3.96553594e+05, 6.08767375e+05, 3.96559031e+05, 3.95202984e+05, 2.12244469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88134844e+05, 3.88080625e+05, 3.88129531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88134844e+05, 3.85996734e+05, 3.90271219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.88134844e+05, 3.88134844e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.88110962e+06, 3.88110962e+06, 3.88110962e+06, 3.88110962e+06, 3.88110962e+06, 3.88110962e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.88596922e+05, 3.87962094e+05, 5.95673891e+05, 3.87627469e+05, 3.86905922e+05, 2.07770781e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.88100078e+05, 3.88046094e+05, 3.88095047e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.88100078e+05, 3.85962391e+05, 3.90236062e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.88100078e+05, 3.88100078e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.88076412e+06, 3.88076412e+06, 3.88076412e+06, 3.88076412e+06, 3.88076412e+06, 3.88076412e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.88565062e+05, 3.87928109e+05, 5.95619031e+05, 3.87589234e+05, 3.86870203e+05, 2.07752891e+05, ],
  }),
  ("nof_tree_events",                 396700),
  ("nof_db_events",                   396700),
  ("fsize_local",                     1686487237), # 1.69GB, avg file size 843.24MB
  ("fsize_db",                        17304942771), # 17.30GB, avg file size 2.88GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_3_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_4_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99953766e+05, 3.99982062e+05, 3.99920672e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99953766e+05, 3.99953766e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99984300e+06, 3.99971600e+06, 3.99984300e+06, 3.99984300e+06, 3.99280375e+06, 3.99267662e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00249516e+05, 4.00136172e+05, 6.11552969e+05, 3.99735297e+05, 3.97301609e+05, 2.15149914e+05, ],
    'CountWeightedFull'                                                              : [ 3.99919828e+05, 3.99948000e+05, 3.99887641e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99919828e+05, 3.99919828e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99950162e+06, 3.99937462e+06, 3.99950162e+06, 3.99950162e+06, 3.99246325e+06, 3.99233638e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00218219e+05, 4.00102359e+05, 6.11499047e+05, 3.99697844e+05, 3.97266922e+05, 2.15132234e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91613266e+05, 3.91617875e+05, 3.91603016e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91613266e+05, 3.89509672e+05, 3.93716562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.91613266e+05, 3.91613266e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.91630475e+06, 3.91618300e+06, 3.91630475e+06, 3.91630475e+06, 3.90945838e+06, 3.90933650e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.92237562e+05, 3.91688094e+05, 5.98651031e+05, 3.90940047e+05, 3.89117578e+05, 2.10748273e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.91580516e+05, 3.91585094e+05, 3.91570656e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.91580516e+05, 3.89477281e+05, 3.93683500e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.91580516e+05, 3.91580516e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.91597650e+06, 3.91585500e+06, 3.91597650e+06, 3.91597650e+06, 3.90913088e+06, 3.90900888e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.92207406e+05, 3.91655688e+05, 5.98599281e+05, 3.90904031e+05, 3.89084188e+05, 2.10731328e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1647390968), # 1.65GB, avg file size 823.70MB
  ("fsize_db",                        17171599807), # 17.17GB, avg file size 2.86GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_4_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_5_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 394500, ],
    'CountWeighted'                                                                  : [ 3.94453281e+05, 3.94462406e+05, 3.94446734e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94453281e+05, 3.94453281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94487725e+06, 3.94487725e+06, 3.94487725e+06, 3.94487725e+06, 3.94487725e+06, 3.94487725e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.94464562e+05, 3.94204109e+05, 6.07633688e+05, 3.94557531e+05, 3.92414844e+05, 2.08641297e+05, ],
    'CountWeightedFull'                                                              : [ 3.94411641e+05, 3.94420750e+05, 3.94405141e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.94411641e+05, 3.94411641e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.94445625e+06, 3.94445625e+06, 3.94445625e+06, 3.94445625e+06, 3.94445625e+06, 3.94445625e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.94425734e+05, 3.94164703e+05, 6.07567172e+05, 3.94511578e+05, 3.92370016e+05, 2.08619492e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.85179828e+05, 3.85181234e+05, 3.85177266e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.85179828e+05, 3.82899031e+05, 3.87462859e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.85179828e+05, 3.85179828e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.85198750e+06, 3.85198750e+06, 3.85198750e+06, 3.85198750e+06, 3.85198750e+06, 3.85198750e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.85546453e+05, 3.84802156e+05, 5.93230844e+05, 3.84807844e+05, 3.83337062e+05, 2.03813023e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.85139703e+05, 3.85141078e+05, 3.85137000e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.85139703e+05, 3.82859234e+05, 3.87422297e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.85139703e+05, 3.85139703e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.85158375e+06, 3.85158375e+06, 3.85158375e+06, 3.85158375e+06, 3.85158375e+06, 3.85158375e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.85509203e+05, 3.84764422e+05, 5.93167031e+05, 3.84763781e+05, 3.83293828e+05, 2.03792117e+05, ],
  }),
  ("nof_tree_events",                 394500),
  ("nof_db_events",                   394500),
  ("fsize_local",                     1813688315), # 1.81GB, avg file size 906.84MB
  ("fsize_db",                        18014461194), # 18.01GB, avg file size 3.00GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_5_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_7_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 397000, ],
    'CountWeighted'                                                                  : [ 3.96991938e+05, 3.96936656e+05, 3.96987312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96991938e+05, 3.96991938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97006050e+06, 3.96927750e+06, 3.97006050e+06, 3.97006050e+06, 3.94818325e+06, 3.94740062e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.97074016e+05, 3.97128250e+05, 6.09172703e+05, 3.96909281e+05, 3.96367891e+05, 2.13324875e+05, ],
    'CountWeightedFull'                                                              : [ 3.96957000e+05, 3.96902125e+05, 3.96952625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96957000e+05, 3.96957000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96970312e+06, 3.96892075e+06, 3.96970312e+06, 3.96970312e+06, 3.94782888e+06, 3.94704662e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.97041656e+05, 3.97094281e+05, 6.09117625e+05, 3.96870984e+05, 3.96331703e+05, 2.13306578e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88745578e+05, 3.88704578e+05, 3.88753516e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88745578e+05, 3.86667453e+05, 3.90822281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.88745578e+05, 3.88745578e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.88754062e+06, 3.88677438e+06, 3.88754062e+06, 3.88754062e+06, 3.86620688e+06, 3.86544050e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.89165969e+05, 3.88793422e+05, 5.96445391e+05, 3.88233000e+05, 3.88285500e+05, 2.08981250e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.88711844e+05, 3.88671062e+05, 3.88720078e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.88711844e+05, 3.86634047e+05, 3.90788281e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.88711844e+05, 3.88711844e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.88720100e+06, 3.88643475e+06, 3.88720100e+06, 3.88720100e+06, 3.86587000e+06, 3.86510350e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.89134766e+05, 3.88760797e+05, 5.96392469e+05, 3.88196219e+05, 3.88250625e+05, 2.08963602e+05, ],
  }),
  ("nof_tree_events",                 397000),
  ("nof_db_events",                   397000),
  ("fsize_local",                     1637148054), # 1.64GB, avg file size 818.57MB
  ("fsize_db",                        17033242389), # 17.03GB, avg file size 3.41GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_7_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_8_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 398900, ],
    'CountWeighted'                                                                  : [ 3.98859078e+05, 3.98902047e+05, 3.98865281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.98859078e+05, 3.98859078e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.16490320e+05, 3.16377812e+05, 4.84694188e+05, 3.16587594e+05, 3.15551930e+05, 1.70443066e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.98847266e+05, 3.98706531e+05, 6.10022438e+05, 3.98963797e+05, 3.96870031e+05, 2.14799250e+05, ],
    'CountWeightedFull'                                                              : [ 3.98824750e+05, 3.98867375e+05, 3.98830953e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.98824750e+05, 3.98824750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.16465180e+05, 3.16350570e+05, 4.84650328e+05, 3.16557188e+05, 3.15523539e+05, 1.70428824e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98815531e+05, 3.98672234e+05, 6.09967125e+05, 3.98925453e+05, 3.96834219e+05, 2.14781203e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.90636703e+05, 3.90654094e+05, 3.90643812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.90636703e+05, 3.88560625e+05, 3.92709172e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.90636703e+05, 3.90636703e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.10229469e+05, 3.09763539e+05, 4.74632750e+05, 3.09714984e+05, 3.09180375e+05, 1.66993367e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.90953266e+05, 3.90366469e+05, 5.97353062e+05, 3.90298406e+05, 3.88852547e+05, 2.10449375e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.90603656e+05, 3.90620938e+05, 3.90610625e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.90603656e+05, 3.88527938e+05, 3.92675812e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.90603656e+05, 3.90603656e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.10205305e+05, 3.09737453e+05, 4.74590703e+05, 3.09685820e+05, 3.09153047e+05, 1.66979707e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.90922766e+05, 3.90333484e+05, 5.97299969e+05, 3.90261672e+05, 3.88818047e+05, 2.10432102e+05, ],
  }),
  ("nof_tree_events",                 398900),
  ("nof_db_events",                   398900),
  ("fsize_local",                     1639149968), # 1.64GB, avg file size 819.57MB
  ("fsize_db",                        16954806742), # 16.95GB, avg file size 3.39GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_8_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2016["/GluGluToHHTo2B2Tau_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_2b2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    33),
  ("nof_events",                      {
    'Count'                                                                          : [ 947200, ],
    'CountWeighted'                                                                  : [ 8.91626439e+05, 8.91625781e+05, 8.91594895e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.03161475e+06, 1.01360823e+06, 1.00094082e+06, 9.11858600e+05, 8.91626408e+05, 8.75317845e+05, 8.08402305e+05, 7.87562255e+05, 7.69781453e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.06805186e+06, 7.51965003e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.91574062e+05, 8.92116366e+05, 1.35066993e+06, 8.91623040e+05, 8.86489703e+05, 4.86281340e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.06628201e+04, 6.07120281e+04, 9.21621692e+04, 6.06736201e+04, 6.05590752e+04, 3.30792935e+04, ],
    'CountWeightedFull'                                                              : [ 5.70285768e+04, 5.70298709e+04, 5.70253759e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 6.59834004e+04, 6.48312410e+04, 6.40205119e+04, 5.83239361e+04, 5.70285748e+04, 5.59862303e+04, 5.17063469e+04, 5.03731520e+04, 4.92355723e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 6.83144113e+04, 4.80961211e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 5.70264496e+04, 5.70607145e+04, 8.63904420e+04, 5.70290617e+04, 5.67010525e+04, 3.11032017e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.88854032e+03, 3.89176952e+03, 5.90789626e+03, 3.88921178e+03, 3.88193088e+03, 2.12029676e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.77520033e+05, 8.77494868e+05, 8.77527422e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.77520033e+05, 8.73838272e+05, 8.81191484e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.01510330e+06, 9.97522409e+05, 9.85175568e+05, 8.97316095e+05, 8.77520033e+05, 8.61589000e+05, 7.95541104e+05, 7.75147618e+05, 7.57744370e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.05097931e+06, 7.40209195e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.77574743e+05, 8.77861646e+05, 1.32922224e+06, 8.77403214e+05, 8.72727284e+05, 4.78740771e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 5.97003884e+04, 5.97313251e+04, 9.06827531e+04, 5.96958315e+04, 5.96082525e+04, 3.25606491e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 5.61267838e+04, 5.61260408e+04, 5.61260518e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 5.61267838e+04, 5.58910525e+04, 5.63614673e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 6.49270197e+04, 6.38020353e+04, 6.30119788e+04, 5.73936539e+04, 5.61267838e+04, 5.51080355e+04, 5.08835320e+04, 4.95789698e+04, 4.84655768e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 6.72221264e+04, 4.73440526e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 5.61308366e+04, 5.61488133e+04, 8.50184594e+04, 5.61194664e+04, 5.58206750e+04, 3.06208198e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.82679520e+03, 3.82886755e+03, 5.81298878e+03, 3.82648603e+03, 3.82091375e+03, 2.08702267e+03, ],
  }),
  ("nof_tree_events",                 947200),
  ("nof_db_events",                   947200),
  ("fsize_local",                     3825203536), # 3.83GB, avg file size 765.04MB
  ("fsize_db",                        38664951189), # 38.66GB, avg file size 1.17GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH0_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2b2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    29),
  ("nof_events",                      {
    'Count'                                                                          : [ 999400, ],
    'CountWeighted'                                                                  : [ 8.95152828e+05, 8.95215367e+05, 8.94994711e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.01903467e+06, 1.00279631e+06, 9.92092094e+05, 9.15704938e+05, 8.95130121e+05, 8.78947566e+05, 8.21921258e+05, 7.99508262e+05, 7.80722672e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.06270847e+06, 7.57019203e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.95233320e+05, 8.94804672e+05, 1.35909065e+06, 8.94980996e+05, 8.92166125e+05, 4.86743656e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98756636e+04, 2.98747656e+04, 4.54550225e+04, 2.98749377e+04, 2.98709497e+04, 1.62573541e+04, ],
    'CountWeightedFull'                                                              : [ 2.67319463e+04, 2.67367085e+04, 2.67278010e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.04328418e+04, 2.99474519e+04, 2.96275256e+04, 2.73469233e+04, 2.67314716e+04, 2.62486290e+04, 2.45456710e+04, 2.38760819e+04, 2.33148972e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.17372627e+04, 2.26071282e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.67353232e+04, 2.67225322e+04, 4.05878848e+04, 2.67275969e+04, 2.66434479e+04, 1.45359932e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 8.93780174e+02, 8.94048893e+02, 1.35947157e+03, 8.93856812e+02, 8.93467098e+02, 4.86796036e+02, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.80423711e+05, 8.80494031e+05, 8.80282688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.80423711e+05, 8.76605754e+05, 8.84230387e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.00205334e+06, 9.86222219e+05, 9.75817344e+05, 9.00521047e+05, 8.80398891e+05, 8.64610141e+05, 8.08340562e+05, 7.86415984e+05, 7.68037676e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.04502855e+06, 7.44716484e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.80632488e+05, 8.79945867e+05, 1.33663388e+06, 8.80115344e+05, 8.77724648e+05, 4.78882641e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.93855183e+04, 2.93756128e+04, 4.47002966e+04, 2.93759280e+04, 2.93853228e+04, 1.59931234e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.62921691e+04, 2.62962462e+04, 2.62884871e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.62921691e+04, 2.61780754e+04, 2.64059891e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 2.99254597e+04, 2.94523069e+04, 2.91413435e+04, 2.68932732e+04, 2.62915818e+04, 2.58203481e+04, 2.41399397e+04, 2.34849943e+04, 2.29360189e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.12090386e+04, 2.22396245e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.62991682e+04, 2.62786089e+04, 3.99170115e+04, 2.62835156e+04, 2.62120310e+04, 1.43011779e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 8.79123230e+02, 8.79117470e+02, 1.33690044e+03, 8.78934448e+02, 8.78950577e+02, 4.78896702e+02, ],
  }),
  ("nof_tree_events",                 999400),
  ("nof_db_events",                   999400),
  ("fsize_local",                     4151626463), # 4.15GB, avg file size 830.33MB
  ("fsize_db",                        41235766334), # 41.24GB, avg file size 1.42GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2b2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    31),
  ("nof_events",                      {
    'Count'                                                                          : [ 951000, ],
    'CountWeighted'                                                                  : [ 8.19716976e+05, 8.19628049e+05, 8.19844712e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.34415124e+05, 9.21427892e+05, 9.13162350e+05, 8.36502222e+05, 8.19710608e+05, 8.06615466e+05, 7.49072428e+05, 7.30590638e+05, 7.15036793e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.84549429e+05, 6.84215528e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.19773133e+05, 8.19875292e+05, 1.24697909e+06, 8.19678103e+05, 8.16926660e+05, 4.44112813e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.24903100e+04, 1.24912485e+04, 1.90471416e+04, 1.24879735e+04, 1.24954256e+04, 6.76828958e+03, ],
    'CountWeightedFull'                                                              : [ 1.07508627e+04, 1.07513771e+04, 1.07527450e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.22559798e+04, 1.20852828e+04, 1.19765488e+04, 1.09716601e+04, 1.07507151e+04, 1.05791389e+04, 9.82461047e+03, 9.58201182e+03, 9.37786013e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.29135808e+04, 8.97368684e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.07520055e+04, 1.07532467e+04, 1.63548672e+04, 1.07505746e+04, 1.07144168e+04, 5.82485298e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.64121515e+02, 1.64128786e+02, 2.50252487e+02, 1.64084530e+02, 1.64169812e+02, 8.89381571e+01, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.06110853e+05, 8.06014512e+05, 8.06233276e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.06110853e+05, 8.02581921e+05, 8.09627964e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.18667967e+05, 9.06035062e+05, 8.98029995e+05, 8.22478571e+05, 8.06098489e+05, 7.93328182e+05, 7.36558371e+05, 7.18503952e+05, 7.03307916e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.67997611e+05, 6.72982724e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.06276053e+05, 8.06073482e+05, 1.22610268e+06, 8.05909660e+05, 8.03601934e+05, 4.36916107e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.22829965e+04, 1.22794534e+04, 1.87262088e+04, 1.22765861e+04, 1.22901017e+04, 6.65754493e+03, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.05723581e+04, 1.05722405e+04, 1.05740655e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.05723581e+04, 1.05261518e+04, 1.06185204e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.20492640e+04, 1.18832541e+04, 1.17779664e+04, 1.07875762e+04, 1.05721539e+04, 1.04047887e+04, 9.66038277e+03, 9.42340852e+03, 9.22396662e+03, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.26963099e+04, 8.82629724e+03, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.05748656e+04, 1.05721033e+04, 1.60809159e+04, 1.05698975e+04, 1.05395914e+04, 5.73041042e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.61390287e+02, 1.61338738e+02, 2.46025821e+02, 1.61299895e+02, 1.61466268e+02, 8.74787225e+01, ],
  }),
  ("nof_tree_events",                 951000),
  ("nof_db_events",                   951000),
  ("fsize_local",                     3963612162), # 3.96GB, avg file size 792.72MB
  ("fsize_db",                        39424683698), # 39.42GB, avg file size 1.27GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2B2Tau_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_2b2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    28),
  ("nof_events",                      {
    'Count'                                                                          : [ 984200, ],
    'CountWeighted'                                                                  : [ 9.68689180e+05, 9.68855855e+05, 9.68932410e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.16061366e+06, 1.13860822e+06, 1.12165208e+06, 9.88230719e+05, 9.68674949e+05, 9.52384793e+05, 8.50968008e+05, 8.33821805e+05, 8.18308141e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.19591621e+06, 8.01762926e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.68769430e+05, 9.69342285e+05, 1.46733340e+06, 9.68877977e+05, 9.64962746e+05, 5.29715656e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 7.89666104e+04, 7.90134297e+04, 1.19942017e+05, 7.89837422e+04, 7.90031904e+04, 4.31888230e+04, ],
    'CountWeightedFull'                                                              : [ 7.77032881e+04, 7.77118452e+04, 7.77123252e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 9.30905190e+04, 9.13241777e+04, 8.99629590e+04, 7.92640698e+04, 7.77008511e+04, 7.63871108e+04, 6.82528013e+04, 6.68767791e+04, 6.56318130e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.59228989e+04, 6.43049607e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 7.77021792e+04, 7.77486621e+04, 1.17688682e+05, 7.77103789e+04, 7.73945864e+04, 4.24867842e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 6.33902762e+03, 6.34294543e+03, 9.62638708e+03, 6.34034979e+03, 6.34159308e+03, 3.46847514e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.54570996e+05, 9.54629797e+05, 9.54760098e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.54570996e+05, 9.50805930e+05, 9.58322484e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.14332286e+06, 1.12181732e+06, 1.10525984e+06, 9.73619203e+05, 9.54551953e+05, 9.38572477e+05, 8.38459012e+05, 8.21690336e+05, 8.06508211e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.17814537e+06, 7.90190129e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.54718395e+05, 9.54999488e+05, 1.44574714e+06, 9.54540246e+05, 9.51162422e+05, 5.22167420e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 7.78146802e+04, 7.78374346e+04, 1.18167762e+05, 7.78083662e+04, 7.78668350e+04, 4.25695781e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 7.65669141e+04, 7.65694507e+04, 7.65763149e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 7.65669141e+04, 7.62642227e+04, 7.68679512e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 9.17027119e+04, 8.99767100e+04, 8.86477007e+04, 7.80914072e+04, 7.65645518e+04, 7.52787148e+04, 6.72489763e+04, 6.59033911e+04, 6.46850671e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.44964150e+04, 6.33763562e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 7.65746548e+04, 7.65976147e+04, 1.15956602e+05, 7.65597305e+04, 7.62872705e+04, 4.18810059e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 6.24638736e+03, 6.24836081e+03, 9.48374921e+03, 6.24584247e+03, 6.25024768e+03, 3.41864529e+03, ],
  }),
  ("nof_tree_events",                 984200),
  ("nof_db_events",                   984200),
  ("fsize_local",                     3711587241), # 3.71GB, avg file size 742.32MB
  ("fsize_db",                        38800257105), # 38.80GB, avg file size 1.39GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2t',          'signal_ggf_nonresonant_node_box_hh_2b2t',         'signal_ggf_nonresonant_node_1_hh_2b2t',           'signal_ggf_nonresonant_node_2_hh_2b2t',           'signal_ggf_nonresonant_node_3_hh_2b2t',           'signal_ggf_nonresonant_node_4_hh_2b2t',           'signal_ggf_nonresonant_node_5_hh_2b2t',           'signal_ggf_nonresonant_node_6_hh_2b2t',           'signal_ggf_nonresonant_node_7_hh_2b2t',           'signal_ggf_nonresonant_node_8_hh_2b2t',           'signal_ggf_nonresonant_node_9_hh_2b2t',           'signal_ggf_nonresonant_node_10_hh_2b2t',          'signal_ggf_nonresonant_node_11_hh_2b2t',          'signal_ggf_nonresonant_node_12_hh_2b2t',          'signal_ggf_nonresonant_node_13_hh_2b2t',           ],
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2v',          'signal_ggf_nonresonant_node_box_hh_2b2v',         'signal_ggf_nonresonant_node_1_hh_2b2v',           'signal_ggf_nonresonant_node_2_hh_2b2v',           'signal_ggf_nonresonant_node_3_hh_2b2v',           'signal_ggf_nonresonant_node_4_hh_2b2v',           'signal_ggf_nonresonant_node_5_hh_2b2v',           'signal_ggf_nonresonant_node_6_hh_2b2v',           'signal_ggf_nonresonant_node_7_hh_2b2v',           'signal_ggf_nonresonant_node_8_hh_2b2v',           'signal_ggf_nonresonant_node_9_hh_2b2v',           'signal_ggf_nonresonant_node_10_hh_2b2v',          'signal_ggf_nonresonant_node_11_hh_2b2v',          'signal_ggf_nonresonant_node_12_hh_2b2v',           ],
  [ 'signal_ggf_spin0_900_hh_2b2t',                    'signal_ggf_spin0_900_hh_2b2t_PSWeights',           ],
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2v_sl_PSWeights', 'signal_ggf_nonresonant_node_1_hh_2b2v_sl_PSWeights', 'signal_ggf_nonresonant_node_2_hh_2b2v_sl_PSWeights', 'signal_ggf_nonresonant_node_3_hh_2b2v_sl_PSWeights', 'signal_ggf_nonresonant_node_4_hh_2b2v_sl_PSWeights', 'signal_ggf_nonresonant_node_5_hh_2b2v_sl',        'signal_ggf_nonresonant_node_6_hh_2b2v_sl_PSWeights', 'signal_ggf_nonresonant_node_7_hh_2b2v_sl',        'signal_ggf_nonresonant_node_8_hh_2b2v_sl_PSWeights', 'signal_ggf_nonresonant_node_9_hh_2b2v_sl',        'signal_ggf_nonresonant_node_10_hh_2b2v_sl_PSWeights', 'signal_ggf_nonresonant_node_11_hh_2b2v_sl_PSWeights', 'signal_ggf_nonresonant_node_12_hh_2b2v_sl_PSWeights',  ],
  [ 'signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff', 'signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff_ext1',  ],
]

