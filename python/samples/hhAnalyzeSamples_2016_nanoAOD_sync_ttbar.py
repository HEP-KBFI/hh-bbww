from collections import OrderedDict as OD

# file generated at 2020-04-23 11:55:41 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh_sync_ttbar.py -p /hdfs/local/snandan/sync_ntuples/2016/nanoAODproduction/2020Apr22 -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_nanoAOD_sync_ttbar.py -M

samples_2016 = OD()
samples_2016["/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "background"),
  ("process_name_specific",           "TTTo2L2Nu"),
  ("nof_files",                       1),
  ("nof_db_files",                    778),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 47200),
  ("nof_db_events",                   67926800),
  ("fsize_local",                     124972754), # 124.97MB, avg file size 124.97MB
  ("fsize_db",                        2988515757147), # 2.99TB, avg file size 3.84GB
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
        ("path",      "/hdfs/local/snandan/sync_ntuples/2016/nanoAODproduction/2020Apr22/TTTo2L2Nu"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
]

