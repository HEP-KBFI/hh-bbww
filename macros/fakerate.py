import ROOT as r
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--era ", dest="era", help="which era")
options = parser.parse_args()
era = options.era

filename = "data/FR_lep_mva_hh_bbWW_wFullSyst_%s_KBFI_2021Feb3_wCERNUncs2_FRErrTheshold_0p01_new.root" %era
fnew = r.TFile(filename, "recreate")

fold = r.TFile("data/FR_lep_mva_hh_bbWW_wFullSyst_%s_KBFI_2021Feb3_wCERNUncs2_FRErrTheshold_0p01.root" %era)
for h in [k.GetName() for k in fold.GetListOfKeys()]:
    hist = fold.Get(h)
    fnew.cd()
    hist.Write()

def create_newhist(centralhist, sysnames, syshistup, syshistdown):
    for sys in sysnames:
        histname = central + sys
        histsys = centralhist.Clone(histname)
        if '_br' in sys:
            if 'low' in sys:
                if 'up' in sys:
                    histsys.SetBinContent(1, 1, syshistup.GetBinContent(1,1))
                elif 'down' in sys:
                    histsys.SetBinContent(1, 1, syshistdown.GetBinContent(1,1))
            elif 'mid' in sys:
                if 'up' in sys:
                    histsys.SetBinContent(2, 1, syshistup.GetBinContent(2,1))
                elif 'down' in sys:
                    histsys.SetBinContent(2, 1, syshistdown.GetBinContent(2,1))
            elif 'high' in sys:
                if 'up' in sys:
                    histsys.SetBinContent(3, 1, syshistup.GetBinContent(3,1))
                elif 'down' in sys:
                    histsys.SetBinContent(3, 1, syshistdown.GetBinContent(3,1))
        elif '_ee' in sys:
            if 'low' in sys:
                if 'up' in sys:
                    histsys.SetBinContent(1, 2, syshistup.GetBinContent(1,2))
                elif 'down' in sys:
                    histsys.SetBinContent(1, 2, syshistdown.GetBinContent(1,2))
            elif 'mid' in sys:
                if 'up' in sys:
                    histsys.SetBinContent(2, 2, syshistup.GetBinContent(2,2))
                elif 'down' in sys:
                    histsys.SetBinContent(2, 2, syshistdown.GetBinContent(2,2))
            elif 'high' in sys:
                if 'up' in sys:
                    histsys.SetBinContent(3, 2, syshistup.GetBinContent(3,2))
                elif 'down' in sys:
                    histsys.SetBinContent(3, 2, syshistdown.GetBinContent(3,2))
        fnew.cd()
        histsys.Write()
    

central = 'FR_mva030_el_data_comb'
centralhist = fold.Get(central)
syshistup = fold.Get('FR_mva030_el_data_comb_up')
syshistdown = fold.Get('FR_mva030_el_data_comb_down')
sysnames = ['_br_low_ptup', '_br_low_ptdown', '_br_mid_ptup', '_br_mid_ptdown', '_br_high_ptup', '_br_high_ptdown', '_ee_low_ptup', '_ee_low_ptdown', '_ee_mid_ptup', '_ee_mid_ptdown', '_ee_high_ptup', '_ee_high_ptdown']
create_newhist(centralhist, sysnames, syshistup, syshistdown)

central = 'FR_mva050_mu_data_comb'
centralhist = fold.Get(central)
syshistup = fold.Get('FR_mva050_mu_data_comb_up')
syshistdown = fold.Get('FR_mva050_mu_data_comb_down')
create_newhist(centralhist,sysnames, syshistup, syshistdown)

central = 'FR_mva030_el_data_comb_QCD_fakes'
centralhist = fold.Get(central)
syshistup = fold.Get('FR_mva030_el_data_comb_QCD_fakes_up')
syshistdown = fold.Get('FR_mva030_el_data_comb_QCD_fakes_down')
create_newhist(centralhist,sysnames, syshistup, syshistdown)

central = 'FR_mva050_mu_data_comb_QCD_fakes'
centralhist = fold.Get(central)
syshistup = fold.Get('FR_mva050_mu_data_comb_QCD_fakes_up')
syshistdown = fold.Get('FR_mva050_mu_data_comb_QCD_fakes_down')
create_newhist(centralhist,sysnames, syshistup, syshistdown)
