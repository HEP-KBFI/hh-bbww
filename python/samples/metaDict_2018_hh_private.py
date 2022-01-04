from collections import OrderedDict as OD

# file generated at 2021-12-28 15:42:48 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_hh_bbww_mc_2018_RunIIAutumn18MiniAOD_private.txt -m python/samples/metaDict_2018_hh_private.py -c python/samples/sampleLocations_2018_nanoAOD_hh_bbww.txt

meta_dictionary = OD()


### event sums

sum_events = { 
}


meta_dictionary["/GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD/USER"] =  OD([
  ("crab_string",           "2018_2021Dec27_GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD"),
  ("sample_category",       "signal_ggf_spin0_450_hh_bbvv"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_2b2v_private"),
  ("nof_db_events",         297199),
  ("nof_db_files",          743),
  ("fsize_db",              23548779929),
  ("xsection",              0.027654),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.55GB; nevents: 297.20k; release: 9_4_0; last modified: 2021-12-27 13:52:14"),
])


# event statistics by sample category:
# signal_ggf_spin0_450_hh_bbvv: 297.20k

