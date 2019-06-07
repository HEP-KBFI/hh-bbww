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
# X: to get the binning of the histogram it should contruct

for era in [2016, 2017, 2018] :
  for channel in [ "bbvv", "bbtt" ] :
    if era == 2017 : samples = samples_2017
    else :
        print ("Invalid era: %s" % era)
        continue

    list = []
    for sample_name, sample_info in samples.items():
      if not sample_name == "sum_events" :
        if sample_info["sample_category"] == "signal_ggf_nonresonant_" + channel :
          list = list + glob.glob(sample_info["local_paths"][0]['path'] + "/*/*.root")

    label = list[0].split("/")[6]
    #outputfile = cms_base + "/src/hhAnalysis/bbww/data/denominator_reweighting_" + str(era) + ".root"
    outputfile = cms_base + "/src/hhAnalysis/bbww/data/denominator_reweighting_" + channel + "_" + str(era) + ".root"
    if ( os.path.exists(outputfile) ) :
        ifile = ROOT.TFile(outputfile, "READ")
        try : ifile.Get(label)
        except : print ("remaking ", outputfile, " with label ", label)
        else :
            print ("There is no need to remake ", outputfile, " with label ", label)
            continue

    inputTree = "Events"
    denominator_reweighting = Hist2D(model.binGenMHH, model.binGenCostS, name='denominator_reweighting')
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
                denominator_reweighting.Fill( PHH_SUM.M(), abs(P1boost.CosTheta()) )
            print ("# events without two Higgses", countErr)
            if countErr > 1 :
                print ("Too many # events without two Higgses")
                break

    denominator_label = Hist(1,0,1, name=label)
    f = ROOT.TFile(outputfile, "recreate")
    f.cd()
    denominator_reweighting.Write()
    denominator_label.Write()
    f.Close()
    print ("saved", outputfile)
