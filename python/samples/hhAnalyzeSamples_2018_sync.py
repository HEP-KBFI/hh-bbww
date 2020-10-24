from collections import OrderedDict as OD

# file generated at 2020-10-24 22:13:06 with the following command:
# create_dictionary.py -m python/samples/metaDict_2018_hh_sync.py -p /hdfs/local/karl/ttHNtupleProduction/2018/2020Oct24_woPresel_nonNom_hh_bbww_sync/ntuples -N samples_2018 -E 2018 -o python/samples -g hhAnalyzeSamples_2018_sync.py -M

samples_2018 = OD()
samples_2018["/GluGluToRadionToHHTo2B2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 42000, ],
    'CountWeighted'                                                                  : [ 4.19596836e+04, 4.19609219e+04, 4.19518242e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.19596836e+04, 4.19596836e+04, ],
    'CountWeightedFull'                                                              : [ 4.19560547e+04, 4.19573594e+04, 4.19482500e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.19560547e+04, 4.19560547e+04, ],
  }),
  ("nof_tree_events",                 42000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     202632307), # 202.63MB, avg file size 202.63MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Oct24_woPresel_nonNom_hh_bbww_sync/ntuples/signal_ggf_spin0_750_hh_2b2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
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

