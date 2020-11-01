from collections import OrderedDict as OD

# file generated at 2020-11-01 11:55:06 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh.py -p python/samples/sampleLocations_2016_preselected.txt -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_hh_preselected.py -M

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
  ("nof_tree_events",                 71015),
  ("nof_db_events",                   299998),
  ("fsize_local",                     268591815), # 268.59MB, avg file size 268.59MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 71772),
  ("nof_db_events",                   294629),
  ("fsize_local",                     275514647), # 275.51MB, avg file size 275.51MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 79631),
  ("nof_db_events",                   300000),
  ("fsize_local",                     317947164), # 317.95MB, avg file size 317.95MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 84593),
  ("nof_db_events",                   295149),
  ("fsize_local",                     356911408), # 356.91MB, avg file size 356.91MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 91131),
  ("nof_db_events",                   299997),
  ("fsize_local",                     401923313), # 401.92MB, avg file size 401.92MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 93166),
  ("nof_db_events",                   296256),
  ("fsize_local",                     425251400), # 425.25MB, avg file size 425.25MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 96899),
  ("nof_db_events",                   300000),
  ("fsize_local",                     455225498), # 455.23MB, avg file size 455.23MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 99127),
  ("nof_db_events",                   299999),
  ("fsize_local",                     478063109), # 478.06MB, avg file size 478.06MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 100121),
  ("nof_db_events",                   299999),
  ("fsize_local",                     492170434), # 492.17MB, avg file size 492.17MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 100755),
  ("nof_db_events",                   299538),
  ("fsize_local",                     502296506), # 502.30MB, avg file size 502.30MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 101394),
  ("nof_db_events",                   298727),
  ("fsize_local",                     514922933), # 514.92MB, avg file size 514.92MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 100724),
  ("nof_db_events",                   299705),
  ("fsize_local",                     515210110), # 515.21MB, avg file size 515.21MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 99559),
  ("nof_db_events",                   298733),
  ("fsize_local",                     514727147), # 514.73MB, avg file size 514.73MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 98969),
  ("nof_db_events",                   299999),
  ("fsize_local",                     517243914), # 517.24MB, avg file size 517.24MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 71103),
  ("nof_db_events",                   300000),
  ("fsize_local",                     274054491), # 274.05MB, avg file size 274.05MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_260_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 73284),
  ("nof_db_events",                   300000),
  ("fsize_local",                     285760433), # 285.76MB, avg file size 285.76MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_270_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 80288),
  ("nof_db_events",                   299999),
  ("fsize_local",                     328383993), # 328.38MB, avg file size 328.38MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_300_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 88962),
  ("nof_db_events",                   300000),
  ("fsize_local",                     385701711), # 385.70MB, avg file size 385.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_350_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 94883),
  ("nof_db_events",                   300000),
  ("fsize_local",                     429919496), # 429.92MB, avg file size 429.92MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_400_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 98952),
  ("nof_db_events",                   299999),
  ("fsize_local",                     463280524), # 463.28MB, avg file size 463.28MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_450_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 101957),
  ("nof_db_events",                   299999),
  ("fsize_local",                     493122819), # 493.12MB, avg file size 493.12MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_500_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 104237),
  ("nof_db_events",                   299999),
  ("fsize_local",                     516334815), # 516.33MB, avg file size 516.33MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_550_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 104466),
  ("nof_db_events",                   299999),
  ("fsize_local",                     526031535), # 526.03MB, avg file size 526.03MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_600_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 105369),
  ("nof_db_events",                   298806),
  ("fsize_local",                     537054027), # 537.05MB, avg file size 537.05MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_650_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 105423),
  ("nof_db_events",                   299999),
  ("fsize_local",                     540835913), # 540.84MB, avg file size 540.84MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_700_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 104509),
  ("nof_db_events",                   299999),
  ("fsize_local",                     541950793), # 541.95MB, avg file size 541.95MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_800_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 103217),
  ("nof_db_events",                   299999),
  ("fsize_local",                     539736074), # 539.74MB, avg file size 539.74MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_900_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 101707),
  ("nof_db_events",                   299118),
  ("fsize_local",                     534938068), # 534.94MB, avg file size 534.94MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_1000_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 398999, ],
    'CountWeighted'                                                                  : [ 3.97556594e+05, 3.97604312e+05, 3.97604094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97556594e+05, 3.97556594e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97540150e+06, 3.97540150e+06, 3.97540150e+06, 3.97540150e+06, 3.97540150e+06, 3.97540150e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.98980656e+05, 3.99385812e+05, 5.89739562e+05, 3.98996344e+05, 3.98132125e+05, 2.28737688e+05, ],
    'CountWeightedFull'                                                              : [ 3.97379125e+05, 3.97424219e+05, 3.97425500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97379125e+05, 3.97379125e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97364450e+06, 3.97364450e+06, 3.97364450e+06, 3.97364450e+06, 3.97364450e+06, 3.97364450e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98802125e+05, 3.99206844e+05, 5.89472875e+05, 3.98817188e+05, 3.97953062e+05, 2.28636250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.82396406e+05, 3.82413406e+05, 3.82404219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.82396406e+05, 3.78595625e+05, 3.86201594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.82396406e+05, 3.82396406e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.82391125e+06, 3.82391125e+06, 3.82391125e+06, 3.82391125e+06, 3.82391125e+06, 3.82391125e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.83769062e+05, 3.83940688e+05, 5.67044812e+05, 3.83713844e+05, 3.83194844e+05, 2.20218344e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.82226406e+05, 3.82242844e+05, 3.82234250e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.82226406e+05, 3.78427875e+05, 3.86029531e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.82226406e+05, 3.82226406e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.82221550e+06, 3.82221550e+06, 3.82221550e+06, 3.82221550e+06, 3.82221550e+06, 3.82221550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.83599062e+05, 3.83770312e+05, 5.66791438e+05, 3.83543250e+05, 3.83024000e+05, 2.20121594e+05, ],
  }),
  ("nof_tree_events",                 106299),
  ("nof_db_events",                   398999),
  ("fsize_local",                     457911127), # 457.91MB, avg file size 457.91MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 396799, ],
    'CountWeighted'                                                                  : [ 3.95403125e+05, 3.95429875e+05, 3.95394562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95403125e+05, 3.95403125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95388775e+06, 3.95388775e+06, 3.95388775e+06, 3.95388775e+06, 3.95388775e+06, 3.95388775e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96835812e+05, 3.96572688e+05, 5.89944812e+05, 3.96740719e+05, 3.95666000e+05, 2.24042500e+05, ],
    'CountWeightedFull'                                                              : [ 3.95213000e+05, 3.95241250e+05, 3.95205625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95213000e+05, 3.95213000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95200575e+06, 3.95200575e+06, 3.95200575e+06, 3.95200575e+06, 3.95200575e+06, 3.95200575e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96647125e+05, 3.96384812e+05, 5.89661062e+05, 3.96550250e+05, 3.95474875e+05, 2.23936156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.76588844e+05, 3.76590188e+05, 3.76587625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.76588844e+05, 3.72032562e+05, 3.81165156e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76588844e+05, 3.76588844e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.76584275e+06, 3.76584275e+06, 3.76584275e+06, 3.76584275e+06, 3.76584275e+06, 3.76584275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.78004000e+05, 3.77539875e+05, 5.61663062e+05, 3.77756750e+05, 3.77050000e+05, 2.13593344e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.76410844e+05, 3.76412781e+05, 3.76409500e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.76410844e+05, 3.71857156e+05, 3.80984438e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.76410844e+05, 3.76410844e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.76406425e+06, 3.76406425e+06, 3.76406425e+06, 3.76406425e+06, 3.76406425e+06, 3.76406425e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.77826344e+05, 3.77362844e+05, 5.61395812e+05, 3.77577500e+05, 3.76869938e+05, 2.13493203e+05, ],
  }),
  ("nof_tree_events",                 103804),
  ("nof_db_events",                   396799),
  ("fsize_local",                     476228459), # 476.23MB, avg file size 476.23MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 399200, ],
    'CountWeighted'                                                                  : [ 3.97047906e+05, 3.97063500e+05, 3.97048531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97047906e+05, 3.97047906e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97045200e+06, 3.97045200e+06, 3.97045200e+06, 3.97045200e+06, 3.97045200e+06, 3.97045200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99080594e+05, 3.99500625e+05, 5.91679500e+05, 3.99371781e+05, 3.98283781e+05, 2.27272688e+05, ],
    'CountWeightedFull'                                                              : [ 3.96856438e+05, 3.96872125e+05, 3.96855688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96856438e+05, 3.96856438e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96853525e+06, 3.96853525e+06, 3.96853525e+06, 3.96853525e+06, 3.96853525e+06, 3.96853525e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98889125e+05, 3.99307750e+05, 5.91392562e+05, 3.99178719e+05, 3.98091969e+05, 2.27164484e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.80849719e+05, 3.80853312e+05, 3.80855875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.80849719e+05, 3.76985062e+05, 3.84733188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.80849719e+05, 3.80849719e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.80846925e+06, 3.80846925e+06, 3.80846925e+06, 3.80846925e+06, 3.80846925e+06, 3.80846925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.82821000e+05, 3.83028344e+05, 5.67323875e+05, 3.82975719e+05, 3.82254188e+05, 2.18213438e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.80667969e+05, 3.80671312e+05, 3.80673125e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.80667969e+05, 3.76805594e+05, 3.84549062e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.80667969e+05, 3.80667969e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.80664950e+06, 3.80664950e+06, 3.80664950e+06, 3.80664950e+06, 3.80664950e+06, 3.80664950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.82639062e+05, 3.82845031e+05, 5.67051625e+05, 3.82792438e+05, 3.82071938e+05, 2.18110516e+05, ],
  }),
  ("nof_tree_events",                 125215),
  ("nof_db_events",                   399200),
  ("fsize_local",                     619719769), # 619.72MB, avg file size 619.72MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.98673125e+05, 3.98693125e+05, 3.98663062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.98673125e+05, 3.98673125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.98659075e+06, 3.98659075e+06, 3.98659075e+06, 3.98659075e+06, 3.98659075e+06, 3.98659075e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00039656e+05, 3.99914469e+05, 5.89801375e+05, 3.99929312e+05, 3.98916031e+05, 2.30073469e+05, ],
    'CountWeightedFull'                                                              : [ 3.98500594e+05, 3.98520031e+05, 3.98492500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.98500594e+05, 3.98500594e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.98486975e+06, 3.98486975e+06, 3.98486975e+06, 3.98486975e+06, 3.98486975e+06, 3.98486975e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99867500e+05, 3.99741656e+05, 5.89549125e+05, 3.99757750e+05, 3.98747875e+05, 2.29975359e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.85426250e+05, 3.85426281e+05, 3.85427656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.85426250e+05, 3.82077906e+05, 3.88775500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.85426250e+05, 3.85426250e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.85418525e+06, 3.85418525e+06, 3.85418525e+06, 3.85418525e+06, 3.85418525e+06, 3.85418525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.86778500e+05, 3.86487375e+05, 5.70028250e+05, 3.86589625e+05, 3.85831219e+05, 2.22605016e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.85261375e+05, 3.85261531e+05, 3.85263375e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.85261375e+05, 3.81914906e+05, 3.88608969e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.85261375e+05, 3.85261375e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.85253950e+06, 3.85253950e+06, 3.85253950e+06, 3.85253950e+06, 3.85253950e+06, 3.85253950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.86613594e+05, 3.86321812e+05, 5.69786250e+05, 3.86425312e+05, 3.85669656e+05, 2.22510906e+05, ],
  }),
  ("nof_tree_events",                 111563),
  ("nof_db_events",                   399999),
  ("fsize_local",                     478092506), # 478.09MB, avg file size 478.09MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 398799, ],
    'CountWeighted'                                                                  : [ 3.97056000e+05, 3.97116688e+05, 3.97093500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97056000e+05, 3.97056000e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97091350e+06, 3.97091350e+06, 3.97091350e+06, 3.97091350e+06, 3.97091350e+06, 3.97091350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.98828812e+05, 3.98403812e+05, 5.89212250e+05, 3.98745031e+05, 3.98372438e+05, 2.28467875e+05, ],
    'CountWeightedFull'                                                              : [ 3.96875562e+05, 3.96932125e+05, 3.96909688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96875562e+05, 3.96875562e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96909775e+06, 3.96909775e+06, 3.96909775e+06, 3.96909775e+06, 3.96909775e+06, 3.96909775e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98646688e+05, 3.98221625e+05, 5.88943000e+05, 3.98562438e+05, 3.98191312e+05, 2.28363938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81992750e+05, 3.82013250e+05, 3.82010312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81992750e+05, 3.78287125e+05, 3.85708688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81992750e+05, 3.81992750e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.82008900e+06, 3.82008900e+06, 3.82008900e+06, 3.82008900e+06, 3.82008900e+06, 3.82008900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.83698219e+05, 3.83078938e+05, 5.66732875e+05, 3.83540281e+05, 3.83566750e+05, 2.19983562e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81819781e+05, 3.81838875e+05, 3.81835938e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81819781e+05, 3.78116094e+05, 3.85533812e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81819781e+05, 3.81819781e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81835400e+06, 3.81835400e+06, 3.81835400e+06, 3.81835400e+06, 3.81835400e+06, 3.81835400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.83524812e+05, 3.82905438e+05, 5.66476312e+05, 3.83366188e+05, 3.83394000e+05, 2.19884344e+05, ],
  }),
  ("nof_tree_events",                 118177),
  ("nof_db_events",                   398799),
  ("fsize_local",                     546430804), # 546.43MB, avg file size 546.43MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 399097, ],
    'CountWeighted'                                                                  : [ 3.97024656e+05, 3.97012938e+05, 3.97038281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97024656e+05, 3.97024656e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97029025e+06, 3.97029025e+06, 3.97029025e+06, 3.97029025e+06, 3.97029025e+06, 3.97029025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.98944844e+05, 3.99761906e+05, 5.89342875e+05, 3.99287938e+05, 3.96196031e+05, 2.27711812e+05, ],
    'CountWeightedFull'                                                              : [ 3.96833219e+05, 3.96823562e+05, 3.96846750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96833219e+05, 3.96833219e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96838975e+06, 3.96838975e+06, 3.96838975e+06, 3.96838975e+06, 3.96838975e+06, 3.96838975e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98754875e+05, 3.99570312e+05, 5.89061188e+05, 3.99096000e+05, 3.96008312e+05, 2.27603719e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81186781e+05, 3.81172188e+05, 3.81202062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81186781e+05, 3.77375406e+05, 3.85009750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81186781e+05, 3.81186781e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81187525e+06, 3.81187525e+06, 3.81187525e+06, 3.81187525e+06, 3.81187525e+06, 3.81187525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.83057312e+05, 3.83615594e+05, 5.65602125e+05, 3.83267781e+05, 3.80631750e+05, 2.18854625e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81005750e+05, 3.80992000e+05, 3.81020969e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81005750e+05, 3.77196969e+05, 3.84826688e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81005750e+05, 3.81005750e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81007000e+06, 3.81007000e+06, 3.81007000e+06, 3.81007000e+06, 3.81007000e+06, 3.81007000e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.82876906e+05, 3.83433938e+05, 5.65334688e+05, 3.83085344e+05, 3.80453156e+05, 2.18751938e+05, ],
  }),
  ("nof_tree_events",                 124002),
  ("nof_db_events",                   399097),
  ("fsize_local",                     603317785), # 603.32MB, avg file size 603.32MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 396800, ],
    'CountWeighted'                                                                  : [ 3.94914562e+05, 3.94933875e+05, 3.94925312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94914562e+05, 3.94914562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94891675e+06, 3.94891675e+06, 3.94891675e+06, 3.94891675e+06, 3.94891675e+06, 3.94891675e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96868156e+05, 3.96727250e+05, 5.85768500e+05, 3.96697188e+05, 3.95530750e+05, 2.27334531e+05, ],
    'CountWeightedFull'                                                              : [ 3.94732688e+05, 3.94752844e+05, 3.94739938e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.94732688e+05, 3.94732688e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.94710575e+06, 3.94710575e+06, 3.94710575e+06, 3.94710575e+06, 3.94710575e+06, 3.94710575e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96684719e+05, 3.96543594e+05, 5.85494812e+05, 3.96512531e+05, 3.95346156e+05, 2.27230359e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.79473438e+05, 3.79474719e+05, 3.79479562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.79473438e+05, 3.75716156e+05, 3.83244344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.79473438e+05, 3.79473438e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.79463200e+06, 3.79463200e+06, 3.79463200e+06, 3.79463200e+06, 3.79463200e+06, 3.79463200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.81377281e+05, 3.81009781e+05, 5.62658750e+05, 3.81105781e+05, 3.80311375e+05, 2.18655391e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.79299719e+05, 3.79301719e+05, 3.79304562e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.79299719e+05, 3.75544844e+05, 3.83068406e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.79299719e+05, 3.79299719e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.79289675e+06, 3.79289675e+06, 3.79289675e+06, 3.79289675e+06, 3.79289675e+06, 3.79289675e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.81203250e+05, 3.80835188e+05, 5.62398750e+05, 3.80930406e+05, 3.80136062e+05, 2.18556312e+05, ],
  }),
  ("nof_tree_events",                 119624),
  ("nof_db_events",                   396800),
  ("fsize_local",                     565291619), # 565.29MB, avg file size 565.29MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 92855),
  ("nof_db_events",                   299999),
  ("fsize_local",                     432706369), # 432.71MB, avg file size 432.71MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 90043),
  ("nof_db_events",                   299999),
  ("fsize_local",                     409882318), # 409.88MB, avg file size 409.88MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_box_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 91442),
  ("nof_db_events",                   299999),
  ("fsize_local",                     434913074), # 434.91MB, avg file size 434.91MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 2564),
  ("nof_db_events",                   300000),
  ("fsize_local",                     13650442), # 13.65MB, avg file size 13.65MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 93468),
  ("nof_db_events",                   299998),
  ("fsize_local",                     441376927), # 441.38MB, avg file size 441.38MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_3_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 89992),
  ("nof_db_events",                   299999),
  ("fsize_local",                     413011673), # 413.01MB, avg file size 413.01MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 95014),
  ("nof_db_events",                   299999),
  ("fsize_local",                     468701303), # 468.70MB, avg file size 468.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_5_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 87243),
  ("nof_db_events",                   299999),
  ("fsize_local",                     397998545), # 398.00MB, avg file size 398.00MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 80983),
  ("nof_db_events",                   299997),
  ("fsize_local",                     343337661), # 343.34MB, avg file size 343.34MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 91356),
  ("nof_db_events",                   299999),
  ("fsize_local",                     432277615), # 432.28MB, avg file size 432.28MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 95388),
  ("nof_db_events",                   299998),
  ("fsize_local",                     464904372), # 464.90MB, avg file size 464.90MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 81223),
  ("nof_db_events",                   299998),
  ("fsize_local",                     349386699), # 349.39MB, avg file size 349.39MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 86423),
  ("nof_db_events",                   299364),
  ("fsize_local",                     392245738), # 392.25MB, avg file size 392.25MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 85761),
  ("nof_db_events",                   299997),
  ("fsize_local",                     376777849), # 376.78MB, avg file size 376.78MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    89),
  ("nof_events",                      {
    'Count'                                                                          : [ 396798, ],
    'CountWeighted'                                                                  : [ 3.55736562e+05, 3.55707406e+05, 3.55764750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.05001188e+05, 3.98537188e+05, 3.94274125e+05, 3.63937188e+05, 3.55725344e+05, 3.49300656e+05, 3.26635000e+05, 3.17715844e+05, 3.10243750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.22376062e+05, 3.00800625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.55645875e+05, 3.55454438e+05, 5.39986125e+05, 3.55857469e+05, 3.54755125e+05, 1.93727781e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.18724736e+04, 1.18694053e+04, 1.80651328e+04, 1.18778779e+04, 1.18854316e+04, 6.47055225e+03, ],
    'CountWeightedFull'                                                              : [ 1.06224902e+04, 1.06224648e+04, 1.06232861e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.20936465e+04, 1.19004883e+04, 1.17731055e+04, 1.08677793e+04, 1.06224072e+04, 1.04305059e+04, 9.75339648e+03, 9.48698926e+03, 9.26381055e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.26128887e+04, 8.98185352e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.06201562e+04, 1.06143076e+04, 1.61248018e+04, 1.06262803e+04, 1.05935674e+04, 5.78497217e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.55950256e+02, 3.55960175e+02, 5.41120605e+02, 3.56162567e+02, 3.56111816e+02, 1.94318832e+02, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.50235844e+05, 3.50202406e+05, 3.50265344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.50235844e+05, 3.48806594e+05, 3.51663000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98637781e+05, 3.92334000e+05, 3.88189594e+05, 3.58255344e+05, 3.50224812e+05, 3.43944531e+05, 3.21558344e+05, 3.12824969e+05, 3.05508000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.15747250e+05, 2.96212812e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.50191375e+05, 3.49887938e+05, 5.31575750e+05, 3.50295781e+05, 3.49366250e+05, 1.90801297e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.16892432e+04, 1.16827188e+04, 1.77821973e+04, 1.16911260e+04, 1.17034473e+04, 6.37208057e+03, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.04582803e+04, 1.04578379e+04, 1.04591641e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.04582803e+04, 1.04155537e+04, 1.05008691e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.19035322e+04, 1.17151738e+04, 1.15913398e+04, 1.06980410e+04, 1.04581025e+04, 1.02705107e+04, 9.60174707e+03, 9.34090625e+03, 9.12238281e+03, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.24148418e+04, 8.84483691e+03, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.04572158e+04, 1.04480488e+04, 1.58735439e+04, 1.04601338e+04, 1.04325488e+04, 5.69756299e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.50441498e+02, 3.50343231e+02, 5.32619568e+02, 3.50545990e+02, 3.50649841e+02, 1.91356232e+02, ],
  }),
  ("nof_tree_events",                 119700),
  ("nof_db_events",                   396798),
  ("fsize_local",                     524747321), # 524.75MB, avg file size 524.75MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 398400, ],
    'CountWeighted'                                                                  : [ 3.43460812e+05, 3.43474219e+05, 3.43457062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.91843500e+05, 3.86327562e+05, 3.82795250e+05, 3.50528812e+05, 3.43455844e+05, 3.37916438e+05, 3.13714750e+05, 3.05950625e+05, 2.99419500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.12573625e+05, 2.86767281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.43666000e+05, 3.43842125e+05, 5.22053812e+05, 3.43215562e+05, 3.41542250e+05, 1.86092250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.23530566e+03, 5.23623340e+03, 7.97928467e+03, 5.22924609e+03, 5.23097461e+03, 2.83538867e+03, ],
    'CountWeightedFull'                                                              : [ 4.50374561e+03, 4.50377539e+03, 4.50395410e+03, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.13858154e+03, 5.06611768e+03, 5.01971240e+03, 4.59679102e+03, 4.50366113e+03, 4.43124023e+03, 4.11391553e+03, 4.01203809e+03, 3.92634814e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.41045361e+03, 3.76043896e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.50674463e+03, 4.50910107e+03, 6.84590039e+03, 4.50071143e+03, 4.47866650e+03, 2.44033838e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 6.87947388e+01, 6.88183060e+01, 1.04847870e+02, 6.87095032e+01, 6.87173157e+01, 3.72528305e+01, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.38092406e+05, 3.38093500e+05, 3.38099938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.38092406e+05, 3.36699188e+05, 3.39480125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.85627375e+05, 3.80258938e+05, 3.76835594e+05, 3.44996062e+05, 3.38085406e+05, 3.32682969e+05, 3.08779812e+05, 3.01187688e+05, 2.94800250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.06035812e+05, 2.82349188e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.38347281e+05, 3.38411875e+05, 5.13829938e+05, 3.37788781e+05, 3.36292000e+05, 1.83261312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 5.15338184e+03, 5.15249609e+03, 7.85263574e+03, 5.14563281e+03, 5.15013867e+03, 2.79164917e+03, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 4.43339551e+03, 4.43334814e+03, 4.43366797e+03, ],
    'CountWeightedFullL1Prefire'                                                     : [ 4.43339551e+03, 4.41513232e+03, 4.45162891e+03, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 5.05701660e+03, 4.98649854e+03, 4.94153320e+03, 4.52420312e+03, 4.43329590e+03, 4.36259131e+03, 4.04917676e+03, 3.94956055e+03, 3.86575610e+03, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 5.32467920e+03, 3.70248828e+03, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 4.43697363e+03, 4.43785986e+03, 6.73803906e+03, 4.42952832e+03, 4.40982227e+03, 2.40320557e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 6.77159500e+01, 6.77156296e+01, 1.03180611e+02, 6.76086273e+01, 6.76534653e+01, 3.66769104e+01, ],
  }),
  ("nof_tree_events",                 116153),
  ("nof_db_events",                   398400),
  ("fsize_local",                     512518532), # 512.52MB, avg file size 512.52MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    42),
  ("nof_events",                      {
    'Count'                                                                          : [ 394800, ],
    'CountWeighted'                                                                  : [ 3.88464906e+05, 3.88493750e+05, 3.88421125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.65392625e+05, 4.56639875e+05, 4.49907906e+05, 3.96175000e+05, 3.88462219e+05, 3.81931156e+05, 3.41108688e+05, 3.34279438e+05, 3.28102156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.79520062e+05, 3.21513000e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.88558625e+05, 3.88751812e+05, 5.87666438e+05, 3.88355438e+05, 3.86219344e+05, 2.12480484e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.16907871e+04, 3.17101523e+04, 4.80682734e+04, 3.16724570e+04, 3.16381172e+04, 1.73320938e+04, ],
    'CountWeightedFull'                                                              : [ 3.11534160e+04, 3.11543125e+04, 3.11511094e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.73218984e+04, 3.66196719e+04, 3.60795547e+04, 3.17712285e+04, 3.11529531e+04, 3.06284707e+04, 2.73547754e+04, 2.68069316e+04, 2.63114941e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.84551133e+04, 2.57830508e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.11601758e+04, 3.11753887e+04, 4.71285117e+04, 3.11437070e+04, 3.09736758e+04, 1.70395586e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.54405322e+03, 2.54557910e+03, 3.85786572e+03, 2.54258838e+03, 2.53986694e+03, 1.39220654e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.83062281e+05, 3.83079750e+05, 3.83034594e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.83062281e+05, 3.81623469e+05, 3.84492500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.58791812e+05, 4.50230594e+05, 4.43651906e+05, 3.90605844e+05, 3.83056625e+05, 3.76666156e+05, 3.36346344e+05, 3.29660750e+05, 3.23609938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.72739594e+05, 3.17103688e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.83201188e+05, 3.83259344e+05, 5.79400750e+05, 3.82890188e+05, 3.80961656e+05, 2.09617578e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.12514414e+04, 3.12594277e+04, 4.73889766e+04, 3.12245723e+04, 3.12057441e+04, 1.70974238e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.07196445e+04, 3.07203184e+04, 3.07181895e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.07196445e+04, 3.06042266e+04, 3.08342129e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 3.67922812e+04, 3.61054492e+04, 3.55776914e+04, 3.13243652e+04, 3.07190410e+04, 3.02061035e+04, 2.69727305e+04, 2.64364219e+04, 2.59510977e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.79110938e+04, 2.54293203e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.07303789e+04, 3.07348066e+04, 4.64654102e+04, 3.07052871e+04, 3.05518457e+04, 1.68099102e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.50879004e+03, 2.50939551e+03, 3.80333765e+03, 2.50663525e+03, 2.50515942e+03, 1.37337146e+03, ],
  }),
  ("nof_tree_events",                 102595),
  ("nof_db_events",                   394800),
  ("fsize_local",                     415560274), # 415.56MB, avg file size 415.56MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99977844e+05, 2.99975156e+05, 2.99971656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99977844e+05, 2.99977844e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99950375e+06, 2.99950375e+06, 2.99950375e+06, 2.99950375e+06, 2.99950375e+06, 2.99950375e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00004781e+05, 3.00014375e+05, 4.67898094e+05, 2.99984844e+05, 2.98216656e+05, 1.54086297e+05, ],
    'CountWeightedFull'                                                              : [ 2.99913656e+05, 2.99911344e+05, 2.99907500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99913656e+05, 2.99913656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99886875e+06, 2.99886875e+06, 2.99886875e+06, 2.99886875e+06, 2.99886875e+06, 2.99886875e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99942969e+05, 2.99950750e+05, 4.67797844e+05, 2.99918031e+05, 2.98152812e+05, 1.54053547e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93702031e+05, 2.93692125e+05, 2.93704125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93702031e+05, 2.92119656e+05, 2.95281906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93702031e+05, 2.93702031e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.93686275e+06, 2.93686275e+06, 2.93686275e+06, 2.93686275e+06, 2.93686275e+06, 2.93686275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.94002625e+05, 2.93665938e+05, 4.58021938e+05, 2.93359812e+05, 2.92072938e+05, 1.50924344e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.93639906e+05, 2.93630156e+05, 2.93641781e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.93639906e+05, 2.92057938e+05, 2.95219281e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.93639906e+05, 2.93639906e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.93624325e+06, 2.93624325e+06, 2.93624325e+06, 2.93624325e+06, 2.93624325e+06, 2.93624325e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.93942500e+05, 2.93604188e+05, 4.57924500e+05, 2.93295094e+05, 2.92010875e+05, 1.50892500e+05, ],
  }),
  ("nof_tree_events",                 19404),
  ("nof_db_events",                   299996),
  ("fsize_local",                     91498103), # 91.50MB, avg file size 91.50MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 297895, ],
    'CountWeighted'                                                                  : [ 2.97839406e+05, 2.97861531e+05, 2.97843656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.97839406e+05, 2.97839406e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.33926600e+06, 2.10582575e+06, 2.83364350e+06, 2.31685850e+06, 1.77908588e+06, 1.21065962e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.97768812e+05, 2.97535750e+05, 4.64419562e+05, 2.98084812e+05, 2.96860688e+05, 1.53495375e+05, ],
    'CountWeightedFull'                                                              : [ 2.97779000e+05, 2.97801531e+05, 2.97783219e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.97779000e+05, 2.97779000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.33880625e+06, 2.10540225e+06, 2.83307050e+06, 2.31637275e+06, 1.77872450e+06, 1.21041488e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.97710500e+05, 2.97475938e+05, 4.64325281e+05, 2.98022188e+05, 2.96800438e+05, 1.53464375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91869562e+05, 2.91878062e+05, 2.91873656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91869562e+05, 2.90352938e+05, 2.93381906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.91869562e+05, 2.91869562e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.29426700e+06, 2.06341162e+06, 2.77677550e+06, 2.26809375e+06, 1.74424350e+06, 1.18688112e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.92050250e+05, 2.91473656e+05, 4.55081250e+05, 2.91774219e+05, 2.91082625e+05, 1.50478969e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.91810812e+05, 2.91819656e+05, 2.91814875e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.91810812e+05, 2.90294719e+05, 2.93322812e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.91810812e+05, 2.91810812e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.29381900e+06, 2.06299975e+06, 2.77621700e+06, 2.26762250e+06, 1.74389050e+06, 1.18664288e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.91993500e+05, 2.91415688e+05, 4.54989625e+05, 2.91713344e+05, 2.91023906e+05, 1.50448797e+05, ],
  }),
  ("nof_tree_events",                 19341),
  ("nof_db_events",                   297895),
  ("fsize_local",                     89100526), # 89.10MB, avg file size 89.10MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_1_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 298398, ],
    'CountWeighted'                                                                  : [ 2.98344719e+05, 2.98319812e+05, 2.98345000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98344719e+05, 2.98344719e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98349125e+06, 2.98349125e+06, 2.98349125e+06, 2.98349125e+06, 2.98349125e+06, 2.98349125e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98416125e+05, 2.98598375e+05, 4.68638719e+05, 2.98405969e+05, 2.95418500e+05, 1.49715859e+05, ],
    'CountWeightedFull'                                                              : [ 2.98274188e+05, 2.98249844e+05, 2.98275594e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98274188e+05, 2.98274188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98278425e+06, 2.98278425e+06, 2.98278425e+06, 2.98278425e+06, 2.98278425e+06, 2.98278425e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98348594e+05, 2.98529219e+05, 4.68528438e+05, 2.98332562e+05, 2.95348594e+05, 1.49680969e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91174188e+05, 2.91154781e+05, 2.91176938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91174188e+05, 2.89424094e+05, 2.92925312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.91174188e+05, 2.91174188e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.91176775e+06, 2.91176775e+06, 2.91176775e+06, 2.91176775e+06, 2.91176775e+06, 2.91176775e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.91529094e+05, 2.91338562e+05, 4.57291719e+05, 2.90857750e+05, 2.88398438e+05, 1.46175297e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.91106062e+05, 2.91087062e+05, 2.91109500e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.91106062e+05, 2.89356531e+05, 2.92856719e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.91106062e+05, 2.91106062e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.91108650e+06, 2.91108650e+06, 2.91108650e+06, 2.91108650e+06, 2.91108650e+06, 2.91108650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.91463562e+05, 2.91271656e+05, 4.57184969e+05, 2.90786875e+05, 2.88330719e+05, 1.46141516e+05, ],
  }),
  ("nof_tree_events",                 15100),
  ("nof_db_events",                   298398),
  ("fsize_local",                     79124934), # 79.12MB, avg file size 79.12MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_2_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 293698, ],
    'CountWeighted'                                                                  : [ 2.93651500e+05, 2.93665781e+05, 2.93648531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.93651500e+05, 2.93651500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.93653650e+06, 2.93609325e+06, 2.93653650e+06, 2.93653650e+06, 2.92294625e+06, 2.92250375e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.93829594e+05, 2.93270688e+05, 4.57721562e+05, 2.93565219e+05, 2.92629250e+05, 1.51250875e+05, ],
    'CountWeightedFull'                                                              : [ 2.93590688e+05, 2.93604750e+05, 2.93588031e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.93590688e+05, 2.93590688e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.93592750e+06, 2.93548450e+06, 2.93592750e+06, 2.93592750e+06, 2.92234050e+06, 2.92189750e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.93770906e+05, 2.93211406e+05, 4.57626094e+05, 2.93501562e+05, 2.92567250e+05, 1.51219672e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.87805594e+05, 2.87811844e+05, 2.87807312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.87805594e+05, 2.86319406e+05, 2.89288656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.87805594e+05, 2.87805594e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.87807750e+06, 2.87764275e+06, 2.87807750e+06, 2.87807750e+06, 2.86481625e+06, 2.86438175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.88226219e+05, 2.87357562e+05, 4.48598312e+05, 2.87403406e+05, 2.86961312e+05, 1.48294297e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.87746469e+05, 2.87752656e+05, 2.87748406e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.87746469e+05, 2.86260781e+05, 2.89229125e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.87746469e+05, 2.87746469e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.87748550e+06, 2.87705125e+06, 2.87748550e+06, 2.87748550e+06, 2.86422750e+06, 2.86379250e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.88169156e+05, 2.87300000e+05, 4.48505406e+05, 2.87341625e+05, 2.86901000e+05, 1.48263891e+05, ],
  }),
  ("nof_tree_events",                 19117),
  ("nof_db_events",                   293698),
  ("fsize_local",                     88070759), # 88.07MB, avg file size 88.07MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_4_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEWeightScale'                                                    : [ 3.89002969e+05, 3.60214562e+05, 3.34692344e+05, 3.24086594e+05, 2.99937625e+05, 2.78655906e+05, 2.74200438e+05, 2.53744562e+05, 2.35637141e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.89002969e+05, 2.35637141e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93315719e+05, 2.93330156e+05, 2.93358844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93315719e+05, 2.91665812e+05, 2.94965438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.80302656e+05, 3.52245031e+05, 3.27353844e+05, 3.16827094e+05, 2.93312500e+05, 2.72537031e+05, 2.68050156e+05, 2.48113391e+05, 2.30454844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.80302656e+05, 2.30454844e+05, ],
  }),
  ("nof_tree_events",                 18031),
  ("nof_db_events",                   299098),
  ("fsize_local",                     95014318), # 95.01MB, avg file size 95.01MB
  ("fsize_db",                        14447245371), # 14.45GB, avg file size 760.38MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_5_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 298896, ],
    'CountWeighted'                                                                  : [ 2.98865906e+05, 2.98846656e+05, 2.98861812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98865906e+05, 2.98865906e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98886925e+06, 2.98886925e+06, 2.98886925e+06, 2.98886925e+06, 2.98886925e+06, 2.98886925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98890500e+05, 2.98870500e+05, 4.66457344e+05, 2.98931781e+05, 2.97604875e+05, 1.53640094e+05, ],
    'CountWeightedFull'                                                              : [ 2.98804562e+05, 2.98786781e+05, 2.98800031e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98804562e+05, 2.98804562e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98824800e+06, 2.98824800e+06, 2.98824800e+06, 2.98824800e+06, 2.98824800e+06, 2.98824800e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98831562e+05, 2.98809625e+05, 4.66359594e+05, 2.98867406e+05, 2.97542281e+05, 1.53608984e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92814125e+05, 2.92790188e+05, 2.92825969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92814125e+05, 2.91280500e+05, 2.94344469e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.92814125e+05, 2.92814125e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.92826400e+06, 2.92826400e+06, 2.92826400e+06, 2.92826400e+06, 2.92826400e+06, 2.92826400e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.93094875e+05, 2.92723500e+05, 4.56974312e+05, 2.92546438e+05, 2.91737969e+05, 1.50587422e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.92754438e+05, 2.92731406e+05, 2.92766156e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.92754438e+05, 2.91221312e+05, 2.94284406e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.92754438e+05, 2.92754438e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.92766425e+06, 2.92766425e+06, 2.92766425e+06, 2.92766425e+06, 2.92766425e+06, 2.92766425e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.93037625e+05, 2.92664375e+05, 4.56879594e+05, 2.92484031e+05, 2.91677219e+05, 1.50557188e+05, ],
  }),
  ("nof_tree_events",                 19449),
  ("nof_db_events",                   298896),
  ("fsize_local",                     90351168), # 90.35MB, avg file size 90.35MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_6_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'CountWeightedLHEWeightScale'                                                    : [ 3.79174844e+05, 3.66134312e+05, 3.52515219e+05, 3.10721188e+05, 2.99976531e+05, 2.88811156e+05, 2.59266125e+05, 2.50295312e+05, 2.40945609e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.79174844e+05, 2.40945609e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94945344e+05, 2.94912438e+05, 2.94919656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94945344e+05, 2.93634938e+05, 2.96246625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.72740844e+05, 3.59981281e+05, 3.46636656e+05, 3.05442219e+05, 2.94939156e+05, 2.83991500e+05, 2.54859812e+05, 2.46082500e+05, 2.36921938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.72740844e+05, 2.36921938e+05, ],
  }),
  ("nof_tree_events",                 19820),
  ("nof_db_events",                   298398),
  ("fsize_local",                     88141684), # 88.14MB, avg file size 88.14MB
  ("fsize_db",                        13451681242), # 13.45GB, avg file size 747.32MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_7_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 298899, ],
    'CountWeighted'                                                                  : [ 2.98876562e+05, 2.98884906e+05, 2.98908000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98876562e+05, 2.98876562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.37148250e+05, 2.37471891e+05, 3.69380625e+05, 2.37102797e+05, 2.35315109e+05, 1.22093109e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98912438e+05, 2.99315375e+05, 4.64865844e+05, 2.98860719e+05, 2.95888969e+05, 1.53895766e+05, ],
    'CountWeightedFull'                                                              : [ 2.98815031e+05, 2.98823594e+05, 2.98845812e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98815031e+05, 2.98815031e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.37101141e+05, 2.37424047e+05, 3.69304156e+05, 2.37052250e+05, 2.35265734e+05, 1.22068172e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98853000e+05, 2.99255250e+05, 4.64769531e+05, 2.98796969e+05, 2.95826656e+05, 1.53864297e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92902219e+05, 2.92901781e+05, 2.92925812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92902219e+05, 2.91385062e+05, 2.94415750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.92902219e+05, 2.92902219e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.32605656e+05, 2.32675953e+05, 3.61936781e+05, 2.32109469e+05, 2.30680500e+05, 1.19699695e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.93186188e+05, 2.93270469e+05, 4.55494156e+05, 2.92565938e+05, 2.90058438e+05, 1.50878812e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.92842531e+05, 2.92842156e+05, 2.92865719e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.92842531e+05, 2.91325750e+05, 2.94355719e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.92842531e+05, 2.92842531e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.32559812e+05, 2.32629469e+05, 3.61862438e+05, 2.32060516e+05, 2.30632438e+05, 1.19675484e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.93128281e+05, 2.93212000e+05, 4.55400688e+05, 2.92504188e+05, 2.89997875e+05, 1.50848203e+05, ],
  }),
  ("nof_tree_events",                 19305),
  ("nof_db_events",                   298899),
  ("fsize_local",                     88891941), # 88.89MB, avg file size 88.89MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_8_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99941125e+05, 2.99947906e+05, 2.99939812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99941125e+05, 2.99941125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99934950e+06, 2.99934950e+06, 2.99934950e+06, 2.99934950e+06, 2.99934950e+06, 2.99934950e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99915406e+05, 2.99795719e+05, 4.69221156e+05, 3.00058375e+05, 2.97834156e+05, 1.52438250e+05, ],
    'CountWeightedFull'                                                              : [ 2.99876062e+05, 2.99882625e+05, 2.99874844e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99876062e+05, 2.99876062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99869625e+06, 2.99869625e+06, 2.99869625e+06, 2.99869625e+06, 2.99869625e+06, 2.99869625e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99853031e+05, 2.99731844e+05, 4.69118781e+05, 2.99990750e+05, 2.97768750e+05, 1.52405609e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93195125e+05, 2.93189156e+05, 2.93203781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93195125e+05, 2.91519750e+05, 2.94870562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93195125e+05, 2.93195125e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.93192325e+06, 2.93192325e+06, 2.93192325e+06, 2.93192325e+06, 2.93192325e+06, 2.93192325e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.93445250e+05, 2.92944500e+05, 4.58631000e+05, 2.92952688e+05, 2.91303469e+05, 1.49069375e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.93132250e+05, 2.93126281e+05, 2.93140875e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.93132250e+05, 2.91457375e+05, 2.94807219e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.93132250e+05, 2.93132250e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.93129375e+06, 2.93129375e+06, 2.93129375e+06, 2.93129375e+06, 2.93129375e+06, 2.93129375e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.93384875e+05, 2.92882625e+05, 4.58531938e+05, 2.92887375e+05, 2.91240156e+05, 1.49037781e+05, ],
  }),
  ("nof_tree_events",                 17697),
  ("nof_db_events",                   299996),
  ("fsize_local",                     88384289), # 88.38MB, avg file size 88.38MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_9_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99945750e+05, 2.99933750e+05, 2.99945688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99945750e+05, 2.99945750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.00513012e+06, 1.00248431e+06, 1.50093800e+06, 1.00649950e+06, 9.37024500e+05, 5.17499156e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99837906e+05, 2.99908250e+05, 4.67766625e+05, 3.00249469e+05, 2.98692125e+05, 1.54378062e+05, ],
    'CountWeightedFull'                                                              : [ 2.99883375e+05, 2.99871375e+05, 2.99883031e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99883375e+05, 2.99883375e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.00492831e+06, 1.00227375e+06, 1.50062375e+06, 1.00628069e+06, 9.36831875e+05, 5.17392688e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99777688e+05, 2.99845312e+05, 4.67668688e+05, 3.00184250e+05, 2.98630688e+05, 1.54346266e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93855562e+05, 2.93837562e+05, 2.93866312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93855562e+05, 2.92311562e+05, 2.95395938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93855562e+05, 2.93855562e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.85616500e+05, 9.81860250e+05, 1.47033000e+06, 9.84913438e+05, 9.18509812e+05, 5.07206125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.94009281e+05, 2.93724125e+05, 4.58208875e+05, 2.93802156e+05, 2.92767875e+05, 1.51302656e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.93794906e+05, 2.93776875e+05, 2.93805375e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.93794906e+05, 2.92251344e+05, 2.95334812e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.93794906e+05, 2.93794906e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.85419938e+05, 9.81655625e+05, 1.47002450e+06, 9.84700812e+05, 9.18322625e+05, 5.07102562e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.93950625e+05, 2.93662875e+05, 4.58113656e+05, 2.93738688e+05, 2.92708062e+05, 1.51271766e+05, ],
  }),
  ("nof_tree_events",                 19301),
  ("nof_db_events",                   299998),
  ("fsize_local",                     88752284), # 88.75MB, avg file size 88.75MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_10_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 298398, ],
    'CountWeighted'                                                                  : [ 2.98354969e+05, 2.98384812e+05, 2.98361188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98354969e+05, 2.98354969e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98320400e+06, 2.98320400e+06, 2.98320400e+06, 2.98320400e+06, 2.98320400e+06, 2.98320400e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98360719e+05, 2.98498281e+05, 4.65090938e+05, 2.98415406e+05, 2.96183125e+05, 1.53199516e+05, ],
    'CountWeightedFull'                                                              : [ 2.98292656e+05, 2.98321906e+05, 2.98299906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98292656e+05, 2.98292656e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98258700e+06, 2.98258700e+06, 2.98258700e+06, 2.98258700e+06, 2.98258700e+06, 2.98258700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98300688e+05, 2.98436562e+05, 4.64993812e+05, 2.98350500e+05, 2.96121312e+05, 1.53167938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92133125e+05, 2.92144375e+05, 2.92140188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92133125e+05, 2.90563500e+05, 2.93701562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.92133125e+05, 2.92133125e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.92114700e+06, 2.92114700e+06, 2.92114700e+06, 2.92114700e+06, 2.92114700e+06, 2.92114700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.92395781e+05, 2.92174062e+05, 4.55309344e+05, 2.91844656e+05, 2.90126625e+05, 1.50070297e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.92072625e+05, 2.92083438e+05, 2.92080344e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.92072625e+05, 2.90503562e+05, 2.93640625e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.92072625e+05, 2.92072625e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.92054500e+06, 2.92054500e+06, 2.92054500e+06, 2.92054500e+06, 2.92054500e+06, 2.92054500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.92337500e+05, 2.92114188e+05, 4.55215062e+05, 2.91781750e+05, 2.90066594e+05, 1.50039594e+05, ],
  }),
  ("nof_tree_events",                 19197),
  ("nof_db_events",                   298398),
  ("fsize_local",                     90349019), # 90.35MB, avg file size 90.35MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_11_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 295397, ],
    'CountWeighted'                                                                  : [ 2.95409531e+05, 2.95402125e+05, 2.95408406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.95409531e+05, 2.95409531e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.18421641e+05, 2.18504609e+05, 3.40209969e+05, 2.18491203e+05, 2.17117484e+05, 1.12494320e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.95348219e+05, 2.95458938e+05, 4.59179531e+05, 2.95441625e+05, 2.92736750e+05, 1.52114938e+05, ],
    'CountWeightedFull'                                                              : [ 2.95348688e+05, 2.95341562e+05, 2.95347656e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.95348688e+05, 2.95348688e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.18378422e+05, 2.18460422e+05, 3.40138500e+05, 2.18444422e+05, 2.17071469e+05, 1.12471672e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.95289781e+05, 2.95399062e+05, 4.59083406e+05, 2.95378500e+05, 2.92674812e+05, 1.52084344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.89484875e+05, 2.89473188e+05, 2.89490750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.89484875e+05, 2.87984062e+05, 2.90981906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.89484875e+05, 2.89484875e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.14234266e+05, 2.14076359e+05, 3.33332812e+05, 2.13875344e+05, 2.12835641e+05, 1.10289820e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.89685000e+05, 2.89470656e+05, 4.49896219e+05, 2.89198125e+05, 2.86962469e+05, 1.49133062e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.89425781e+05, 2.89414156e+05, 2.89431812e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.89425781e+05, 2.87925344e+05, 2.90922438e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.89425781e+05, 2.89425781e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.14192203e+05, 2.14033359e+05, 3.33263219e+05, 2.13829828e+05, 2.12790781e+05, 1.10267781e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.89628062e+05, 2.89412406e+05, 4.49802469e+05, 2.89136750e+05, 2.86902031e+05, 1.49103297e+05, ],
  }),
  ("nof_tree_events",                 19155),
  ("nof_db_events",                   295397),
  ("fsize_local",                     87940980), # 87.94MB, avg file size 87.94MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_12_hh_2b2v_sl_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    43),
  ("nof_events",                      {
    'Count'                                                                          : [ 398998, ],
    'CountWeighted'                                                                  : [ 3.57598875e+05, 3.57530375e+05, 3.57620438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06886094e+05, 4.00472344e+05, 3.96251844e+05, 3.65771562e+05, 3.57562250e+05, 3.51154188e+05, 3.28400688e+05, 3.19468938e+05, 3.11981406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.24594188e+05, 3.02261281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.57620781e+05, 3.57689062e+05, 5.52594812e+05, 3.57509781e+05, 3.55817781e+05, 1.86020594e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.19199854e+04, 1.19198447e+04, 1.84904180e+04, 1.19202471e+04, 1.19314824e+04, 6.20109863e+03, ],
    'CountWeightedFull'                                                              : [ 1.06774365e+04, 1.06760801e+04, 1.06781406e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.21494512e+04, 1.19578242e+04, 1.18317324e+04, 1.09218047e+04, 1.06761143e+04, 1.04852061e+04, 9.80583594e+03, 9.53902539e+03, 9.31542676e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.26782520e+04, 9.02520703e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.06783193e+04, 1.06806426e+04, 1.64999512e+04, 1.06750762e+04, 1.06240801e+04, 5.55442236e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.56106964e+02, 3.56095886e+02, 5.52491455e+02, 3.56234131e+02, 3.56572266e+02, 1.85271301e+02, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.52075156e+05, 3.52005875e+05, 3.52115062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.52075156e+05, 3.50627688e+05, 3.53519500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.00519844e+05, 3.94259344e+05, 3.90151594e+05, 3.60079000e+05, 3.52049000e+05, 3.45779500e+05, 3.23308312e+05, 3.14561000e+05, 3.07226500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.17966000e+05, 2.97649188e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.52150969e+05, 3.52082062e+05, 5.44079375e+05, 3.51934000e+05, 3.50502844e+05, 1.83203469e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.17356699e+04, 1.17313555e+04, 1.82026152e+04, 1.17324072e+04, 1.17510371e+04, 6.10606641e+03, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.05126484e+04, 1.05109531e+04, 1.05137617e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.05126484e+04, 1.04693477e+04, 1.05557559e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.19593027e+04, 1.17722676e+04, 1.16495498e+04, 1.07517861e+04, 1.05117188e+04, 1.03246914e+04, 9.65376465e+03, 9.39245605e+03, 9.17344238e+03, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.24802695e+04, 8.88748633e+03, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.05149346e+04, 1.05131865e+04, 1.62456484e+04, 1.05085293e+04, 1.04653584e+04, 5.47028125e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.50594116e+02, 3.50459595e+02, 5.43876404e+02, 3.50606445e+02, 3.51165466e+02, 1.82427414e+02, ],
  }),
  ("nof_tree_events",                 25794),
  ("nof_db_events",                   398998),
  ("fsize_local",                     119731644), # 119.73MB, avg file size 119.73MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 391395, ],
    'CountWeighted'                                                                  : [ 3.37001594e+05, 3.36914875e+05, 3.37102062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84151312e+05, 3.78848719e+05, 3.75483156e+05, 3.43880031e+05, 3.36997219e+05, 3.31619688e+05, 3.07904438e+05, 3.00332156e+05, 2.93960125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04670531e+05, 2.81380344e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.37087250e+05, 3.37110656e+05, 5.21428812e+05, 3.36887812e+05, 3.34943594e+05, 1.74612109e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.14020312e+03, 5.14185547e+03, 7.99240527e+03, 5.14106836e+03, 5.14740137e+03, 2.66314551e+03, ],
    'CountWeightedFull'                                                              : [ 4.41910840e+03, 4.41802441e+03, 4.42039600e+03, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.03751562e+03, 4.96790771e+03, 4.92369873e+03, 4.50942920e+03, 4.41904639e+03, 4.34854492e+03, 4.03762280e+03, 3.93826660e+03, 3.85467407e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.30659766e+03, 3.68973291e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.42032227e+03, 4.42068994e+03, 6.83775488e+03, 4.41761475e+03, 4.39221826e+03, 2.28968384e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 6.75435028e+01, 6.75634613e+01, 1.05029068e+02, 6.75533829e+01, 6.76452484e+01, 3.49931221e+01, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.31647188e+05, 3.31554812e+05, 3.31753031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.31647188e+05, 3.30251688e+05, 3.33039000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.77955438e+05, 3.72796750e+05, 3.69535656e+05, 3.38363500e+05, 3.31640812e+05, 3.26398000e+05, 3.02983250e+05, 2.95581188e+05, 2.89350625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98156906e+05, 2.76968469e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.31785688e+05, 3.31695906e+05, 5.13083812e+05, 3.31466625e+05, 3.29711750e+05, 1.71907359e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 5.05864453e+03, 5.05842383e+03, 7.86325146e+03, 5.05766357e+03, 5.06622119e+03, 2.62151270e+03, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 4.34891943e+03, 4.34772803e+03, 4.35028906e+03, ],
    'CountWeightedFullL1Prefire'                                                     : [ 4.34891943e+03, 4.33061230e+03, 4.36716895e+03, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.95625732e+03, 4.88853613e+03, 4.84569922e+03, 4.43707959e+03, 4.34883398e+03, 4.28006445e+03, 3.97307715e+03, 3.87595776e+03, 3.79423145e+03, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 5.22116455e+03, 3.63187598e+03, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 4.35079541e+03, 4.34966943e+03, 6.72829150e+03, 4.34650732e+03, 4.32359961e+03, 2.25421680e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 6.64693451e+01, 6.64647141e+01, 1.03328354e+02, 6.64550781e+01, 6.65763092e+01, 3.44447861e+01, ],
  }),
  ("nof_tree_events",                 23975),
  ("nof_db_events",                   391395),
  ("fsize_local",                     111364992), # 111.36MB, avg file size 111.36MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 18060),
  ("nof_db_events",                   299997),
  ("fsize_local",                     71213245), # 71.21MB, avg file size 71.21MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 18709),
  ("nof_db_events",                   299402),
  ("fsize_local",                     74728869), # 74.73MB, avg file size 74.73MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_260_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 19134),
  ("nof_db_events",                   299995),
  ("fsize_local",                     77376377), # 77.38MB, avg file size 77.38MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_270_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 19933),
  ("nof_db_events",                   299996),
  ("fsize_local",                     83607860), # 83.61MB, avg file size 83.61MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_300_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 21296),
  ("nof_db_events",                   299998),
  ("fsize_local",                     94924463), # 94.92MB, avg file size 94.92MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_350_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 21729),
  ("nof_db_events",                   300000),
  ("fsize_local",                     101740233), # 101.74MB, avg file size 101.74MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_400_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 20592),
  ("nof_db_events",                   292028),
  ("fsize_local",                     100633809), # 100.63MB, avg file size 100.63MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_450_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 21004),
  ("nof_db_events",                   299997),
  ("fsize_local",                     106464992), # 106.46MB, avg file size 106.46MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 20198),
  ("nof_db_events",                   299996),
  ("fsize_local",                     105236928), # 105.24MB, avg file size 105.24MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_550_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 19595),
  ("nof_db_events",                   299999),
  ("fsize_local",                     104850063), # 104.85MB, avg file size 104.85MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_600_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.99972656e+05, 2.99988500e+05, 3.00024094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.25221219e+05, 2.99953062e+05, 2.77657844e+05, 3.25221219e+05, 2.99953062e+05, 2.77657844e+05, 3.25221219e+05, 2.99953062e+05, 2.77657844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.25221219e+05, 2.77657844e+05, ],
    'CountWeightedFull'                                                              : [ 2.99972656e+05, 2.99988500e+05, 3.00024094e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.25221219e+05, 2.99953062e+05, 2.77657844e+05, 3.25221219e+05, 2.99953062e+05, 2.77657844e+05, 3.25221219e+05, 2.99953062e+05, 2.77657844e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.25221219e+05, 2.77657844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93001812e+05, 2.93002281e+05, 2.93041750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93001812e+05, 2.91275938e+05, 2.94731250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.17600500e+05, 2.92989281e+05, 2.71234844e+05, 3.17600500e+05, 2.92989281e+05, 2.71234844e+05, 3.17600500e+05, 2.92989281e+05, 2.71234844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.17600500e+05, 2.71234844e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.93001812e+05, 2.93002281e+05, 2.93041750e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.93001812e+05, 2.91275938e+05, 2.94731250e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 3.17600500e+05, 2.92989281e+05, 2.71234844e+05, 3.17600500e+05, 2.92989281e+05, 2.71234844e+05, 3.17600500e+05, 2.92989281e+05, 2.71234844e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.17600500e+05, 2.71234844e+05, ],
  }),
  ("nof_tree_events",                 19063),
  ("nof_db_events",                   299997),
  ("fsize_local",                     103462684), # 103.46MB, avg file size 103.46MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_650_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 18182),
  ("nof_db_events",                   299998),
  ("fsize_local",                     100274082), # 100.27MB, avg file size 100.27MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_700_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 16861),
  ("nof_db_events",                   299999),
  ("fsize_local",                     94985924), # 94.99MB, avg file size 94.99MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_800_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 15569),
  ("nof_db_events",                   300000),
  ("fsize_local",                     88949568), # 88.95MB, avg file size 88.95MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_900_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 14457),
  ("nof_db_events",                   299469),
  ("fsize_local",                     83394718), # 83.39MB, avg file size 83.39MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_1000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 18015),
  ("nof_db_events",                   299998),
  ("fsize_local",                     72344261), # 72.34MB, avg file size 72.34MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_250_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 18703),
  ("nof_db_events",                   300000),
  ("fsize_local",                     75880407), # 75.88MB, avg file size 75.88MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_260_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 19035),
  ("nof_db_events",                   299231),
  ("fsize_local",                     78643114), # 78.64MB, avg file size 78.64MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_270_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 20639),
  ("nof_db_events",                   299998),
  ("fsize_local",                     88960249), # 88.96MB, avg file size 88.96MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_300_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 21347),
  ("nof_db_events",                   299402),
  ("fsize_local",                     98099822), # 98.10MB, avg file size 98.10MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_350_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 21587),
  ("nof_db_events",                   299993),
  ("fsize_local",                     104606756), # 104.61MB, avg file size 104.61MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_400_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 21077),
  ("nof_db_events",                   299998),
  ("fsize_local",                     107056983), # 107.06MB, avg file size 107.06MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_450_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 20781),
  ("nof_db_events",                   299999),
  ("fsize_local",                     109711677), # 109.71MB, avg file size 109.71MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_500_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 20023),
  ("nof_db_events",                   299995),
  ("fsize_local",                     108496645), # 108.50MB, avg file size 108.50MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_550_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 18949),
  ("nof_db_events",                   299995),
  ("fsize_local",                     104720015), # 104.72MB, avg file size 104.72MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_600_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 18154),
  ("nof_db_events",                   299997),
  ("fsize_local",                     102246631), # 102.25MB, avg file size 102.25MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_650_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 17341),
  ("nof_db_events",                   299995),
  ("fsize_local",                     98827486), # 98.83MB, avg file size 98.83MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_700_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 15857),
  ("nof_db_events",                   299998),
  ("fsize_local",                     91692717), # 91.69MB, avg file size 91.69MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_800_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 14627),
  ("nof_db_events",                   299999),
  ("fsize_local",                     85394912), # 85.39MB, avg file size 85.39MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_900_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 13417),
  ("nof_db_events",                   299997),
  ("fsize_local",                     78911455), # 78.91MB, avg file size 78.91MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_1000_hh_2b2v_sl"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 398999, ],
    'CountWeighted'                                                                  : [ 3.97651625e+05, 3.97671875e+05, 3.97656938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97651625e+05, 3.97651625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97660150e+06, 3.97660150e+06, 3.97660150e+06, 3.97660150e+06, 3.97660150e+06, 3.97660150e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99031906e+05, 3.98957406e+05, 5.99661250e+05, 3.98934406e+05, 3.96935125e+05, 2.19056266e+05, ],
    'CountWeightedFull'                                                              : [ 3.97476312e+05, 3.97494125e+05, 3.97480844e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97476312e+05, 3.97476312e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97483550e+06, 3.97483550e+06, 3.97483550e+06, 3.97483550e+06, 3.97483550e+06, 3.97483550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98855625e+05, 3.98780750e+05, 5.99396625e+05, 3.98756812e+05, 3.96760688e+05, 2.18959875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.84569438e+05, 3.84567750e+05, 3.84581188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.84569438e+05, 3.81239625e+05, 3.87898094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.84569438e+05, 3.84569438e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.84570800e+06, 3.84570800e+06, 3.84570800e+06, 3.84570800e+06, 3.84570800e+06, 3.84570800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.85934094e+05, 3.85617875e+05, 5.79828188e+05, 3.85742250e+05, 3.84186625e+05, 2.12019109e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.84400500e+05, 3.84397812e+05, 3.84411906e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.84400500e+05, 3.81072469e+05, 3.87727312e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.84400500e+05, 3.84400500e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.84401525e+06, 3.84401525e+06, 3.84401525e+06, 3.84401525e+06, 3.84401525e+06, 3.84401525e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.85765125e+05, 3.85448688e+05, 5.79574250e+05, 3.85572062e+05, 3.84019156e+05, 2.11926594e+05, ],
  }),
  ("nof_tree_events",                 29135),
  ("nof_db_events",                   398999),
  ("fsize_local",                     129758759), # 129.76MB, avg file size 129.76MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.98606781e+05, 3.98628406e+05, 3.98610625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.98606781e+05, 3.98606781e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.98617275e+06, 3.98617275e+06, 3.98617275e+06, 3.98617275e+06, 3.98617275e+06, 3.98617275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00087438e+05, 3.99754188e+05, 6.02205500e+05, 3.99850219e+05, 3.98716156e+05, 2.19123516e+05, ],
    'CountWeightedFull'                                                              : [ 3.98424969e+05, 3.98445281e+05, 3.98428250e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.98424969e+05, 3.98424969e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.98434225e+06, 3.98434225e+06, 3.98434225e+06, 3.98434225e+06, 3.98434225e+06, 3.98434225e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99904094e+05, 3.99570188e+05, 6.01929375e+05, 3.99666375e+05, 3.98534906e+05, 2.19023531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.83425156e+05, 3.83441562e+05, 3.83413375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.83425156e+05, 3.79606344e+05, 3.87251938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.83425156e+05, 3.83425156e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.83429075e+06, 3.83429075e+06, 3.83429075e+06, 3.83429075e+06, 3.83429075e+06, 3.83429075e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.84882969e+05, 3.84352000e+05, 5.79064812e+05, 3.84546031e+05, 3.83729406e+05, 2.10969875e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.83251312e+05, 3.83267062e+05, 3.83239250e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.83251312e+05, 3.79434375e+05, 3.87075812e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.83251312e+05, 3.83251312e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.83254850e+06, 3.83254850e+06, 3.83254850e+06, 3.83254850e+06, 3.83254850e+06, 3.83254850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.84708375e+05, 3.84176875e+05, 5.78801625e+05, 3.84370938e+05, 3.83556500e+05, 2.10874438e+05, ],
  }),
  ("nof_tree_events",                 27511),
  ("nof_db_events",                   399998),
  ("fsize_local",                     123035301), # 123.04MB, avg file size 123.04MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 395494, ],
    'CountWeighted'                                                                  : [ 3.94065688e+05, 3.94075875e+05, 3.94063250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94065688e+05, 3.94065688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94136175e+06, 3.94136175e+06, 3.94136175e+06, 3.94136175e+06, 3.94136175e+06, 3.94136175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95626625e+05, 3.95388062e+05, 5.99343000e+05, 3.95347312e+05, 3.93732812e+05, 2.13440000e+05, ],
    'CountWeightedFull'                                                              : [ 3.93872188e+05, 3.93882688e+05, 3.93871438e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.93872188e+05, 3.93872188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.93940250e+06, 3.93940250e+06, 3.93940250e+06, 3.93940250e+06, 3.93940250e+06, 3.93940250e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95437875e+05, 3.95199875e+05, 5.99053312e+05, 3.95158250e+05, 3.93541750e+05, 2.13339344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.75191375e+05, 3.75190312e+05, 3.75189375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.75191375e+05, 3.70609438e+05, 3.79792344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.75191375e+05, 3.75191375e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.75213625e+06, 3.75213625e+06, 3.75213625e+06, 3.75213625e+06, 3.75213625e+06, 3.75213625e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.76705250e+05, 3.76193250e+05, 5.70502062e+05, 3.76319594e+05, 3.75227438e+05, 2.03408656e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.75010250e+05, 3.75008812e+05, 3.75008938e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.75010250e+05, 3.70430906e+05, 3.79608250e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.75010250e+05, 3.75010250e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.75031400e+06, 3.75031400e+06, 3.75031400e+06, 3.75031400e+06, 3.75031400e+06, 3.75031400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.76527469e+05, 3.76016250e+05, 5.70229500e+05, 3.76141812e+05, 3.75047500e+05, 2.03313875e+05, ],
  }),
  ("nof_tree_events",                 27249),
  ("nof_db_events",                   395494),
  ("fsize_local",                     129447850), # 129.45MB, avg file size 129.45MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 398193, ],
    'CountWeighted'                                                                  : [ 3.95900938e+05, 3.95966250e+05, 3.95883438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95900938e+05, 3.95900938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95878350e+06, 3.95878350e+06, 3.95878350e+06, 3.95878350e+06, 3.95878350e+06, 3.95878350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.98323938e+05, 3.98286250e+05, 6.00835625e+05, 3.97998625e+05, 3.96097844e+05, 2.16490125e+05, ],
    'CountWeightedFull'                                                              : [ 3.95702438e+05, 3.95762844e+05, 3.95683938e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95702438e+05, 3.95702438e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95679700e+06, 3.95679700e+06, 3.95679700e+06, 3.95679700e+06, 3.95679700e+06, 3.95679700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98125406e+05, 3.98088125e+05, 6.00534125e+05, 3.97799250e+05, 3.95899219e+05, 2.16382844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.79365875e+05, 3.79383938e+05, 3.79364562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.79365875e+05, 3.75422938e+05, 3.83325562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.79365875e+05, 3.79365875e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.79355750e+06, 3.79355750e+06, 3.79355750e+06, 3.79355750e+06, 3.79355750e+06, 3.79355750e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.81715250e+05, 3.81461594e+05, 5.75600750e+05, 3.81303844e+05, 3.79865375e+05, 2.07651672e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.79177938e+05, 3.79194156e+05, 3.79176188e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.79177938e+05, 3.75237500e+05, 3.83135406e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.79177938e+05, 3.79177938e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.79168000e+06, 3.79168000e+06, 3.79168000e+06, 3.79168000e+06, 3.79168000e+06, 3.79168000e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.81526781e+05, 3.81273750e+05, 5.75314875e+05, 3.81115188e+05, 3.79676812e+05, 2.07549828e+05, ],
  }),
  ("nof_tree_events",                 22566),
  ("nof_db_events",                   398193),
  ("fsize_local",                     119484346), # 119.48MB, avg file size 119.48MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.97938094e+05, 3.97989000e+05, 3.97977250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97938094e+05, 3.97938094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97993425e+06, 3.97993425e+06, 3.97993425e+06, 3.97993425e+06, 3.97993425e+06, 3.97993425e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00060969e+05, 4.00606250e+05, 6.03050938e+05, 3.99899406e+05, 3.97167125e+05, 2.17715078e+05, ],
    'CountWeightedFull'                                                              : [ 3.97743125e+05, 3.97794625e+05, 3.97782750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97743125e+05, 3.97743125e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97799325e+06, 3.97799325e+06, 3.97799325e+06, 3.97799325e+06, 3.97799325e+06, 3.97799325e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99866031e+05, 4.00410000e+05, 6.02755312e+05, 3.99702906e+05, 3.96973656e+05, 2.17609641e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81969969e+05, 3.81987406e+05, 3.81983156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81969969e+05, 3.78113219e+05, 3.85842094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81969969e+05, 3.81969969e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81987600e+06, 3.81987600e+06, 3.81987600e+06, 3.81987600e+06, 3.81987600e+06, 3.81987600e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.83999094e+05, 3.84310531e+05, 5.78629188e+05, 3.83741000e+05, 3.81451250e+05, 2.09164594e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81784938e+05, 3.81802219e+05, 3.81798625e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81784938e+05, 3.77930438e+05, 3.85654562e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81784938e+05, 3.81784938e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81802900e+06, 3.81802900e+06, 3.81802900e+06, 3.81802900e+06, 3.81802900e+06, 3.81802900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.83813875e+05, 3.84124438e+05, 5.78348500e+05, 3.83554688e+05, 3.81267188e+05, 2.09064266e+05, ],
  }),
  ("nof_tree_events",                 24236),
  ("nof_db_events",                   399994),
  ("fsize_local",                     124571255), # 124.57MB, avg file size 124.57MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                                          : [ 399096, ],
    'CountWeighted'                                                                  : [ 3.97141719e+05, 3.97171094e+05, 3.97125312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97141719e+05, 3.97141719e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97136625e+06, 3.97136625e+06, 3.97136625e+06, 3.97136625e+06, 3.97136625e+06, 3.97136625e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99108281e+05, 3.99136031e+05, 6.00630688e+05, 3.99070500e+05, 3.96841781e+05, 2.18205688e+05, ],
    'CountWeightedFull'                                                              : [ 3.96954875e+05, 3.96982531e+05, 3.96938594e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96954875e+05, 3.96954875e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96949875e+06, 3.96949875e+06, 3.96949875e+06, 3.96949875e+06, 3.96949875e+06, 3.96949875e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98920125e+05, 3.98947438e+05, 6.00345062e+05, 3.98881562e+05, 3.96653969e+05, 2.18103625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81566750e+05, 3.81567375e+05, 3.81564094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81566750e+05, 3.77761031e+05, 3.85385406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81566750e+05, 3.81566750e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81563200e+06, 3.81563200e+06, 3.81563200e+06, 3.81563200e+06, 3.81563200e+06, 3.81563200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.83476438e+05, 3.83279156e+05, 5.76912000e+05, 3.83335312e+05, 3.81547969e+05, 2.09843328e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81388000e+05, 3.81388250e+05, 3.81385531e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81388000e+05, 3.77584719e+05, 3.85204469e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81388000e+05, 3.81388000e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81384750e+06, 3.81384750e+06, 3.81384750e+06, 3.81384750e+06, 3.81384750e+06, 3.81384750e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.83297344e+05, 3.83099656e+05, 5.76640312e+05, 3.83155406e+05, 3.81369000e+05, 2.09745938e+05, ],
  }),
  ("nof_tree_events",                 24993),
  ("nof_db_events",                   399096),
  ("fsize_local",                     123853595), # 123.85MB, avg file size 123.85MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2v_sl_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 399200, ],
    'CountWeighted'                                                                  : [ 3.99153438e+05, 3.99141062e+05, 3.99158000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99153438e+05, 3.99153438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99168150e+06, 3.99168150e+06, 3.99168150e+06, 3.99168150e+06, 3.99168150e+06, 3.99168150e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99116562e+05, 3.98877125e+05, 6.46680875e+05, 3.99323250e+05, 3.94030688e+05, 1.83652219e+05, ],
    'CountWeightedFull'                                                              : [ 3.99109938e+05, 3.99098219e+05, 3.99114312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99109938e+05, 3.99109938e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99125025e+06, 3.99125025e+06, 3.99125025e+06, 3.99125025e+06, 3.99125025e+06, 3.99125025e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99076312e+05, 3.98835938e+05, 6.46609875e+05, 3.99276469e+05, 3.93986500e+05, 1.83633031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.90983781e+05, 3.90970750e+05, 3.90987031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.90983781e+05, 3.88888750e+05, 3.93069062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.90983781e+05, 3.90983781e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.90989500e+06, 3.90989500e+06, 3.90989500e+06, 3.90989500e+06, 3.90989500e+06, 3.90989500e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.91313375e+05, 3.90616312e+05, 6.33344875e+05, 3.90686312e+05, 3.86137938e+05, 1.80012266e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.90941969e+05, 3.90929188e+05, 3.90945125e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.90941969e+05, 3.88847406e+05, 3.93027031e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.90941969e+05, 3.90941969e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.90948000e+06, 3.90948000e+06, 3.90948000e+06, 3.90948000e+06, 3.90948000e+06, 3.90948000e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.91274625e+05, 3.90576656e+05, 6.33276500e+05, 3.90641375e+05, 3.86095438e+05, 1.79993750e+05, ],
  }),
  ("nof_tree_events",                 67287),
  ("nof_db_events",                   399200),
  ("fsize_local",                     357262108), # 357.26MB, avg file size 357.26MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 395000, ],
    'CountWeighted'                                                                  : [ 3.94950688e+05, 3.94955625e+05, 3.94933062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94950688e+05, 3.94950688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94913725e+06, 3.94913725e+06, 3.94913725e+06, 3.94913725e+06, 3.94913725e+06, 3.94913725e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95156438e+05, 3.95237688e+05, 6.40830250e+05, 3.94816969e+05, 3.89340188e+05, 1.80847672e+05, ],
    'CountWeightedFull'                                                              : [ 3.94908562e+05, 3.94913062e+05, 3.94891312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.94908562e+05, 3.94908562e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.94872500e+06, 3.94872500e+06, 3.94872500e+06, 3.94872500e+06, 3.94872500e+06, 3.94872500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95117312e+05, 3.95197812e+05, 6.40759500e+05, 3.94771281e+05, 3.89295625e+05, 1.80829031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86742250e+05, 3.86734312e+05, 3.86745562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86742250e+05, 3.84639688e+05, 3.88838062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.86742250e+05, 3.86742250e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.86721550e+06, 3.86721550e+06, 3.86721550e+06, 3.86721550e+06, 3.86721550e+06, 3.86721550e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.87301500e+05, 3.86922656e+05, 6.27475562e+05, 3.86155250e+05, 3.81470562e+05, 1.77188156e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.86701594e+05, 3.86693531e+05, 3.86705188e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.86701594e+05, 3.84599500e+05, 3.88797188e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.86701594e+05, 3.86701594e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.86681350e+06, 3.86681350e+06, 3.86681350e+06, 3.86681350e+06, 3.86681350e+06, 3.86681350e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.87263656e+05, 3.86884250e+05, 6.27407375e+05, 3.86111125e+05, 3.81427562e+05, 1.77170156e+05, ],
  }),
  ("nof_tree_events",                 67625),
  ("nof_db_events",                   395000),
  ("fsize_local",                     363693766), # 363.69MB, avg file size 363.69MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 395700, ],
    'CountWeighted'                                                                  : [ 3.95613188e+05, 3.95619625e+05, 3.95612938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95613188e+05, 3.95613188e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95634100e+06, 3.95634100e+06, 3.95634100e+06, 3.95634100e+06, 3.95634100e+06, 3.95634100e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95740500e+05, 3.96221938e+05, 6.43525938e+05, 3.95708719e+05, 3.90266250e+05, 1.80465312e+05, ],
    'CountWeightedFull'                                                              : [ 3.95568875e+05, 3.95576219e+05, 3.95568375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95568875e+05, 3.95568875e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95589575e+06, 3.95589575e+06, 3.95589575e+06, 3.95589575e+06, 3.95589575e+06, 3.95589575e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95699625e+05, 3.96180438e+05, 6.43452625e+05, 3.95660688e+05, 3.90220000e+05, 1.80445797e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87235750e+05, 3.87233375e+05, 3.87238812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87235750e+05, 3.85097000e+05, 3.89373250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.87235750e+05, 3.87235750e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.87249200e+06, 3.87249200e+06, 3.87249200e+06, 3.87249200e+06, 3.87249200e+06, 3.87249200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.87710062e+05, 3.87680812e+05, 6.29769125e+05, 3.86851438e+05, 3.82191750e+05, 1.76750578e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.87193125e+05, 3.87191344e+05, 3.87196188e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.87193125e+05, 3.85054844e+05, 3.89330250e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.87193125e+05, 3.87193125e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.87206350e+06, 3.87206350e+06, 3.87206350e+06, 3.87206350e+06, 3.87206350e+06, 3.87206350e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.87670562e+05, 3.87640688e+05, 6.29698375e+05, 3.86805125e+05, 3.82146906e+05, 1.76731781e+05, ],
  }),
  ("nof_tree_events",                 69905),
  ("nof_db_events",                   395700),
  ("fsize_local",                     380623911), # 380.62MB, avg file size 380.62MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 396400, ],
    'CountWeighted'                                                                  : [ 3.96297812e+05, 3.96331000e+05, 3.96291156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96297812e+05, 3.96297812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96319700e+06, 3.96319700e+06, 3.96319700e+06, 3.96319700e+06, 3.96319700e+06, 3.96319700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96364812e+05, 3.96612438e+05, 6.45074625e+05, 3.96415375e+05, 3.91253500e+05, 1.80343719e+05, ],
    'CountWeightedFull'                                                              : [ 3.96253156e+05, 3.96285938e+05, 3.96246781e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96253156e+05, 3.96253156e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96274550e+06, 3.96274550e+06, 3.96274550e+06, 3.96274550e+06, 3.96274550e+06, 3.96274550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96322875e+05, 3.96569094e+05, 6.44999125e+05, 3.96366625e+05, 3.91206219e+05, 1.80323891e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87849500e+05, 3.87863500e+05, 3.87849062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87849500e+05, 3.85692344e+05, 3.90001562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.87849500e+05, 3.87849500e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.87861025e+06, 3.87861025e+06, 3.87861025e+06, 3.87861025e+06, 3.87861025e+06, 3.87861025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.88252812e+05, 3.88012375e+05, 6.31149562e+05, 3.87480000e+05, 3.83042438e+05, 1.76594375e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.87806281e+05, 3.87820156e+05, 3.87806062e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.87806281e+05, 3.85649562e+05, 3.89958000e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.87806281e+05, 3.87806281e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.87817775e+06, 3.87817775e+06, 3.87817775e+06, 3.87817775e+06, 3.87817775e+06, 3.87817775e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.88212375e+05, 3.87970781e+05, 6.31076812e+05, 3.87432969e+05, 3.82996938e+05, 1.76575156e+05, ],
  }),
  ("nof_tree_events",                 72710),
  ("nof_db_events",                   396400),
  ("fsize_local",                     400582944), # 400.58MB, avg file size 400.58MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99958469e+05, 2.99975281e+05, 2.99948781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99958469e+05, 2.99958469e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99982350e+06, 2.99982350e+06, 2.99982350e+06, 2.99982350e+06, 2.99982350e+06, 2.99982350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00055438e+05, 3.00166688e+05, 4.89148188e+05, 2.99982031e+05, 2.95856562e+05, 1.35547703e+05, ],
    'CountWeightedFull'                                                              : [ 2.99922312e+05, 2.99939219e+05, 2.99912688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99922312e+05, 2.99922312e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99946350e+06, 2.99946350e+06, 2.99946350e+06, 2.99946350e+06, 2.99946350e+06, 2.99946350e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00021688e+05, 3.00132031e+05, 4.89087188e+05, 2.99943281e+05, 2.95818250e+05, 1.35531938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93329375e+05, 2.93337062e+05, 2.93324156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93329375e+05, 2.91643781e+05, 2.95010688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93329375e+05, 2.93329375e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.93340550e+06, 2.93340550e+06, 2.93340550e+06, 2.93340550e+06, 2.93340550e+06, 2.93340550e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.93695906e+05, 2.93447000e+05, 4.78240438e+05, 2.92984875e+05, 2.89416656e+05, 1.32631188e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.93294656e+05, 2.93302469e+05, 2.93289469e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.93294656e+05, 2.91609312e+05, 2.94975594e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.93294656e+05, 2.93294656e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.93306025e+06, 2.93306025e+06, 2.93306025e+06, 2.93306025e+06, 2.93306025e+06, 2.93306025e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.93663469e+05, 2.93413750e+05, 4.78181719e+05, 2.92947562e+05, 2.89379844e+05, 1.32615969e+05, ],
  }),
  ("nof_tree_events",                 58934),
  ("nof_db_events",                   300000),
  ("fsize_local",                     332392733), # 332.39MB, avg file size 332.39MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299200, ],
    'CountWeighted'                                                                  : [ 2.99167688e+05, 2.99160312e+05, 2.99151344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99167688e+05, 2.99167688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99155525e+06, 2.99155525e+06, 2.99155525e+06, 2.99155525e+06, 2.99155400e+06, 2.99155400e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99338625e+05, 2.99148844e+05, 4.88454656e+05, 2.99016156e+05, 2.95277688e+05, 1.34737484e+05, ],
    'CountWeightedFull'                                                              : [ 2.99131906e+05, 2.99124562e+05, 2.99115969e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99131906e+05, 2.99131906e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99119925e+06, 2.99119925e+06, 2.99119925e+06, 2.99119925e+06, 2.99119800e+06, 2.99119800e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99305156e+05, 2.99114844e+05, 4.88395062e+05, 2.98977719e+05, 2.95240500e+05, 1.34721938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92394344e+05, 2.92387219e+05, 2.92389812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92394344e+05, 2.90682844e+05, 2.94104000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.92394344e+05, 2.92394344e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.92389175e+06, 2.92389175e+06, 2.92389175e+06, 2.92389175e+06, 2.92389050e+06, 2.92389050e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.92849250e+05, 2.92272219e+05, 4.77368469e+05, 2.91870250e+05, 2.88785094e+05, 1.31756734e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.92360000e+05, 2.92352875e+05, 2.92355562e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.92360000e+05, 2.90648969e+05, 2.94069312e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.92360000e+05, 2.92360000e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.92354975e+06, 2.92354975e+06, 2.92354975e+06, 2.92354975e+06, 2.92354850e+06, 2.92354850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.92817125e+05, 2.92239438e+05, 4.77310969e+05, 2.91833406e+05, 2.88749281e+05, 1.31741812e+05, ],
  }),
  ("nof_tree_events",                 62282),
  ("nof_db_events",                   299200),
  ("fsize_local",                     358879565), # 358.88MB, avg file size 358.88MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 298000, ],
    'CountWeighted'                                                                  : [ 2.97964594e+05, 2.97966875e+05, 2.97969219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.97964594e+05, 2.97964594e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.97968025e+06, 2.97968025e+06, 2.97968025e+06, 2.97968025e+06, 2.97968025e+06, 2.97968025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98120438e+05, 2.97761062e+05, 4.88112500e+05, 2.97819625e+05, 2.94498125e+05, 1.33026391e+05, ],
    'CountWeightedFull'                                                              : [ 2.97927469e+05, 2.97929750e+05, 2.97931875e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.97927469e+05, 2.97927469e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.97930575e+06, 2.97930575e+06, 2.97930575e+06, 2.97930575e+06, 2.97930575e+06, 2.97930575e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98085438e+05, 2.97724875e+05, 4.88050125e+05, 2.97779156e+05, 2.94459625e+05, 1.33010062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91029562e+05, 2.91026375e+05, 2.91033531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91029562e+05, 2.89282562e+05, 2.92772625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.91029562e+05, 2.91029562e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.91032725e+06, 2.91032725e+06, 2.91032725e+06, 2.91032725e+06, 2.91032725e+06, 2.91032725e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.91468312e+05, 2.90679531e+05, 4.76661906e+05, 2.90513969e+05, 2.87815812e+05, 1.30012000e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.90993781e+05, 2.90990500e+05, 2.90997750e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.90993781e+05, 2.89247125e+05, 2.92736531e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.90993781e+05, 2.90993781e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.90996650e+06, 2.90996650e+06, 2.90996650e+06, 2.90996650e+06, 2.90996650e+06, 2.90996650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.91434625e+05, 2.90644812e+05, 4.76601812e+05, 2.90475094e+05, 2.87778875e+05, 1.29996297e+05, ],
  }),
  ("nof_tree_events",                 67778),
  ("nof_db_events",                   298000),
  ("fsize_local",                     400649861), # 400.65MB, avg file size 400.65MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 298400, ],
    'CountWeighted'                                                                  : [ 2.98328062e+05, 2.98320812e+05, 2.98313219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98328062e+05, 2.98328062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98313850e+06, 2.98313850e+06, 2.98313850e+06, 2.98313850e+06, 2.98313850e+06, 2.98313850e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98147812e+05, 2.98057156e+05, 4.89610531e+05, 2.98749438e+05, 2.93934156e+05, 1.31910188e+05, ],
    'CountWeightedFull'                                                              : [ 2.98288344e+05, 2.98281125e+05, 2.98273625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98288344e+05, 2.98288344e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98274275e+06, 2.98274275e+06, 2.98274275e+06, 2.98274275e+06, 2.98274275e+06, 2.98274275e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98110344e+05, 2.98018719e+05, 4.89544125e+05, 2.98706500e+05, 2.93893812e+05, 1.31893094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91132938e+05, 2.91118031e+05, 2.91130344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91132938e+05, 2.89331500e+05, 2.92931594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.91132938e+05, 2.91132938e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.91125075e+06, 2.91125075e+06, 2.91125075e+06, 2.91125075e+06, 2.91125075e+06, 2.91125075e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.91246094e+05, 2.90781031e+05, 4.77787156e+05, 2.91161219e+05, 2.87013625e+05, 1.28783375e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.91094688e+05, 2.91079781e+05, 2.91092344e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.91094688e+05, 2.89293688e+05, 2.92893000e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.91094688e+05, 2.91094688e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.91086950e+06, 2.91086950e+06, 2.91086950e+06, 2.91086950e+06, 2.91086950e+06, 2.91086950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.91210125e+05, 2.90744250e+05, 4.77723531e+05, 2.91120062e+05, 2.86974969e+05, 1.28766984e+05, ],
  }),
  ("nof_tree_events",                 75470),
  ("nof_db_events",                   298400),
  ("fsize_local",                     461773864), # 461.77MB, avg file size 461.77MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 298400, ],
    'CountWeighted'                                                                  : [ 2.98346000e+05, 2.98329750e+05, 2.98260750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98346000e+05, 2.98346000e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98365425e+06, 2.98365425e+06, 2.98365425e+06, 2.98365425e+06, 2.98365425e+06, 2.98365425e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98457312e+05, 2.98590500e+05, 4.91953125e+05, 2.98349438e+05, 2.94009969e+05, 1.30501516e+05, ],
    'CountWeightedFull'                                                              : [ 2.98304281e+05, 2.98288656e+05, 2.98220438e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98304281e+05, 2.98304281e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98323025e+06, 2.98323025e+06, 2.98323025e+06, 2.98323025e+06, 2.98323025e+06, 2.98323025e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98418156e+05, 2.98550062e+05, 4.91883312e+05, 2.98304656e+05, 2.93967562e+05, 1.30483766e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90963688e+05, 2.90946469e+05, 2.90926875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90963688e+05, 2.89121688e+05, 2.92805344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.90963688e+05, 2.90963688e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.90973850e+06, 2.90973850e+06, 2.90973850e+06, 2.90973850e+06, 2.90973850e+06, 2.90973850e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.91369438e+05, 2.91050062e+05, 4.79742125e+05, 2.90584250e+05, 2.86939375e+05, 1.27334992e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.90923625e+05, 2.90906750e+05, 2.90887375e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.90923625e+05, 2.89082094e+05, 2.92765000e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.90923625e+05, 2.90923625e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.90933500e+06, 2.90933500e+06, 2.90933500e+06, 2.90933500e+06, 2.90933500e+06, 2.90933500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.91331844e+05, 2.91011250e+05, 4.79675062e+05, 2.90541312e+05, 2.86898406e+05, 1.27317945e+05, ],
  }),
  ("nof_tree_events",                 82154),
  ("nof_db_events",                   298400),
  ("fsize_local",                     517433119), # 517.43MB, avg file size 517.43MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99946531e+05, 2.99962438e+05, 3.00006281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99946531e+05, 2.99946531e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99932525e+06, 2.99932525e+06, 2.99932525e+06, 2.99932525e+06, 2.99932525e+06, 2.99932525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00056781e+05, 3.00089344e+05, 4.94773188e+05, 2.99977688e+05, 2.94463375e+05, 1.30089281e+05, ],
    'CountWeightedFull'                                                              : [ 2.99903625e+05, 2.99918688e+05, 2.99962188e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99903625e+05, 2.99903625e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99890100e+06, 2.99890100e+06, 2.99890100e+06, 2.99890100e+06, 2.99890100e+06, 2.99890100e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.00016344e+05, 3.00047812e+05, 4.94700625e+05, 2.99931281e+05, 2.94419031e+05, 1.30070852e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92368625e+05, 2.92366469e+05, 2.92407438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92368625e+05, 2.90482875e+05, 2.94256188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.92368625e+05, 2.92368625e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.92361175e+06, 2.92361175e+06, 2.92361175e+06, 2.92361175e+06, 2.92361175e+06, 2.92361175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.92775000e+05, 2.92401500e+05, 4.82243375e+05, 2.92008000e+05, 2.87187125e+05, 1.26852414e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.92327438e+05, 2.92324812e+05, 2.92365812e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.92327438e+05, 2.90442125e+05, 2.94214562e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.92327438e+05, 2.92327438e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.92320150e+06, 2.92320150e+06, 2.92320150e+06, 2.92320150e+06, 2.92320150e+06, 2.92320150e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.92736219e+05, 2.92361688e+05, 4.82173875e+05, 2.91963594e+05, 2.87144531e+05, 1.26834672e+05, ],
  }),
  ("nof_tree_events",                 87898),
  ("nof_db_events",                   300000),
  ("fsize_local",                     567186286), # 567.19MB, avg file size 567.19MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 299300, ],
    'CountWeighted'                                                                  : [ 2.99209969e+05, 2.99252688e+05, 2.99242656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99209969e+05, 2.99209969e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99232300e+06, 2.99232300e+06, 2.99232300e+06, 2.99232300e+06, 2.99232300e+06, 2.99232300e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99428688e+05, 2.99103688e+05, 4.94978156e+05, 2.99128500e+05, 2.94362062e+05, 1.28983828e+05, ],
    'CountWeightedFull'                                                              : [ 2.99166531e+05, 2.99208938e+05, 2.99199594e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.99166531e+05, 2.99166531e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.99188850e+06, 2.99188850e+06, 2.99188850e+06, 2.99188850e+06, 2.99188850e+06, 2.99188850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99387750e+05, 2.99061531e+05, 4.94905750e+05, 2.99081750e+05, 2.94318500e+05, 1.28965430e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91524312e+05, 2.91544719e+05, 2.91544125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91524312e+05, 2.89613938e+05, 2.93433750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.91524312e+05, 2.91524312e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.91537100e+06, 2.91537100e+06, 2.91537100e+06, 2.91537100e+06, 2.91537100e+06, 2.91537100e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.92035250e+05, 2.91312531e+05, 4.82225531e+05, 2.91022625e+05, 2.86943812e+05, 1.25709688e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.91482719e+05, 2.91502812e+05, 2.91502625e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.91482719e+05, 2.89572812e+05, 2.93391594e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.91482719e+05, 2.91482719e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.91495450e+06, 2.91495450e+06, 2.91495450e+06, 2.91495450e+06, 2.91495450e+06, 2.91495450e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.91995969e+05, 2.91272125e+05, 4.82156500e+05, 2.90977812e+05, 2.86902094e+05, 1.25692055e+05, ],
  }),
  ("nof_tree_events",                 91968),
  ("nof_db_events",                   299300),
  ("fsize_local",                     604921490), # 604.92MB, avg file size 604.92MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 64151),
  ("nof_db_events",                   200000),
  ("fsize_local",                     429258295), # 429.26MB, avg file size 429.26MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 66531),
  ("nof_db_events",                   200000),
  ("fsize_local",                     451454158), # 451.45MB, avg file size 451.45MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 68420),
  ("nof_db_events",                   200000),
  ("fsize_local",                     469046119), # 469.05MB, avg file size 469.05MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 69808),
  ("nof_db_events",                   200000),
  ("fsize_local",                     482665375), # 482.67MB, avg file size 482.67MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 70855),
  ("nof_db_events",                   199300),
  ("fsize_local",                     493418448), # 493.42MB, avg file size 493.42MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 71125),
  ("nof_db_events",                   199400),
  ("fsize_local",                     498671544), # 498.67MB, avg file size 498.67MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 72290),
  ("nof_db_events",                   199600),
  ("fsize_local",                     509722918), # 509.72MB, avg file size 509.72MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 36201),
  ("nof_db_events",                   100000),
  ("fsize_local",                     258916832), # 258.92MB, avg file size 258.92MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 33904),
  ("nof_db_events",                   100000),
  ("fsize_local",                     245246826), # 245.25MB, avg file size 245.25MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 29786),
  ("nof_db_events",                   99700),
  ("fsize_local",                     217110357), # 217.11MB, avg file size 217.11MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 25394),
  ("nof_db_events",                   99500),
  ("fsize_local",                     186072512), # 186.07MB, avg file size 186.07MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 21649),
  ("nof_db_events",                   99600),
  ("fsize_local",                     159748937), # 159.75MB, avg file size 159.75MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 14084),
  ("nof_db_events",                   99600),
  ("fsize_local",                     103982408), # 103.98MB, avg file size 103.98MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin0_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 399300, ],
    'CountWeighted'                                                                  : [ 3.97513375e+05, 3.97584875e+05, 3.97620500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97513375e+05, 3.97513375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97627475e+06, 3.97627475e+06, 3.97627475e+06, 3.97627475e+06, 3.97627475e+06, 3.97627475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99200375e+05, 3.99161312e+05, 6.10473000e+05, 3.99439750e+05, 3.96856719e+05, 2.10797812e+05, ],
    'CountWeightedFull'                                                              : [ 3.97323844e+05, 3.97389625e+05, 3.97425375e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97323844e+05, 3.97323844e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97431950e+06, 3.97431950e+06, 3.97431950e+06, 3.97431950e+06, 3.97431950e+06, 3.97431950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99005938e+05, 3.98966156e+05, 6.10171438e+05, 3.99243500e+05, 3.96661688e+05, 2.10696453e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.79038250e+05, 3.79058375e+05, 3.79092938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.79038250e+05, 3.74757438e+05, 3.83346875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.79038250e+05, 3.79038250e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.79090350e+06, 3.79090350e+06, 3.79090350e+06, 3.79090350e+06, 3.79090350e+06, 3.79090350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.80643031e+05, 3.80349688e+05, 5.82072125e+05, 3.80651719e+05, 3.78598062e+05, 2.00954625e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.78856750e+05, 3.78874625e+05, 3.78909062e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.78856750e+05, 3.74578344e+05, 3.83162875e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.78856750e+05, 3.78856750e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.78906200e+06, 3.78906200e+06, 3.78906200e+06, 3.78906200e+06, 3.78906200e+06, 3.78906200e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.80459656e+05, 3.80165594e+05, 5.81787438e+05, 3.80466812e+05, 3.78413812e+05, 2.00859062e+05, ],
  }),
  ("nof_tree_events",                 49317),
  ("nof_db_events",                   399300),
  ("fsize_local",                     265564184), # 265.56MB, avg file size 265.56MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 399000, ],
    'CountWeighted'                                                                  : [ 3.97775062e+05, 3.97749812e+05, 3.97719000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97775062e+05, 3.97775062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97740025e+06, 3.97740025e+06, 3.97740025e+06, 3.97740025e+06, 3.97740025e+06, 3.97740025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99053938e+05, 3.98727406e+05, 6.00791875e+05, 3.98936125e+05, 3.97259688e+05, 2.18876188e+05, ],
    'CountWeightedFull'                                                              : [ 3.97616000e+05, 3.97590250e+05, 3.97561125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97616000e+05, 3.97616000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97581500e+06, 3.97581500e+06, 3.97581500e+06, 3.97581500e+06, 3.97581500e+06, 3.97581500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98894000e+05, 3.98567188e+05, 6.00549375e+05, 3.98775000e+05, 3.97100188e+05, 2.18789453e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81472625e+05, 3.81441406e+05, 3.81460438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81472625e+05, 3.77571625e+05, 3.85386250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81472625e+05, 3.81472625e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81454825e+06, 3.81454825e+06, 3.81454825e+06, 3.81454825e+06, 3.81454825e+06, 3.81454825e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.82757312e+05, 3.82284719e+05, 5.76045750e+05, 3.82467188e+05, 3.81103438e+05, 2.10023438e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81321094e+05, 3.81290125e+05, 3.81309656e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81321094e+05, 3.77422188e+05, 3.85232812e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81321094e+05, 3.81321094e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81303550e+06, 3.81303550e+06, 3.81303550e+06, 3.81303550e+06, 3.81303550e+06, 3.81303550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.82605938e+05, 3.82133125e+05, 5.75815688e+05, 3.82314375e+05, 3.80952406e+05, 2.09941312e+05, ],
  }),
  ("nof_tree_events",                 62393),
  ("nof_db_events",                   399000),
  ("fsize_local",                     302145476), # 302.15MB, avg file size 302.15MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 399100, ],
    'CountWeighted'                                                                  : [ 3.97803750e+05, 3.97836094e+05, 3.97781062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97803750e+05, 3.97803750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97778925e+06, 3.97778925e+06, 3.97778925e+06, 3.97778925e+06, 3.97778925e+06, 3.97778925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99000938e+05, 3.99067375e+05, 6.01369500e+05, 3.99218750e+05, 3.97602469e+05, 2.18766875e+05, ],
    'CountWeightedFull'                                                              : [ 3.97645625e+05, 3.97675688e+05, 3.97619688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97645625e+05, 3.97645625e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97621850e+06, 3.97621850e+06, 3.97621850e+06, 3.97621850e+06, 3.97621850e+06, 3.97621850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98842375e+05, 3.98909125e+05, 6.01127250e+05, 3.99058531e+05, 3.97442094e+05, 2.18681188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81536344e+05, 3.81530250e+05, 3.81540062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81536344e+05, 3.77642875e+05, 3.85445062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81536344e+05, 3.81536344e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81526150e+06, 3.81526150e+06, 3.81526150e+06, 3.81526150e+06, 3.81526150e+06, 3.81526150e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.82719781e+05, 3.82496875e+05, 5.76686500e+05, 3.82753438e+05, 3.81661000e+05, 2.09950312e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81386188e+05, 3.81379188e+05, 3.81389031e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81386188e+05, 3.77494625e+05, 3.85292812e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81386188e+05, 3.81386188e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81376475e+06, 3.81376475e+06, 3.81376475e+06, 3.81376475e+06, 3.81376475e+06, 3.81376475e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.82569688e+05, 3.82347250e+05, 5.76457125e+05, 3.82602000e+05, 3.81509094e+05, 2.09869219e+05, ],
  }),
  ("nof_tree_events",                 65832),
  ("nof_db_events",                   399100),
  ("fsize_local",                     319697910), # 319.70MB, avg file size 319.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 399200, ],
    'CountWeighted'                                                                  : [ 3.97924625e+05, 3.97876875e+05, 3.97874375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97924625e+05, 3.97924625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97831100e+06, 3.97831100e+06, 3.97831100e+06, 3.97831100e+06, 3.97831100e+06, 3.97831100e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99346250e+05, 3.99065344e+05, 6.00973312e+05, 3.99033469e+05, 3.97589625e+05, 2.19157953e+05, ],
    'CountWeightedFull'                                                              : [ 3.97766250e+05, 3.97717188e+05, 3.97715969e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.97766250e+05, 3.97766250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.97673125e+06, 3.97673125e+06, 3.97673125e+06, 3.97673125e+06, 3.97673125e+06, 3.97673125e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99187719e+05, 3.98906875e+05, 6.00730375e+05, 3.98873438e+05, 3.97429000e+05, 2.19072188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81435781e+05, 3.81399781e+05, 3.81433938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81435781e+05, 3.77493031e+05, 3.85394250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81435781e+05, 3.81435781e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.81400100e+06, 3.81400100e+06, 3.81400100e+06, 3.81400100e+06, 3.81400100e+06, 3.81400100e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.82848500e+05, 3.82345688e+05, 5.75947188e+05, 3.82376875e+05, 3.81330625e+05, 2.10218062e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.81285625e+05, 3.81249125e+05, 3.81283781e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.81285625e+05, 3.77344938e+05, 3.85242125e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.81285625e+05, 3.81285625e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.81249975e+06, 3.81249975e+06, 3.81249975e+06, 3.81249975e+06, 3.81249975e+06, 3.81249975e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.82698500e+05, 3.82195438e+05, 5.75717000e+05, 3.82225375e+05, 3.81178875e+05, 2.10136797e+05, ],
  }),
  ("nof_tree_events",                 68952),
  ("nof_db_events",                   399200),
  ("fsize_local",                     336691204), # 336.69MB, avg file size 336.69MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.98974375e+05, 2.98946688e+05, 2.98993031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98974375e+05, 2.98974375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98977850e+06, 2.98977850e+06, 2.98977850e+06, 2.98977850e+06, 2.98977850e+06, 2.98977850e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99913312e+05, 3.00239125e+05, 4.51423500e+05, 3.00116281e+05, 2.98696812e+05, 1.65132516e+05, ],
    'CountWeightedFull'                                                              : [ 2.98859344e+05, 2.98833281e+05, 2.98874594e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98859344e+05, 2.98859344e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98862175e+06, 2.98862175e+06, 2.98862175e+06, 2.98862175e+06, 2.98862175e+06, 2.98862175e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99797125e+05, 3.00123312e+05, 4.51246969e+05, 2.99998438e+05, 2.98580344e+05, 1.65069062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.86600719e+05, 2.86574625e+05, 2.86616750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.86600719e+05, 2.83630250e+05, 2.89583406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.86600719e+05, 2.86600719e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.86600225e+06, 2.86600225e+06, 2.86600225e+06, 2.86600225e+06, 2.86600225e+06, 2.86600225e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.87522500e+05, 2.87649312e+05, 4.32560562e+05, 2.87571000e+05, 2.86435281e+05, 1.58388984e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.86490875e+05, 2.86465281e+05, 2.86505719e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.86490875e+05, 2.83521812e+05, 2.89471844e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.86490875e+05, 2.86490875e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.86490250e+06, 2.86490250e+06, 2.86490250e+06, 2.86490250e+06, 2.86490250e+06, 2.86490250e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.87412375e+05, 2.87539594e+05, 4.32393656e+05, 2.87459688e+05, 2.86324781e+05, 1.58328812e+05, ],
  }),
  ("nof_tree_events",                 57381),
  ("nof_db_events",                   300000),
  ("fsize_local",                     282157225), # 282.16MB, avg file size 282.16MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299000, ],
    'CountWeighted'                                                                  : [ 2.98041750e+05, 2.98033688e+05, 2.98040312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98041750e+05, 2.98041750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98022350e+06, 2.98022350e+06, 2.98022350e+06, 2.98022350e+06, 2.98022350e+06, 2.98022350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98962219e+05, 2.99271375e+05, 4.49780000e+05, 2.99059344e+05, 2.97960688e+05, 1.64797062e+05, ],
    'CountWeightedFull'                                                              : [ 2.97924406e+05, 2.97917688e+05, 2.97923719e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.97924406e+05, 2.97924406e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.97906000e+06, 2.97906000e+06, 2.97906000e+06, 2.97906000e+06, 2.97906000e+06, 2.97906000e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98844938e+05, 2.99153250e+05, 4.49602250e+05, 2.98941281e+05, 2.97844562e+05, 1.64733219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.85711438e+05, 2.85688219e+05, 2.85730438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.85711438e+05, 2.82747188e+05, 2.88687812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.85711438e+05, 2.85711438e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.85704525e+06, 2.85704525e+06, 2.85704525e+06, 2.85704525e+06, 2.85704525e+06, 2.85704525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.86608125e+05, 2.86748438e+05, 4.31072875e+05, 2.86605125e+05, 2.85795781e+05, 1.58079375e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.85600375e+05, 2.85577812e+05, 2.85619906e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.85600375e+05, 2.82637906e+05, 2.88575406e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.85600375e+05, 2.85600375e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.85594250e+06, 2.85594250e+06, 2.85594250e+06, 2.85594250e+06, 2.85594250e+06, 2.85594250e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.86497375e+05, 2.86637094e+05, 4.30905219e+05, 2.86493594e+05, 2.85686062e+05, 1.58019062e+05, ],
  }),
  ("nof_tree_events",                 61502),
  ("nof_db_events",                   299000),
  ("fsize_local",                     304013077), # 304.01MB, avg file size 304.01MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99005406e+05, 2.99071062e+05, 2.99067406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99005406e+05, 2.99005406e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99042550e+06, 2.99042550e+06, 2.99042550e+06, 2.99042550e+06, 2.99042550e+06, 2.99042550e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99938688e+05, 3.00066156e+05, 4.50259875e+05, 3.00094500e+05, 2.98814469e+05, 1.66018469e+05, ],
    'CountWeightedFull'                                                              : [ 2.98890875e+05, 2.98955562e+05, 2.98949812e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98890875e+05, 2.98890875e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98927350e+06, 2.98927350e+06, 2.98927350e+06, 2.98927350e+06, 2.98927350e+06, 2.98927350e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99822812e+05, 2.99949781e+05, 4.50086062e+05, 2.99978312e+05, 2.98700625e+05, 1.65955062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.86601812e+05, 2.86613375e+05, 2.86635625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.86601812e+05, 2.83608938e+05, 2.89609656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.86601812e+05, 2.86601812e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.86614525e+06, 2.86614525e+06, 2.86614525e+06, 2.86614525e+06, 2.86614525e+06, 2.86614525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.87503312e+05, 2.87476438e+05, 4.31316531e+05, 2.87495688e+05, 2.86417500e+05, 1.59215828e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.86492750e+05, 2.86504156e+05, 2.86525188e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.86492750e+05, 2.83501469e+05, 2.89498969e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.86492750e+05, 2.86492750e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.86505275e+06, 2.86505275e+06, 2.86505275e+06, 2.86505275e+06, 2.86505275e+06, 2.86505275e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.87393562e+05, 2.87366375e+05, 4.31151906e+05, 2.87385594e+05, 2.86309625e+05, 1.59155688e+05, ],
  }),
  ("nof_tree_events",                 66633),
  ("nof_db_events",                   300000),
  ("fsize_local",                     331234562), # 331.23MB, avg file size 331.23MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.98878500e+05, 2.98892500e+05, 2.98921344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.98878500e+05, 2.98878500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98911350e+06, 2.98911350e+06, 2.98911350e+06, 2.98911350e+06, 2.98911350e+06, 2.98911350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00022031e+05, 3.00494375e+05, 4.48917281e+05, 2.99960594e+05, 2.97712375e+05, 1.66478500e+05, ],
    'CountWeightedFull'                                                              : [ 2.98763188e+05, 2.98777156e+05, 2.98804531e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.98763188e+05, 2.98763188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.98795575e+06, 2.98795575e+06, 2.98795575e+06, 2.98795575e+06, 2.98795575e+06, 2.98795575e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.99906000e+05, 3.00378688e+05, 4.48741562e+05, 2.99843281e+05, 2.97595406e+05, 1.66414844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.86213094e+05, 2.86222938e+05, 2.86227344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.86213094e+05, 2.83160719e+05, 2.89281938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.86213094e+05, 2.86213094e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.86226800e+06, 2.86226800e+06, 2.86226800e+06, 2.86226800e+06, 2.86226800e+06, 2.86226800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.87305625e+05, 2.87565406e+05, 4.29676000e+05, 2.87133344e+05, 2.85202688e+05, 1.59534656e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.86103469e+05, 2.86113344e+05, 2.86117156e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.86103469e+05, 2.83052469e+05, 2.89170594e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.86103469e+05, 2.86103469e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.86116950e+06, 2.86116950e+06, 2.86116950e+06, 2.86116950e+06, 2.86116950e+06, 2.86116950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.87195938e+05, 2.87455969e+05, 4.29509688e+05, 2.87022406e+05, 2.85092094e+05, 1.59474297e+05, ],
  }),
  ("nof_tree_events",                 72772),
  ("nof_db_events",                   300000),
  ("fsize_local",                     365404455), # 365.40MB, avg file size 365.40MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 295800, ],
    'CountWeighted'                                                                  : [ 2.94629250e+05, 2.94629531e+05, 2.94591938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.94629250e+05, 2.94629250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.94661750e+06, 2.94661750e+06, 2.94661750e+06, 2.94661750e+06, 2.94661750e+06, 2.94661750e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.95741375e+05, 2.96115469e+05, 4.41608875e+05, 2.95877562e+05, 2.93459969e+05, 1.64825391e+05, ],
    'CountWeightedFull'                                                              : [ 2.94517000e+05, 2.94519031e+05, 2.94482125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.94517000e+05, 2.94517000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.94549325e+06, 2.94549325e+06, 2.94549325e+06, 2.94549325e+06, 2.94549325e+06, 2.94549325e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.95629750e+05, 2.96003906e+05, 4.41439250e+05, 2.95764938e+05, 2.93346844e+05, 1.64764078e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.81958688e+05, 2.81945312e+05, 2.81960094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.81958688e+05, 2.78900062e+05, 2.85028375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.81958688e+05, 2.81958688e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.81971650e+06, 2.81971650e+06, 2.81971650e+06, 2.81971650e+06, 2.81971650e+06, 2.81971650e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.83040875e+05, 2.83245125e+05, 4.22481094e+05, 2.83066969e+05, 2.80969812e+05, 1.57851406e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.81853312e+05, 2.81840344e+05, 2.81855469e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.81853312e+05, 2.78796219e+05, 2.84921594e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.81853312e+05, 2.81853312e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.81866075e+06, 2.81866075e+06, 2.81866075e+06, 2.81866075e+06, 2.81866075e+06, 2.81866075e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.82935625e+05, 2.83140062e+05, 4.22321125e+05, 2.82960844e+05, 2.80863250e+05, 1.57793484e+05, ],
  }),
  ("nof_tree_events",                 76055),
  ("nof_db_events",                   295800),
  ("fsize_local",                     384026500), # 384.03MB, avg file size 384.03MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299100, ],
    'CountWeighted'                                                                  : [ 2.97948219e+05, 2.97923469e+05, 2.97931031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.97948219e+05, 2.97948219e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.97943075e+06, 2.97943075e+06, 2.97943075e+06, 2.97943075e+06, 2.97943075e+06, 2.97943075e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98984281e+05, 2.99165531e+05, 4.46855250e+05, 2.99249781e+05, 2.97621375e+05, 1.66935938e+05, ],
    'CountWeightedFull'                                                              : [ 2.97834750e+05, 2.97810125e+05, 2.97817875e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 2.97834750e+05, 2.97834750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.97829600e+06, 2.97829600e+06, 2.97829600e+06, 2.97829600e+06, 2.97829600e+06, 2.97829600e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 2.98870500e+05, 2.99051562e+05, 4.46683875e+05, 2.99135594e+05, 2.97508250e+05, 1.66873391e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.84815156e+05, 2.84800656e+05, 2.84820312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.84815156e+05, 2.81657562e+05, 2.87989625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.84815156e+05, 2.84815156e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.84813825e+06, 2.84813825e+06, 2.84813825e+06, 2.84813825e+06, 2.84813825e+06, 2.84813825e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.85840531e+05, 2.85846875e+05, 4.27016844e+05, 2.85981344e+05, 2.84649594e+05, 1.59703828e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.84707625e+05, 2.84693094e+05, 2.84712812e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.84707625e+05, 2.81551594e+05, 2.87880500e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 2.84707625e+05, 2.84707625e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.84706450e+06, 2.84706450e+06, 2.84706450e+06, 2.84706450e+06, 2.84706450e+06, 2.84706450e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 2.85732969e+05, 2.85738938e+05, 4.26854594e+05, 2.85873438e+05, 2.84542469e+05, 1.59644750e+05, ],
  }),
  ("nof_tree_events",                 80347),
  ("nof_db_events",                   299100),
  ("fsize_local",                     409737382), # 409.74MB, avg file size 409.74MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 57437),
  ("nof_db_events",                   200000),
  ("fsize_local",                     297842608), # 297.84MB, avg file size 297.84MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 58638),
  ("nof_db_events",                   197300),
  ("fsize_local",                     305793531), # 305.79MB, avg file size 305.79MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 60684),
  ("nof_db_events",                   200000),
  ("fsize_local",                     317908107), # 317.91MB, avg file size 317.91MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 61972),
  ("nof_db_events",                   198000),
  ("fsize_local",                     325836965), # 325.84MB, avg file size 325.84MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 64310),
  ("nof_db_events",                   197200),
  ("fsize_local",                     339662836), # 339.66MB, avg file size 339.66MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 65713),
  ("nof_db_events",                   199100),
  ("fsize_local",                     347981735), # 347.98MB, avg file size 347.98MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 33843),
  ("nof_db_events",                   99200),
  ("fsize_local",                     180452578), # 180.45MB, avg file size 180.45MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 33986),
  ("nof_db_events",                   100000),
  ("fsize_local",                     180884115), # 180.88MB, avg file size 180.88MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_1200_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 25853),
  ("nof_db_events",                   100000),
  ("fsize_local",                     135025461), # 135.03MB, avg file size 135.03MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 22931),
  ("nof_db_events",                   99300),
  ("fsize_local",                     119725194), # 119.73MB, avg file size 119.73MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_spin2_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 8467),
  ("nof_db_events",                   50000),
  ("fsize_local",                     34346359), # 34.35MB, avg file size 34.35MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 8353),
  ("nof_db_events",                   50000),
  ("fsize_local",                     34290497), # 34.29MB, avg file size 34.29MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 8590),
  ("nof_db_events",                   50000),
  ("fsize_local",                     35761018), # 35.76MB, avg file size 35.76MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 8703),
  ("nof_db_events",                   49600),
  ("fsize_local",                     36762054), # 36.76MB, avg file size 36.76MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 83877),
  ("nof_db_events",                   450000),
  ("fsize_local",                     348097622), # 348.10MB, avg file size 348.10MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 9722),
  ("nof_db_events",                   50000),
  ("fsize_local",                     42731840), # 42.73MB, avg file size 42.73MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 9904),
  ("nof_db_events",                   48000),
  ("fsize_local",                     44356566), # 44.36MB, avg file size 44.36MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 10597),
  ("nof_db_events",                   50000),
  ("fsize_local",                     47767263), # 47.77MB, avg file size 47.77MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 59842),
  ("nof_db_events",                   250000),
  ("fsize_local",                     274426579), # 274.43MB, avg file size 274.43MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 26234),
  ("nof_db_events",                   99600),
  ("fsize_local",                     125540215), # 125.54MB, avg file size 125.54MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 28395),
  ("nof_db_events",                   99200),
  ("fsize_local",                     139782254), # 139.78MB, avg file size 139.78MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 30589),
  ("nof_db_events",                   100000),
  ("fsize_local",                     155406080), # 155.41MB, avg file size 155.41MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 31942),
  ("nof_db_events",                   100000),
  ("fsize_local",                     165146669), # 165.15MB, avg file size 165.15MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 33651),
  ("nof_db_events",                   100000),
  ("fsize_local",                     176881987), # 176.88MB, avg file size 176.88MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 68249),
  ("nof_db_events",                   199000),
  ("fsize_local",                     344914018), # 344.91MB, avg file size 344.91MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 70470),
  ("nof_db_events",                   198200),
  ("fsize_local",                     359405309), # 359.41MB, avg file size 359.41MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 37653),
  ("nof_db_events",                   100000),
  ("fsize_local",                     204474900), # 204.47MB, avg file size 204.47MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 199100, ],
    'CountWeighted'                                                                  : [ 1.99060688e+05, 1.99043297e+05, 1.99053578e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99060688e+05, 1.99060688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.34727672e+05, 1.34888703e+05, 2.08639219e+05, 1.34684453e+05, 1.33894578e+05, 7.03756719e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99112969e+05, 1.99347406e+05, 3.07748875e+05, 1.99049391e+05, 1.97293203e+05, 1.04014961e+05, ],
    'CountWeightedFull'                                                              : [ 1.99039422e+05, 1.99022234e+05, 1.99032500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.99039422e+05, 1.99039422e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.34714422e+05, 1.34874578e+05, 2.08616688e+05, 1.34668766e+05, 1.33880062e+05, 7.03683203e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99093406e+05, 1.99326609e+05, 3.07715781e+05, 1.99026156e+05, 1.97271922e+05, 1.04004117e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93788375e+05, 1.93773469e+05, 1.93786484e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93788375e+05, 1.92512766e+05, 1.95065781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.93788375e+05, 1.93788375e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.31300484e+05, 1.31299000e+05, 2.03095812e+05, 1.30941727e+05, 1.30381664e+05, 6.85280078e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.94042734e+05, 1.94036844e+05, 2.99569594e+05, 1.93511844e+05, 1.92115719e+05, 1.01280250e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.93768094e+05, 1.93753125e+05, 1.93766312e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.93768094e+05, 1.92492734e+05, 1.95045297e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.93768094e+05, 1.93768094e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.31287797e+05, 1.31285500e+05, 2.03074250e+05, 1.30926766e+05, 1.30367781e+05, 6.85209844e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.94024031e+05, 1.94016906e+05, 2.99537906e+05, 1.93489703e+05, 1.92095500e+05, 1.01269883e+05, ],
  }),
  ("nof_tree_events",                 75268),
  ("nof_db_events",                   199100),
  ("fsize_local",                     389666117), # 389.67MB, avg file size 389.67MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 40009),
  ("nof_db_events",                   100000),
  ("fsize_local",                     219806120), # 219.81MB, avg file size 219.81MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 76966),
  ("nof_db_events",                   200000),
  ("fsize_local",                     400899206), # 400.90MB, avg file size 400.90MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_900_hh_2b2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 40011),
  ("nof_db_events",                   100000),
  ("fsize_local",                     211561405), # 211.56MB, avg file size 211.56MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 39402),
  ("nof_db_events",                   100000),
  ("fsize_local",                     210948419), # 210.95MB, avg file size 210.95MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 32976),
  ("nof_db_events",                   100000),
  ("fsize_local",                     176974978), # 176.97MB, avg file size 176.97MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 26829),
  ("nof_db_events",                   100000),
  ("fsize_local",                     144748880), # 144.75MB, avg file size 144.75MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 21609),
  ("nof_db_events",                   100000),
  ("fsize_local",                     117301090), # 117.30MB, avg file size 117.30MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 15451),
  ("nof_db_events",                   100000),
  ("fsize_local",                     84382152), # 84.38MB, avg file size 84.38MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_2500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 12689),
  ("nof_db_events",                   100000),
  ("fsize_local",                     68902895), # 68.90MB, avg file size 68.90MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin0_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 8139),
  ("nof_db_events",                   50000),
  ("fsize_local",                     33532588), # 33.53MB, avg file size 33.53MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 8216),
  ("nof_db_events",                   50000),
  ("fsize_local",                     34185416), # 34.19MB, avg file size 34.19MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_260_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 8330),
  ("nof_db_events",                   50000),
  ("fsize_local",                     35485847), # 35.49MB, avg file size 35.49MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_270_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 8794),
  ("nof_db_events",                   50000),
  ("fsize_local",                     37874341), # 37.87MB, avg file size 37.87MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_280_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 83619),
  ("nof_db_events",                   447400),
  ("fsize_local",                     356358506), # 356.36MB, avg file size 356.36MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_300_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 10111),
  ("nof_db_events",                   50000),
  ("fsize_local",                     45463660), # 45.46MB, avg file size 45.46MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_320_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 10757),
  ("nof_db_events",                   50000),
  ("fsize_local",                     49318608), # 49.32MB, avg file size 49.32MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_340_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 10905),
  ("nof_db_events",                   50000),
  ("fsize_local",                     50533433), # 50.53MB, avg file size 50.53MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_350_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 62354),
  ("nof_db_events",                   250000),
  ("fsize_local",                     294005947), # 294.01MB, avg file size 294.01MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_400_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 27892),
  ("nof_db_events",                   100000),
  ("fsize_local",                     136893683), # 136.89MB, avg file size 136.89MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_450_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 30668),
  ("nof_db_events",                   100000),
  ("fsize_local",                     155418769), # 155.42MB, avg file size 155.42MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 33000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     171330002), # 171.33MB, avg file size 171.33MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_550_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 35122),
  ("nof_db_events",                   100000),
  ("fsize_local",                     186060670), # 186.06MB, avg file size 186.06MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_600_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 36865),
  ("nof_db_events",                   100000),
  ("fsize_local",                     198164728), # 198.16MB, avg file size 198.16MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_650_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 76786),
  ("nof_db_events",                   200000),
  ("fsize_local",                     394834069), # 394.83MB, avg file size 394.83MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_700_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 40106),
  ("nof_db_events",                   100000),
  ("fsize_local",                     218836282), # 218.84MB, avg file size 218.84MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 40885),
  ("nof_db_events",                   100000),
  ("fsize_local",                     225124200), # 225.12MB, avg file size 225.12MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_800_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 83909),
  ("nof_db_events",                   200000),
  ("fsize_local",                     440270038), # 440.27MB, avg file size 440.27MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_850_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 85827),
  ("nof_db_events",                   200000),
  ("fsize_local",                     452580821), # 452.58MB, avg file size 452.58MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_900_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 43895),
  ("nof_db_events",                   100000),
  ("fsize_local",                     233563563), # 233.56MB, avg file size 233.56MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_1000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 41229),
  ("nof_db_events",                   100000),
  ("fsize_local",                     220785014), # 220.79MB, avg file size 220.79MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_1250_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 31029),
  ("nof_db_events",                   100000),
  ("fsize_local",                     165772520), # 165.77MB, avg file size 165.77MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_1500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 22761),
  ("nof_db_events",                   100000),
  ("fsize_local",                     121308846), # 121.31MB, avg file size 121.31MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_1750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 16729),
  ("nof_db_events",                   100000),
  ("fsize_local",                     90036312), # 90.04MB, avg file size 90.04MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_2000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 11336),
  ("nof_db_events",                   100000),
  ("fsize_local",                     61002890), # 61.00MB, avg file size 61.00MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_2500_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 9918),
  ("nof_db_events",                   100000),
  ("fsize_local",                     53091222), # 53.09MB, avg file size 53.09MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_spin2_3000_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    39),
  ("nof_events",                      {
    'Count'                                                                          : [ 993600, ],
    'CountWeighted'                                                                  : [ 9.90312938e+05, 9.90210562e+05, 9.90250062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.90312938e+05, 9.90312938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.90029800e+06, 9.90029800e+06, 9.90029800e+06, 9.90029800e+06, 9.90029800e+06, 9.90029800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.93655688e+05, 9.94692938e+05, 1.46434675e+06, 9.93585750e+05, 9.88654000e+05, 5.71410625e+05, ],
    'CountWeightedFull'                                                              : [ 9.89994000e+05, 9.89894250e+05, 9.89932750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.89994000e+05, 9.89994000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.89723000e+06, 9.89723000e+06, 9.89723000e+06, 9.89723000e+06, 9.89723000e+06, 9.89723000e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.93339125e+05, 9.94377500e+05, 1.46387500e+06, 9.93266625e+05, 9.88333938e+05, 5.71229750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.56131438e+05, 9.56084312e+05, 9.56117750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.56131438e+05, 9.47522750e+05, 9.64755562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.56131438e+05, 9.56131438e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.56033700e+06, 9.56033700e+06, 9.56033700e+06, 9.56033700e+06, 9.56033700e+06, 9.56033700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.59481438e+05, 9.59924625e+05, 1.41354188e+06, 9.59188750e+05, 9.55266938e+05, 5.52168438e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.55827875e+05, 9.55781500e+05, 9.55814688e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.55827875e+05, 9.47222125e+05, 9.64448625e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.55827875e+05, 9.55827875e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.55733700e+06, 9.55733700e+06, 9.55733700e+06, 9.55733700e+06, 9.55733700e+06, 9.55733700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.59178812e+05, 9.59623188e+05, 1.41309150e+06, 9.58883750e+05, 9.54961312e+05, 5.51995188e+05, ],
  }),
  ("nof_tree_events",                 213264),
  ("nof_db_events",                   993600),
  ("fsize_local",                     937690392), # 937.69MB, avg file size 937.69MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_0_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 1996000, ],
    'CountWeighted'                                                                  : [ 1.98887862e+06, 1.98851762e+06, 1.98858800e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.98887862e+06, 1.98887862e+06, ],
    'CountWeightedPSWeight'                                                          : [ 1.98856140e+07, 1.98856140e+07, 1.98856140e+07, 1.98856140e+07, 1.98856140e+07, 1.98856140e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99607162e+06, 1.99581812e+06, 2.94593475e+06, 1.99600775e+06, 1.99021938e+06, 1.14518562e+06, ],
    'CountWeightedFull'                                                              : [ 1.98819738e+06, 1.98786325e+06, 1.98791750e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.98819738e+06, 1.98819738e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.98790100e+07, 1.98790100e+07, 1.98790100e+07, 1.98790100e+07, 1.98790100e+07, 1.98790100e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99540075e+06, 1.99514712e+06, 2.94493650e+06, 1.99533262e+06, 1.98954800e+06, 1.14480438e+06, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.90976150e+06, 1.90957438e+06, 1.90972388e+06, ],
    'CountWeightedL1Prefire'                                                         : [ 1.90976150e+06, 1.89000975e+06, 1.92955325e+06, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.90976150e+06, 1.90976150e+06, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.90965120e+07, 1.90965120e+07, 1.90965120e+07, 1.90965120e+07, 1.90965120e+07, 1.90965120e+07, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.91696012e+06, 1.91562850e+06, 2.82814625e+06, 1.91640512e+06, 1.91252688e+06, 1.10074612e+06, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.90912325e+06, 1.90894375e+06, 1.90908912e+06, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.90912325e+06, 1.88938025e+06, 1.92890612e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.90912325e+06, 1.90912325e+06, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.90901800e+07, 1.90901800e+07, 1.90901800e+07, 1.90901800e+07, 1.90901800e+07, 1.90901800e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.91632438e+06, 1.91499312e+06, 2.82720000e+06, 1.91576512e+06, 1.91189012e+06, 1.10038425e+06, ],
  }),
  ("nof_tree_events",                 403382),
  ("nof_db_events",                   1996000),
  ("fsize_local",                     1783791197), # 1.78GB, avg file size 1.78GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 998000, ],
    'CountWeighted'                                                                  : [ 9.94452625e+05, 9.94457875e+05, 9.94364875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.94452625e+05, 9.94452625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.94441000e+06, 9.94441000e+06, 9.94441000e+06, 9.94441000e+06, 9.94441000e+06, 9.94441000e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.98007750e+05, 9.97984750e+05, 1.48432750e+06, 9.98019125e+05, 9.94833875e+05, 5.63277562e+05, ],
    'CountWeightedFull'                                                              : [ 9.94085188e+05, 9.94090750e+05, 9.94002688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.94085188e+05, 9.94085188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.94076200e+06, 9.94076200e+06, 9.94076200e+06, 9.94076200e+06, 9.94076200e+06, 9.94076200e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.97641312e+05, 9.97618312e+05, 1.48377925e+06, 9.97650062e+05, 9.94468375e+05, 5.63073312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.45699375e+05, 9.45672125e+05, 9.45679125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.45699375e+05, 9.33897125e+05, 9.57556750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.45699375e+05, 9.45699375e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.45683700e+06, 9.45683700e+06, 9.45683700e+06, 9.45683700e+06, 9.45683700e+06, 9.45683700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.49196375e+05, 9.48488688e+05, 1.41121075e+06, 9.48863500e+05, 9.46924438e+05, 5.36209750e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.45355500e+05, 9.45328188e+05, 9.45337500e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.45355500e+05, 9.33559000e+05, 9.57207250e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.45355500e+05, 9.45355500e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.45340700e+06, 9.45340700e+06, 9.45340700e+06, 9.45340700e+06, 9.45340700e+06, 9.45340700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.48852688e+05, 9.48145375e+05, 1.41069625e+06, 9.48517625e+05, 9.46580750e+05, 5.36018000e+05, ],
  }),
  ("nof_tree_events",                 201823),
  ("nof_db_events",                   998000),
  ("fsize_local",                     949559733), # 949.56MB, avg file size 949.56MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_2_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 1996000, ],
    'CountWeighted'                                                                  : [ 1.98489238e+06, 1.98486738e+06, 1.98477412e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.98489238e+06, 1.98489238e+06, ],
    'CountWeightedPSWeight'                                                          : [ 1.98466620e+07, 1.98466620e+07, 1.98466620e+07, 1.98466620e+07, 1.98466620e+07, 1.98466620e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99613950e+06, 1.99572100e+06, 2.95504300e+06, 1.99578250e+06, 1.99054650e+06, 1.13674512e+06, ],
    'CountWeightedFull'                                                              : [ 1.98414175e+06, 1.98411250e+06, 1.98401962e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.98414175e+06, 1.98414175e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.98391280e+07, 1.98391280e+07, 1.98391280e+07, 1.98391280e+07, 1.98391280e+07, 1.98391280e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99539000e+06, 1.99496975e+06, 2.95392225e+06, 1.99502950e+06, 1.98979575e+06, 1.13632262e+06, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.90187525e+06, 1.90179475e+06, 1.90189062e+06, ],
    'CountWeightedL1Prefire'                                                         : [ 1.90187525e+06, 1.88213175e+06, 1.92172175e+06, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.90187525e+06, 1.90187525e+06, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.90178700e+07, 1.90178700e+07, 1.90178700e+07, 1.90178700e+07, 1.90178700e+07, 1.90178700e+07, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.91287575e+06, 1.91149462e+06, 2.83048475e+06, 1.91199725e+06, 1.90849688e+06, 1.09038225e+06, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.90116738e+06, 1.90108588e+06, 1.90118025e+06, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.90116738e+06, 1.88143362e+06, 1.92100450e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.90116738e+06, 1.90116738e+06, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.90107740e+07, 1.90107740e+07, 1.90107740e+07, 1.90107740e+07, 1.90107740e+07, 1.90107740e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.91216650e+06, 1.91078462e+06, 2.82942525e+06, 1.91128538e+06, 1.90778700e+06, 1.08998238e+06, ],
  }),
  ("nof_tree_events",                 665938),
  ("nof_db_events",                   1996000),
  ("fsize_local",                     3431261427), # 3.43GB, avg file size 3.43GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 995500, ],
    'CountWeighted'                                                                  : [ 9.90985250e+05, 9.91072125e+05, 9.91083438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.90985250e+05, 9.90985250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.91071400e+06, 9.91071400e+06, 9.91071400e+06, 9.91071400e+06, 9.91071400e+06, 9.91071400e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.95582000e+05, 9.95669750e+05, 1.47079075e+06, 9.95399000e+05, 9.93059875e+05, 5.70219062e+05, ],
    'CountWeightedFull'                                                              : [ 9.90644875e+05, 9.90724875e+05, 9.90744438e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.90644875e+05, 9.90644875e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.90732900e+06, 9.90732900e+06, 9.90732900e+06, 9.90732900e+06, 9.90732900e+06, 9.90732900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.95242188e+05, 9.95330000e+05, 1.47028250e+06, 9.95057500e+05, 9.92716875e+05, 5.70026875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.52178750e+05, 9.52160375e+05, 9.52269688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.52178750e+05, 9.42643875e+05, 9.61741562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.52178750e+05, 9.52178750e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.52199200e+06, 9.52199200e+06, 9.52199200e+06, 9.52199200e+06, 9.52199200e+06, 9.52199200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.56609375e+05, 9.56126375e+05, 1.41284025e+06, 9.56203688e+05, 9.54920188e+05, 5.48336750e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.51856125e+05, 9.51835625e+05, 9.51947500e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.51856125e+05, 9.42325688e+05, 9.61414688e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.51856125e+05, 9.51856125e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.51877800e+06, 9.51877800e+06, 9.51877800e+06, 9.51877800e+06, 9.51877800e+06, 9.51877800e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.56287125e+05, 9.55804500e+05, 1.41235825e+06, 9.55879875e+05, 9.54594500e+05, 5.48154250e+05, ],
  }),
  ("nof_tree_events",                 268200),
  ("nof_db_events",                   995500),
  ("fsize_local",                     1296691585), # 1.30GB, avg file size 1.30GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 999000, ],
    'CountWeighted'                                                                  : [ 9.94030375e+05, 9.94064500e+05, 9.93901375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.94030375e+05, 9.94030375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.93909700e+06, 9.93909700e+06, 9.93909700e+06, 9.93909700e+06, 9.93909700e+06, 9.93909700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.98827125e+05, 9.99072125e+05, 1.47716675e+06, 9.99216125e+05, 9.95442562e+05, 5.70228500e+05, ],
    'CountWeightedFull'                                                              : [ 9.93667062e+05, 9.93700938e+05, 9.93538938e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.93667062e+05, 9.93667062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.93546100e+06, 9.93546100e+06, 9.93546100e+06, 9.93546100e+06, 9.93546100e+06, 9.93546100e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.98465000e+05, 9.98708312e+05, 1.47662912e+06, 9.98852000e+05, 9.95083062e+05, 5.70023750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.53478188e+05, 9.53499688e+05, 9.53419500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.53478188e+05, 9.43738688e+05, 9.63264438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.53478188e+05, 9.53478188e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.53433500e+06, 9.53433500e+06, 9.53433500e+06, 9.53433500e+06, 9.53433500e+06, 9.53433500e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.58165125e+05, 9.57797375e+05, 1.41640612e+06, 9.58281312e+05, 9.55535688e+05, 5.47560375e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.53135250e+05, 9.53156438e+05, 9.53076688e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.53135250e+05, 9.43400312e+05, 9.62916812e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.53135250e+05, 9.53135250e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.53090800e+06, 9.53090800e+06, 9.53090800e+06, 9.53090800e+06, 9.53090800e+06, 9.53090800e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.57822375e+05, 9.57453438e+05, 1.41589700e+06, 9.57936375e+05, 9.55195062e+05, 5.47366188e+05, ],
  }),
  ("nof_tree_events",                 315582),
  ("nof_db_events",                   999000),
  ("fsize_local",                     1598986903), # 1.60GB, avg file size 1.60GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 1998600, ],
    'CountWeighted'                                                                  : [ 1.98914712e+06, 1.98941300e+06, 1.98909512e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.98914712e+06, 1.98914712e+06, ],
    'CountWeightedPSWeight'                                                          : [ 1.98894120e+07, 1.98894120e+07, 1.98894120e+07, 1.98894120e+07, 1.98894120e+07, 1.98894120e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99873012e+06, 1.99935025e+06, 2.95187525e+06, 1.99846338e+06, 1.99167675e+06, 1.14402800e+06, ],
    'CountWeightedFull'                                                              : [ 1.98843875e+06, 1.98869125e+06, 1.98838775e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.98843875e+06, 1.98843875e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.98823660e+07, 1.98823660e+07, 1.98823660e+07, 1.98823660e+07, 1.98823660e+07, 1.98823660e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.99802350e+06, 1.99864212e+06, 2.95082400e+06, 1.99775175e+06, 1.99097138e+06, 1.14362725e+06, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.90929425e+06, 1.90934838e+06, 1.90935062e+06, ],
    'CountWeightedL1Prefire'                                                         : [ 1.90929425e+06, 1.88989375e+06, 1.92877888e+06, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.90929425e+06, 1.90929425e+06, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.90921320e+07, 1.90921320e+07, 1.90921320e+07, 1.90921320e+07, 1.90921320e+07, 1.90921320e+07, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.91868175e+06, 1.91824025e+06, 2.83253725e+06, 1.91792050e+06, 1.91297088e+06, 1.09915825e+06, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.90862475e+06, 1.90867388e+06, 1.90868088e+06, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.90862475e+06, 1.88923275e+06, 1.92810012e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.90862475e+06, 1.90862475e+06, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.90854520e+07, 1.90854520e+07, 1.90854520e+07, 1.90854520e+07, 1.90854520e+07, 1.90854520e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.91801275e+06, 1.91756900e+06, 2.83154225e+06, 1.91724700e+06, 1.91230312e+06, 1.09877800e+06, ],
  }),
  ("nof_tree_events",                 580150),
  ("nof_db_events",                   1998600),
  ("fsize_local",                     2865973990), # 2.87GB, avg file size 2.87GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                                          : [ 496500, ],
    'CountWeighted'                                                                  : [ 4.94130938e+05, 4.94151625e+05, 4.94152000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.94130938e+05, 4.94130938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.94145550e+06, 4.94145550e+06, 4.94145550e+06, 4.94145550e+06, 4.94145550e+06, 4.94145550e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.96553281e+05, 4.96093906e+05, 7.33790562e+05, 4.96419156e+05, 4.95949625e+05, 2.84281688e+05, ],
    'CountWeightedFull'                                                              : [ 4.93958719e+05, 4.93978969e+05, 4.93976969e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.93958719e+05, 4.93958719e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.93971800e+06, 4.93971800e+06, 4.93971800e+06, 4.93971800e+06, 4.93971800e+06, 4.93971800e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.96380188e+05, 4.95920188e+05, 7.33533750e+05, 4.96244406e+05, 4.95778344e+05, 2.84183250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.74460750e+05, 4.74466125e+05, 4.74473156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 4.74460750e+05, 4.69669719e+05, 4.79272469e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.74460750e+05, 4.74460750e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 4.74468450e+06, 4.74468450e+06, 4.74468450e+06, 4.74468450e+06, 4.74468450e+06, 4.74468450e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 4.76817906e+05, 4.76095562e+05, 7.04357250e+05, 4.76552656e+05, 4.76534938e+05, 2.73208656e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 4.74297031e+05, 4.74302250e+05, 4.74308156e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 4.74297031e+05, 4.69508031e+05, 4.79106219e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.74297031e+05, 4.74297031e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 4.74303850e+06, 4.74303850e+06, 4.74303850e+06, 4.74303850e+06, 4.74303850e+06, 4.74303850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 4.76653781e+05, 4.75930750e+05, 7.04113625e+05, 4.76387156e+05, 4.76371875e+05, 2.73115250e+05, ],
  }),
  ("nof_tree_events",                 144587),
  ("nof_db_events",                   496500),
  ("fsize_local",                     716026716), # 716.03MB, avg file size 716.03MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2b2t_dipoleRecoilOff_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00009844e+05, 2.99984125e+05, 3.00018375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84326188e+05, 3.62835312e+05, 3.42679219e+05, 3.17798969e+05, 3.00007219e+05, 2.83309688e+05, 2.67174250e+05, 2.52189594e+05, 2.38142625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.84326188e+05, 2.38142625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93734156e+05, 2.93720969e+05, 2.93734188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93734156e+05, 2.92155688e+05, 2.95309938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.76219406e+05, 3.55255125e+05, 3.35576062e+05, 3.11092031e+05, 2.93730000e+05, 2.77433625e+05, 2.61532562e+05, 2.46914969e+05, 2.33200547e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76219406e+05, 2.33200547e+05, ],
  }),
  ("nof_tree_events",                 77426),
  ("nof_db_events",                   300000),
  ("fsize_local",                     381053089), # 381.05MB, avg file size 381.05MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_sm_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 277140, ],
    'CountWeighted'                                                                  : [ 2.77140594e+05, 2.77151875e+05, 2.77124281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.53745438e+05, 3.36001250e+05, 3.18998875e+05, 2.91807500e+05, 2.77136969e+05, 2.63092312e+05, 2.44831062e+05, 2.32503594e+05, 2.20699828e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.53745438e+05, 2.20699828e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.71541031e+05, 2.71531438e+05, 2.71544500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.71541031e+05, 2.70120406e+05, 2.72956062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.46528344e+05, 3.29216062e+05, 3.12611188e+05, 2.85849469e+05, 2.71535969e+05, 2.57819484e+05, 2.39829312e+05, 2.27802078e+05, 2.16274062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.46528344e+05, 2.16274062e+05, ],
  }),
  ("nof_tree_events",                 67328),
  ("nof_db_events",                   277140),
  ("fsize_local",                     323685010), # 323.69MB, avg file size 323.69MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_box_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99923094e+05, 3.99971750e+05, 3.99925562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99923094e+05, 3.99923094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.98699150e+06, 3.65965625e+06, 3.99810750e+06, 3.97392700e+06, 3.20732800e+06, 2.86001700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00089406e+05, 3.99662500e+05, 6.12934750e+05, 3.99880562e+05, 3.99153250e+05, 2.15061281e+05, ],
    'CountWeightedFull'                                                              : [ 3.99888188e+05, 3.99936906e+05, 3.99890812e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99888188e+05, 3.99888188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.98664675e+06, 3.65934500e+06, 3.99776100e+06, 3.97358050e+06, 3.20705350e+06, 2.85977800e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00057438e+05, 3.99628375e+05, 6.12879500e+05, 3.99841938e+05, 3.99117375e+05, 2.15043297e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91566250e+05, 3.91594281e+05, 3.91562500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91566250e+05, 3.89456688e+05, 3.93673562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.91566250e+05, 3.91566250e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.90363400e+06, 3.58328800e+06, 3.91443000e+06, 3.89050650e+06, 3.14111300e+06, 2.80120975e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.92053031e+05, 3.91238375e+05, 5.99969875e+05, 3.91064812e+05, 3.90865062e+05, 2.10638969e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.91532812e+05, 3.91560750e+05, 3.91529062e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.91532812e+05, 3.89423500e+05, 3.93639688e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.91532812e+05, 3.91532812e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.90330250e+06, 3.58298850e+06, 3.91409700e+06, 3.89017425e+06, 3.14084900e+06, 2.80097950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.92022312e+05, 3.91205438e+05, 5.99916875e+05, 3.91027875e+05, 3.90830594e+05, 2.10621641e+05, ],
  }),
  ("nof_tree_events",                 98388),
  ("nof_db_events",                   400000),
  ("fsize_local",                     444996901), # 445.00MB, avg file size 445.00MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 291000, ],
    'CountWeighted'                                                                  : [ 2.91008250e+05, 2.91000312e+05, 2.90997844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.71669500e+05, 3.52735594e+05, 3.34726281e+05, 3.06701094e+05, 2.91006812e+05, 2.76077812e+05, 2.57423547e+05, 2.44188344e+05, 2.31621125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.71669500e+05, 2.31621125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.85180438e+05, 2.85165562e+05, 2.85176906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.85180438e+05, 2.83704281e+05, 2.86649531e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.64148375e+05, 3.45687281e+05, 3.28106531e+05, 3.00483812e+05, 2.85178312e+05, 2.70608031e+05, 2.52196781e+05, 2.39292109e+05, 2.27024969e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.64148375e+05, 2.27024969e+05, ],
  }),
  ("nof_tree_events",                 71785),
  ("nof_db_events",                   291000),
  ("fsize_local",                     351995432), # 352.00MB, avg file size 352.00MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_2_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 396700, ],
    'CountWeighted'                                                                  : [ 3.96679312e+05, 3.96596250e+05, 3.96660688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96679312e+05, 3.96679312e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96637350e+06, 3.96637350e+06, 3.96637350e+06, 3.96637350e+06, 3.96637350e+06, 3.96637350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96801625e+05, 3.96589031e+05, 6.08824438e+05, 3.96598781e+05, 3.95240125e+05, 2.12263141e+05, ],
    'CountWeightedFull'                                                              : [ 3.96642969e+05, 3.96560625e+05, 3.96624812e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96642969e+05, 3.96642969e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96601425e+06, 3.96601425e+06, 3.96601425e+06, 3.96601425e+06, 3.96601425e+06, 3.96601425e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96768406e+05, 3.96553594e+05, 6.08767375e+05, 3.96559031e+05, 3.95203000e+05, 2.12244469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88134844e+05, 3.88080625e+05, 3.88129531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88134844e+05, 3.85996750e+05, 3.90271219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.88134844e+05, 3.88134844e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.88110950e+06, 3.88110950e+06, 3.88110950e+06, 3.88110950e+06, 3.88110950e+06, 3.88110950e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.88596938e+05, 3.87962094e+05, 5.95673875e+05, 3.87627469e+05, 3.86905938e+05, 2.07770781e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.88100062e+05, 3.88046094e+05, 3.88095062e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.88100062e+05, 3.85962375e+05, 3.90236062e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.88100062e+05, 3.88100062e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.88076400e+06, 3.88076400e+06, 3.88076400e+06, 3.88076400e+06, 3.88076400e+06, 3.88076400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.88565062e+05, 3.87928125e+05, 5.95619000e+05, 3.87589250e+05, 3.86870188e+05, 2.07752891e+05, ],
  }),
  ("nof_tree_events",                 104363),
  ("nof_db_events",                   396700),
  ("fsize_local",                     487138840), # 487.14MB, avg file size 487.14MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_3_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99953750e+05, 3.99982062e+05, 3.99920688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99953750e+05, 3.99953750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99984300e+06, 3.99971600e+06, 3.99984300e+06, 3.99984300e+06, 3.99280375e+06, 3.99267650e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00249500e+05, 4.00136188e+05, 6.11553000e+05, 3.99735312e+05, 3.97301625e+05, 2.15149906e+05, ],
    'CountWeightedFull'                                                              : [ 3.99919812e+05, 3.99948000e+05, 3.99887625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99919812e+05, 3.99919812e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99950150e+06, 3.99937450e+06, 3.99950150e+06, 3.99950150e+06, 3.99246325e+06, 3.99233650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00218219e+05, 4.00102375e+05, 6.11499062e+05, 3.99697844e+05, 3.97266938e+05, 2.15132234e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91613250e+05, 3.91617875e+05, 3.91603000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91613250e+05, 3.89509688e+05, 3.93716562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.91613250e+05, 3.91613250e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.91630475e+06, 3.91618300e+06, 3.91630475e+06, 3.91630475e+06, 3.90945850e+06, 3.90933650e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.92237562e+05, 3.91688094e+05, 5.98651000e+05, 3.90940062e+05, 3.89117562e+05, 2.10748281e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.91580500e+05, 3.91585094e+05, 3.91570656e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.91580500e+05, 3.89477281e+05, 3.93683500e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.91580500e+05, 3.91580500e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.91597650e+06, 3.91585500e+06, 3.91597650e+06, 3.91597650e+06, 3.90913100e+06, 3.90900900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.92207406e+05, 3.91655688e+05, 5.98599250e+05, 3.90904031e+05, 3.89084188e+05, 2.10731328e+05, ],
  }),
  ("nof_tree_events",                 98377),
  ("nof_db_events",                   400000),
  ("fsize_local",                     445756925), # 445.76MB, avg file size 445.76MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_4_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 394500, ],
    'CountWeighted'                                                                  : [ 3.94453281e+05, 3.94462406e+05, 3.94446750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94453281e+05, 3.94453281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94487725e+06, 3.94487725e+06, 3.94487725e+06, 3.94487725e+06, 3.94487725e+06, 3.94487725e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.94464562e+05, 3.94204125e+05, 6.07633688e+05, 3.94557531e+05, 3.92414844e+05, 2.08641297e+05, ],
    'CountWeightedFull'                                                              : [ 3.94411625e+05, 3.94420750e+05, 3.94405125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.94411625e+05, 3.94411625e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.94445625e+06, 3.94445625e+06, 3.94445625e+06, 3.94445625e+06, 3.94445625e+06, 3.94445625e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.94425750e+05, 3.94164688e+05, 6.07567188e+05, 3.94511562e+05, 3.92370000e+05, 2.08619500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.85179812e+05, 3.85181250e+05, 3.85177250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.85179812e+05, 3.82899031e+05, 3.87462875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.85179812e+05, 3.85179812e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.85198750e+06, 3.85198750e+06, 3.85198750e+06, 3.85198750e+06, 3.85198750e+06, 3.85198750e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.85546438e+05, 3.84802156e+05, 5.93230875e+05, 3.84807844e+05, 3.83337062e+05, 2.03813031e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.85139688e+05, 3.85141062e+05, 3.85137000e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.85139688e+05, 3.82859250e+05, 3.87422312e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.85139688e+05, 3.85139688e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.85158375e+06, 3.85158375e+06, 3.85158375e+06, 3.85158375e+06, 3.85158375e+06, 3.85158375e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.85509188e+05, 3.84764438e+05, 5.93167000e+05, 3.84763781e+05, 3.83293812e+05, 2.03792125e+05, ],
  }),
  ("nof_tree_events",                 121136),
  ("nof_db_events",                   394500),
  ("fsize_local",                     602148315), # 602.15MB, avg file size 602.15MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_5_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 397000, ],
    'CountWeighted'                                                                  : [ 3.96991938e+05, 3.96936656e+05, 3.96987312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96991938e+05, 3.96991938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97006050e+06, 3.96927750e+06, 3.97006050e+06, 3.97006050e+06, 3.94818325e+06, 3.94740050e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.97074000e+05, 3.97128250e+05, 6.09172688e+05, 3.96909281e+05, 3.96367875e+05, 2.13324875e+05, ],
    'CountWeightedFull'                                                              : [ 3.96957000e+05, 3.96902125e+05, 3.96952625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96957000e+05, 3.96957000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96970300e+06, 3.96892075e+06, 3.96970300e+06, 3.96970300e+06, 3.94782900e+06, 3.94704650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.97041656e+05, 3.97094281e+05, 6.09117625e+05, 3.96871000e+05, 3.96331688e+05, 2.13306578e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88745562e+05, 3.88704562e+05, 3.88753500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88745562e+05, 3.86667438e+05, 3.90822281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.88745562e+05, 3.88745562e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.88754050e+06, 3.88677450e+06, 3.88754050e+06, 3.88754050e+06, 3.86620700e+06, 3.86544050e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.89165969e+05, 3.88793438e+05, 5.96445375e+05, 3.88233000e+05, 3.88285500e+05, 2.08981250e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.88711844e+05, 3.88671062e+05, 3.88720062e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.88711844e+05, 3.86634062e+05, 3.90788281e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.88711844e+05, 3.88711844e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.88720100e+06, 3.88643475e+06, 3.88720100e+06, 3.88720100e+06, 3.86587000e+06, 3.86510350e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.89134750e+05, 3.88760812e+05, 5.96392500e+05, 3.88196219e+05, 3.88250625e+05, 2.08963594e+05, ],
  }),
  ("nof_tree_events",                 98100),
  ("nof_db_events",                   397000),
  ("fsize_local",                     443434521), # 443.43MB, avg file size 443.43MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_7_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 398900, ],
    'CountWeighted'                                                                  : [ 3.98859062e+05, 3.98902062e+05, 3.98865281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.98859062e+05, 3.98859062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.16490312e+05, 3.16377812e+05, 4.84694188e+05, 3.16587594e+05, 3.15551938e+05, 1.70443062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.98847250e+05, 3.98706531e+05, 6.10022438e+05, 3.98963812e+05, 3.96870031e+05, 2.14799250e+05, ],
    'CountWeightedFull'                                                              : [ 3.98824750e+05, 3.98867375e+05, 3.98830938e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.98824750e+05, 3.98824750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.16465188e+05, 3.16350562e+05, 4.84650312e+05, 3.16557188e+05, 3.15523531e+05, 1.70428828e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.98815531e+05, 3.98672250e+05, 6.09967125e+05, 3.98925438e+05, 3.96834219e+05, 2.14781203e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.90636688e+05, 3.90654094e+05, 3.90643812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.90636688e+05, 3.88560625e+05, 3.92709188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.90636688e+05, 3.90636688e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.10229469e+05, 3.09763531e+05, 4.74632750e+05, 3.09715000e+05, 3.09180375e+05, 1.66993375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.90953250e+05, 3.90366469e+05, 5.97353062e+05, 3.90298406e+05, 3.88852562e+05, 2.10449375e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.90603656e+05, 3.90620938e+05, 3.90610625e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.90603656e+05, 3.88527938e+05, 3.92675812e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.90603656e+05, 3.90603656e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.10205312e+05, 3.09737438e+05, 4.74590688e+05, 3.09685812e+05, 3.09153062e+05, 1.66979703e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.90922750e+05, 3.90333500e+05, 5.97300000e+05, 3.90261688e+05, 3.88818062e+05, 2.10432094e+05, ],
  }),
  ("nof_tree_events",                 97771),
  ("nof_db_events",                   398900),
  ("fsize_local",                     441256907), # 441.26MB, avg file size 441.26MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_8_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99988406e+05, 2.99993938e+05, 3.00008094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.80809656e+05, 3.65080312e+05, 3.49381156e+05, 3.12974969e+05, 2.99965500e+05, 2.87063031e+05, 2.61793906e+05, 2.50908875e+05, 2.40060156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.80809656e+05, 2.40060156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94390562e+05, 2.94388719e+05, 2.94411031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94390562e+05, 2.92959906e+05, 2.95821344e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.73631562e+05, 3.58271500e+05, 3.42922406e+05, 3.07070438e+05, 2.94375469e+05, 2.81750469e+05, 2.56850094e+05, 2.46220000e+05, 2.35613266e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.73631562e+05, 2.35613266e+05, ],
  }),
  ("nof_tree_events",                 65642),
  ("nof_db_events",                   300000),
  ("fsize_local",                     306006578), # 306.01MB, avg file size 306.01MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_9_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00014750e+05, 3.00000062e+05, 2.99985938e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.82021031e+05, 3.64307312e+05, 3.47067000e+05, 3.14636969e+05, 3.00007000e+05, 2.85766562e+05, 2.63646406e+05, 2.51348562e+05, 2.39399188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.82021031e+05, 2.39399188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.94150625e+05, 2.94134781e+05, 2.94142094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.94150625e+05, 2.92662375e+05, 2.95636062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.74491000e+05, 3.57201094e+05, 3.40357656e+05, 3.08428812e+05, 2.94144281e+05, 2.80237375e+05, 2.58440016e+05, 2.46437312e+05, 2.34763188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.74491000e+05, 2.34763188e+05, ],
  }),
  ("nof_tree_events",                 70112),
  ("nof_db_events",                   300000),
  ("fsize_local",                     333522201), # 333.52MB, avg file size 333.52MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_10_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00003125e+05, 2.99983125e+05, 2.99961719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84467062e+05, 3.62940531e+05, 3.42915188e+05, 3.17930188e+05, 3.00001219e+05, 2.83344250e+05, 2.67335531e+05, 2.52166578e+05, 2.38092922e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.84467062e+05, 2.38092922e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93844625e+05, 2.93835781e+05, 2.93817719e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93844625e+05, 2.92300469e+05, 2.95389656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.76488406e+05, 3.55511562e+05, 3.35976594e+05, 3.11316062e+05, 2.93840938e+05, 2.77596656e+05, 2.61762188e+05, 2.46980484e+05, 2.33252750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76488406e+05, 2.33252750e+05, ],
  }),
  ("nof_tree_events",                 78222),
  ("nof_db_events",                   300000),
  ("fsize_local",                     393997363), # 394.00MB, avg file size 394.00MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_11_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 298800, ],
    'CountWeighted'                                                                  : [ 2.98741000e+05, 2.98815719e+05, 2.98793375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.85318438e+05, 3.59966281e+05, 3.36994375e+05, 3.19936531e+05, 2.98735625e+05, 2.79662875e+05, 2.69922875e+05, 2.52028109e+05, 2.35837453e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.85318438e+05, 2.35837453e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92410906e+05, 2.92449000e+05, 2.92446500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92410906e+05, 2.90830781e+05, 2.93991031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.77046562e+05, 3.52321188e+05, 3.29902875e+05, 3.13058750e+05, 2.92405250e+05, 2.73769312e+05, 2.64114094e+05, 2.46663125e+05, 2.30862250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.77046562e+05, 2.30862250e+05, ],
  }),
  ("nof_tree_events",                 87802),
  ("nof_db_events",                   298800),
  ("fsize_local",                     454167886), # 454.17MB, avg file size 454.17MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_12_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99962812e+05, 3.00001531e+05, 2.99985906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.88568031e+05, 3.60322938e+05, 3.35113594e+05, 3.23568062e+05, 2.99957875e+05, 2.78971062e+05, 2.73631375e+05, 2.53665562e+05, 2.35855688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.88568031e+05, 2.35855688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93102469e+05, 2.93120406e+05, 2.93116438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93102469e+05, 2.91399562e+05, 2.94802500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.79586375e+05, 3.52067531e+05, 3.27492812e+05, 3.16083375e+05, 2.93098375e+05, 2.72622688e+05, 2.67298344e+05, 2.47846812e+05, 2.30485500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.79586375e+05, 2.30485500e+05, ],
  }),
  ("nof_tree_events",                 92646),
  ("nof_db_events",                   300000),
  ("fsize_local",                     485446282), # 485.45MB, avg file size 485.45MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_node_13_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    33),
  ("nof_events",                      {
    'Count'                                                                          : [ 947200, ],
    'CountWeighted'                                                                  : [ 8.91626438e+05, 8.91625750e+05, 8.91594875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.03161475e+06, 1.01360825e+06, 1.00094075e+06, 9.11858625e+05, 8.91626438e+05, 8.75317812e+05, 8.08402312e+05, 7.87562312e+05, 7.69781438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.06805175e+06, 7.51965062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.91574062e+05, 8.92116438e+05, 1.35066988e+06, 8.91623000e+05, 8.86489688e+05, 4.86281344e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.06628203e+04, 6.07120234e+04, 9.21621719e+04, 6.06736172e+04, 6.05590781e+04, 3.30792930e+04, ],
    'CountWeightedFull'                                                              : [ 5.70285742e+04, 5.70298711e+04, 5.70253789e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 6.59834062e+04, 6.48312422e+04, 6.40205156e+04, 5.83239336e+04, 5.70285742e+04, 5.59862266e+04, 5.17063516e+04, 5.03731523e+04, 4.92355703e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 6.83144141e+04, 4.80961211e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 5.70264492e+04, 5.70607148e+04, 8.63904453e+04, 5.70290625e+04, 5.67010508e+04, 3.11032031e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.88854004e+03, 3.89176929e+03, 5.90789648e+03, 3.88921167e+03, 3.88193115e+03, 2.12029663e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.77520000e+05, 8.77494875e+05, 8.77527375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.77520000e+05, 8.73838312e+05, 8.81191500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.01510331e+06, 9.97522375e+05, 9.85175562e+05, 8.97316125e+05, 8.77520000e+05, 8.61589000e+05, 7.95541062e+05, 7.75147625e+05, 7.57744375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.05097938e+06, 7.40209188e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.77574750e+05, 8.77861688e+05, 1.32922225e+06, 8.77403188e+05, 8.72727250e+05, 4.78740781e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 5.97003906e+04, 5.97313242e+04, 9.06827500e+04, 5.96958281e+04, 5.96082500e+04, 3.25606523e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 5.61267852e+04, 5.61260391e+04, 5.61260508e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 5.61267852e+04, 5.58910547e+04, 5.63614688e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 6.49270195e+04, 6.38020352e+04, 6.30119766e+04, 5.73936523e+04, 5.61267852e+04, 5.51080352e+04, 5.08835352e+04, 4.95789727e+04, 4.84655820e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 6.72221250e+04, 4.73440508e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 5.61308398e+04, 5.61488125e+04, 8.50184609e+04, 5.61194648e+04, 5.58206758e+04, 3.06208203e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.82679517e+03, 3.82886743e+03, 5.81298877e+03, 3.82648608e+03, 3.82091382e+03, 2.08702271e+03, ],
  }),
  ("nof_tree_events",                 221979),
  ("nof_db_events",                   947200),
  ("fsize_local",                     980136197), # 980.14MB, avg file size 980.14MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH0_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    29),
  ("nof_events",                      {
    'Count'                                                                          : [ 999400, ],
    'CountWeighted'                                                                  : [ 8.95152875e+05, 8.95215375e+05, 8.94994750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.01903462e+06, 1.00279631e+06, 9.92092062e+05, 9.15705000e+05, 8.95130125e+05, 8.78947562e+05, 8.21921250e+05, 7.99508250e+05, 7.80722750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.06270850e+06, 7.57019188e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.95233312e+05, 8.94804688e+05, 1.35909062e+06, 8.94981000e+05, 8.92166125e+05, 4.86743625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98756641e+04, 2.98747656e+04, 4.54550195e+04, 2.98749375e+04, 2.98709492e+04, 1.62573535e+04, ],
    'CountWeightedFull'                                                              : [ 2.67319473e+04, 2.67367070e+04, 2.67278008e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.04328418e+04, 2.99474531e+04, 2.96275273e+04, 2.73469238e+04, 2.67314727e+04, 2.62486289e+04, 2.45456719e+04, 2.38760801e+04, 2.33148965e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.17372637e+04, 2.26071270e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.67353223e+04, 2.67225312e+04, 4.05878828e+04, 2.67275957e+04, 2.66434492e+04, 1.45359922e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 8.93780212e+02, 8.94048889e+02, 1.35947156e+03, 8.93856812e+02, 8.93467102e+02, 4.86796021e+02, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.80423688e+05, 8.80494125e+05, 8.80282750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.80423688e+05, 8.76605750e+05, 8.84230312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.00205331e+06, 9.86222188e+05, 9.75817375e+05, 9.00521062e+05, 8.80398875e+05, 8.64610125e+05, 8.08340500e+05, 7.86415938e+05, 7.68037625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.04502850e+06, 7.44716500e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.80632500e+05, 8.79945812e+05, 1.33663388e+06, 8.80115375e+05, 8.77724562e+05, 4.78882656e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.93855176e+04, 2.93756133e+04, 4.47003008e+04, 2.93759258e+04, 2.93853223e+04, 1.59931240e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 2.62921680e+04, 2.62962461e+04, 2.62884863e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 2.62921680e+04, 2.61780762e+04, 2.64059883e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 2.99254609e+04, 2.94523066e+04, 2.91413438e+04, 2.68932734e+04, 2.62915801e+04, 2.58203496e+04, 2.41399395e+04, 2.34849961e+04, 2.29360195e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.12090391e+04, 2.22396250e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.62991699e+04, 2.62786094e+04, 3.99170117e+04, 2.62835156e+04, 2.62120312e+04, 1.43011787e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 8.79123169e+02, 8.79117432e+02, 1.33690051e+03, 8.78934448e+02, 8.78950562e+02, 4.78896698e+02, ],
  }),
  ("nof_tree_events",                 250967),
  ("nof_db_events",                   999400),
  ("fsize_local",                     1134029806), # 1.13GB, avg file size 1.13GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH1_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    31),
  ("nof_events",                      {
    'Count'                                                                          : [ 951000, ],
    'CountWeighted'                                                                  : [ 8.19716938e+05, 8.19628000e+05, 8.19844750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.34415125e+05, 9.21427938e+05, 9.13162375e+05, 8.36502312e+05, 8.19710562e+05, 8.06615500e+05, 7.49072438e+05, 7.30590625e+05, 7.15036750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.84549438e+05, 6.84215562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.19773125e+05, 8.19875312e+05, 1.24697912e+06, 8.19678062e+05, 8.16926625e+05, 4.44112844e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.24903105e+04, 1.24912480e+04, 1.90471426e+04, 1.24879736e+04, 1.24954248e+04, 6.76828955e+03, ],
    'CountWeightedFull'                                                              : [ 1.07508623e+04, 1.07513770e+04, 1.07527451e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.22559805e+04, 1.20852822e+04, 1.19765479e+04, 1.09716611e+04, 1.07507148e+04, 1.05791396e+04, 9.82461035e+03, 9.58201172e+03, 9.37786035e+03, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.29135801e+04, 8.97368750e+03, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.07520059e+04, 1.07532471e+04, 1.63548672e+04, 1.07505752e+04, 1.07144160e+04, 5.82485303e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.64121521e+02, 1.64128799e+02, 2.50252487e+02, 1.64084534e+02, 1.64169800e+02, 8.89381561e+01, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.06110875e+05, 8.06014500e+05, 8.06233250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.06110875e+05, 8.02581875e+05, 8.09628000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.18667938e+05, 9.06035125e+05, 8.98030000e+05, 8.22478562e+05, 8.06098438e+05, 7.93328188e+05, 7.36558438e+05, 7.18504000e+05, 7.03307875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.67997625e+05, 6.72982688e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.06276062e+05, 8.06073438e+05, 1.22610275e+06, 8.05909688e+05, 8.03601938e+05, 4.36916094e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.22829961e+04, 1.22794531e+04, 1.87262090e+04, 1.22765859e+04, 1.22901006e+04, 6.65754541e+03, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 1.05723584e+04, 1.05722402e+04, 1.05740654e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 1.05723584e+04, 1.05261523e+04, 1.06185215e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.20492637e+04, 1.18832549e+04, 1.17779658e+04, 1.07875762e+04, 1.05721543e+04, 1.04047881e+04, 9.66038281e+03, 9.42340918e+03, 9.22396680e+03, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.26963096e+04, 8.82629688e+03, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.05748652e+04, 1.05721035e+04, 1.60809160e+04, 1.05698975e+04, 1.05395918e+04, 5.73041064e+03, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 1.61390289e+02, 1.61338745e+02, 2.46025818e+02, 1.61299896e+02, 1.61466263e+02, 8.74787216e+01, ],
  }),
  ("nof_tree_events",                 235513),
  ("nof_db_events",                   951000),
  ("fsize_local",                     1077530316), # 1.08GB, avg file size 1.08GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    28),
  ("nof_events",                      {
    'Count'                                                                          : [ 984200, ],
    'CountWeighted'                                                                  : [ 9.68689188e+05, 9.68855875e+05, 9.68932375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.16061362e+06, 1.13860825e+06, 1.12165212e+06, 9.88230688e+05, 9.68674938e+05, 9.52384812e+05, 8.50968000e+05, 8.33821812e+05, 8.18308125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.19591612e+06, 8.01762938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.68769375e+05, 9.69342312e+05, 1.46733338e+06, 9.68878000e+05, 9.64962750e+05, 5.29715688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 7.89666094e+04, 7.90134375e+04, 1.19942016e+05, 7.89837422e+04, 7.90031875e+04, 4.31888203e+04, ],
    'CountWeightedFull'                                                              : [ 7.77032891e+04, 7.77118516e+04, 7.77123281e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 9.30905156e+04, 9.13241797e+04, 8.99629609e+04, 7.92640703e+04, 7.77008516e+04, 7.63871172e+04, 6.82528047e+04, 6.68767812e+04, 6.56318125e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.59228984e+04, 6.43049570e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 7.77021797e+04, 7.77486641e+04, 1.17688688e+05, 7.77103750e+04, 7.73945859e+04, 4.24867812e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 6.33902734e+03, 6.34294531e+03, 9.62638672e+03, 6.34034961e+03, 6.34159277e+03, 3.46847510e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.54571000e+05, 9.54629750e+05, 9.54760062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.54571000e+05, 9.50805938e+05, 9.58322500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.14332288e+06, 1.12181738e+06, 1.10525988e+06, 9.73619188e+05, 9.54551938e+05, 9.38572500e+05, 8.38459062e+05, 8.21690375e+05, 8.06508188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.17814538e+06, 7.90190125e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.54718438e+05, 9.54999500e+05, 1.44574712e+06, 9.54540250e+05, 9.51162375e+05, 5.22167375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 7.78146797e+04, 7.78374375e+04, 1.18167758e+05, 7.78083594e+04, 7.78668281e+04, 4.25695781e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 7.65669141e+04, 7.65694531e+04, 7.65763203e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 7.65669141e+04, 7.62642188e+04, 7.68679531e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 9.17027109e+04, 8.99767109e+04, 8.86476953e+04, 7.80914062e+04, 7.65645469e+04, 7.52787188e+04, 6.72489844e+04, 6.59033906e+04, 6.46850703e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.44964141e+04, 6.33763555e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 7.65746562e+04, 7.65976094e+04, 1.15956602e+05, 7.65597344e+04, 7.62872656e+04, 4.18810078e+04, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 6.24638721e+03, 6.24836084e+03, 9.48374902e+03, 6.24584229e+03, 6.25024805e+03, 3.41864526e+03, ],
  }),
  ("nof_tree_events",                 190710),
  ("nof_db_events",                   984200),
  ("fsize_local",                     793863281), # 793.86MB, avg file size 793.86MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Oct31_wPresel_nom_all/ntuples/signal_ggf_nonresonant_cHHH5_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

