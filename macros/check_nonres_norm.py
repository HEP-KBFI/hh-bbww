import ROOT
import glob
from HHStatAnalysis.AnalyticalModels.NonResonantModel import NonResonantModel
from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017 import samples_2017
## Have the same for 2016 and
from rootpy.plotting import Hist2D, Hist
import os
os.environ["MKL_NUM_THREADS"] = "1"

cms_base = os.environ['CMSSW_BASE']
model = NonResonantModel()
dumb = model.ReadCoefficients(cms_base+"/src/HHStatAnalysis/AnalyticalModels/data/coefficientsByBin_extended_3M_costHHSim_19-4.txt")

klJHEP = [1.0,  7.5,  1.0,  1.0,  -3.5, 1.0, 2.4, 5.0, 15.0, 1.0, 10.0, 2.4, 15.0]
ktJHEP = [1.0,  1.0,  1.0,  1.0,  1.5,  1.0, 1.0, 1.0, 1.0,  1.0, 1.5,  1.0, 1.0]
c2JHEP = [0.0,  -1.0, 0.5, -1.5, -3.0,  0.0, 0.0, 0.0, 0.0,  1.0, -1.0, 0.0, 1.0]
cgJHEP = [0.0,  0.0, -0.8,  0.0, 0.0,   0.8, 0.2, 0.2, -1.0, -0.6, 0.0, 1.0, 0.0]
c2gJHEP = [0.0, 0.0, 0.6, -0.8, 0.0, -1.0, -0.2,-0.2,  1.0,  0.6, 0.0, -1.0, 0.0]

histfile = cms_base+"/src/Support/NonResonant/Distros_5p_SM3M_sumBenchJHEP_13TeV_19-4.root"
histtitle = "H1bin4"

norm = []
for ii in range(0, 13) :
    norm = norm + [model.getNormalization(
        klJHEP[ii],
        ktJHEP[ii],
        c2JHEP[ii],
        cgJHEP[ii],
        c2gJHEP[ii],
        histfile, histtitle)]
print (norm)

# X: to get the binning of the histogram it should contruct

for era in [2016, 2017, 2018] :
  sumOfWeightsSM = 0.
  sumOfWeightsBM1 = 0.
  sumOfWeightsBM2 = 0.
  sumOfWeightsBM3 = 0.
  sumOfWeightsBM4 = 0.
  sumOfWeightsBM5 = 0.
  sumOfWeightsBM6 = 0.
  sumOfWeightsBM7 = 0.
  sumOfWeightsBM8 = 0.
  sumOfWeightsBM9 = 0.
  sumOfWeightsBM10 = 0.
  sumOfWeightsBM11 = 0.
  sumOfWeightsBM12 = 0.

  for channel in [ "bbvv" ] : #, "bbtt" ] :
    if era == 2017 : samples = samples_2017
    else :
        print ("Invalid era: %s" % era)
        continue

    list = []
    for sample_name, sample_info in samples.items():
      if not sample_name == "sum_events" :
        if sample_info["sample_category"] == "signal_ggf_nonresonant_" + channel :
          list = list + glob.glob(sample_info["local_paths"][0]['path'] + "/*/*.root")
    for fi in list : print (fi)

    label = list[0].split("/")[6]
    outputfile = cms_base + "/src/hhAnalysis/bbww/data/denominator_reweighting_" + channel + "_" + str(era) + ".root"
    histfile = outputfile
    histtitle = 'denominator_reweighting'
    fileHH=ROOT.TFile(histfile)
    sumEvt = fileHH.Get(histtitle)

    inputTree = "Events"
    for ii in range(0, len(list)) : #
        print (list[ii] ,inputTree)
        try: tfile = ROOT.TFile(list[ii], "READ")
        except :
        	print "Doesn't exist"
        	print ('file ', list[ii],' corrupt')
        	continue
        try: tree = tfile.Get(inputTree)
        except :
            print ("FAIL read inputTree", inputTree)
            continue
        if tree is not None :
            countErr = 0
            for ee, event in enumerate(tree):
                #if ee > 1 : break
                if not len(event.GenHiggs_mass) == 2 :
                    ## only the first entry always has 0 lenght
                    countErr = countErr + 1
                    continue
                PHH = [ROOT.TLorentzVector(), ROOT.TLorentzVector()]
                for ll in xrange(len(event.GenHiggs_mass)) :
                    PHH[ll].SetPtEtaPhiM(
                        event.GenHiggs_pt[ll],
                        event.GenHiggs_eta[ll],
                        event.GenHiggs_phi[ll],
                        event.GenHiggs_mass[ll]
                    )
                PHH_SUM = PHH[0] + PHH[1]
                P1boost = PHH[0]
                P1boost.Boost(-PHH_SUM.BoostVector())
                mhh_gen = PHH_SUM.M()
                cost_gen = abs(P1boost.CosTheta())

                for ii in range(0, 13) :
                    denominator = sumEvt.GetBinContent(sumEvt.GetXaxis().FindBin(mhh_gen), sumEvt.GetYaxis().FindBin(abs(cost_gen)))
                    weight = model.getScaleFactor(
                        mhh_gen,
                        cost_gen,
                        klJHEP[ii],
                        ktJHEP[ii],
                        c2JHEP[ii],
                        cgJHEP[ii],
                        c2gJHEP[ii],
                        denominator,
                        norm[ii])

                    if ii == 0 : sumOfWeightsSM  = weight + sumOfWeightsSM
                    if ii == 1 : sumOfWeightsBM1 = weight + sumOfWeightsBM1
                    if ii == 2 : sumOfWeightsBM2 = weight + sumOfWeightsBM2
                    if ii == 3 : sumOfWeightsBM3 = weight + sumOfWeightsBM3
                    if ii == 4 : sumOfWeightsBM4 = weight + sumOfWeightsBM4
                    if ii == 5 : sumOfWeightsBM5 = weight + sumOfWeightsBM5
                    if ii == 6 : sumOfWeightsBM6 = weight + sumOfWeightsBM6
                    if ii == 7 : sumOfWeightsBM7 = weight + sumOfWeightsBM7
                    if ii == 8 : sumOfWeightsBM8 = weight + sumOfWeightsBM8
                    if ii == 9 : sumOfWeightsBM9 = weight + sumOfWeightsBM9
                    if ii == 10 : sumOfWeightsBM10 = weight + sumOfWeightsBM10
                    if ii == 11 : sumOfWeightsBM11 = weight + sumOfWeightsBM11
                    if ii == 12 : sumOfWeightsBM12 = weight + sumOfWeightsBM12

            print ("# events without two Higgses", countErr)
            if countErr > 1 :
                print ("Too many # events without two Higgses")
                break

  print ("sumOfWeightsSM", sumOfWeightsSM)
  print ("sumOfWeightsBM1", sumOfWeightsBM1)
  print ("sumOfWeightsBM2", sumOfWeightsBM2)
  print ("sumOfWeightsBM3", sumOfWeightsBM3)
  print ("sumOfWeightsBM4", sumOfWeightsBM4)
  print ("sumOfWeightsBM5", sumOfWeightsBM5)
  print ("sumOfWeightsBM6", sumOfWeightsBM6)
  print ("sumOfWeightsBM7", sumOfWeightsBM7)
  print ("sumOfWeightsBM8", sumOfWeightsBM8)
  print ("sumOfWeightsBM9", sumOfWeightsBM9)
  print ("sumOfWeightsBM10", sumOfWeightsBM10)
  print ("sumOfWeightsBM11", sumOfWeightsBM11)
  print ("sumOfWeightsBM12", sumOfWeightsBM12)
