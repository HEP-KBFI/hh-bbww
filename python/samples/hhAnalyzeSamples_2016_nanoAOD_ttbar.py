from collections import OrderedDict as OD

# file generated at 2020-04-02 16:02:44 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_ttbar.py -p python/samples/sampleLocations_2016_nanoAOD_ttbar.txt -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_nanoAOD_ttbar.py -M

samples_2016 = OD()
samples_2016["/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTTo2L2Nu_hdampDOWN"),
  ("nof_files",                       100),
  ("nof_db_files",                    143),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9763600),
  ("nof_db_events",                   9963900),
  ("fsize_local",                     20858284951), # 20.86GB, avg file size 208.58MB
  ("fsize_db",                        440499394219), # 440.50GB, avg file size 3.08GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_130304"),
        ("selection", "*"),
        ("blacklist", [47, 75]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTTo2L2Nu_hdampDOWN_ext1"),
  ("nof_files",                       50),
  ("nof_db_files",                    112),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4944800),
  ("nof_db_events",                   4944800),
  ("fsize_local",                     10567951648), # 10.57GB, avg file size 211.36MB
  ("fsize_db",                        218167419681), # 218.17GB, avg file size 1.95GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/200331_131019"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTToSemiLeptonic_hdampDOWN"),
  ("nof_files",                       296),
  ("nof_db_files",                    414),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 19575100),
  ("nof_db_events",                   29818400),
  ("fsize_local",                     43813764923), # 43.81GB, avg file size 148.02MB
  ("fsize_db",                        1348075651578), # 1.35TB, avg file size 3.26GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_132134"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 13, 14, 21, 22, 34, 37, 39, 40, 41, 42, 46, 52, 57, 58, 62, 68, 69, 73, 74, 78, 79, 82, 88, 91, 97, 99, 108, 110, 111, 112, 116, 121, 124, 128, 129, 132, 133, 139, 140, 147, 157, 158, 159, 160, 166, 170, 179, 182, 186, 209, 213, 215, 216, 219, 220, 222, 223, 226, 229, 235, 237, 238, 239, 244, 245, 247, 248, 250, 251, 253, 255, 256, 257, 262, 263, 264, 265, 267, 269, 270, 271, 273, 275, 277, 278, 280, 283, 284, 285, 286, 287, 288, 289, 291, 294]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTToHadronic_hdampDOWN"),
  ("nof_files",                       303),
  ("nof_db_files",                    411),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 19437100),
  ("nof_db_events",                   28900700),
  ("fsize_local",                     44456619404), # 44.46GB, avg file size 146.72MB
  ("fsize_db",                        1338002370689), # 1.34TB, avg file size 3.26GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/200331_133751"),
        ("selection", "*"),
        ("blacklist", [2, 3, 13, 16, 17, 22, 23, 25, 30, 33, 36, 40, 43, 50, 51, 55, 58, 59, 60, 61, 62, 66, 67, 69, 71, 72, 73, 77, 78, 79, 80, 83, 86, 87, 93, 97, 99, 100, 103, 104, 110, 111, 112, 115, 116, 119, 127, 128, 133, 136, 138, 144, 145, 147, 148, 150, 153, 159, 164, 165, 166, 167, 170, 172, 175, 176, 177, 178, 180, 184, 185, 186, 188, 189, 190, 192, 194, 196, 197, 198, 202, 206, 207, 214, 217, 220, 223, 225, 227, 228, 229, 249, 282, 286, 290, 293, 298]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampUp"),
  ("process_name_specific",           "TTTo2L2Nu_hdampUP"),
  ("nof_files",                       100),
  ("nof_db_files",                    143),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9923800),
  ("nof_db_events",                   9923800),
  ("fsize_local",                     21429245481), # 21.43GB, avg file size 214.29MB
  ("fsize_db",                        440216123353), # 440.22GB, avg file size 3.08GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_134230"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampUp"),
  ("process_name_specific",           "TTTo2L2Nu_hdampUP_ext1"),
  ("nof_files",                       44),
  ("nof_db_files",                    93),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 1798000),
  ("nof_db_events",                   4965300),
  ("fsize_local",                     3884002530), # 3.88GB, avg file size 88.27MB
  ("fsize_db",                        220079948375), # 220.08GB, avg file size 2.37GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/200331_135847"),
        ("selection", "*"),
        ("blacklist", [1, 3, 4, 7, 9, 10, 11, 12, 13, 15, 17, 18, 20, 22, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 43]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampUp"),
  ("process_name_specific",           "TTToSemiLeptonic_hdampUP"),
  ("nof_files",                       22),
  ("nof_db_files",                    385),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 699200),
  ("nof_db_events",                   29671272),
  ("fsize_local",                     1579951923), # 1.58GB, avg file size 71.82MB
  ("fsize_db",                        1349067910706), # 1.35TB, avg file size 3.50GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_140232"),
        ("selection", "*"),
        ("blacklist", [2, 4, 5, 6, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampUp"),
  ("process_name_specific",           "TTToHadronic_hdampUP"),
  ("nof_files",                       161),
  ("nof_db_files",                    396),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 11090400),
  ("nof_db_events",                   28695100),
  ("fsize_local",                     25609335977), # 25.61GB, avg file size 159.06MB
  ("fsize_db",                        1337128214755), # 1.34TB, avg file size 3.38GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_140410"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 8, 9, 12, 14, 15, 16, 21, 26, 27, 29, 33, 35, 44, 45, 48, 57, 58, 59, 63, 66, 72, 74, 75, 78, 85, 86, 92, 93, 96, 97, 98, 104, 106, 107, 114, 120, 123, 128, 132, 138, 139, 140, 143, 144, 158]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueDown"),
  ("process_name_specific",           "TTTo2L2Nu_ueDown"),
  ("nof_files",                       95),
  ("nof_db_files",                    136),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 8216700),
  ("nof_db_events",                   9414200),
  ("fsize_local",                     17637419694), # 17.64GB, avg file size 185.66MB
  ("fsize_db",                        414089278252), # 414.09GB, avg file size 3.04GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_141023"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 10, 27, 33, 35, 45, 66, 70]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueDown"),
  ("process_name_specific",           "TTTo2L2Nu_ueDown_ext1"),
  ("nof_files",                       50),
  ("nof_db_files",                    95),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4852600),
  ("nof_db_events",                   4952600),
  ("fsize_local",                     10414614529), # 10.41GB, avg file size 208.29MB
  ("fsize_db",                        217895870557), # 217.90GB, avg file size 2.29GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/200331_141158"),
        ("selection", "*"),
        ("blacklist", [45]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueDown"),
  ("process_name_specific",           "TTToSemiLeptonic_ueDown"),
  ("nof_files",                       7),
  ("nof_db_files",                    415),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199600),
  ("nof_db_events",                   28951700),
  ("fsize_local",                     448947987), # 448.95MB, avg file size 64.14MB
  ("fsize_db",                        1305952192284), # 1.31TB, avg file size 3.15GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_141334"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueDown"),
  ("process_name_specific",           "TTToHadronic_ueDown"),
  ("nof_files",                       295),
  ("nof_db_files",                    372),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 16812100),
  ("nof_db_events",                   27921200),
  ("fsize_local",                     38611237173), # 38.61GB, avg file size 130.89MB
  ("fsize_db",                        1289925205797), # 1.29TB, avg file size 3.47GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_141512"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 36, 37, 38, 39, 40, 49, 51, 53, 56, 57, 58, 59, 60, 61, 63, 65, 66, 68, 69, 70, 71, 72, 74, 75, 76, 79, 80, 81, 82, 83, 84, 86, 87, 187, 188, 201, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 220, 221, 222, 223, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 263, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 280, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueUp"),
  ("process_name_specific",           "TTTo2L2Nu_ueUp"),
  ("nof_files",                       91),
  ("nof_db_files",                    144),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 3200000),
  ("nof_db_events",                   9851000),
  ("fsize_local",                     6887513741), # 6.89GB, avg file size 75.69MB
  ("fsize_db",                        436397875157), # 436.40GB, avg file size 3.03GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_141648"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 7, 9, 11, 12, 13, 14, 15, 18, 20, 21, 22, 23, 25, 26, 28, 29, 30, 32, 34, 35, 36, 39, 41, 43, 44, 46, 52, 54, 56, 59, 61, 62, 63, 64, 65, 66, 69, 70, 72, 73, 74, 75, 76, 77, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueUp"),
  ("process_name_specific",           "TTTo2L2Nu_ueUp_ext1"),
  ("nof_files",                       50),
  ("nof_db_files",                    79),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4687600),
  ("nof_db_events",                   4987600),
  ("fsize_local",                     10085511096), # 10.09GB, avg file size 201.71MB
  ("fsize_db",                        220909282587), # 220.91GB, avg file size 2.80GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/200331_141928"),
        ("selection", "*"),
        ("blacklist", [4, 29, 34]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueUp"),
  ("process_name_specific",           "TTToHadronic_ueUp"),
  ("nof_files",                       240),
  ("nof_db_files",                    400),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 11476300),
  ("nof_db_events",                   27939400),
  ("fsize_local",                     26414849320), # 26.41GB, avg file size 110.06MB
  ("fsize_db",                        1300075329090), # 1.30TB, avg file size 3.25GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_142213"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 7, 8, 9, 10, 15, 18, 21, 26, 28, 29, 34, 35, 36, 37, 38, 39, 42, 43, 45, 46, 47, 52, 53, 57, 58, 59, 60, 61, 66, 71, 72, 73, 75, 76, 78, 81, 82, 84, 86, 87, 89, 90, 92, 94, 95, 96, 97, 99, 102, 105, 106, 107, 110, 111, 112, 117, 119, 120, 124, 127, 132, 135, 138, 139, 140, 141, 143, 145, 147, 148, 149, 151, 152, 155, 158, 159, 161, 162, 165, 166, 167, 170, 171, 173, 175, 176, 180, 181, 183, 184, 185, 189, 190, 191, 193, 196, 197, 198, 199, 207, 210, 211, 212, 214, 216, 218, 219, 220, 224, 228, 229, 230, 231, 232, 234, 236, 237, 238, 239]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_QCDbased"),
  ("process_name_specific",           "TTTo2L2Nu_QCDbased"),
  ("nof_files",                       149),
  ("nof_db_files",                    186),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 14746400),
  ("nof_db_events",                   14846400),
  ("fsize_local",                     31911777567), # 31.91GB, avg file size 214.17MB
  ("fsize_db",                        663165284807), # 663.17GB, avg file size 3.57GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_142421"),
        ("selection", "*"),
        ("blacklist", [6]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_QCDbased"),
  ("process_name_specific",           "TTToSemiLeptonic_QCDbased"),
  ("nof_files",                       294),
  ("nof_db_files",                    458),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 10808200),
  ("nof_db_events",                   29208200),
  ("fsize_local",                     24499250787), # 24.50GB, avg file size 83.33MB
  ("fsize_db",                        1339803390539), # 1.34TB, avg file size 2.93GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_142527"),
        ("selection", "*"),
        ("blacklist", [3, 5, 8, 13, 16, 18, 19, 26, 27, 36, 42, 44, 46, 49, 51, 54, 55, 63, 66, 69, 73, 74, 75, 77, 79, 80, 81, 82, 84, 85, 89, 95, 96, 98, 99, 103, 108, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 127, 129, 130, 131, 132, 133, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 152, 153, 154, 155, 157, 159, 160, 161, 162, 164, 165, 166, 167, 168, 169, 170, 172, 173, 174, 175, 176, 177, 178, 179, 180, 182, 183, 184, 185, 187, 188, 189, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 224, 226, 227, 228, 229, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 263, 266, 267, 268, 269, 270, 272, 274, 276, 278, 279, 281, 282, 284, 286, 288, 290, 293]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_QCDbased"),
  ("process_name_specific",           "TTToHadronic_QCDbased"),
  ("nof_files",                       289),
  ("nof_db_files",                    352),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 6786000),
  ("nof_db_events",                   27446200),
  ("fsize_local",                     15746004728), # 15.75GB, avg file size 54.48MB
  ("fsize_db",                        1287103451975), # 1.29TB, avg file size 3.66GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_142733"),
        ("selection", "*"),
        ("blacklist", [4, 5, 10, 11, 15, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 36, 47, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 142, 144, 145, 146, 147, 148, 149, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 251, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_GluonMove"),
  ("process_name_specific",           "TTTo2L2Nu_GluonMove"),
  ("nof_files",                       160),
  ("nof_db_files",                    222),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 10540600),
  ("nof_db_events",                   13515700),
  ("fsize_local",                     22715516373), # 22.72GB, avg file size 141.97MB
  ("fsize_db",                        598185262238), # 598.19GB, avg file size 2.69GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_142909"),
        ("selection", "*"),
        ("blacklist", [1, 3, 4, 5, 25, 37, 40, 44, 45, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 110, 114, 115, 116, 117, 118, 123, 124, 125, 128, 132, 154, 155, 156, 157, 158, 159]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_GluonMove"),
  ("process_name_specific",           "TTToSemiLeptonic_GluonMove"),
  ("nof_files",                       274),
  ("nof_db_files",                    322),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 10273200),
  ("nof_db_events",                   26468200),
  ("fsize_local",                     23150070752), # 23.15GB, avg file size 84.49MB
  ("fsize_db",                        1198509880349), # 1.20TB, avg file size 3.72GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_143044"),
        ("selection", "*"),
        ("blacklist", [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 124, 137, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 213, 218, 223]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_GluonMove"),
  ("process_name_specific",           "TTToHadronic_GluonMove"),
  ("nof_files",                       284),
  ("nof_db_files",                    413),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 10673000),
  ("nof_db_events",                   28881600),
  ("fsize_local",                     24576817671), # 24.58GB, avg file size 86.54MB
  ("fsize_db",                        1342210039307), # 1.34TB, avg file size 3.25GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_143221"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 34, 45, 55, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 170, 172, 173, 174, 175, 176, 177, 178, 179, 185, 187, 189, 191, 193, 196, 197, 198, 199, 200, 201, 202, 205, 207, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 276, 278, 279]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_erdON"),
  ("process_name_specific",           "TTTo2L2Nu_erdON"),
  ("nof_files",                       98),
  ("nof_db_files",                    215),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 8325600),
  ("nof_db_events",                   9725600),
  ("fsize_local",                     18018577226), # 18.02GB, avg file size 183.86MB
  ("fsize_db",                        432559736598), # 432.56GB, avg file size 2.01GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_143356"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 8, 9, 10, 64, 76, 82, 84, 88, 89]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_erdON"),
  ("process_name_specific",           "TTTo2L2Nu_erdON_ext1"),
  ("nof_files",                       65),
  ("nof_db_files",                    130),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4737700),
  ("nof_db_events",                   4837600),
  ("fsize_local",                     10299474116), # 10.30GB, avg file size 158.45MB
  ("fsize_db",                        214453762002), # 214.45GB, avg file size 1.65GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/200331_143536"),
        ("selection", "*"),
        ("blacklist", [59]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToSemiLeptonic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_erdON"),
  ("process_name_specific",           "TTToSemiLeptonic_erdON"),
  ("nof_files",                       302),
  ("nof_db_files",                    433),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5538400),
  ("nof_db_events",                   28973400),
  ("fsize_local",                     12533645279), # 12.53GB, avg file size 41.50MB
  ("fsize_db",                        1316453559336), # 1.32TB, avg file size 3.04GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToSemiLeptonic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_143712"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 7, 10, 15, 17, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 140, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 185, 197, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 258, 262, 263, 264, 265, 266, 267, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 298, 299, 300]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToHadronic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_erdON"),
  ("process_name_specific",           "TTToHadronic_erdON"),
  ("nof_files",                       281),
  ("nof_db_files",                    424),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 7839000),
  ("nof_db_events",                   27338000),
  ("fsize_local",                     18079752717), # 18.08GB, avg file size 64.34MB
  ("fsize_db",                        1273462459025), # 1.27TB, avg file size 3.00GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToHadronic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToHadronic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/200331_144020"),
        ("selection", "*"),
        ("blacklist", [46, 50, 51, 52, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 155, 156, 159, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 246, 247, 248, 249, 250, 251, 252, 253, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 278, 280]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop169p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop169p5_PSweights_backup"),
  ("nof_files",                       11),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 989200),
  ("nof_db_events",                   989200),
  ("fsize_local",                     2114549551), # 2.11GB, avg file size 192.23MB
  ("fsize_db",                        43359624747), # 43.36GB, avg file size 4.82GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/200331_144157"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToSemiLeptonic_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop169p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop169p5_PSweights_backup"),
  ("nof_files",                       22),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 1864000),
  ("nof_db_events",                   2042800),
  ("fsize_local",                     4171203066), # 4.17GB, avg file size 189.60MB
  ("fsize_db",                        91708676625), # 91.71GB, avg file size 4.37GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToSemiLeptonic_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/200331_144435"),
        ("selection", "*"),
        ("blacklist", [3, 4]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTTo2L2Nu_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop175p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop175p5_PSweights_backup"),
  ("nof_files",                       41),
  ("nof_db_files",                    72),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 2168200),
  ("nof_db_events",                   2431800),
  ("fsize_local",                     4738460458), # 4.74GB, avg file size 115.57MB
  ("fsize_db",                        108213630785), # 108.21GB, avg file size 1.50GB
  ("use_it",                          False),
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTTo2L2Nu_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8/2016v3_2020Mar31_TTTo2L2Nu_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/200331_144742"),
        ("selection", "*"),
        ("blacklist", [12, 13]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/TTToSemiLeptonic_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop175p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop175p5_PSweights_backup"),
  ("nof_files",                       25),
  ("nof_db_files",                    31),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 2066800),
  ("nof_db_events",                   2703600),
  ("fsize_local",                     4686651051), # 4.69GB, avg file size 187.47MB
  ("fsize_db",                        122243863139), # 122.24GB, avg file size 3.94GB
  ("use_it",                          False),
  ("xsection",                        365.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Mar31/TTToSemiLeptonic_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8/2016v3_2020Mar31_TTToSemiLeptonic_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/200331_144920"),
        ("selection", "*"),
        ("blacklist", [2, 5]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  [ 'TTTo2L2Nu_ueUp',                                  'TTTo2L2Nu_ueUp_ext1',                              ],
  [ 'TTTo2L2Nu_hdampDOWN',                             'TTTo2L2Nu_hdampDOWN_ext1',                         ],
  [ 'TTTo2L2Nu_erdON',                                 'TTTo2L2Nu_erdON_ext1',                             ],
  [ 'TTTo2L2Nu_ueDown',                                'TTTo2L2Nu_ueDown_ext1',                            ],
  [ 'TTTo2L2Nu_hdampUP',                               'TTTo2L2Nu_hdampUP_ext1',                           ],
]

