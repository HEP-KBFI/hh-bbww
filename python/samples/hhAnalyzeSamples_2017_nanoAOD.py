from collections import OrderedDict as OD

# file generated at 2019-12-04 17:52:29 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh.py -p python/samples/sampleLocations_2017_nanoAOD_hh_bbww.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_nanoAOD.py -M

samples_2017 = OD()
samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 279999),
  ("nof_db_events",                   279999),
  ("fsize_local",                     803191565), # 803.19MB, avg file size 267.73MB
  ("fsize_db",                        18070036516), # 18.07GB, avg file size 1.29GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/191005_065749"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_350_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_350_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 285000),
  ("nof_db_events",                   285000),
  ("fsize_local",                     853345073), # 853.35MB, avg file size 284.45MB
  ("fsize_db",                        18927275912), # 18.93GB, avg file size 996.17MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/191005_065956"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_400_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_400_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     310041447), # 310.04MB, avg file size 310.04MB
  ("fsize_db",                        6827583120), # 6.83GB, avg file size 682.76MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/191005_070211"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_750_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_spin0_750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     352847578), # 352.85MB, avg file size 352.85MB
  ("fsize_db",                        7423075893), # 7.42GB, avg file size 571.01MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/191005_070353"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     709382729), # 709.38MB, avg file size 177.35MB
  ("fsize_db",                        20842533885), # 20.84GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_070541"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     713903905), # 713.90MB, avg file size 178.48MB
  ("fsize_db",                        20086379241), # 20.09GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_070717"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     701826035), # 701.83MB, avg file size 175.46MB
  ("fsize_db",                        19501546911), # 19.50GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_070928"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     707400357), # 707.40MB, avg file size 176.85MB
  ("fsize_db",                        20165336883), # 20.17GB, avg file size 1.44GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_071109"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     572860746), # 572.86MB, avg file size 190.95MB
  ("fsize_db",                        15538010606), # 15.54GB, avg file size 776.90MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_071350"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     588726103), # 588.73MB, avg file size 196.24MB
  ("fsize_db",                        15654716885), # 15.65GB, avg file size 1.30GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_071634"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     598369995), # 598.37MB, avg file size 199.46MB
  ("fsize_db",                        15536600053), # 15.54GB, avg file size 971.04MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_071814"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     636998472), # 637.00MB, avg file size 212.33MB
  ("fsize_db",                        16296871303), # 16.30GB, avg file size 814.84MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_071951"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     437356432), # 437.36MB, avg file size 218.68MB
  ("fsize_db",                        10964750047), # 10.96GB, avg file size 913.73MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_072157"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     458853167), # 458.85MB, avg file size 229.43MB
  ("fsize_db",                        11169462986), # 11.17GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_072411"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     467365804), # 467.37MB, avg file size 233.68MB
  ("fsize_db",                        11395262580), # 11.40GB, avg file size 949.61MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_072553"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     473730531), # 473.73MB, avg file size 236.87MB
  ("fsize_db",                        11438629863), # 11.44GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_072736"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     482333314), # 482.33MB, avg file size 241.17MB
  ("fsize_db",                        11931037531), # 11.93GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_072914"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 197000),
  ("nof_db_events",                   197000),
  ("fsize_local",                     480071284), # 480.07MB, avg file size 240.04MB
  ("fsize_db",                        11877663068), # 11.88GB, avg file size 791.84MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_073056"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     492317518), # 492.32MB, avg file size 246.16MB
  ("fsize_db",                        12127308050), # 12.13GB, avg file size 808.49MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_073240"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     246044502), # 246.04MB, avg file size 246.04MB
  ("fsize_db",                        5935911198), # 5.94GB, avg file size 539.63MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/191005_073445"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     249939562), # 249.94MB, avg file size 249.94MB
  ("fsize_db",                        5930718483), # 5.93GB, avg file size 847.25MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_073651"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     257605703), # 257.61MB, avg file size 257.61MB
  ("fsize_db",                        6224151597), # 6.22GB, avg file size 778.02MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_073903"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     257437430), # 257.44MB, avg file size 257.44MB
  ("fsize_db",                        6171310375), # 6.17GB, avg file size 514.28MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_074042"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     261669127), # 261.67MB, avg file size 261.67MB
  ("fsize_db",                        6356319473), # 6.36GB, avg file size 635.63MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_074218"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     262262474), # 262.26MB, avg file size 262.26MB
  ("fsize_db",                        6172348486), # 6.17GB, avg file size 771.54MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_074425"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 97000),
  ("nof_db_events",                   97000),
  ("fsize_local",                     258641786), # 258.64MB, avg file size 258.64MB
  ("fsize_db",                        6425534542), # 6.43GB, avg file size 494.27MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_074640"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 97999),
  ("nof_db_events",                   97999),
  ("fsize_local",                     262705242), # 262.71MB, avg file size 262.71MB
  ("fsize_db",                        6497731845), # 6.50GB, avg file size 590.70MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_074822"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2v"),
  ("nof_files",                       5),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     720685067), # 720.69MB, avg file size 144.14MB
  ("fsize_db",                        20041115926), # 20.04GB, avg file size 871.35MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_075005"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2v"),
  ("nof_files",                       5),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     730913883), # 730.91MB, avg file size 146.18MB
  ("fsize_db",                        20202072552), # 20.20GB, avg file size 962.00MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_075643"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     738681560), # 738.68MB, avg file size 184.67MB
  ("fsize_db",                        20268702810), # 20.27GB, avg file size 921.30MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_075819"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2b2v"),
  ("nof_files",                       5),
  ("nof_db_files",                    31),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     751706594), # 751.71MB, avg file size 150.34MB
  ("fsize_db",                        20542842010), # 20.54GB, avg file size 662.67MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_080029"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    26),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     768268401), # 768.27MB, avg file size 192.07MB
  ("fsize_db",                        20998766588), # 21.00GB, avg file size 807.64MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_080239"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 293998),
  ("nof_db_events",                   293998),
  ("fsize_local",                     578223315), # 578.22MB, avg file size 192.74MB
  ("fsize_db",                        15577989269), # 15.58GB, avg file size 916.35MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_080452"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 281999),
  ("nof_db_events",                   281999),
  ("fsize_local",                     572687170), # 572.69MB, avg file size 190.90MB
  ("fsize_db",                        15217194365), # 15.22GB, avg file size 845.40MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_080628"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 298000),
  ("nof_db_events",                   298000),
  ("fsize_local",                     631736925), # 631.74MB, avg file size 210.58MB
  ("fsize_db",                        16133391096), # 16.13GB, avg file size 806.67MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_080804"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     660965733), # 660.97MB, avg file size 220.32MB
  ("fsize_db",                        16485829471), # 16.49GB, avg file size 867.68MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_080946"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     455487702), # 455.49MB, avg file size 227.74MB
  ("fsize_db",                        11497248581), # 11.50GB, avg file size 547.49MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_081153"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     469671004), # 469.67MB, avg file size 156.56MB
  ("fsize_db",                        11543534297), # 11.54GB, avg file size 679.03MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_081331"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     458362549), # 458.36MB, avg file size 229.18MB
  ("fsize_db",                        11191273021), # 11.19GB, avg file size 746.08MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_081517"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     485151330), # 485.15MB, avg file size 242.58MB
  ("fsize_db",                        11871616225), # 11.87GB, avg file size 539.62MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_081726"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     490133223), # 490.13MB, avg file size 245.07MB
  ("fsize_db",                        11820942716), # 11.82GB, avg file size 656.72MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_082037"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 198000),
  ("nof_db_events",                   198000),
  ("fsize_local",                     489669879), # 489.67MB, avg file size 244.83MB
  ("fsize_db",                        11778577981), # 11.78GB, avg file size 785.24MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_082212"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2v"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     499168642), # 499.17MB, avg file size 249.58MB
  ("fsize_db",                        11967660431), # 11.97GB, avg file size 598.38MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_082347"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_2b2v"),
  ("nof_files",                       3),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     508887630), # 508.89MB, avg file size 169.63MB
  ("fsize_db",                        12348394332), # 12.35GB, avg file size 823.23MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-850_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_082554"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     255604434), # 255.60MB, avg file size 255.60MB
  ("fsize_db",                        6022388849), # 6.02GB, avg file size 669.15MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realist/191005_082807"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     264444769), # 264.44MB, avg file size 66.11MB
  ("fsize_db",                        6101733672), # 6.10GB, avg file size 610.17MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/191005_083013"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     260867565), # 260.87MB, avg file size 260.87MB
  ("fsize_db",                        6305015701), # 6.31GB, avg file size 900.72MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/191005_083224"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     261032359), # 261.03MB, avg file size 261.03MB
  ("fsize_db",                        6512057209), # 6.51GB, avg file size 434.14MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/191005_083432"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     262699234), # 262.70MB, avg file size 262.70MB
  ("fsize_db",                        6489134095), # 6.49GB, avg file size 540.76MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/191005_083640"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     262956819), # 262.96MB, avg file size 262.96MB
  ("fsize_db",                        6328288934), # 6.33GB, avg file size 575.30MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/191005_083848"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98000),
  ("nof_db_events",                   98000),
  ("fsize_local",                     260162510), # 260.16MB, avg file size 260.16MB
  ("fsize_db",                        6377937593), # 6.38GB, avg file size 490.61MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-2500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/191005_084027"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_2b2v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     266487149), # 266.49MB, avg file size 266.49MB
  ("fsize_db",                        6547475897), # 6.55GB, avg file size 545.62MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-3000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realis/191005_084207"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbvv"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     869515964), # 869.52MB, avg file size 217.38MB
  ("fsize_db",                        22186460848), # 22.19GB, avg file size 1.85GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph/2017v2_2019Oct05_VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_084344"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 388999),
  ("nof_db_events",                   388999),
  ("fsize_local",                     872340005), # 872.34MB, avg file size 218.09MB
  ("fsize_db",                        21257341288), # 21.26GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_084526"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     969650388), # 969.65MB, avg file size 242.41MB
  ("fsize_db",                        23088598268), # 23.09GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_2_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_084704"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     855399543), # 855.40MB, avg file size 213.85MB
  ("fsize_db",                        20768532098), # 20.77GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_3_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_084910"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 392999),
  ("nof_db_events",                   392999),
  ("fsize_local",                     863249078), # 863.25MB, avg file size 215.81MB
  ("fsize_db",                        21440735341), # 21.44GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_7_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_085121"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 386999),
  ("nof_db_events",                   386999),
  ("fsize_local",                     942727926), # 942.73MB, avg file size 235.68MB
  ("fsize_db",                        22534822736), # 22.53GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_9_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_085327"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbvv"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2v"),
  ("nof_files",                       4),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     875964629), # 875.96MB, avg file size 218.99MB
  ("fsize_db",                        21561540290), # 21.56GB, avg file size 937.46MB
  ("use_it",                          True),
  ("xsection",                        0.026422),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2VTo2L2Nu_node_12_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_085534"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_250_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1072508643), # 1.07GB, avg file size 268.13MB
  ("fsize_db",                        24640211831), # 24.64GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_085742"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_260_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_260_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     1052851632), # 1.05GB, avg file size 263.21MB
  ("fsize_db",                        24012313674), # 24.01GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_085959"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_270_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_270_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1055403421), # 1.06GB, avg file size 263.85MB
  ("fsize_db",                        23968184441), # 23.97GB, avg file size 1.41GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/191005_090154"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_280_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_280_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1110740177), # 1.11GB, avg file size 277.69MB
  ("fsize_db",                        25138262751), # 25.14GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_090401"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     850002325), # 850.00MB, avg file size 283.33MB
  ("fsize_db",                        19012035463), # 19.01GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/191005_090616"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_350_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_350_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     890678185), # 890.68MB, avg file size 296.89MB
  ("fsize_db",                        19447040410), # 19.45GB, avg file size 1.77GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/191005_090750"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_400_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_400_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     308063952), # 308.06MB, avg file size 308.06MB
  ("fsize_db",                        6609409571), # 6.61GB, avg file size 944.20MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/191005_090927"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_450_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_450_hh_2b2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     963346411), # 963.35MB, avg file size 160.56MB
  ("fsize_db",                        20167217854), # 20.17GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2019Nov24/VBFToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/2017v2_2019Nov24_VBFToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191124_193818"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_500_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 290000),
  ("nof_db_events",                   290000),
  ("fsize_local",                     946796980), # 946.80MB, avg file size 315.60MB
  ("fsize_db",                        19708690689), # 19.71GB, avg file size 1.79GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_091220"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_550_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_550_hh_2b2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1011979350), # 1.01GB, avg file size 168.66MB
  ("fsize_db",                        20644816504), # 20.64GB, avg file size 1.59GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2019Nov24/VBFToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/2017v2_2019Nov24_VBFToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191124_194020"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_600_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_600_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     687261847), # 687.26MB, avg file size 171.82MB
  ("fsize_db",                        13957904944), # 13.96GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2019Nov24/VBFToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/2017v2_2019Nov24_VBFToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191124_194254"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_650_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_650_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     697359752), # 697.36MB, avg file size 174.34MB
  ("fsize_db",                        14016331858), # 14.02GB, avg file size 2.00GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2019Nov24/VBFToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/2017v2_2019Nov24_VBFToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191124_194456"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_700_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_700_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     708788263), # 708.79MB, avg file size 177.20MB
  ("fsize_db",                        14253263609), # 14.25GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2019Nov24/VBFToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph/2017v2_2019Nov24_VBFToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191124_194728"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     355271059), # 355.27MB, avg file size 355.27MB
  ("fsize_db",                        7146269195), # 7.15GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/191005_092245"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_800_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_800_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     725032754), # 725.03MB, avg file size 181.26MB
  ("fsize_db",                        14420020815), # 14.42GB, avg file size 1.31GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2019Nov24/VBFToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/2017v2_2019Nov24_VBFToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191124_195234"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_850_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_850_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     731082944), # 731.08MB, avg file size 182.77MB
  ("fsize_db",                        14617490096), # 14.62GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2019Nov24/VBFToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph/2017v2_2019Nov24_VBFToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191124_195000"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_900_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     365967242), # 365.97MB, avg file size 365.97MB
  ("fsize_db",                        7382733082), # 7.38GB, avg file size 671.16MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_092845"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1000_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     374154467), # 374.15MB, avg file size 187.08MB
  ("fsize_db",                        7364574553), # 7.36GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2019Nov24/VBFToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph/2017v2_2019Nov24_VBFToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191124_195436"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1250_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     381956413), # 381.96MB, avg file size 190.98MB
  ("fsize_db",                        7497237044), # 7.50GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2019Nov24/VBFToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph/2017v2_2019Nov24_VBFToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191124_195708"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1500_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     386791723), # 386.79MB, avg file size 193.40MB
  ("fsize_db",                        7582428905), # 7.58GB, avg file size 1.52GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2017v2_2019Nov24/VBFToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph/2017v2_2019Nov24_VBFToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191124_193617"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     386625092), # 386.63MB, avg file size 386.63MB
  ("fsize_db",                        7802866732), # 7.80GB, avg file size 650.24MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_093624"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_2000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     388488567), # 388.49MB, avg file size 388.49MB
  ("fsize_db",                        7810715378), # 7.81GB, avg file size 710.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_093804"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_3000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin0_3000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     393530119), # 393.53MB, avg file size 393.53MB
  ("fsize_db",                        7943092984), # 7.94GB, avg file size 992.89MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_093946"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_250_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_250_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     1054963473), # 1.05GB, avg file size 263.74MB
  ("fsize_db",                        23569723909), # 23.57GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_094200"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_260_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_260_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     976507767), # 976.51MB, avg file size 244.13MB
  ("fsize_db",                        22974833125), # 22.97GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_094409"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_270_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_270_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     974649357), # 974.65MB, avg file size 243.66MB
  ("fsize_db",                        22808220732), # 22.81GB, avg file size 1.20GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_094617"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_280_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_280_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     973841735), # 973.84MB, avg file size 243.46MB
  ("fsize_db",                        22983626173), # 22.98GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_094823"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_300_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_300_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 282000),
  ("nof_db_events",                   282000),
  ("fsize_local",                     685407027), # 685.41MB, avg file size 228.47MB
  ("fsize_db",                        15951259391), # 15.95GB, avg file size 839.54MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_095036"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_320_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_320_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     728431485), # 728.43MB, avg file size 242.81MB
  ("fsize_db",                        17224376684), # 17.22GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_095216"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_350_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_350_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     728188375), # 728.19MB, avg file size 242.73MB
  ("fsize_db",                        16911146727), # 16.91GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_095416"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_400_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_400_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     709225199), # 709.23MB, avg file size 236.41MB
  ("fsize_db",                        16538417486), # 16.54GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_095553"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_450_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_450_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     731752208), # 731.75MB, avg file size 243.92MB
  ("fsize_db",                        16984173640), # 16.98GB, avg file size 808.77MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_095728"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_500_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_500_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     735216721), # 735.22MB, avg file size 245.07MB
  ("fsize_db",                        16980250583), # 16.98GB, avg file size 1.54GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_095934"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_600_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_600_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     495852713), # 495.85MB, avg file size 247.93MB
  ("fsize_db",                        11350421129), # 11.35GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_100336"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_650_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_650_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 197000),
  ("nof_db_events",                   197000),
  ("fsize_local",                     491890274), # 491.89MB, avg file size 245.95MB
  ("fsize_db",                        11416936121), # 11.42GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_100447"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_700_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_700_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     501603085), # 501.60MB, avg file size 250.80MB
  ("fsize_db",                        11593555122), # 11.59GB, avg file size 966.13MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_100625"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_750_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     504610203), # 504.61MB, avg file size 252.31MB
  ("fsize_db",                        11489097788), # 11.49GB, avg file size 2.30GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_100837"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_850_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_850_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     508510980), # 508.51MB, avg file size 254.26MB
  ("fsize_db",                        11469515493), # 11.47GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_101051"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_900_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     254782082), # 254.78MB, avg file size 254.78MB
  ("fsize_db",                        5871346880), # 5.87GB, avg file size 489.28MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_101257"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     256538587), # 256.54MB, avg file size 256.54MB
  ("fsize_db",                        5935760871), # 5.94GB, avg file size 494.65MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_101502"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1750_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     256808535), # 256.81MB, avg file size 256.81MB
  ("fsize_db",                        5865706342), # 5.87GB, avg file size 651.75MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_101709"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_2000_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_spin2_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     256161974), # 256.16MB, avg file size 256.16MB
  ("fsize_db",                        6015024771), # 6.02GB, avg file size 601.50MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph/2017v2_2019Oct05_VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_101920"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 390000),
  ("nof_db_events",                   390000),
  ("fsize_local",                     682823348), # 682.82MB, avg file size 170.71MB
  ("fsize_db",                        20093492648), # 20.09GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_102130"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 360000),
  ("nof_db_events",                   360000),
  ("fsize_local",                     634702103), # 634.70MB, avg file size 158.68MB
  ("fsize_db",                        17758553715), # 17.76GB, avg file size 986.59MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_102312"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     698497470), # 698.50MB, avg file size 174.62MB
  ("fsize_db",                        19361033085), # 19.36GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_102449"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 398000),
  ("nof_db_events",                   398000),
  ("fsize_local",                     723301762), # 723.30MB, avg file size 180.83MB
  ("fsize_db",                        20704800616), # 20.70GB, avg file size 900.21MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_102655"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     552933065), # 552.93MB, avg file size 184.31MB
  ("fsize_db",                        15151937781), # 15.15GB, avg file size 688.72MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_102835"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     566019950), # 566.02MB, avg file size 188.67MB
  ("fsize_db",                        15215406969), # 15.22GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_103047"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     582629072), # 582.63MB, avg file size 194.21MB
  ("fsize_db",                        15430234358), # 15.43GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_103253"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 296000),
  ("nof_db_events",                   296000),
  ("fsize_local",                     600990588), # 600.99MB, avg file size 200.33MB
  ("fsize_db",                        15540706594), # 15.54GB, avg file size 971.29MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_103500"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 272000),
  ("nof_db_events",                   272000),
  ("fsize_local",                     574444175), # 574.44MB, avg file size 191.48MB
  ("fsize_db",                        14544281532), # 14.54GB, avg file size 808.02MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_103727"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 190000),
  ("nof_db_events",                   190000),
  ("fsize_local",                     414797424), # 414.80MB, avg file size 207.40MB
  ("fsize_db",                        10300681960), # 10.30GB, avg file size 858.39MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_103908"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     448870170), # 448.87MB, avg file size 224.44MB
  ("fsize_db",                        10884541416), # 10.88GB, avg file size 989.50MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_104048"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     460110334), # 460.11MB, avg file size 230.06MB
  ("fsize_db",                        11044936345), # 11.04GB, avg file size 920.41MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_104257"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 188000),
  ("nof_db_events",                   188000),
  ("fsize_local",                     441723774), # 441.72MB, avg file size 220.86MB
  ("fsize_db",                        10510514184), # 10.51GB, avg file size 700.70MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_104508"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     477643276), # 477.64MB, avg file size 238.82MB
  ("fsize_db",                        11214998225), # 11.21GB, avg file size 1.40GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_104645"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     478456610), # 478.46MB, avg file size 239.23MB
  ("fsize_db",                        11545737081), # 11.55GB, avg file size 962.14MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_104823"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     494000553), # 494.00MB, avg file size 247.00MB
  ("fsize_db",                        11819983411), # 11.82GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_105002"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     480068652), # 480.07MB, avg file size 240.03MB
  ("fsize_db",                        11490975329), # 11.49GB, avg file size 766.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-850_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_105143"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 95000),
  ("nof_db_events",                   95000),
  ("fsize_local",                     238194488), # 238.19MB, avg file size 238.19MB
  ("fsize_db",                        5517036529), # 5.52GB, avg file size 788.15MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_105320"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     255079894), # 255.08MB, avg file size 255.08MB
  ("fsize_db",                        5887358169), # 5.89GB, avg file size 654.15MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_105506"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     263715476), # 263.72MB, avg file size 263.72MB
  ("fsize_db",                        6210975535), # 6.21GB, avg file size 690.11MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-1250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_105642"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     262257587), # 262.26MB, avg file size 262.26MB
  ("fsize_db",                        5949909431), # 5.95GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-1500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_105823"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     265422412), # 265.42MB, avg file size 265.42MB
  ("fsize_db",                        6303523737), # 6.30GB, avg file size 573.05MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-1750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_110033"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 92000),
  ("nof_db_events",                   92000),
  ("fsize_local",                     243542023), # 243.54MB, avg file size 243.54MB
  ("fsize_db",                        5565938746), # 5.57GB, avg file size 927.66MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-2000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_110240"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-2500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     267330838), # 267.33MB, avg file size 267.33MB
  ("fsize_db",                        6456631366), # 6.46GB, avg file size 586.97MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-2500_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-2500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_110453"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     267499019), # 267.50MB, avg file size 267.50MB
  ("fsize_db",                        6431618251), # 6.43GB, avg file size 803.95MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToRadionToHHTo2B2Tau_M-3000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_110706"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     706156267), # 706.16MB, avg file size 176.54MB
  ("fsize_db",                        20195673518), # 20.20GB, avg file size 878.07MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_110948"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     688946899), # 688.95MB, avg file size 172.24MB
  ("fsize_db",                        19164112451), # 19.16GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_111154"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 390000),
  ("nof_db_events",                   390000),
  ("fsize_local",                     710602282), # 710.60MB, avg file size 177.65MB
  ("fsize_db",                        19739699313), # 19.74GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_111425"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 379000),
  ("nof_db_events",                   379000),
  ("fsize_local",                     700152853), # 700.15MB, avg file size 175.04MB
  ("fsize_db",                        19359006495), # 19.36GB, avg file size 967.95MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_111705"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2b2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    33),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 40000),
  ("nof_db_events",                   981549),
  ("fsize_local",                     78442319), # 78.44MB, avg file size 78.44MB
  ("fsize_db",                        50466696906), # 50.47GB, avg file size 1.53GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2tau_M-300_narrow_13TeV-madgraph/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2tau_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_111918"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     602332021), # 602.33MB, avg file size 200.78MB
  ("fsize_db",                        15849336173), # 15.85GB, avg file size 2.26GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_112126"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     631999139), # 632.00MB, avg file size 210.67MB
  ("fsize_db",                        16220410321), # 16.22GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_112304"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     658859551), # 658.86MB, avg file size 219.62MB
  ("fsize_db",                        16455015197), # 16.46GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_112439"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     454718823), # 454.72MB, avg file size 227.36MB
  ("fsize_db",                        11098842678), # 11.10GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_112722"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     450302715), # 450.30MB, avg file size 225.15MB
  ("fsize_db",                        10855478264), # 10.86GB, avg file size 775.39MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_112901"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     480701769), # 480.70MB, avg file size 240.35MB
  ("fsize_db",                        11487024358), # 11.49GB, avg file size 675.71MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_113113"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 188000),
  ("nof_db_events",                   188000),
  ("fsize_local",                     460872317), # 460.87MB, avg file size 230.44MB
  ("fsize_db",                        10754684541), # 10.75GB, avg file size 768.19MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_113421"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     503271007), # 503.27MB, avg file size 251.64MB
  ("fsize_db",                        11547164401), # 11.55GB, avg file size 888.24MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_113730"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2b2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     487964837), # 487.96MB, avg file size 243.98MB
  ("fsize_db",                        11179122535), # 11.18GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/191005_114006"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    26),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 369000),
  ("nof_db_events",                   369000),
  ("fsize_local",                     796089252), # 796.09MB, avg file size 199.02MB
  ("fsize_db",                        20317409524), # 20.32GB, avg file size 781.44MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph/2017v2_2019Oct05_VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_114346"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2b2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     647546896), # 647.55MB, avg file size 215.85MB
  ("fsize_db",                        16551491719), # 16.55GB, avg file size 827.57MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/2017v2_2019Oct05_VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/191005_114600"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     918835048), # 918.84MB, avg file size 229.71MB
  ("fsize_db",                        22555887148), # 22.56GB, avg file size 2.51GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph/2017v2_2019Oct05_VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_115111"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    24),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1043617216), # 1.04GB, avg file size 260.90MB
  ("fsize_db",                        23834632407), # 23.83GB, avg file size 993.11MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_13TeV-madgraph/2017v2_2019Oct05_VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_115252"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_bbtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     926912731), # 926.91MB, avg file size 231.73MB
  ("fsize_db",                        22237635973), # 22.24GB, avg file size 1.39GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph/2017v2_2019Oct05_VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/191005_115859"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     850291712), # 850.29MB, avg file size 212.57MB
  ("fsize_db",                        20440095707), # 20.44GB, avg file size 1.14GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_120308"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     955775689), # 955.78MB, avg file size 238.94MB
  ("fsize_db",                        22130629455), # 22.13GB, avg file size 1.58GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2Tau_node_2_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2Tau_node_2_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_120551"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     888496941), # 888.50MB, avg file size 222.12MB
  ("fsize_db",                        21371438091), # 21.37GB, avg file size 971.43MB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2Tau_node_3_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2Tau_node_3_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_120731"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_4_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     872442315), # 872.44MB, avg file size 218.11MB
  ("fsize_db",                        21451946375), # 21.45GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2Tau_node_4_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2Tau_node_4_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_120936"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 376000),
  ("nof_db_events",                   376000),
  ("fsize_local",                     821260742), # 821.26MB, avg file size 205.32MB
  ("fsize_db",                        20190349511), # 20.19GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2Tau_node_7_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2Tau_node_7_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_121216"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     979681104), # 979.68MB, avg file size 244.92MB
  ("fsize_db",                        22924430937), # 22.92GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2Tau_node_9_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2Tau_node_9_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_121522"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2B2Tau_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_bbtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2b2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     870864895), # 870.86MB, avg file size 217.72MB
  ("fsize_db",                        21176117597), # 21.18GB, avg file size 2.12GB
  ("use_it",                          True),
  ("xsection",                        0.073056),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2017v2_2019Oct05/GluGluToHHTo2B2Tau_node_12_13TeV-madgraph_correctedcfg/2017v2_2019Oct05_GluGluToHHTo2B2Tau_node_12_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/191005_121729"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2v',          'signal_ggf_nonresonant_node_2_hh_2b2v',           'signal_ggf_nonresonant_node_3_hh_2b2v',           'signal_ggf_nonresonant_node_7_hh_2b2v',           'signal_ggf_nonresonant_node_9_hh_2b2v',           'signal_ggf_nonresonant_node_12_hh_2b2v',           ],
  [ 'signal_ggf_nonresonant_node_sm_hh_2b2t',          'signal_ggf_nonresonant_node_2_hh_2b2t',           'signal_ggf_nonresonant_node_3_hh_2b2t',           'signal_ggf_nonresonant_node_4_hh_2b2t',           'signal_ggf_nonresonant_node_7_hh_2b2t',           'signal_ggf_nonresonant_node_9_hh_2b2t',           'signal_ggf_nonresonant_node_12_hh_2b2t',           ],
]

