import FWCore.ParameterSet.Config as cms

from hhAnalysis.bbww.configs.makePlots_cfi import process

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/HT"),
        xAxisTitle = cms.string("HT [GeV]"),
        yAxisTitle = cms.string("dN/dHT [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/met"),
        xAxisTitle = cms.string("met"),
        yAxisTitle = cms.string("dN/dmet")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/met_phi"),
        xAxisTitle = cms.string("#Phi(met)"),
        yAxisTitle = cms.string("dN/d#Phi(met)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/lepPairCharge_loose"),
        xAxisTitle = cms.string("lepPairCharge_loose"),
        yAxisTitle = cms.string("dN/dlepPairCharge_loose")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_wlep"),
        xAxisTitle = cms.string("m_wlep"),
        yAxisTitle = cms.string("dN/dm_wlep")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/met_LD"),
        xAxisTitle = cms.string("met_LD"),
        yAxisTitle = cms.string("dN/dmet_LD")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/lep_pt"),
        xAxisTitle = cms.string("p_{T}^{lep} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{lep} [1/GeV]")
    ),    
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/mll_loose"),
        xAxisTitle = cms.string("mll_loose [GeV]"),
        yAxisTitle = cms.string("dN/dmll_loose [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_Hbb"),
        xAxisTitle = cms.string("#Delta R_{Hbb}"),
        yAxisTitle = cms.string("dN/d#Delta R_{Hbb}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_Hbb"),
        xAxisTitle = cms.string("p_{T}^{Hbb} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{Hbb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_Hbb_regCorr"),
        xAxisTitle = cms.string("m_{Hbb}^{regCorr} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{Hbb}^{regCorr} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_HH_bbregCorr"),
        xAxisTitle = cms.string("m_{HH_bb}^{regCorr} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{HH_bb}^{regCorr} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/mbb_medium"),
        xAxisTitle = cms.string("mbb_{medium} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{bb_medium} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_HH_vis"),
        xAxisTitle = cms.string("m_{HH_vis} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{HH_vis} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_HH"),
        xAxisTitle = cms.string("m_{HH} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{HH} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dPhi_met_lep"),
        xAxisTitle = cms.string("#Delta#Phi(met,lep)"),
        yAxisTitle = cms.string("dN/d#Delta#Phi(met,lep)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dPhi_Hww"),
        xAxisTitle = cms.string("#Delta#Phi(Hww)"),
        yAxisTitle = cms.string("dN/d#Delta#Phi(Hww)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dPhi_HHvis"),
        xAxisTitle = cms.string("#Delta#Phi(HHvis)"),
        yAxisTitle = cms.string("dN/d#Delta#Phi(HHvis)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dPhi_met_Hbb"),
        xAxisTitle = cms.string("#Delta#Phi(met,Hbb)"),
        yAxisTitle = cms.string("dN/d#Delta#Phi(met,Hbb)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dPhi_met_Wjj"),
        xAxisTitle = cms.string("#Delta#Phi(met,Wjj)"),
        yAxisTitle = cms.string("dN/d#Delta#Phi(met,Wjj)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_Hww"),
        xAxisTitle = cms.string("m_{Hww} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{Hww} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_Hww"),
        xAxisTitle = cms.string("pT_{Hww} [GeV]"),
        yAxisTitle = cms.string("dN/dpT_{Hww} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_HH"),
        xAxisTitle = cms.string("p_{T}^{HH} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{HH} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_HHvis"),
        xAxisTitle = cms.string("p_{T}^{HHvis} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{HHvis} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_b1lep"),
        xAxisTitle = cms.string("#Delta R^{b1lep}"),
        yAxisTitle = cms.string("dN/d#Delta R^{b1lep}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_b2lep"),
        xAxisTitle = cms.string("#Delta R^{b2lep}"),
        yAxisTitle = cms.string("dN/d#Delta R^{b2lep}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_lep_Wjj"),
        xAxisTitle = cms.string("#DeltaR(lep,Wjj)"),
        yAxisTitle = cms.string("dN/d#DeltaR(lep,Wjj)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_lep_Hbb"),
        xAxisTitle = cms.string("#DeltaR(lep,Hbb)"),
        yAxisTitle = cms.string("dN/d#DeltaR(lep,Hbb)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_wlep"),
        xAxisTitle = cms.string("pT_wlep"),
        yAxisTitle = cms.string("dN/dpT_wlep")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/bjet1_btagCSV"),
        xAxisTitle = cms.string("bjet1_btagCSV"),
        yAxisTitle = cms.string("dN/dbjet1_btagCSV")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/bjet2_btagCSV"),
        xAxisTitle = cms.string("bjet2_btagCSV"),
        yAxisTitle = cms.string("dN/dbjet2_btagCSV")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/wjet1_btagCSV"),
        xAxisTitle = cms.string("wjet1_btagCSV"),
        yAxisTitle = cms.string("dN/dwjet1_btagCSV")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/wjet2_btagCSV"),
        xAxisTitle = cms.string("wjet2_btagCSV"),
        yAxisTitle = cms.string("dN/dwjet2_btagCSV")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/selLepton_type"),
        xAxisTitle = cms.string("selLepton_type"),
        yAxisTitle = cms.string("dN/dselLepton_type")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_HH_B2G_18_008"),
        xAxisTitle = cms.string("m_{HH} (B2G-18-008) [GeV]"),
        yAxisTitle = cms.string("dN/dm_{HH} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/mjj_highestpt"),
        xAxisTitle = cms.string("m_{jj}^{highestpt} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{jj}^{highestpt} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Hbb_lead_pt"),
        xAxisTitle = cms.string("Hbb_lead_pT"),
        yAxisTitle = cms.string("dN/dHbb_lead_pT")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Hbb_lead_eta"),
        xAxisTitle = cms.string("Hbb_lead_#eta"),
        yAxisTitle = cms.string("dN/dHbb_lead_#eta")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Hbb_lead_phi"),
        xAxisTitle = cms.string("#Phi(Hbb_lead)"),
        yAxisTitle = cms.string("dN/d#Phi(Hbb_lead)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Hbb_sublead_pt"),
        xAxisTitle = cms.string("Hbb_sublead_pT"),
        yAxisTitle = cms.string("dN/dpT(Hbb_sublead)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Hbb_sublead_eta"),
        xAxisTitle = cms.string("#eta(Hbb_sublead)"),
        yAxisTitle = cms.string("dN/d#eta(Hbb_sublead)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Hbb_sublead_phi"),
        xAxisTitle = cms.string("#Phi(Hbb_sublead)"),
        yAxisTitle = cms.string("dN/d#Phi(Hbb_sublead)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Hbb_sublead_m"),
        xAxisTitle = cms.string("Hbb_sublead_m"),
        yAxisTitle = cms.string("dN/dHbb_sublead_m")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Hbb_lead_m"),
        xAxisTitle = cms.string("Hbb_lead_m"),
        yAxisTitle = cms.string("dN/dHbb_lead_m")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Wjj_sublead_pt"),
        xAxisTitle = cms.string("Wjj_sublead_pT"),
        yAxisTitle = cms.string("dN/dWjj_sublead_pT")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Wjj_sublead_eta"),
        xAxisTitle = cms.string("#eta(Wjj_sublead)"),
        yAxisTitle = cms.string("dN/d#eta(Wjj_sublead)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Wjj_sublead_phi"),
        xAxisTitle = cms.string("#Phi(Wjj_sublead)"),
        yAxisTitle = cms.string("dN/d#Phi(Wjj_sublead)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Wjj_lead_pt"),
        xAxisTitle = cms.string("Wjj_lead_pT"),
        yAxisTitle = cms.string("dN/dWjj_lead_pT")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Wjj_lead_eta"),
        xAxisTitle = cms.string("#eta(Wjj_lead)"),
        yAxisTitle = cms.string("dN/d#eta(Wjj_lead)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/Wjj_lead_phi"),
        xAxisTitle = cms.string("#Phi(Wjj_lead)"),
        yAxisTitle = cms.string("dN/d#Phi(Wjj_lead)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/jet1_pt"),
        xAxisTitle = cms.string("jet1_pT"),
        yAxisTitle = cms.string("dN/djet1_pT")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/jet1_eta"),
        xAxisTitle = cms.string("#eta(jet1)"),
        yAxisTitle = cms.string("dN/d#eta(jet1)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/jet1_phi"),
        xAxisTitle = cms.string("#Phi(jet1)"),
        yAxisTitle = cms.string("dN/d#Phi(jet1)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/jet2_pt"),
        xAxisTitle = cms.string("jet2_pT"),
        yAxisTitle = cms.string("dN/djet2_pT")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/jet2_eta"),
        xAxisTitle = cms.string("#eta(jet2)"),
        yAxisTitle = cms.string("dN/d#eta(jet2)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/jet2_phi"),
        xAxisTitle = cms.string("#Phi(jet2)"),
        yAxisTitle = cms.string("dN/d#Phi(jet2)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/mT_W"),
        xAxisTitle = cms.string("m_{T}^{W} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{T}^{W} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/mT_top_3particle"),
        xAxisTitle = cms.string("m_{T}^{top} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{T}^{top} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/mT_top_2particle"),
        xAxisTitle = cms.string("m_{T}^{top} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{T}^{top} [1/GeV]")
    ),
     cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/mindr_lep1_jet"),
        xAxisTitle = cms.string("min#DeltaR(lep1,jet)"),
        yAxisTitle = cms.string("dN/dmin#DeltaR(lep1,jet)")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/avg_dr_jet_central"),
        xAxisTitle = cms.string("avg_dr_jet_central"),
        yAxisTitle = cms.string("dN/davg_dr_jet_central")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/lepPairType_loose"),
        xAxisTitle = cms.string("lepPairType_loose"),
        yAxisTitle = cms.string("dN/dlepPairType_loose")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/selLepton_type"),
        xAxisTitle = cms.string("selLepton_type"),
        yAxisTitle = cms.string("dN/dselLepton_type")
    ),
    cms.PSet(
            histogramName = cms.string("sel/evt/$PROCESS/tau21_Hbb"),
            xAxisTitle = cms.string("tau21_Hbb"),
            yAxisTitle = cms.string("Events")
        ),
    
##    cms.PSet(
##        histogramName = cms.string("sel/evt/$PROCESS/mvaOutput_Hj_tagger"),
##        xAxisTitle = cms.string("MVA Discriminant Hj Tagger"),
##        yAxisTitle = cms.string("dN/dMVA")
##    ),
##    cms.PSet(
##        histogramName = cms.string("sel/evt/$PROCESS/mvaOutput_Hjj_tagger"),
##        xAxisTitle = cms.string("MVA Discriminant Hjj Tagger"),
##        yAxisTitle = cms.string("dN/dMVA")
##    ),
##     cms.PSet(
##         histogramName = cms.string("sel/evt/$PROCESS/vbf_jet1_pt"),
##         xAxisTitle = cms.string("leading VBF jet p_{T} [GeV]"),
##         yAxisTitle = cms.string("dN/dp_{T} [1/GeV]")
##     ),
##     cms.PSet(
##         histogramName = cms.string("sel/evt/$PROCESS/vbf_jet1_eta"),
##         xAxisTitle = cms.string("leading VBF jet #eta"),
##         yAxisTitle = cms.string("dN/d#eta [1/GeV]")
##     ),
##     cms.PSet(
##         histogramName = cms.string("sel/evt/$PROCESS/vbf_jet2_pt"),
##         xAxisTitle = cms.string("subleading VBF jet p_{T} [GeV]"),
##         yAxisTitle = cms.string("dN/dp_{T} [1/GeV]")
##     ),
##     cms.PSet(
##         histogramName = cms.string("sel/evt/$PROCESS/vbf_jet2_eta"),
##         xAxisTitle = cms.string("subleading VBF jet #eta"),
##         yAxisTitle = cms.string("dN/d#eta [1/GeV]")
##     ),
##     cms.PSet(
##         histogramName = cms.string("sel/evt/$PROCESS/vbf_m_jj"),
##         xAxisTitle = cms.string("VBF jet m_{jj} [GeV]"),
##         yAxisTitle = cms.string("dN/dm_{jj} [1/GeV]")
##     ),
##     cms.PSet(
##         histogramName = cms.string("sel/evt/$PROCESS/vbf_deta_jj"),
##         xAxisTitle = cms.string("VBF jet #Delta#eta_{jj} [GeV]"),
##         yAxisTitle = cms.string("dN/d#Delta#eta_{jj}")
##     ),
    cms.PSet(
           histogramName = cms.string("sel/evtYield/$PROCESS/evtYield"),
           xAxisTitle = cms.string("Run Period"),
           yAxisTitle = cms.string("Events / 1 fb^{-1}"),
           divideByBinWidth = cms.bool(False)
    )
])
