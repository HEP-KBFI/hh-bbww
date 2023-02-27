import ROOT as r
import collections

r.gStyle.SetPaintTextFormat('0.3f')

hist_an = collections.OrderedDict([
    ('Muon', r.TH2D("Muon","Muon", 10, 25, 45, 10, 15, 35)),
    ('Electron', r.TH2D("Electron","Electron", 10, 25, 45, 10, 15, 35))
])
fsf=r.TFile('sf_1.root', 'recreate')

for obj in ['Muon', 'Electron']:
    hist = hist_an[obj]
    for ybin in range(1,hist.GetYaxis().GetNbins()+1):
        for xbin in range(1,hist.GetYaxis().GetNbins()+1):
            if obj == 'Muon':
                hist.SetBinContent(xbin, ybin, 0.99)
            elif obj == 'Electron':
                if hist.GetYaxis().GetBinCenter(ybin) > 15 and hist.GetYaxis().GetBinCenter(ybin) <= 25:
                    hist.SetBinContent(xbin, ybin, 0.98)
                else:
                    hist.SetBinContent(xbin, ybin, 1)
    hist.Write()

files = collections.OrderedDict([
    ('Muon', collections.OrderedDict([ 
        ('leadingLeg', '../../tthAnalysis/HiggsToTauTau/data/HLT_Mu17Mu8_Muon17.root'),
        ('subleadingLeg', '../../tthAnalysis/HiggsToTauTau/data/HLT_Mu17Mu8_Muon8.root'),
        ('single', '../../tthAnalysis/HiggsToTauTau/data/triggerSF/2016/Muon_Run2016_legacy_IsoMu22.root')
    ])),
    ('Electron', collections.OrderedDict([
        ('leadingLeg', '../../tthAnalysis/HiggsToTauTau/data/Electron_Ele23leg_eff.root'),
        ('subleadingLeg', '../../tthAnalysis/HiggsToTauTau/data/Electron_Ele12leg_eff.root'),
        ('single', '../../tthAnalysis/HiggsToTauTau/data/triggerSF/2016/Electron_Run2016_legacy_Ele25.root')
    ]))
])

def constrainValue(value,
                 lowerBound,
                 upperBound):
    assert(lowerBound <= upperBound);
    value = max(value, lowerBound);
    value = min(value, upperBound);
    return value;

def effi(ditrig_lead_eff, ditrig_sublead__eff, sltrig_sublead__eff, sltrig_lead__eff):
    return ditrig_lead_eff * ditrig_sublead__eff + (( 1 - ditrig_lead_eff ) * sltrig_sublead__eff) + (( 1 - ditrig_sublead__eff ) * sltrig_lead__eff)

def effi_v2(ditrig_lead_leg1_eff, ditrig_sublead_leg2_eff, 
            ditrig_lead_leg2_eff, ditrig_sublead_leg1_eff,
            sltrig_lead_leg1_eff, sltrig_lead_leg2_eff,
            sltrig_sublead_leg1_eff, sltrig_sublead_leg2_eff
        ):
    PS = sltrig_lead_leg1_eff + sltrig_sublead_leg2_eff - (sltrig_lead_leg1_eff * sltrig_sublead_leg1_eff)
    PD = ditrig_lead_leg1_eff * ditrig_sublead_leg2_eff +\
         ditrig_lead_leg2_eff * ditrig_sublead_leg1_eff -\
         ditrig_lead_leg1_eff * ditrig_sublead_leg1_eff

    third_term = ditrig_sublead_leg2_eff * sltrig_lead_leg1_eff
    fourth_term = ditrig_lead_leg2_eff * sltrig_sublead_leg1_eff
    fifth_term = third_term * fourth_term / PD
    PT = PS + PD - third_term - fourth_term + fifth_term
    if(PT <0) : print('less 0 ', PT)
    #assert(PT >=0)
    return PT
def GetgraphValue(ditrig_graph_lead_MC, ditrig_graph_lead_Data, x):
    return ditrig_graph_lead_MC.Eval(x), ditrig_graph_lead_Data.Eval(x)

c = r.TCanvas('','',600,800)
def fill_2d_from_pogvalue(ditrig_graph_lead_MC, ditrig_graph_sublead_MC, 
                          leadleg_sltrig_graph_MC,subleadleg_sltrig_graph_MC,
                          ditrig_graph_lead_Data, ditrig_graph_sublead_Data, 
                          leadleg_sltrig_graph_Data, subleadleg_sltrig_graph_Data,
                          hist, v2=True):
    xaxis = ditrig_graph_sublead_MC.GetXaxis()
    xaxis_sl = leadleg_sltrig_graph_MC.GetXaxis()
    for ybin in range(1,hist.GetYaxis().GetNbins()+1):
        sublead_bincenter = hist.GetYaxis().GetBinCenter(ybin)
        sublead_x = constrainValue(sublead_bincenter, xaxis.GetXmin(), xaxis.GetXmax());
        sublead_x_sl = constrainValue(sublead_bincenter, xaxis_sl.GetXmin(), xaxis_sl.GetXmax())
        ditrig_sublead__leg2_eff_MC, ditrig_sublead__leg2_eff_Data = GetgraphValue(ditrig_graph_sublead_MC, ditrig_graph_sublead_Data, sublead_x)
        sltrig_sublead__leg2_eff_MC, sltrig_sublead__leg2_eff_Data = GetgraphValue(subleadleg_sltrig_graph_MC, subleadleg_sltrig_graph_Data, sublead_x_sl)
        for xbin in range(1,hist.GetXaxis().GetNbins()+1):
            lead_bincenter = hist.GetXaxis().GetBinCenter(xbin)
            lead_x = constrainValue(lead_bincenter, xaxis.GetXmin(), xaxis.GetXmax());
            lead_x_sl = constrainValue(lead_bincenter, xaxis_sl.GetXmin(), xaxis_sl.GetXmax());
            ditrig_lead_leg1_eff_MC, ditrig_lead_leg1_eff_Data = GetgraphValue(ditrig_graph_lead_MC, ditrig_graph_lead_Data, lead_x)
            sltrig_lead__leg1_eff_MC, sltrig_lead__leg1_eff_Data = GetgraphValue(leadleg_sltrig_graph_MC, leadleg_sltrig_graph_Data, lead_x_sl)
            ditrig_lead_leg2_eff_MC, ditrig_lead_leg2_eff_Data = GetgraphValue(ditrig_graph_lead_MC, ditrig_graph_lead_Data, sublead_x)
            sltrig_lead__leg2_eff_MC, sltrig_lead__leg2_eff_Data = GetgraphValue(leadleg_sltrig_graph_MC, leadleg_sltrig_graph_Data, sublead_x_sl)
            ditrig_sublead__leg1_eff_MC, ditrig_sublead__leg1_eff_Data = GetgraphValue(ditrig_graph_sublead_MC, ditrig_graph_sublead_Data, lead_x)
            sltrig_sublead__leg1_eff_MC, sltrig_sublead__leg1_eff_Data = GetgraphValue(subleadleg_sltrig_graph_MC, subleadleg_sltrig_graph_Data, lead_x_sl)
            eff_MC = effi(ditrig_lead_leg1_eff_MC, ditrig_sublead__leg2_eff_MC, sltrig_sublead__leg2_eff_MC, sltrig_lead__leg1_eff_MC)
            assert(eff_MC <1)
            eff_Data = effi(ditrig_lead_leg1_eff_Data, ditrig_sublead__leg2_eff_Data, sltrig_sublead__leg2_eff_Data, sltrig_lead__leg1_eff_Data)
            if v2:
                eff_MC = effi_v2(ditrig_lead_leg1_eff_MC, ditrig_sublead__leg2_eff_MC, 
                              ditrig_lead_leg2_eff_MC, ditrig_sublead__leg1_eff_MC,
                              sltrig_lead__leg1_eff_MC, sltrig_lead__leg2_eff_MC,
                              sltrig_sublead__leg1_eff_MC, sltrig_sublead__leg2_eff_MC
                )
                if(eff_MC >1):print('******* ', eff_MC)
                #assert(eff_MC <1)
                eff_Data = effi_v2(ditrig_lead_leg1_eff_MC, ditrig_sublead__leg2_eff_Data,
                              ditrig_lead_leg2_eff_MC, ditrig_sublead__leg1_eff_Data,
                              sltrig_lead__leg1_eff_MC, sltrig_lead__leg2_eff_Data,
                              sltrig_sublead__leg1_eff_MC, sltrig_sublead__leg2_eff_Data
                )
                if(eff_Data > 1): print('*8data ', eff_Data)
                #assert(eff_Data <1)
            hist.SetBinContent(xbin, ybin, eff_Data/eff_MC)

eta_bins = collections.OrderedDict([
    ( 'Muon', ["Lt0p9", "0p9to1p2", "1p2to2p1", 'Gt2p1']),
    ( 'Electron', ['Lt1p0', '1p0to1p48', '1p48to1p65', '1p65to2p1', 'Gt2p1'])
])

def Getgraph(graphname_mc, file):
    graph_mc = file.Get(graphname_mc)
    graphname_data = graphname_mc.replace('MC', 'Data')
    graph_data = file.Get(graphname_data)
    return graph_mc, graph_data

for obj in ['Muon', 'Electron']:
    for leadleg_eta_bin in eta_bins[obj]:
        for subleadleg_eta_bin in eta_bins[obj]:
            hist  = r.TH2D('%s_leadleg_%s_subleadleg_%s'%(obj, leadleg_eta_bin, subleadleg_eta_bin), '%s_leadingleg_Eta_%s_subleadingleg_Eta_%s'%(obj, leadleg_eta_bin, subleadleg_eta_bin), 10, 25, 45, 10, 15, 35)
            hist.GetXaxis().SetTitle('Leading lepton pT')
            hist.GetYaxis().SetTitle('Subleading lepton pT')
            hist.SetStats(0)
            leadleg_graphname_MC = 'ZMassEta%s_MC' %(leadleg_eta_bin)
            subleadleg_graphname_MC = 'ZMassEta%s_MC' %(subleadleg_eta_bin)
            f = r.TFile(files[obj]['single'])
            leadleg_sltrig_graph_MC, leadleg_sltrig_graph_Data = Getgraph(leadleg_graphname_MC, f)
            subleadleg_sltrig_graph_MC, subleadleg_sltrig_graph_Data = Getgraph(subleadleg_graphname_MC, f)
            f = r.TFile(files[obj]['leadingLeg'])
            if obj == 'Electron':
                leadleg_graphname_MC = leadleg_graphname_MC.replace('Lt1p0', 'Lt1p48')
                leadleg_graphname_MC = leadleg_graphname_MC.replace('1p0to1p48', 'Lt1p48')
                leadleg_graphname_MC = leadleg_graphname_MC.replace('1p48to1p65', '1p48to2p1')
                leadleg_graphname_MC = leadleg_graphname_MC.replace('1p65to2p1', '1p48to2p1')
                subleadleg_graphname_MC = subleadleg_graphname_MC.replace('Lt1p0', 'Lt1p48')
                subleadleg_graphname_MC = subleadleg_graphname_MC.replace('1p0to1p48', 'Lt1p48')
                subleadleg_graphname_MC = subleadleg_graphname_MC.replace('1p48to1p65', '1p48to2p1')
                subleadleg_graphname_MC = subleadleg_graphname_MC.replace('1p65to2p1', '1p48to2p1')
            ditrig_lead_graph_MC, ditrig_lead_graph_Data = Getgraph(leadleg_graphname_MC, f)
            f = r.TFile(files[obj]['subleadingLeg'])
            ditrig_sublead_graph_MC, ditrig_sublead_graph_Data = Getgraph(subleadleg_graphname_MC, f)
            f.Close()
            fill_2d_from_pogvalue(ditrig_lead_graph_MC, ditrig_sublead_graph_MC, 
                                  leadleg_sltrig_graph_MC, subleadleg_sltrig_graph_MC,
                                  ditrig_lead_graph_Data, ditrig_sublead_graph_Data, 
                                  leadleg_sltrig_graph_Data, subleadleg_sltrig_graph_Data,
                                  hist)
            fsf.cd()
            hist.Write()
            histratio = hist.Clone('ratio_%s' %hist.GetName())
            histratio.Divide(hist_an[obj])
            histratio.Draw('text')
            c.SaveAs('%s.png' %histratio.GetName())
            c.SaveAs('%s.pdf' %histratio.GetName())
            c.Clear()
            histratio.Write()
fsf.Close()

