from collections import OrderedDict as OD

# file generated at 2020-10-17 17:41:44 with the following command:
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
  ("nof_tree_events",                 5476459),
  ("nof_db_events",                   5476459),
  ("fsize_local",                     11672907411), # 11.67GB, avg file size 212.23MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 9963000),
  ("nof_db_events",                   9963000),
  ("fsize_local",                     21244154851), # 21.24GB, avg file size 210.34MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 26849863),
  ("nof_db_events",                   26849863),
  ("fsize_local",                     59843810789), # 59.84GB, avg file size 221.64MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       273),
  ("nof_db_files",                    418),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 26422090),
  ("nof_db_events",                   27117982),
  ("fsize_local",                     60254468461), # 60.25GB, avg file size 220.71MB
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
        ("blacklist", [1, 187, 190, 208, 210, 233, 239]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampUp"),
  ("process_name_specific",           "TTTo2L2Nu_hdampUP"),
  ("nof_files",                       67),
  ("nof_db_files",                    67),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 3288128),
  ("nof_db_events",                   3288128),
  ("fsize_local",                     7185058060), # 7.19GB, avg file size 107.24MB
  ("fsize_db",                        176301752654), # 176.30GB, avg file size 2.63GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Apr22/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Apr22_TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200422_130616"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 9872999),
  ("nof_db_events",                   9872999),
  ("fsize_local",                     21263965772), # 21.26GB, avg file size 214.79MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 23977012),
  ("nof_db_events",                   23977012),
  ("fsize_local",                     53980874377), # 53.98GB, avg file size 223.99MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_hdampUp"),
  ("process_name_specific",           "TTToHadronic_hdampUP"),
  ("nof_files",                       274),
  ("nof_db_files",                    489),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 25964520),
  ("nof_db_events",                   27260880),
  ("fsize_local",                     59780067779), # 59.78GB, avg file size 218.18MB
  ("fsize_db",                        1509180190914), # 1.51TB, avg file size 3.09GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/200331_152916"),
        ("selection", "*"),
        ("blacklist", [2, 5, 70, 135, 160, 196, 198, 259, 260, 263, 266, 269, 273]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 5500000),
  ("nof_db_events",                   5500000),
  ("fsize_local",                     11776261656), # 11.78GB, avg file size 210.29MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueDown"),
  ("process_name_specific",           "TTTo2L2Nu_ueDown_ext1"),
  ("nof_files",                       97),
  ("nof_db_files",                    246),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9109000),
  ("nof_db_events",                   9609000),
  ("fsize_local",                     19501791480), # 19.50GB, avg file size 201.05MB
  ("fsize_db",                        515372873445), # 515.37GB, avg file size 2.10GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/200331_153232"),
        ("selection", "*"),
        ("blacklist", [4, 71, 87, 92, 94]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 27252808),
  ("nof_db_events",                   27252808),
  ("fsize_local",                     62396309659), # 62.40GB, avg file size 227.72MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueUp"),
  ("process_name_specific",           "TTTo2L2Nu_ueUp"),
  ("nof_files",                       111),
  ("nof_db_files",                    87),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5500000),
  ("nof_db_events",                   5500000),
  ("fsize_local",                     11971576338), # 11.97GB, avg file size 107.85MB
  ("fsize_db",                        294673644731), # 294.67GB, avg file size 3.39GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Apr22/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/2017v2_2020Apr22_TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200422_130729"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueUp"),
  ("process_name_specific",           "TTTo2L2Nu_ueUp_ext1"),
  ("nof_files",                       100),
  ("nof_db_files",                    239),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9992000),
  ("nof_db_events",                   9992000),
  ("fsize_local",                     21457295483), # 21.46GB, avg file size 214.57MB
  ("fsize_db",                        539036705125), # 539.04GB, avg file size 2.26GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/200331_153857"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueUp"),
  ("process_name_specific",           "TTTo2L2Nu_ueUp_ext2"),
  ("nof_files",                       613),
  ("nof_db_files",                    762),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 27446000),
  ("nof_db_events",                   29890000),
  ("fsize_local",                     59830786293), # 59.83GB, avg file size 97.60MB
  ("fsize_db",                        1824390970121), # 1.82TB, avg file size 2.39GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Oct13/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/2017v2_2020Oct13_TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext2-v2/201013_102548"),
        ("selection", "*"),
        ("blacklist", [121, 124, 125, 131, 134, 137, 138, 181, 184, 189, 196, 197, 200, 215, 231, 236, 275, 277, 306, 320, 352, 354, 355, 356, 368, 369, 370, 384, 389, 390, 391, 392, 393, 394, 398, 400, 401, 406, 407, 408, 409, 410, 411, 412, 414, 415, 421, 436, 523, 527]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_ueUp"),
  ("process_name_specific",           "TTToSemiLeptonic_ueUp"),
  ("nof_files",                       203),
  ("nof_db_files",                    330),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 19425980),
  ("nof_db_events",                   20122010),
  ("fsize_local",                     43603087653), # 43.60GB, avg file size 214.79MB
  ("fsize_db",                        1095057474309), # 1.10TB, avg file size 3.32GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/200331_154005"),
        ("selection", "*"),
        ("blacklist", [20, 145, 166, 190, 193, 197, 200]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 27108792),
  ("nof_db_events",                   27108792),
  ("fsize_local",                     62235965113), # 62.24GB, avg file size 227.97MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_QCDbased"),
  ("process_name_specific",           "TTTo2L2Nu_QCDbased"),
  ("nof_files",                       55),
  ("nof_db_files",                    143),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5500000),
  ("nof_db_events",                   5500000),
  ("fsize_local",                     11870538996), # 11.87GB, avg file size 215.83MB
  ("fsize_db",                        299508226429), # 299.51GB, avg file size 2.09GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/200331_154318"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 9999000),
  ("nof_db_events",                   9999000),
  ("fsize_local",                     21584111866), # 21.58GB, avg file size 213.70MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_QCDbased"),
  ("process_name_specific",           "TTToSemiLeptonic_QCDbased"),
  ("nof_files",                       272),
  ("nof_db_files",                    546),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 27125000),
  ("nof_db_events",                   27125000),
  ("fsize_local",                     61220572832), # 61.22GB, avg file size 225.08MB
  ("fsize_db",                        1498188372333), # 1.50TB, avg file size 2.74GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/200331_154634"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 27241000),
  ("nof_db_events",                   27341000),
  ("fsize_local",                     62914446491), # 62.91GB, avg file size 229.61MB
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
        ("blacklist", [268]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_GluonMove"),
  ("process_name_specific",           "TTTo2L2Nu_GluonMove"),
  ("nof_files",                       55),
  ("nof_db_files",                    139),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5461000),
  ("nof_db_events",                   5461000),
  ("fsize_local",                     11717970169), # 11.72GB, avg file size 213.05MB
  ("fsize_db",                        294536631445), # 294.54GB, avg file size 2.12GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/200331_154946"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       114),
  ("nof_db_files",                    258),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9818000),
  ("nof_db_events",                   9818000),
  ("fsize_local",                     21102976436), # 21.10GB, avg file size 185.11MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 27409000),
  ("nof_db_events",                   27409000),
  ("fsize_local",                     61518972861), # 61.52GB, avg file size 213.61MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 27469000),
  ("nof_db_events",                   27469000),
  ("fsize_local",                     62992674620), # 62.99GB, avg file size 229.06MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 5092000),
  ("nof_db_events",                   5092000),
  ("fsize_local",                     10997065589), # 11.00GB, avg file size 215.63MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 9966000),
  ("nof_db_events",                   9966000),
  ("fsize_local",                     21570916753), # 21.57GB, avg file size 184.37MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       183),
  ("nof_db_files",                    658),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9117000),
  ("nof_db_events",                   27292000),
  ("fsize_local",                     20789962374), # 20.79GB, avg file size 113.61MB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Apr22/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/2017v2_2020Apr22_TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/200422_130910"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       269),
  ("nof_db_files",                    457),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 26893000),
  ("nof_db_events",                   26893000),
  ("fsize_local",                     61798582243), # 61.80GB, avg file size 229.73MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       25),
  ("nof_db_files",                    51),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 2330486),
  ("nof_db_events",                   2430849),
  ("fsize_local",                     4933292666), # 4.93GB, avg file size 197.33MB
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
        ("blacklist", [22]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2017["/TTToSemiLeptonic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop166p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop166p5"),
  ("nof_files",                       100),
  ("nof_db_files",                    148),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9940122),
  ("nof_db_events",                   9940122),
  ("fsize_local",                     21973361527), # 21.97GB, avg file size 219.73MB
  ("fsize_db",                        536119573228), # 536.12GB, avg file size 3.62GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_mtop166p5_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/200331_160459"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 9553066),
  ("nof_db_events",                   9553066),
  ("fsize_local",                     21114345523), # 21.11GB, avg file size 219.94MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       98),
  ("nof_db_files",                    186),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9495448),
  ("nof_db_events",                   9694576),
  ("fsize_local",                     21378966207), # 21.38GB, avg file size 218.15MB
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
        ("blacklist", [72, 97]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop166p5"),
  ("process_name_specific",           "TTToHadronic_mtop166p5_PSweights"),
  ("nof_files",                       101),
  ("nof_db_files",                    177),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9800051),
  ("nof_db_events",                   10000000),
  ("fsize_local",                     22144553319), # 22.14GB, avg file size 219.25MB
  ("fsize_db",                        548417838778), # 548.42GB, avg file size 3.10GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v/200331_160953"),
        ("selection", "*"),
        ("blacklist", [2, 3]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop169p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop169p5"),
  ("nof_files",                       50),
  ("nof_db_files",                    76),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4955578),
  ("nof_db_events",                   4955578),
  ("fsize_local",                     10554875780), # 10.55GB, avg file size 211.10MB
  ("fsize_db",                        263959681021), # 263.96GB, avg file size 3.47GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200331_161132"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 9674000),
  ("nof_db_events",                   9674000),
  ("fsize_local",                     20611782111), # 20.61GB, avg file size 212.49MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop169p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop169p5"),
  ("nof_files",                       189),
  ("nof_db_files",                    280),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 17308204),
  ("nof_db_events",                   18802372),
  ("fsize_local",                     38525664515), # 38.53GB, avg file size 203.84MB
  ("fsize_db",                        1016431882420), # 1.02TB, avg file size 3.63GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v/200331_161414"),
        ("selection", "*"),
        ("blacklist", [131, 139, 143, 149, 151, 153, 162, 168, 169, 171, 176, 177, 179, 180, 185]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       99),
  ("nof_db_files",                    257),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9858000),
  ("nof_db_events",                   9858000),
  ("fsize_local",                     21946364192), # 21.95GB, avg file size 221.68MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       188),
  ("nof_db_files",                    411),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 18739000),
  ("nof_db_events",                   18739000),
  ("fsize_local",                     42645609555), # 42.65GB, avg file size 226.84MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop171p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop171p5"),
  ("nof_files",                       60),
  ("nof_db_files",                    105),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5954696),
  ("nof_db_events",                   5954696),
  ("fsize_local",                     12741305095), # 12.74GB, avg file size 212.36MB
  ("fsize_db",                        317838339272), # 317.84GB, avg file size 3.03GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/200331_161907"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop171p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop171p5"),
  ("nof_files",                       504),
  ("nof_db_files",                    429),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 25000000),
  ("nof_db_events",                   25000000),
  ("fsize_local",                     56661662447), # 56.66GB, avg file size 112.42MB
  ("fsize_db",                        1354549562121), # 1.35TB, avg file size 3.16GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Apr22/TTToSemiLeptonic_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Apr22_TTToSemiLeptonic_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v/200422_131022"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop171p5"),
  ("process_name_specific",           "TTToHadronic_mtop171p5"),
  ("nof_files",                       241),
  ("nof_db_files",                    364),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 23286746),
  ("nof_db_events",                   23983066),
  ("fsize_local",                     53258241346), # 53.26GB, avg file size 220.99MB
  ("fsize_db",                        1323043643849), # 1.32TB, avg file size 3.63GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v/200331_162223"),
        ("selection", "*"),
        ("blacklist", [36, 152, 203, 213, 216, 218, 239]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

samples_2017["/TTToSemiLeptonic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop173p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop173p5"),
  ("nof_files",                       487),
  ("nof_db_files",                    400),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 24132305),
  ("nof_db_events",                   24132305),
  ("fsize_local",                     54924618315), # 54.92GB, avg file size 112.78MB
  ("fsize_db",                        1310413301099), # 1.31TB, avg file size 3.28GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Apr22/TTToSemiLeptonic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Apr22_TTToSemiLeptonic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/200422_131207"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       488),
  ("nof_db_files",                    529),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 24373000),
  ("nof_db_events",                   24373000),
  ("fsize_local",                     56687005320), # 56.69GB, avg file size 116.16MB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Apr22/TTToHadronic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Apr22_TTToHadronic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/200422_131322"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       51),
  ("nof_db_files",                    90),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4987400),
  ("nof_db_events",                   4987400),
  ("fsize_local",                     10759584030), # 10.76GB, avg file size 210.97MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop175p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop175p5_ext1"),
  ("nof_files",                       97),
  ("nof_db_files",                    224),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9642000),
  ("nof_db_events",                   9642000),
  ("fsize_local",                     20807261996), # 20.81GB, avg file size 214.51MB
  ("fsize_db",                        520015250773), # 520.02GB, avg file size 2.32GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/200331_163014"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop175p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop175p5"),
  ("nof_files",                       188),
  ("nof_db_files",                    307),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 17956328),
  ("nof_db_events",                   18651748),
  ("fsize_local",                     40515314640), # 40.52GB, avg file size 215.51MB
  ("fsize_db",                        1015022724714), # 1.02TB, avg file size 3.31GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v/200331_163224"),
        ("selection", "*"),
        ("blacklist", [132, 135, 166, 171, 173, 174, 176]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 9858000),
  ("nof_db_events",                   9858000),
  ("fsize_local",                     22239840996), # 22.24GB, avg file size 224.64MB
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
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop175p5"),
  ("process_name_specific",           "TTToHadronic_mtop175p5"),
  ("nof_files",                       399),
  ("nof_db_files",                    320),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 19688281),
  ("nof_db_events",                   19688281),
  ("fsize_local",                     46020794557), # 46.02GB, avg file size 115.34MB
  ("fsize_db",                        1090427837791), # 1.09TB, avg file size 3.41GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Apr22/TTToHadronic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Apr22_TTToHadronic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v/200422_131507"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop178p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop178p5"),
  ("nof_files",                       25),
  ("nof_db_files",                    42),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 2458584),
  ("nof_db_events",                   2458584),
  ("fsize_local",                     5339955246), # 5.34GB, avg file size 213.60MB
  ("fsize_db",                        132267893447), # 132.27GB, avg file size 3.15GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_mtop178p5_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_mtop178p5_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/200331_163652"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop178p5"),
  ("process_name_specific",           "TTTo2L2Nu_mtop178p5_PSweights"),
  ("nof_files",                       50),
  ("nof_db_files",                    41),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 2459510),
  ("nof_db_events",                   2459510),
  ("fsize_local",                     5413526364), # 5.41GB, avg file size 108.27MB
  ("fsize_db",                        132134836816), # 132.13GB, avg file size 3.22GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Apr22/TTTo2L2Nu_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Apr22_TTTo2L2Nu_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/200422_130250"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop178p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop178p5"),
  ("nof_files",                       100),
  ("nof_db_files",                    167),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9895825),
  ("nof_db_events",                   9895825),
  ("fsize_local",                     22471921292), # 22.47GB, avg file size 224.72MB
  ("fsize_db",                        540169588879), # 540.17GB, avg file size 3.23GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/200331_164013"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop178p5"),
  ("process_name_specific",           "TTToSemiLeptonic_mtop178p5_PSweights"),
  ("nof_files",                       101),
  ("nof_db_files",                    192),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9986177),
  ("nof_db_events",                   9986177),
  ("fsize_local",                     22675250301), # 22.68GB, avg file size 224.51MB
  ("fsize_db",                        545083161451), # 545.08GB, avg file size 2.84GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v/200331_164154"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToHadronic_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_mtop178p5"),
  ("process_name_specific",           "TTToHadronic_mtop178p5"),
  ("nof_files",                       101),
  ("nof_db_files",                    195),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 9960120),
  ("nof_db_events",                   9960120),
  ("fsize_local",                     23162924559), # 23.16GB, avg file size 229.34MB
  ("fsize_db",                        553709620124), # 553.71GB, avg file size 2.84GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToHadronic_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToHadronic_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/200331_164305"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_widthx0p7_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx0p7"),
  ("process_name_specific",           "TTTo2L2Nu_widthx0p7"),
  ("nof_files",                       50),
  ("nof_db_files",                    149),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5000000),
  ("nof_db_events",                   5000000),
  ("fsize_local",                     10721023666), # 10.72GB, avg file size 214.42MB
  ("fsize_db",                        269339051490), # 269.34GB, avg file size 1.81GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_widthx0p7_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_widthx0p7_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200331_164444"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_widthx0p7_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx0p7"),
  ("process_name_specific",           "TTToSemiLeptonic_widthx0p7"),
  ("nof_files",                       200),
  ("nof_db_files",                    412),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 18783000),
  ("nof_db_events",                   19983000),
  ("fsize_local",                     42106017740), # 42.11GB, avg file size 210.53MB
  ("fsize_db",                        1090044678188), # 1.09TB, avg file size 2.65GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_widthx0p7_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_widthx0p7_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200331_164621"),
        ("selection", "*"),
        ("blacklist", [31, 46, 58, 67, 74, 82, 141, 152, 175, 178, 186, 187]),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_widthx0p85_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx0p85"),
  ("process_name_specific",           "TTTo2L2Nu_widthx0p85"),
  ("nof_files",                       49),
  ("nof_db_files",                    129),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4880000),
  ("nof_db_events",                   4880000),
  ("fsize_local",                     10462843252), # 10.46GB, avg file size 213.53MB
  ("fsize_db",                        262546859916), # 262.55GB, avg file size 2.04GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_widthx0p85_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_widthx0p85_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200331_164756"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_widthx0p85_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx0p85"),
  ("process_name_specific",           "TTToSemiLeptonic_widthx0p85"),
  ("nof_files",                       370),
  ("nof_db_files",                    417),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 18499000),
  ("nof_db_events",                   18499000),
  ("fsize_local",                     41992001293), # 41.99GB, avg file size 113.49MB
  ("fsize_db",                        1009682784661), # 1.01TB, avg file size 2.42GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Apr22/TTToSemiLeptonic_widthx0p85_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Apr22_TTToSemiLeptonic_widthx0p85_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/200422_131619"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_widthx1p15_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx1p15"),
  ("process_name_specific",           "TTTo2L2Nu_widthx1p15"),
  ("nof_files",                       50),
  ("nof_db_files",                    117),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4978000),
  ("nof_db_events",                   4978000),
  ("fsize_local",                     10674187950), # 10.67GB, avg file size 213.48MB
  ("fsize_db",                        267654403110), # 267.65GB, avg file size 2.29GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_widthx1p15_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_widthx1p15_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200331_165110"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_widthx1p15_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx1p15"),
  ("process_name_specific",           "TTToSemiLeptonic_widthx1p15"),
  ("nof_files",                       371),
  ("nof_db_files",                    419),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 18513000),
  ("nof_db_events",                   19989000),
  ("fsize_local",                     42019902795), # 42.02GB, avg file size 113.26MB
  ("fsize_db",                        1090831097088), # 1.09TB, avg file size 2.60GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Apr22/TTToSemiLeptonic_widthx1p15_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Apr22_TTToSemiLeptonic_widthx1p15_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200422_130433"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTTo2L2Nu_widthx1p3_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx1p3"),
  ("process_name_specific",           "TTTo2L2Nu_widthx1p3"),
  ("nof_files",                       50),
  ("nof_db_files",                    112),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4947000),
  ("nof_db_events",                   4947000),
  ("fsize_local",                     10606216802), # 10.61GB, avg file size 212.12MB
  ("fsize_db",                        265885976593), # 265.89GB, avg file size 2.37GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTTo2L2Nu_widthx1p3_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Mar31_TTTo2L2Nu_widthx1p3_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200331_165421"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/TTToSemiLeptonic_widthx1p3_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT_widthx1p3"),
  ("process_name_specific",           "TTToSemiLeptonic_widthx1p3"),
  ("nof_files",                       178),
  ("nof_db_files",                    429),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 17719000),
  ("nof_db_events",                   19976000),
  ("fsize_local",                     39717840057), # 39.72GB, avg file size 223.13MB
  ("fsize_db",                        1091053966172), # 1.09TB, avg file size 2.54GB
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
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2020Mar31/TTToSemiLeptonic_widthx1p3_TuneCP5_13TeV-powheg-pythia8/2017v2_2020Mar31_TTToSemiLeptonic_widthx1p3_TuneCP5_13TeV-powheg-pythia8__RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/200331_165628"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  [ 'TTTo2L2Nu_mtop173p5',                             'TTTo2L2Nu_mtop173p5_ext1',                         ],
  [ 'TTTo2L2Nu_mtop178p5',                             'TTTo2L2Nu_mtop178p5_PSweights',                    ],
  [ 'TTTo2L2Nu_QCDbased',                              'TTTo2L2Nu_QCDbased_ext1',                          ],
  [ 'TTTo2L2Nu_mtop175p5',                             'TTTo2L2Nu_mtop175p5_ext1',                        'TTTo2L2Nu_mtop175p5_ext2',                         ],
  [ 'TTToSemiLeptonic_mtop169p5',                      'TTToSemiLeptonic_mtop169p5_ext1',                  ],
  [ 'TTTo2L2Nu_hdampDOWN',                             'TTTo2L2Nu_hdampDOWN_ext1',                        'TTTo2L2Nu_hdampDOWN_ext2',                         ],
  [ 'TTTo2L2Nu_hdampUP',                               'TTTo2L2Nu_hdampUP_ext1',                          'TTTo2L2Nu_hdampUP_ext2',                           ],
  [ 'TTTo2L2Nu_ueDown',                                'TTTo2L2Nu_ueDown_ext1',                           'TTTo2L2Nu_ueDown_ext2',                            ],
  [ 'TTTo2L2Nu_GluonMove',                             'TTTo2L2Nu_GluonMove_ext1',                        'TTTo2L2Nu_GluonMove_ext2',                         ],
  [ 'TTTo2L2Nu_mtop166p5',                             'TTTo2L2Nu_mtop166p5_PSweights',                    ],
  [ 'TTTo2L2Nu_erdON',                                 'TTTo2L2Nu_erdON_ext1',                            'TTTo2L2Nu_erdON_ext2',                             ],
  [ 'TTToSemiLeptonic_mtop166p5',                      'TTToSemiLeptonic_mtop166p5_PSweights',             ],
  [ 'TTTo2L2Nu_mtop169p5',                             'TTTo2L2Nu_mtop169p5_ext1',                        'TTTo2L2Nu_mtop169p5_ext2',                         ],
  [ 'TTTo2L2Nu_ueUp',                                  'TTTo2L2Nu_ueUp_ext1',                             'TTTo2L2Nu_ueUp_ext2',                              ],
  [ 'TTToHadronic_mtop166p5',                          'TTToHadronic_mtop166p5_PSweights',                 ],
  [ 'TTToSemiLeptonic_mtop178p5',                      'TTToSemiLeptonic_mtop178p5_PSweights',             ],
  [ 'TTToSemiLeptonic_mtop175p5',                      'TTToSemiLeptonic_mtop175p5_ext1',                  ],
]

