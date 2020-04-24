from collections import OrderedDict as OD

# file generated at 2020-04-23 11:58:20 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh_sync_ttbar.py -p /hdfs/local/snandan/sync_ntuples/2017/nanoAODproduction/2020Apr22 -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_nanoAOD_sync_ttbar.py -M

samples_2017 = OD()
samples_2017["/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "background"),
  ("process_name_specific",           "TTTo2L2Nu_PSweights"),
  ("nof_files",                       1),
  ("nof_db_files",                    1056),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 47260),
  ("nof_db_events",                   69155808),
  ("fsize_local",                     126566452), # 126.57MB, avg file size 126.57MB
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
        ("path",      "/hdfs/local/snandan/sync_ntuples/2017/nanoAODproduction/2020Apr22/TTTo2L2Nu_PSweights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

