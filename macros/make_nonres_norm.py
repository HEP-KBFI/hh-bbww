import ROOT
import glob
from HHStatAnalysis.AnalyticalModels.NonResonantModel import NonResonantModel
from hhAnalysis.bbww.samples.hhAnalyzeSamples_2017 import samples_2017
## Have the same for 2016 and
from rootpy.plotting import Hist2D
import os
os.environ["MKL_NUM_THREADS"] = "1"

cms_base = os.environ['CMSSW_BASE'] #"/home/acaan/VHbbNtuples_8_0_x/CMSSW_9_4_7/"
print (cms_base)

model = NonResonantModel()
# X: to get the binning of the histogram it should contruct

for era in [2016, 2017, 2018] :
    if era == 2017 : samples = samples_2017
    else : raise ValueError("Invalid era: %s" % era)

    raise ValueError("Just test" )
    procP1=glob.glob("/hdfs/local/karl/ttHNtupleProduction/2017/2018Nov06_hh_bbww_woPresel_nom_hh_bbww/ntuples/signal_ggf_nonresonant_node_*_hh_2b2v/*/*.root")
    denominator_reweighting = Hist2D(model.binGenMHH, model.binGenCostS, name='denominator_reweighting')

    list=procP1
    inputTree = "Events"
    for ii in range(0, len(list)) : #
        print (list[ii] ,inputTree)
        try: tfile = ROOT.TFile(list[ii])
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

    outputfile = cms_base + "src/hhAnalysis/bbww/data/denominator_reweighting_" + str(era) + ".root"
    f = ROOT.TFile(outputfile, "recreate")
    f.cd()
    denominator_reweighting.Write()
    f.Close()
    print ("saved", outputfile)
