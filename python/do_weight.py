#import ROOT
#ROOT.gROOT.SetBatch(True)
import shutil,subprocess
from HHStatAnalysis.AnalyticalModels.NonResonantModel import NonResonantModel
import os
os.environ["MKL_NUM_THREADS"] = "1"

def load(cms_base) :
    print cms_base
    model = NonResonantModel()
    dumb = model.ReadCoefficients(cms_base+"/src/HHStatAnalysis/AnalyticalModels/data/coefficientsByBin_extended_3M_costHHSim_19-4.txt")
    return model

def evaluate_weight(kl, kt, c2, cg, c2g, mhh_gen, cost_gen, calcSumOfWeights, denominator, model) :
    return model.getScaleFactor(mhh_gen, cost_gen, kl, kt, c2, cg, c2g, denominator, calcSumOfWeights)
