from collections import OrderedDict as OD

# file generated at 2020-04-23 11:57:45 with the following command:
# create_dictionary.py -m python/samples/metaDict_2018_hh_sync_ttbar.py -p /local/snandan/sync_ntuples/2018/nanoAODproduction/2020Apr22 -N samples_2018 -E 2018 -o python/samples -g hhAnalyzeSamples_2018_nanoAOD_sync_ttbar.py -M

samples_2018 = OD()
samples_2018["/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "background"),
  ("process_name_specific",           "TTTo2L2Nu"),
  ("nof_files",                       1),
  ("nof_db_files",                    968),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   64310000),
  ("fsize_local",                     132661673), # 132.66MB, avg file size 132.66MB
  ("fsize_db",                        3413760837047), # 3.41TB, avg file size 3.53GB
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
        ("path",      "/local/snandan/sync_ntuples/2018/nanoAODproduction/2020Apr22/TTTo2L2Nu"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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
]

