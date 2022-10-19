from collections import OrderedDict as OD

# file generated at 2020-10-24 22:13:24 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh_sync_ttbar.py -p /local/karl/ttHNtupleProduction/2016/2020Oct24_woPresel_nonNom_hh_bbww_sync_ttbar/ntuples -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_sync_ttbar.py -M

samples_2016 = OD()
samples_2016["/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "background"),
  ("process_name_specific",           "TTTo2L2Nu"),
  ("nof_files",                       1),
  ("nof_db_files",                    778),
  ("nof_events",                      {
    'Count'                                                                          : [ 47200, ],
    'CountWeighted'                                                                  : [ 4.67551562e+04, 4.67589258e+04, 4.67646992e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.26227109e+04, 5.17790664e+04, 5.12513633e+04, 4.78557539e+04, 4.67549453e+04, 4.59233945e+04, 4.33001523e+04, 4.20993203e+04, 4.11156250e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.68774570e+04, 3.83434023e+04, ],
    'CountWeightedPSWeight'                                                          : [ 4.68023555e+04, 4.67111758e+04, 6.62006797e+04, 4.67202812e+04, 4.67466250e+04, 2.92387227e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.72019219e+05, 4.72013656e+05, 4.72019219e+05, 4.72019219e+05, 4.71721625e+05, 4.71716031e+05, ],
    'CountWeightedFull'                                                              : [ 3.39794675e+06, 3.39793500e+06, 3.39816050e+06, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.82412475e+06, 3.76281500e+06, 3.72447600e+06, 3.47774050e+06, 3.39790400e+06, 3.33730600e+06, 3.14669025e+06, 3.05939425e+06, 2.98791650e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.13335900e+06, 2.78646900e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.40119550e+06, 3.39458875e+06, 4.81087500e+06, 3.39518425e+06, 3.39709275e+06, 2.12482175e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.42968040e+07, 3.42963960e+07, 3.42968040e+07, 3.42968040e+07, 3.42752040e+07, 3.42748000e+07, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.58739258e+04, 4.58723203e+04, 4.58845195e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.58739258e+04, 4.56451055e+04, 4.61018125e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.16048438e+04, 5.07869609e+04, 5.02778086e+04, 4.69434375e+04, 4.58733242e+04, 4.50630117e+04, 4.24827344e+04, 4.13117344e+04, 4.03525352e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.57851992e+04, 3.76274492e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 4.59206133e+04, 4.58234844e+04, 6.49423711e+04, 4.58348047e+04, 4.58759414e+04, 2.86995449e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 4.63035000e+05, 4.63029531e+05, 4.63035000e+05, 4.63035000e+05, 4.62744156e+05, 4.62738688e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.33382675e+06, 3.33352500e+06, 3.33431175e+06, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.33382675e+06, 3.31721675e+06, 3.35036450e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 3.75019350e+06, 3.69072750e+06, 3.65375000e+06, 3.41144675e+06, 3.33375900e+06, 3.27476875e+06, 3.08730175e+06, 3.00215850e+06, 2.93248000e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.05399925e+06, 2.73444575e+06, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.33712925e+06, 3.33007450e+06, 4.71945800e+06, 3.33084150e+06, 3.33382900e+06, 2.08564225e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.36459400e+07, 3.36455440e+07, 3.36459400e+07, 3.36459400e+07, 3.36248160e+07, 3.36244200e+07, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [ 4.67964258e+04, 4.67944141e+04, 4.68008789e+04, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [ 4.68946055e+04, 4.68910039e+04, 4.69001484e+04, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [ 4.68298164e+04, 4.68274023e+04, 4.68337578e+04, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [ 4.69509023e+04, 4.69477422e+04, 4.69567734e+04, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [ 4.68420039e+04, 4.68395312e+04, 4.68474727e+04, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [ 4.69996953e+04, 4.69954453e+04, 4.70068125e+04, ],
    'CountWeightedHighPtTopPtRwgtSF'                                                 : [ 4.68369688e+04, 4.68338867e+04, 4.68416914e+04, ],
    'CountWeightedHighPtTopPtRwgtSFSquared'                                          : [ 4.69655312e+04, 4.69613164e+04, 4.69723164e+04, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [ 5.26705234e+04, 5.18314922e+04, 5.13080312e+04, 4.78853203e+04, 4.67950000e+04, 4.59663242e+04, 4.33156914e+04, 4.21237227e+04, 4.11468555e+04, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [ 5.27877852e+04, 5.19508359e+04, 5.14309102e+04, 4.79777930e+04, 4.68931602e+04, 4.60684023e+04, 4.33892461e+04, 4.22034570e+04, 4.12319492e+04, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [ 5.27080859e+04, 5.18671406e+04, 5.13431328e+04, 4.79201445e+04, 4.68284297e+04, 4.59980781e+04, 4.33478359e+04, 4.21538672e+04, 4.11759219e+04, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [ 5.28519414e+04, 5.20128945e+04, 5.14907461e+04, 4.80371367e+04, 4.69495430e+04, 4.61229297e+04, 4.34443594e+04, 4.22554805e+04, 4.12815078e+04, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [ 5.27263828e+04, 5.18855039e+04, 5.13603867e+04, 4.79323750e+04, 4.68406055e+04, 4.60104570e+04, 4.33563555e+04, 4.21626719e+04, 4.11850039e+04, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [ 5.29159141e+04, 5.20754375e+04, 5.15517539e+04, 4.80864961e+04, 4.69982344e+04, 4.61714492e+04, 4.34820977e+04, 4.22942266e+04, 4.13209141e+04, ],
    'CountWeightedLHEWeightScaleHighPtTopPtRwgtSF'                                   : [ 5.27191523e+04, 5.18768984e+04, 5.13509766e+04, 4.79286445e+04, 4.68355664e+04, 4.60040508e+04, 4.33550742e+04, 4.21595703e+04, 4.11805195e+04, ],
    'CountWeightedLHEWeightScaleHighPtTopPtRwgtSFSquared'                            : [ 5.28743047e+04, 5.20320859e+04, 5.15072734e+04, 4.80545820e+04, 4.69640977e+04, 4.61348477e+04, 4.34576836e+04, 4.22667148e+04, 4.12910039e+04, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [ 5.69104141e+04, 3.83923086e+04, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [ 5.70181523e+04, 3.84901016e+04, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [ 5.69519258e+04, 3.84176094e+04, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [ 5.70899688e+04, 3.85337227e+04, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [ 5.69675547e+04, 3.84301406e+04, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [ 5.71496992e+04, 3.85782148e+04, ],
    'CountWeightedLHEEnvelopeHighPtTopPtRwgtSF'                                      : [ 5.69629922e+04, 3.84216055e+04, ],
    'CountWeightedLHEEnvelopeHighPtTopPtRwgtSFSquared'                               : [ 5.71120938e+04, 3.85423750e+04, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [ 4.68417031e+04, 4.67453516e+04, 6.62305234e+04, 4.67532109e+04, 4.67866094e+04, 2.92785234e+04, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [ 4.69420000e+04, 4.68414688e+04, 6.63479297e+04, 4.68469141e+04, 4.68868125e+04, 2.93562109e+04, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [ 4.68745117e+04, 4.67788828e+04, 6.62791094e+04, 4.67863320e+04, 4.68181172e+04, 2.92978867e+04, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [ 4.69984805e+04, 4.68984570e+04, 6.64312656e+04, 4.69042188e+04, 4.69420977e+04, 2.93889473e+04, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [ 4.68874609e+04, 4.67918828e+04, 6.62927969e+04, 4.67980156e+04, 4.68302266e+04, 2.93080801e+04, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [ 4.70485352e+04, 4.69478516e+04, 6.64918359e+04, 4.69518555e+04, 4.69892578e+04, 2.94248984e+04, ],
    'CountWeightedPSWeightHighPtTopPtRwgtSF'                                         : [ 4.68818281e+04, 4.67866797e+04, 6.62900781e+04, 4.67936523e+04, 4.68245430e+04, 2.93011445e+04, ],
    'CountWeightedPSWeightHighPtTopPtRwgtSFSquared'                                  : [ 4.70128164e+04, 4.69138477e+04, 6.64522734e+04, 4.69191523e+04, 4.69538906e+04, 2.93960781e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [ 4.72254188e+05, 4.72248531e+05, 4.72254188e+05, 4.72254188e+05, 4.71960312e+05, 4.71954656e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [ 4.73148031e+05, 4.73142281e+05, 4.73148031e+05, 4.73148031e+05, 4.72857875e+05, 4.72852125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [ 4.72595688e+05, 4.72590000e+05, 4.72595688e+05, 4.72595688e+05, 4.72301375e+05, 4.72295688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [ 4.73733656e+05, 4.73727906e+05, 4.73733656e+05, 4.73733656e+05, 4.73442312e+05, 4.73436500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [ 4.72708688e+05, 4.72703000e+05, 4.72708688e+05, 4.72708688e+05, 4.72414969e+05, 4.72409250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [ 4.74201469e+05, 4.74195656e+05, 4.74201469e+05, 4.74201469e+05, 4.73911031e+05, 4.73905188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPHighPtTopPtRwgtSF'                           : [ 4.72675562e+05, 4.72669875e+05, 4.72675562e+05, 4.72675562e+05, 4.72381250e+05, 4.72375625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPHighPtTopPtRwgtSFSquared'                    : [ 4.73895781e+05, 4.73890031e+05, 4.73895781e+05, 4.73895781e+05, 4.73604031e+05, 4.73598312e+05, ],
    'CountWeightedFullTOP16011TopPtRwgtSF'                                           : [ 3.40073325e+06, 3.40059125e+06, 3.40105925e+06, ],
    'CountWeightedFullTOP16011TopPtRwgtSFSquared'                                    : [ 3.40786125e+06, 3.40761950e+06, 3.40827650e+06, ],
    'CountWeightedFullLinearTopPtRwgtSF'                                             : [ 3.40315000e+06, 3.40300225e+06, 3.40348725e+06, ],
    'CountWeightedFullLinearTopPtRwgtSFSquared'                                      : [ 3.41196150e+06, 3.41177750e+06, 3.41236325e+06, ],
    'CountWeightedFullQuadraticTopPtRwgtSF'                                          : [ 3.40407725e+06, 3.40386400e+06, 3.40443300e+06, ],
    'CountWeightedFullQuadraticTopPtRwgtSFSquared'                                   : [ 3.41550275e+06, 3.41524000e+06, 3.41605175e+06, ],
    'CountWeightedFullHighPtTopPtRwgtSF'                                             : [ 3.40368825e+06, 3.40348425e+06, 3.40403100e+06, ],
    'CountWeightedFullHighPtTopPtRwgtSFSquared'                                      : [ 3.41302050e+06, 3.41273075e+06, 3.41350125e+06, ],
    'CountWeightedFullLHEWeightScaleTOP16011TopPtRwgtSF'                             : [ 3.82762525e+06, 3.76661700e+06, 3.72859600e+06, 3.47986325e+06, 3.40063025e+06, 3.34038525e+06, 3.14781150e+06, 3.06114175e+06, 2.99016975e+06, ],
    'CountWeightedFullLHEWeightScaleTOP16011TopPtRwgtSFSquared'                      : [ 3.83614100e+06, 3.77532800e+06, 3.73754350e+06, 3.48658850e+06, 3.40775850e+06, 3.34783800e+06, 3.15311850e+06, 3.06697375e+06, 2.99637250e+06, ],
    'CountWeightedFullLHEWeightScaleLinearTopPtRwgtSF'                               : [ 3.83033625e+06, 3.76924400e+06, 3.73115350e+06, 3.48239125e+06, 3.40304750e+06, 3.34271725e+06, 3.15013325e+06, 3.06338325e+06, 2.99228700e+06, ],
    'CountWeightedFullLHEWeightScaleLinearTopPtRwgtSFSquared'                        : [ 3.84076475e+06, 3.77982350e+06, 3.74189875e+06, 3.49090725e+06, 3.41186400e+06, 3.35178250e+06, 3.15714200e+06, 3.07074425e+06, 2.99999125e+06, ],
    'CountWeightedFullLHEWeightScaleQuadraticTopPtRwgtSF'                            : [ 3.83170425e+06, 3.77057525e+06, 3.73238150e+06, 3.48329350e+06, 3.40397325e+06, 3.34362625e+06, 3.15070625e+06, 3.06398925e+06, 2.99297025e+06, ],
    'CountWeightedFullLHEWeightScaleQuadraticTopPtRwgtSFSquared'                     : [ 3.84544000e+06, 3.78433375e+06, 3.74631725e+06, 3.49447600e+06, 3.41540350e+06, 3.35534225e+06, 3.15988775e+06, 3.07357000e+06, 3.00285500e+06, ],
    'CountWeightedFullLHEWeightScaleHighPtTopPtRwgtSF'                               : [ 3.83115900e+06, 3.76995800e+06, 3.73171800e+06, 3.48301075e+06, 3.40358250e+06, 3.34315650e+06, 3.15065075e+06, 3.06377350e+06, 2.99263325e+06, ],
    'CountWeightedFullLHEWeightScaleHighPtTopPtRwgtSFSquared'                        : [ 3.84242425e+06, 3.78123700e+06, 3.74308625e+06, 3.49217925e+06, 3.41292225e+06, 3.35266725e+06, 3.15813350e+06, 3.07160150e+06, 3.00066000e+06, ],
    'CountWeightedFullLHEEnvelopeTOP16011TopPtRwgtSF'                                : [ 4.13571775e+06, 2.78998475e+06, ],
    'CountWeightedFullLHEEnvelopeTOP16011TopPtRwgtSFSquared'                         : [ 4.14358600e+06, 2.79712775e+06, ],
    'CountWeightedFullLHEEnvelopeLinearTopPtRwgtSF'                                  : [ 4.13876225e+06, 2.79184550e+06, ],
    'CountWeightedFullLHEEnvelopeLinearTopPtRwgtSFSquared'                           : [ 4.14877425e+06, 2.80029150e+06, ],
    'CountWeightedFullLHEEnvelopeQuadraticTopPtRwgtSF'                               : [ 4.13992500e+06, 2.79276000e+06, ],
    'CountWeightedFullLHEEnvelopeQuadraticTopPtRwgtSFSquared'                        : [ 4.15312150e+06, 2.80351575e+06, ],
    'CountWeightedFullLHEEnvelopeHighPtTopPtRwgtSF'                                  : [ 4.13959725e+06, 2.79213600e+06, ],
    'CountWeightedFullLHEEnvelopeHighPtTopPtRwgtSFSquared'                           : [ 4.15040250e+06, 2.80093150e+06, ],
    'CountWeightedFullPSWeightTOP16011TopPtRwgtSF'                                   : [ 3.40402925e+06, 3.39705175e+06, 4.81303400e+06, 3.39756875e+06, 3.40000625e+06, 2.12771100e+06, ],
    'CountWeightedFullPSWeightTOP16011TopPtRwgtSFSquared'                            : [ 3.41133750e+06, 3.40400050e+06, 4.82158050e+06, 3.40441375e+06, 3.40729875e+06, 2.13337100e+06, ],
    'CountWeightedFullPSWeightLinearTopPtRwgtSF'                                     : [ 3.40640825e+06, 3.39950900e+06, 4.81652200e+06, 3.39999400e+06, 3.40232000e+06, 2.12911600e+06, ],
    'CountWeightedFullPSWeightLinearTopPtRwgtSFSquared'                              : [ 3.41543225e+06, 3.40816850e+06, 4.82761500e+06, 3.40855700e+06, 3.41129975e+06, 2.13573175e+06, ],
    'CountWeightedFullPSWeightQuadraticTopPtRwgtSF'                                  : [ 3.40736425e+06, 3.40040325e+06, 4.81756500e+06, 3.40083925e+06, 3.40316300e+06, 2.12985925e+06, ],
    'CountWeightedFullPSWeightQuadraticTopPtRwgtSFSquared'                           : [ 3.41905475e+06, 3.41171125e+06, 4.83201600e+06, 3.41204250e+06, 3.41474075e+06, 2.13834825e+06, ],
    'CountWeightedFullPSWeightHighPtTopPtRwgtSF'                                     : [ 3.40695650e+06, 3.40003025e+06, 4.81730450e+06, 3.40052150e+06, 3.40273250e+06, 2.12935950e+06, ],
    'CountWeightedFullPSWeightHighPtTopPtRwgtSFSquared'                              : [ 3.41644075e+06, 3.40930075e+06, 4.82912450e+06, 3.40964275e+06, 3.41215125e+06, 2.13626700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                     : [ 3.43189720e+07, 3.43185640e+07, 3.43189720e+07, 3.43189720e+07, 3.42976480e+07, 3.42972360e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'              : [ 3.43841720e+07, 3.43837520e+07, 3.43841720e+07, 3.43841720e+07, 3.43630600e+07, 3.43626440e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                       : [ 3.43439040e+07, 3.43435000e+07, 3.43439040e+07, 3.43439040e+07, 3.43225200e+07, 3.43221120e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                : [ 3.44264760e+07, 3.44260560e+07, 3.44264760e+07, 3.44264760e+07, 3.44053000e+07, 3.44048800e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                    : [ 3.43522920e+07, 3.43518800e+07, 3.43522920e+07, 3.43522920e+07, 3.43309600e+07, 3.43305480e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'             : [ 3.44605760e+07, 3.44601560e+07, 3.44605760e+07, 3.44605760e+07, 3.44394800e+07, 3.44390560e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPHighPtTopPtRwgtSF'                       : [ 3.43497960e+07, 3.43493800e+07, 3.43497960e+07, 3.43497960e+07, 3.43284040e+07, 3.43279880e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPHighPtTopPtRwgtSFSquared'                : [ 3.44385160e+07, 3.44380960e+07, 3.44385160e+07, 3.44385160e+07, 3.44173240e+07, 3.44169040e+07, ],
    'CountWeightedL1PrefireNomTOP16011TopPtRwgtSF'                                   : [ 4.59179727e+04, 4.59127188e+04, 4.59264180e+04, ],
    'CountWeightedL1PrefireNomTOP16011TopPtRwgtSFSquared'                            : [ 4.60197812e+04, 4.60133086e+04, 4.60293594e+04, ],
    'CountWeightedL1PrefireNomLinearTopPtRwgtSF'                                     : [ 4.59503359e+04, 4.59446484e+04, 4.59585508e+04, ],
    'CountWeightedL1PrefireNomLinearTopPtRwgtSFSquared'                              : [ 4.60745000e+04, 4.60681797e+04, 4.60840039e+04, ],
    'CountWeightedL1PrefireNomQuadraticTopPtRwgtSF'                                  : [ 4.59636992e+04, 4.59579219e+04, 4.59729922e+04, ],
    'CountWeightedL1PrefireNomQuadraticTopPtRwgtSFSquared'                           : [ 4.61252109e+04, 4.61179453e+04, 4.61362969e+04, ],
    'CountWeightedL1PrefireNomHighPtTopPtRwgtSF'                                     : [ 4.59576133e+04, 4.59512305e+04, 4.59661914e+04, ],
    'CountWeightedL1PrefireNomHighPtTopPtRwgtSFSquared'                              : [ 4.60890938e+04, 4.60817812e+04, 4.60994727e+04, ],
    'CountWeightedL1PrefireTOP16011TopPtRwgtSF'                                      : [ 4.59179727e+04, 4.56905508e+04, 4.61447500e+04, ],
    'CountWeightedL1PrefireTOP16011TopPtRwgtSFSquared'                               : [ 4.60197812e+04, 4.57928828e+04, 4.62459727e+04, ],
    'CountWeightedL1PrefireLinearTopPtRwgtSF'                                        : [ 4.59503359e+04, 4.57222969e+04, 4.61772188e+04, ],
    'CountWeightedL1PrefireLinearTopPtRwgtSFSquared'                                 : [ 4.60745000e+04, 4.58473203e+04, 4.63011211e+04, ],
    'CountWeightedL1PrefireQuadraticTopPtRwgtSF'                                     : [ 4.59636992e+04, 4.57360469e+04, 4.61904297e+04, ],
    'CountWeightedL1PrefireQuadraticTopPtRwgtSFSquared'                              : [ 4.61252109e+04, 4.58983945e+04, 4.63517461e+04, ],
    'CountWeightedL1PrefireHighPtTopPtRwgtSF'                                        : [ 4.59576133e+04, 4.57298984e+04, 4.61845703e+04, ],
    'CountWeightedL1PrefireHighPtTopPtRwgtSFSquared'                                 : [ 4.60890938e+04, 4.58618945e+04, 4.63157578e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomTOP16011TopPtRwgtSF'                     : [ 5.16590703e+04, 5.08449219e+04, 5.03400273e+04, 4.69786836e+04, 4.59166016e+04, 4.51102969e+04, 4.25032148e+04, 4.13404688e+04, 4.03878633e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomTOP16011TopPtRwgtSFSquared'              : [ 5.17809531e+04, 5.09691250e+04, 5.04670859e+04, 4.70751289e+04, 4.60183047e+04, 4.52160625e+04, 4.25806367e+04, 4.14238320e+04, 4.04763516e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomLinearTopPtRwgtSF'                       : [ 5.16954375e+04, 5.08797070e+04, 5.03738750e+04, 4.70121211e+04, 4.59489492e+04, 4.51411992e+04, 4.25344141e+04, 4.13698984e+04, 4.04163125e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomLinearTopPtRwgtSFSquared'                : [ 5.18430547e+04, 5.10290703e+04, 5.05249766e+04, 4.71322812e+04, 4.60731562e+04, 4.52688320e+04, 4.26337812e+04, 4.14742891e+04, 4.05242930e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomQuadraticTopPtRwgtSF'                    : [ 5.17154805e+04, 5.08993750e+04, 5.03924648e+04, 4.70255898e+04, 4.59623555e+04, 4.51547188e+04, 4.25438086e+04, 4.13797812e+04, 4.04262578e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomQuadraticTopPtRwgtSFSquared'             : [ 5.19093516e+04, 5.10936328e+04, 5.05881953e+04, 4.71840508e+04, 4.61237461e+04, 4.53192305e+04, 4.26736758e+04, 4.15148203e+04, 4.05655508e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomHighPtTopPtRwgtSF'                       : [ 5.17065742e+04, 5.08893086e+04, 5.03820000e+04, 4.70207070e+04, 4.59562344e+04, 4.51472539e+04, 4.25414844e+04, 4.13754727e+04, 4.04208711e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomHighPtTopPtRwgtSFSquared'                : [ 5.18652969e+04, 5.10481484e+04, 5.05412227e+04, 4.71497539e+04, 4.60877070e+04, 4.52812812e+04, 4.26474336e+04, 4.14856211e+04, 4.05339297e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomTOP16011TopPtRwgtSF'                        : [ 5.58248438e+04, 3.76798281e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomTOP16011TopPtRwgtSFSquared'                 : [ 5.59381172e+04, 3.77807500e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomLinearTopPtRwgtSF'                          : [ 5.58654570e+04, 3.77047344e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomLinearTopPtRwgtSFSquared'                   : [ 5.60075703e+04, 3.78227617e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomQuadraticTopPtRwgtSF'                       : [ 5.58825938e+04, 3.77179570e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomQuadraticTopPtRwgtSFSquared'                : [ 5.60698633e+04, 3.78688789e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomHighPtTopPtRwgtSF'                          : [ 5.58766406e+04, 3.77089219e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomHighPtTopPtRwgtSFSquared'                   : [ 5.60295039e+04, 3.78317383e+04, ],
    'CountWeightedPSWeightL1PrefireNomTOP16011TopPtRwgtSF'                           : [ 4.59647031e+04, 4.58628203e+04, 6.49803125e+04, 4.58728594e+04, 4.59208516e+04, 2.87421016e+04, ],
    'CountWeightedPSWeightL1PrefireNomTOP16011TopPtRwgtSFSquared'                    : [ 4.60687227e+04, 4.59627070e+04, 6.51037188e+04, 4.59708516e+04, 4.60251562e+04, 2.88217012e+04, ],
    'CountWeightedPSWeightL1PrefireNomLinearTopPtRwgtSF'                             : [ 4.59968203e+04, 4.58951523e+04, 6.50271836e+04, 4.59052695e+04, 4.59515703e+04, 2.87608223e+04, ],
    'CountWeightedPSWeightL1PrefireNomLinearTopPtRwgtSFSquared'                      : [ 4.61232461e+04, 4.60178047e+04, 6.51840156e+04, 4.60261992e+04, 4.60782656e+04, 2.88534941e+04, ],
    'CountWeightedPSWeightL1PrefireNomQuadraticTopPtRwgtSF'                          : [ 4.60108398e+04, 4.59091172e+04, 6.50429883e+04, 4.59183008e+04, 4.59646602e+04, 2.87717324e+04, ],
    'CountWeightedPSWeightL1PrefireNomQuadraticTopPtRwgtSFSquared'                   : [ 4.61753164e+04, 4.60691406e+04, 6.52474883e+04, 4.60757891e+04, 4.61278047e+04, 2.88907715e+04, ],
    'CountWeightedPSWeightL1PrefireNomHighPtTopPtRwgtSF'                             : [ 4.60038750e+04, 4.59031680e+04, 6.50381055e+04, 4.59123633e+04, 4.59577188e+04, 2.87642539e+04, ],
    'CountWeightedPSWeightL1PrefireNomHighPtTopPtRwgtSFSquared'                      : [ 4.61378789e+04, 4.60331719e+04, 6.52052930e+04, 4.60412109e+04, 4.60900664e+04, 2.88608984e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomTOP16011TopPtRwgtSF'             : [ 4.63334531e+05, 4.63328969e+05, 4.63334531e+05, 4.63334531e+05, 4.63047250e+05, 4.63041688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomTOP16011TopPtRwgtSFSquared'      : [ 4.64271094e+05, 4.64265406e+05, 4.64271094e+05, 4.64271094e+05, 4.63987375e+05, 4.63981688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomLinearTopPtRwgtSF'               : [ 4.63668438e+05, 4.63662875e+05, 4.63668438e+05, 4.63668438e+05, 4.63380906e+05, 4.63375375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomLinearTopPtRwgtSFSquared'        : [ 4.64839531e+05, 4.64833906e+05, 4.64839531e+05, 4.64839531e+05, 4.64554938e+05, 4.64549312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomQuadraticTopPtRwgtSF'            : [ 4.63795469e+05, 4.63789906e+05, 4.63795469e+05, 4.63795469e+05, 4.63508594e+05, 4.63503000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomQuadraticTopPtRwgtSFSquared'     : [ 4.65329375e+05, 4.65323656e+05, 4.65329375e+05, 4.65329375e+05, 4.65045500e+05, 4.65039781e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomHighPtTopPtRwgtSF'               : [ 4.63747750e+05, 4.63742250e+05, 4.63747750e+05, 4.63747750e+05, 4.63460188e+05, 4.63454688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomHighPtTopPtRwgtSFSquared'        : [ 4.65001750e+05, 4.64996062e+05, 4.65001750e+05, 4.65001750e+05, 4.64716719e+05, 4.64711031e+05, ],
    'CountWeightedFullL1PrefireNomTOP16011TopPtRwgtSF'                               : [ 3.33690150e+06, 3.33650800e+06, 3.33748975e+06, ],
    'CountWeightedFullL1PrefireNomTOP16011TopPtRwgtSFSquared'                        : [ 3.34432075e+06, 3.34383725e+06, 3.34499400e+06, ],
    'CountWeightedFullL1PrefireNomLinearTopPtRwgtSF'                                 : [ 3.33924025e+06, 3.33885950e+06, 3.33984775e+06, ],
    'CountWeightedFullL1PrefireNomLinearTopPtRwgtSFSquared'                          : [ 3.34827400e+06, 3.34784175e+06, 3.34896000e+06, ],
    'CountWeightedFullL1PrefireNomQuadraticTopPtRwgtSF'                              : [ 3.34025775e+06, 3.33980575e+06, 3.34088900e+06, ],
    'CountWeightedFullL1PrefireNomQuadraticTopPtRwgtSFSquared'                       : [ 3.35197625e+06, 3.35143650e+06, 3.35276700e+06, ],
    'CountWeightedFullL1PrefireNomHighPtTopPtRwgtSF'                                 : [ 3.33978150e+06, 3.33933525e+06, 3.34039450e+06, ],
    'CountWeightedFullL1PrefireNomHighPtTopPtRwgtSFSquared'                          : [ 3.34933575e+06, 3.34882650e+06, 3.35009500e+06, ],
    'CountWeightedFullL1PrefireTOP16011TopPtRwgtSF'                                  : [ 3.33690150e+06, 3.32036700e+06, 3.35339400e+06, ],
    'CountWeightedFullL1PrefireTOP16011TopPtRwgtSFSquared'                           : [ 3.34432075e+06, 3.32781550e+06, 3.36074275e+06, ],
    'CountWeightedFullL1PrefireLinearTopPtRwgtSF'                                    : [ 3.33924025e+06, 3.32268600e+06, 3.35573400e+06, ],
    'CountWeightedFullL1PrefireLinearTopPtRwgtSFSquared'                             : [ 3.34827400e+06, 3.33174225e+06, 3.36473575e+06, ],
    'CountWeightedFullL1PrefireQuadraticTopPtRwgtSF'                                 : [ 3.34025775e+06, 3.32370850e+06, 3.35673425e+06, ],
    'CountWeightedFullL1PrefireQuadraticTopPtRwgtSFSquared'                          : [ 3.35197625e+06, 3.33546775e+06, 3.36840550e+06, ],
    'CountWeightedFullL1PrefireHighPtTopPtRwgtSF'                                    : [ 3.33978150e+06, 3.32322050e+06, 3.35628525e+06, ],
    'CountWeightedFullL1PrefireHighPtTopPtRwgtSFSquared'                             : [ 3.34933575e+06, 3.33281875e+06, 3.36579650e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomTOP16011TopPtRwgtSF'                 : [ 3.75412200e+06, 3.69494975e+06, 3.65825875e+06, 3.41396525e+06, 3.33680025e+06, 3.27820900e+06, 3.08879375e+06, 3.00424750e+06, 2.93502275e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomTOP16011TopPtRwgtSFSquared'          : [ 3.76299350e+06, 3.70398475e+06, 3.66749075e+06, 3.42099550e+06, 3.34421475e+06, 3.28590575e+06, 3.09435725e+06, 3.01029975e+06, 2.94145675e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomLinearTopPtRwgtSF'                   : [ 3.75674275e+06, 3.69748175e+06, 3.66072450e+06, 3.41640250e+06, 3.33914325e+06, 3.28045150e+06, 3.09104625e+06, 3.00640000e+06, 2.93706950e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomLinearTopPtRwgtSFSquared'            : [ 3.76747125e+06, 3.70830650e+06, 3.67170950e+06, 3.42515750e+06, 3.34817050e+06, 3.28972075e+06, 3.09825425e+06, 3.01396225e+06, 2.94495200e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomQuadraticTopPtRwgtSF'                : [ 3.75822550e+06, 3.69889650e+06, 3.66207175e+06, 3.41738950e+06, 3.34014950e+06, 3.28144825e+06, 3.09168325e+06, 3.00710025e+06, 2.93783225e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomQuadraticTopPtRwgtSFSquared'         : [ 3.77229425e+06, 3.71299650e+06, 3.67628725e+06, 3.42888325e+06, 3.35187175e+06, 3.29341475e+06, 3.10115300e+06, 3.01693200e+06, 2.94794800e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomHighPtTopPtRwgtSF'                   : [ 3.75758125e+06, 3.69818225e+06, 3.66130000e+06, 3.41702575e+06, 3.33967450e+06, 3.28090275e+06, 3.09153225e+06, 3.00681375e+06, 2.93742125e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomHighPtTopPtRwgtSFSquared'            : [ 3.76911300e+06, 3.70973050e+06, 3.67290400e+06, 3.42642725e+06, 3.34923900e+06, 3.29061300e+06, 3.09922700e+06, 3.01482825e+06, 2.94564200e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomTOP16011TopPtRwgtSF'                    : [ 4.05686175e+06, 2.73824075e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomTOP16011TopPtRwgtSFSquared'             : [ 4.06511175e+06, 2.74557500e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomLinearTopPtRwgtSF'                      : [ 4.05980075e+06, 2.74003550e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomLinearTopPtRwgtSFSquared'               : [ 4.07012250e+06, 2.74863050e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomQuadraticTopPtRwgtSF'                   : [ 4.06106800e+06, 2.74101075e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomQuadraticTopPtRwgtSFSquared'            : [ 4.07465925e+06, 2.75197750e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomHighPtTopPtRwgtSF'                      : [ 4.06062125e+06, 2.74033850e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomHighPtTopPtRwgtSFSquared'               : [ 4.07173250e+06, 2.74927850e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomTOP16011TopPtRwgtSF'                       : [ 3.34030875e+06, 3.33290075e+06, 4.72217550e+06, 3.33360075e+06, 3.33707750e+06, 2.08873175e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomTOP16011TopPtRwgtSFSquared'                : [ 3.34788125e+06, 3.34014825e+06, 4.73111700e+06, 3.34073975e+06, 3.34466675e+06, 2.09452938e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomLinearTopPtRwgtSF'                         : [ 3.34262025e+06, 3.33527625e+06, 4.72554600e+06, 3.33596375e+06, 3.33934025e+06, 2.09009225e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomLinearTopPtRwgtSFSquared'                  : [ 3.35184975e+06, 3.34417800e+06, 4.73696250e+06, 3.34475800e+06, 3.34853725e+06, 2.09682300e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomQuadraticTopPtRwgtSF'                      : [ 3.34366225e+06, 3.33626800e+06, 4.72671650e+06, 3.33691050e+06, 3.34029475e+06, 2.09090312e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomQuadraticTopPtRwgtSFSquared'               : [ 3.35561150e+06, 3.34786125e+06, 4.74160050e+06, 3.34838775e+06, 3.35213575e+06, 2.09953650e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomHighPtTopPtRwgtSF'                         : [ 3.34317300e+06, 3.33581800e+06, 4.72635300e+06, 3.33648600e+06, 3.33977200e+06, 2.09035125e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomHighPtTopPtRwgtSFSquared'                  : [ 3.35288375e+06, 3.34530525e+06, 4.73849750e+06, 3.34583850e+06, 3.34939450e+06, 2.09736325e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomTOP16011TopPtRwgtSF'         : [ 3.36710240e+07, 3.36706160e+07, 3.36710240e+07, 3.36710240e+07, 3.36501800e+07, 3.36497720e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomTOP16011TopPtRwgtSFSquared'  : [ 3.37389720e+07, 3.37385640e+07, 3.37389720e+07, 3.37389720e+07, 3.37183560e+07, 3.37179480e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomLinearTopPtRwgtSF'           : [ 3.36952200e+07, 3.36948120e+07, 3.36952200e+07, 3.36952200e+07, 3.36743240e+07, 3.36739200e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomLinearTopPtRwgtSFSquared'    : [ 3.37802080e+07, 3.37798040e+07, 3.37802080e+07, 3.37802080e+07, 3.37595040e+07, 3.37591000e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomQuadraticTopPtRwgtSF'        : [ 3.37044480e+07, 3.37040440e+07, 3.37044480e+07, 3.37044480e+07, 3.36835880e+07, 3.36831840e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomQuadraticTopPtRwgtSFSquared' : [ 3.38158920e+07, 3.38154800e+07, 3.38158920e+07, 3.38158920e+07, 3.37952600e+07, 3.37948440e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomHighPtTopPtRwgtSF'           : [ 3.37011640e+07, 3.37007600e+07, 3.37011640e+07, 3.37011640e+07, 3.36802600e+07, 3.36798560e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomHighPtTopPtRwgtSFSquared'    : [ 3.37921240e+07, 3.37917120e+07, 3.37921240e+07, 3.37921240e+07, 3.37714040e+07, 3.37709920e+07, ],
  }),
  ("nof_tree_events",                 47200),
  ("nof_db_events",                   67926800),
  ("fsize_local",                     216518624), # 216.52MB, avg file size 216.52MB
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
        ("path",      "/local/karl/ttHNtupleProduction/2016/2020Oct24_woPresel_nonNom_hh_bbww_sync_ttbar/ntuples/TTTo2L2Nu"),
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

