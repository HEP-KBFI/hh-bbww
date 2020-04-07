from collections import OrderedDict as OD

# file generated at 2020-04-02 16:15:03 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_ttbar.py -p python/samples/sampleLocations_2017_nanoAOD_ttbar.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_nanoAOD_ttbar.py -M

samples_2017 = OD()
samples_2017["/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTTo2L2Nu_hdampDOWN"),
  ("nof_files",                       55),
  ("nof_db_files",                    85),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5077639),
  ("nof_db_events",                   5476459),
  ("fsize_local",                     10822866465), # 10.82GB, avg file size 196.78MB
  ("fsize_db",                        291527855740), # 291.53GB, avg file size 3.43GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200331_151841"),
        ("selection", "*"),
        ("blacklist", [31, 32, 49, 52]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTTo2L2Nu_hdampDOWN_ext1"),
  ("nof_files",                       101),
  ("nof_db_files",                    254),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 8963000),
  ("nof_db_events",                   9963000),
  ("fsize_local",                     19114277074), # 19.11GB, avg file size 189.25MB
  ("fsize_db",                        534340304188), # 534.34GB, avg file size 2.10GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/200331_152018"),
        ("selection", "*"),
        ("blacklist", [2, 10, 21, 52, 53, 54, 65, 66, 75, 93]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTToSemiLeptonic_hdampDOWN"),
  ("nof_files",                       270),
  ("nof_db_files",                    505),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 26444953),
  ("nof_db_events",                   26849863),
  ("fsize_local",                     58941497044), # 58.94GB, avg file size 218.30MB
  ("fsize_db",                        1453196831832), # 1.45TB, avg file size 2.88GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/200331_152200"),
        ("selection", "*"),
        ("blacklist", [5, 25, 53, 159]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampDown"),
  ("process_name_specific",           "TTToHadronic_hdampDOWN"),
  ("nof_files",                       18),
  ("nof_db_files",                    418),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 597566),
  ("nof_db_events",                   27117982),
  ("fsize_local",                     1363025156), # 1.36GB, avg file size 75.72MB
  ("fsize_db",                        1492982332867), # 1.49TB, avg file size 3.57GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v/200331_152308"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampUp"),
  ("process_name_specific",           "TTTo2L2Nu_hdampUP_ext1"),
  ("nof_files",                       99),
  ("nof_db_files",                    252),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 2373000),
  ("nof_db_events",                   9872999),
  ("fsize_local",                     5109194007), # 5.11GB, avg file size 51.61MB
  ("fsize_db",                        532196934554), # 532.20GB, avg file size 2.11GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/200331_152621"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 5, 6, 9, 15, 20, 21, 23, 24, 25, 26, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 41, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampUp"),
  ("process_name_specific",           "TTToSemiLeptonic_hdampUP"),
  ("nof_files",                       241),
  ("nof_db_files",                    348),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 20192300),
  ("nof_db_events",                   23977012),
  ("fsize_local",                     45459533573), # 45.46GB, avg file size 188.63MB
  ("fsize_db",                        1303431143623), # 1.30TB, avg file size 3.75GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14/200331_152807"),
        ("selection", "*"),
        ("blacklist", [1, 10, 11, 27, 36, 38, 42, 43, 47, 48, 51, 72, 76, 79, 80, 82, 83, 84, 88, 92, 106, 109, 110, 127, 128, 136, 139, 140, 142, 144, 151, 166, 191, 220, 229, 236, 238, 240]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueDown"),
  ("process_name_specific",           "TTTo2L2Nu_ueDown"),
  ("nof_files",                       56),
  ("nof_db_files",                    86),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5400200),
  ("nof_db_events",                   5500000),
  ("fsize_local",                     11562416232), # 11.56GB, avg file size 206.47MB
  ("fsize_db",                        292849978936), # 292.85GB, avg file size 3.41GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200331_153055"),
        ("selection", "*"),
        ("blacklist", [26]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueDown"),
  ("process_name_specific",           "TTToSemiLeptonic_ueDown"),
  ("nof_files",                       231),
  ("nof_db_files",                    330),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 22911672),
  ("nof_db_events",                   22911672),
  ("fsize_local",                     51278220215), # 51.28GB, avg file size 221.98MB
  ("fsize_db",                        1238638894281), # 1.24TB, avg file size 3.75GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/200331_153409"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueDown"),
  ("process_name_specific",           "TTToHadronic_ueDown"),
  ("nof_files",                       274),
  ("nof_db_files",                    460),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 12402592),
  ("nof_db_events",                   27252808),
  ("fsize_local",                     28399184905), # 28.40GB, avg file size 103.65MB
  ("fsize_db",                        1500092628149), # 1.50TB, avg file size 3.26GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/200331_153545"),
        ("selection", "*"),
        ("blacklist", [2, 3, 4, 5, 17, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 42, 43, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 66, 67, 68, 70, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 104, 109, 111, 112, 113, 114, 115, 116, 117, 118, 120, 121, 126, 133, 140, 154, 155, 157, 161, 164, 165, 172, 179, 182, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 206, 207, 208, 209, 212, 215, 216, 223, 224, 225, 226, 227, 228, 229, 232, 233, 234, 235, 237, 240, 242, 246, 247, 249, 252, 254, 255, 258, 260, 261, 269, 270, 271]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueUp"),
  ("process_name_specific",           "TTToHadronic_ueUp"),
  ("nof_files",                       273),
  ("nof_db_files",                    469),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 13573190),
  ("nof_db_events",                   27108792),
  ("fsize_local",                     31160560016), # 31.16GB, avg file size 114.14MB
  ("fsize_db",                        1500611986746), # 1.50TB, avg file size 3.20GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200331_154140"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 5, 14, 15, 16, 25, 28, 29, 31, 32, 35, 36, 42, 47, 48, 49, 54, 61, 62, 63, 64, 65, 66, 67, 68, 69, 73, 74, 77, 80, 87, 90, 91, 92, 97, 102, 103, 110, 118, 120, 122, 124, 125, 128, 129, 130, 131, 133, 137, 138, 141, 142, 143, 144, 145, 146, 147, 148, 150, 151, 153, 154, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 176, 177, 179, 180, 182, 183, 184, 187, 189, 192, 196, 197, 198, 200, 201, 202, 203, 205, 206, 210, 212, 214, 217, 218, 221, 225, 229, 230, 232, 234, 235, 241, 245, 246, 250, 251, 252, 253, 254, 255, 256, 258, 259, 260, 261, 263, 264, 266, 267, 269, 270, 271, 272]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_QCDbased"),
  ("process_name_specific",           "TTTo2L2Nu_QCDbased_ext1"),
  ("nof_files",                       101),
  ("nof_db_files",                    274),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 239000),
  ("nof_db_events",                   9999000),
  ("fsize_local",                     517993312), # 517.99MB, avg file size 5.13MB
  ("fsize_db",                        544472722769), # 544.47GB, avg file size 1.99GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/200331_154455"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_QCDbased"),
  ("process_name_specific",           "TTToHadronic_QCDbased"),
  ("nof_files",                       274),
  ("nof_db_files",                    537),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9841000),
  ("nof_db_events",                   27341000),
  ("fsize_local",                     22730819791), # 22.73GB, avg file size 82.96MB
  ("fsize_db",                        1534244543624), # 1.53TB, avg file size 2.86GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/200331_154811"),
        ("selection", "*"),
        ("blacklist", [1, 3, 4, 5, 8, 11, 22, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 73, 74, 75, 76, 78, 80, 81, 85, 86, 90, 91, 97, 100, 101, 103, 106, 107, 114, 115, 116, 117, 118, 120, 122, 124, 126, 127, 128, 130, 135, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 163, 164, 168, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 202, 203, 204, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 230, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 252, 253, 254, 255, 256, 257, 258, 259, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_GluonMove"),
  ("process_name_specific",           "TTTo2L2Nu_GluonMove_ext1"),
  ("nof_files",                       107),
  ("nof_db_files",                    258),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 3722000),
  ("nof_db_events",                   9818000),
  ("fsize_local",                     7998468319), # 8.00GB, avg file size 74.75MB
  ("fsize_db",                        530494659584), # 530.49GB, avg file size 2.06GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/200331_155123"),
        ("selection", "*"),
        ("blacklist", [2, 3, 4, 5, 7, 8, 10, 11, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 63, 67, 69, 72, 73, 74, 75, 76, 77, 78, 85, 86, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 104, 105]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_GluonMove"),
  ("process_name_specific",           "TTToSemiLeptonic_GluonMove"),
  ("nof_files",                       288),
  ("nof_db_files",                    639),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 16274000),
  ("nof_db_events",                   27409000),
  ("fsize_local",                     36542323197), # 36.54GB, avg file size 126.88MB
  ("fsize_db",                        1502331258937), # 1.50TB, avg file size 2.35GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/200331_155259"),
        ("selection", "*"),
        ("blacklist", [2, 7, 9, 11, 12, 13, 14, 15, 16, 21, 24, 26, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 46, 49, 52, 58, 59, 60, 61, 62, 63, 65, 66, 68, 69, 71, 72, 73, 74, 75, 76, 77, 79, 81, 85, 86, 87, 89, 90, 92, 98, 99, 103, 105, 106, 109, 114, 115, 118, 120, 122, 126, 131, 132, 133, 135, 138, 144, 146, 149, 150, 151, 152, 154, 155, 157, 158, 160, 162, 165, 169, 173, 181, 184, 187, 190, 191, 194, 203, 205, 208, 212, 213, 219, 220, 221, 223, 226, 228, 229, 230, 253, 264, 267, 271, 273, 274, 281, 285, 286, 287]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_GluonMove"),
  ("process_name_specific",           "TTToHadronic_GluonMove"),
  ("nof_files",                       275),
  ("nof_db_files",                    602),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 16969000),
  ("nof_db_events",                   27469000),
  ("fsize_local",                     38918594072), # 38.92GB, avg file size 141.52MB
  ("fsize_db",                        1530584055949), # 1.53TB, avg file size 2.54GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/200331_155437"),
        ("selection", "*"),
        ("blacklist", [5, 6, 7, 8, 12, 14, 15, 17, 18, 20, 24, 25, 26, 31, 32, 33, 34, 35, 36, 38, 41, 42, 43, 47, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 72, 73, 76, 78, 80, 86, 88, 89, 90, 95, 97, 103, 109, 110, 113, 114, 115, 117, 118, 119, 120, 121, 128, 139, 142, 143, 144, 145, 146, 147, 148, 149, 158, 168, 170, 171, 178, 183, 184, 186, 188, 195, 196, 197, 199, 201, 202, 208, 213, 214, 215, 220, 225, 227, 236, 266, 267, 268, 269, 270, 271, 272, 273]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_erdON"),
  ("process_name_specific",           "TTTo2L2Nu_erdON"),
  ("nof_files",                       51),
  ("nof_db_files",                    162),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4792000),
  ("nof_db_events",                   5092000),
  ("fsize_local",                     10348898016), # 10.35GB, avg file size 202.92MB
  ("fsize_db",                        274704284910), # 274.70GB, avg file size 1.70GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/200331_155544"),
        ("selection", "*"),
        ("blacklist", [34, 38, 39]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_erdON"),
  ("process_name_specific",           "TTTo2L2Nu_erdON_ext1"),
  ("nof_files",                       117),
  ("nof_db_files",                    235),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 7004000),
  ("nof_db_events",                   9966000),
  ("fsize_local",                     15173375433), # 15.17GB, avg file size 129.69MB
  ("fsize_db",                        541613889407), # 541.61GB, avg file size 2.30GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/200331_155722"),
        ("selection", "*"),
        ("blacklist", [1, 3, 4, 11, 12, 13, 20, 32, 33, 41, 42, 45, 54, 57, 58, 59, 60, 61, 62, 63, 68, 71, 73, 74, 78, 79, 82, 83, 86, 96]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_erdON"),
  ("process_name_specific",           "TTToSemiLeptonic_erdON"),
  ("nof_files",                       92),
  ("nof_db_files",                    658),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9117000),
  ("nof_db_events",                   27292000),
  ("fsize_local",                     20534826249), # 20.53GB, avg file size 223.20MB
  ("fsize_db",                        1492517947810), # 1.49TB, avg file size 2.27GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/200331_155857"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_erdON"),
  ("process_name_specific",           "TTToHadronic_erdON"),
  ("nof_files",                       65),
  ("nof_db_files",                    457),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4300000),
  ("nof_db_events",                   26893000),
  ("fsize_local",                     9880442171), # 9.88GB, avg file size 152.01MB
  ("fsize_db",                        1491456606989), # 1.49TB, avg file size 3.26GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/200331_160039"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 16, 18, 21, 22, 26, 30, 31, 39, 40, 45, 46, 48, 52, 53, 56, 59, 64]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop166p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop166p5"),
  ("nof_files",                       6),
  ("nof_db_files",                    51),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98575),
  ("nof_db_events",                   2430849),
  ("fsize_local",                     208648017), # 208.65MB, avg file size 34.77MB
  ("fsize_db",                        129108353493), # 129.11GB, avg file size 2.53GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_mtop166p5_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_mtop166p5_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/200331_160144"),
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

samples_2017["/TTTo2L2Nu_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop166p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop166p5_PSweights"),
  ("nof_files",                       26),
  ("nof_db_files",                    42),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 2500000),
  ("nof_db_events",                   2500000),
  ("fsize_local",                     5290613473), # 5.29GB, avg file size 203.49MB
  ("fsize_db",                        132728814159), # 132.73GB, avg file size 3.16GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/200331_160322"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop166p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop166p5_PSweights"),
  ("nof_files",                       96),
  ("nof_db_files",                    147),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9155560),
  ("nof_db_events",                   9553066),
  ("fsize_local",                     20235610982), # 20.24GB, avg file size 210.79MB
  ("fsize_db",                        515058612689), # 515.06GB, avg file size 3.50GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/200331_160636"),
        ("selection", "*"),
        ("blacklist", [40, 75, 77, 94]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop166p5"),
  ("process_name_specific",           "TTToHadronic_mtop166p5"),
  ("nof_files",                       96),
  ("nof_db_files",                    186),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 7364480),
  ("nof_db_events",                   9694576),
  ("fsize_local",                     16580646741), # 16.58GB, avg file size 172.72MB
  ("fsize_db",                        532391268393), # 532.39GB, avg file size 2.86GB
  ("use_it",                          False),
  ("xsection",                        377.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/200331_160816"),
        ("selection", "*"),
        ("blacklist", [3, 6, 7, 12, 13, 15, 18, 22, 25, 27, 29, 36, 42, 60, 64, 66, 72, 73, 85, 89, 93, 94]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop169p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop169p5_ext1"),
  ("nof_files",                       97),
  ("nof_db_files",                    232),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9174000),
  ("nof_db_events",                   9674000),
  ("fsize_local",                     19546033711), # 19.55GB, avg file size 201.51MB
  ("fsize_db",                        518706712218), # 518.71GB, avg file size 2.24GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/200331_161239"),
        ("selection", "*"),
        ("blacklist", [1, 61, 83, 87, 96]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop169p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop169p5_ext1"),
  ("nof_files",                       56),
  ("nof_db_files",                    257),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 500000),
  ("nof_db_events",                   9858000),
  ("fsize_local",                     1112562305), # 1.11GB, avg file size 19.87MB
  ("fsize_db",                        537017483165), # 537.02GB, avg file size 2.09GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-/200331_161551"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop169p5"),
  ("process_name_specific",           "TTToHadronic_mtop169p5"),
  ("nof_files",                       41),
  ("nof_db_files",                    411),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 1600000),
  ("nof_db_events",                   18739000),
  ("fsize_local",                     3641048802), # 3.64GB, avg file size 88.81MB
  ("fsize_db",                        1035722135319), # 1.04TB, avg file size 2.52GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/200331_161729"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 7, 8, 10, 12, 13, 15, 16, 18, 19, 20, 21, 22, 27, 29, 30, 31, 32, 34, 36, 40]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop173p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop173p5"),
  ("nof_files",                       61),
  ("nof_db_files",                    120),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 6000000),
  ("nof_db_events",                   6000000),
  ("fsize_local",                     12895766762), # 12.90GB, avg file size 211.41MB
  ("fsize_db",                        320956100851), # 320.96GB, avg file size 2.67GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200331_162405"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop173p5"),
  ("process_name_specific",           "TTToHadronic_mtop173p5"),
  ("nof_files",                       229),
  ("nof_db_files",                    529),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 1400000),
  ("nof_db_events",                   24373000),
  ("fsize_local",                     3215494157), # 3.22GB, avg file size 14.04MB
  ("fsize_db",                        1353482022084), # 1.35TB, avg file size 2.56GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/200331_162724"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 167, 168, 169, 170, 171, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 219, 220, 228]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop175p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop175p5"),
  ("nof_files",                       43),
  ("nof_db_files",                    90),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 996000),
  ("nof_db_events",                   4987400),
  ("fsize_local",                     2148772027), # 2.15GB, avg file size 49.97MB
  ("fsize_db",                        267023588385), # 267.02GB, avg file size 2.97GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200331_162902"),
        ("selection", "*"),
        ("blacklist", [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 16, 17, 18, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 42]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop175p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop175p5_ext1"),
  ("nof_files",                       99),
  ("nof_db_files",                    237),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9658000),
  ("nof_db_events",                   9858000),
  ("fsize_local",                     21788586760), # 21.79GB, avg file size 220.09MB
  ("fsize_db",                        540202026504), # 540.20GB, avg file size 2.28GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-/200331_163332"),
        ("selection", "*"),
        ("blacklist", [8, 11]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  [ 'TTTo2L2Nu_mtop169p5',                             'TTTo2L2Nu_mtop169p5_ext1',                         ],
  [ 'TTTo2L2Nu_GluonMove',                             'TTTo2L2Nu_GluonMove_ext1',                         ],
  [ 'TTTo2L2Nu_erdON',                                 'TTTo2L2Nu_erdON_ext1',                             ],
  [ 'TTTo2L2Nu_hdampUP',                               'TTTo2L2Nu_hdampUP_ext1',                           ],
  [ 'TTTo2L2Nu_QCDbased',                              'TTTo2L2Nu_QCDbased_ext1',                          ],
  [ 'TTTo2L2Nu_ueDown',                                'TTTo2L2Nu_ueDown_ext1',                            ],
  [ 'TTTo2L2Nu_ueUp',                                  'TTTo2L2Nu_ueUp_ext1',                              ],
  [ 'TTTo2L2Nu_mtop178p5',                             'TTTo2L2Nu_mtop178p5_PSweights',                    ],
  [ 'TTToSemiLeptonic_mtop166p5',                      'TTToSemiLeptonic_mtop166p5_PSweights',             ],
  [ 'TTToSemiLeptonic_mtop169p5',                      'TTToSemiLeptonic_mtop169p5_ext1',                  ],
  [ 'TTTo2L2Nu_mtop166p5',                             'TTTo2L2Nu_mtop166p5_PSweights',                    ],
  [ 'TTTo2L2Nu_mtop175p5',                             'TTTo2L2Nu_mtop175p5_ext1',                         ],
  [ 'TTTo2L2Nu_hdampDOWN',                             'TTTo2L2Nu_hdampDOWN_ext1',                         ],
  [ 'TTToHadronic_mtop166p5',                          'TTToHadronic_mtop166p5_PSweights',                 ],
  [ 'TTToSemiLeptonic_mtop178p5',                      'TTToSemiLeptonic_mtop178p5_PSweights',             ],
  [ 'TTToSemiLeptonic_mtop175p5',                      'TTToSemiLeptonic_mtop175p5_ext1',                  ],
]

