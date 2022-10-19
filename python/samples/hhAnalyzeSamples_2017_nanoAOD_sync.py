from collections import OrderedDict as OD

# file generated at 2020-03-03 10:50:54 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh_sync.py -p /local/karl/sync_ntuples/2017/nanoAODproduction/2019Dec06 -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_nanoAOD_sync.py -M

samples_2017 = OD()
samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 52000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     127116545), # 127.12MB, avg file size 127.12MB
  ("fsize_db",                        11931037531), # 11.93GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.027654),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/sync_ntuples/2017/nanoAODproduction/2019Dec06/signal_ggf_spin0_750_hh_2b2v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

