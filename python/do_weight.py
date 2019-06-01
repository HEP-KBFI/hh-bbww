import ROOT
import shutil,subprocess
from HHStatAnalysis.AnalyticalModels.NonResonantModel import NonResonantModel

def load(cms_base) :
    print cms_base
    model = NonResonantModel()
    dumb = model.ReadCoefficients(cms_base+"/src/HHStatAnalysis/AnalyticalModels/data/coefficientsByBin_extended_3M_costHHSim_19-4.txt")
    return model

def getCX(kl, kt, c2, cg, c2g, model) : return model.functionGF(kl, kt, c2, cg, c2g, model.A13tev)

def getBM(kl, kt, c2, cg, c2g, model, cms_base) :
    histfile = cms_base+"/src/Support/NonResonant/Distros_5p_SM3M_sumBenchJHEP_13TeV_19-4.root"
    histtitle = "H1bin4"
    return model.getCluster(kl, kt, c2, cg, c2g, histfile, histtitle)

def getNorm(kl, kt, c2, cg, c2g, model, cms_base) :
    histfile = cms_base+"/src/Support/NonResonant/Distros_5p_SM3M_sumBenchJHEP_13TeV_19-4.root"
    histtitle = "H1bin4"
    return model.getNormalization(kl, kt, c2, cg, c2g, histfile, histtitle)

def evaluate_weight(kl, kt, c2, cg, c2g, mhh_gen, cost_gen, calcSumOfWeights, cms_base, model) :
    ### this histogram bellow should be adapted to our input events
    histfile = cms_base+"/src/Support/NonResonant/Distros_5p_SM3M_sumBenchJHEP_13TeV_19-4.root"
    histtitle = "H1bin4"
    fileHH=ROOT.TFile(histfile)
    sumEvt = fileHH.Get(histtitle)
    denominator = sumEvt.GetBinContent(sumEvt.GetXaxis().FindBin(mhh_gen), sumEvt.GetYaxis().FindBin(abs(cost_gen)))
    return model.getScaleFactor(mhh_gen, cost_gen, kl, kt, c2, cg, c2g, denominator, calcSumOfWeights)
