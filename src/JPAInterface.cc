#include "hhAnalysis/bbww/interface/JPAInterface.h"

#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs.
#include "hhAnalysis/bbww/interface/comp_metP4_B2G_18_008.h" // comp_metP4_B2G_18_008

#include <TMath.h> // TMath::Abs, TMath::Max, TMath::Min, TMath::Nint
#include <TLorentzVector.h> // TLorentzVector

#include <algorithm> // std::sort

const double topMass = 172.9; // CV: taken from http://pdg.lbl.gov/2019/listings/rpp2019-list-t-quark.pdf ("OUR AVERAGE")
const double higgsBosonMass = 125.;

JPAInterface::JPAInterface(const std::string& mvaInputFilePath)
{
  mvaInputFilePath_ = mvaInputFilePath;
  if ( mvaInputFilePath_.find_last_of("/") != (mvaInputFilePath_.size() - 1) ) mvaInputFilePath_.append("/");

  mvaInputFileNames_1stLayer_even_[(int)JPA::Category_boosted::k2b2W]  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_4jet_boosted_even.xml";
  mvaInputFileNames_1stLayer_odd_[(int)JPA::Category_boosted::k2b2W]   = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_4jet_boosted_odd.xml";
  mvaInputVariables_1stLayer_[(int)JPA::Category_boosted::k2b2W]       = {  
    "wjet1_btagCSV",
    "wjet1_qgDiscr",
    "wjet2_btagCSV",
    "wjet2_qgDiscr",
    "Hbb_pt",
    "HadW_mass",
    "HadW_cosTheta",
    "dR_HadW_lep",
    "min_dR_HadW_bjet",
    "dR_wjet1wjet2",
    "Hww_mass"
  };
  mvaInputFileNames_1stLayer_even_[(int)JPA::Category_boosted::k2b1W]  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingWJet_boosted_even.xml";
  mvaInputFileNames_1stLayer_odd_[(int)JPA::Category_boosted::k2b1W]   = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingWJet_boosted_odd.xml";
  mvaInputVariables_1stLayer_[(int)JPA::Category_boosted::k2b1W]       = {
    "dEta_bjet1_lep",
    "wjet1_ptReg",
    "wjet1_btagCSV",
    "wjet1_qgDiscr",
    "dR_wjet1_lep",
    "Hbb_pt",
    "nBJetMedium"
  };

  for ( int jpaCategory = (int)JPA::Category_boosted::k2b2W; jpaCategory <= (int)JPA::Category_boosted::k2b0W; ++jpaCategory )
  {
    TMVAInterface* mva = new TMVAInterface(
      mvaInputFilePath_ + mvaInputFileNames_1stLayer_even_[jpaCategory], 
      mvaInputFilePath_ + mvaInputFileNames_1stLayer_odd_[jpaCategory], 
      mvaInputVariables_1stLayer_[jpaCategory]);
    mva->enableBDTTransform();
    mvas_1stLayer_[jpaCategory] = mva;
  }

  mvaInputFileNames_1stLayer_even_[(int)JPA::Category_resolved::k2b2W] = "bb1l_jpa_4jet_resolved_even.xml";
  mvaInputFileNames_1stLayer_odd_[(int)JPA::Category_resolved::k2b2W]  = "bb1l_jpa_4jet_resolved_odd.xml";
  mvaInputVariables_1stLayer_[(int)JPA::Category_resolved::k2b2W]      = {
    "bjet1_btagCSV",
    "bjet2_ptReg",
    "bjet2_btagCSV",
    "bjet2_qgDiscr",
    "maxwjetbtagCSV",
    "wjet2_ptReg",
    "wjet2_qgDiscr",
    "HadW_mass",
    "dR_HadW_lep",
    "max_dR_HadW_bjet",
    "dR_wjet1wjet2",
    "mTop1",
    "nBJetMedium",
    "Hbb_massReg"
  };
  mvaInputFileNames_1stLayer_even_[(int)JPA::Category_resolved::k2b1W] = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingWJet_resolved_even.xml";
  mvaInputFileNames_1stLayer_odd_[(int)JPA::Category_resolved::k2b1W]  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingWJet_resolved_odd.xml";
  mvaInputVariables_1stLayer_[(int)JPA::Category_resolved::k2b1W]      = {
    "bjet1_btagCSV",
    "bjet2_ptReg",
    "bjet2_btagCSV",
    "bjet2_qgDiscr",
    "dEta_bjet2_lep",
    "wjet1_ptReg",
    "wjet1_btagCSV",
    "wjet1_qgDiscr",
    "dEta_wjet1_lep",
    "dR_bjet1bjet2",
    "nJet",
    "nBJetLoose",
    "nBJetMedium"
  };
  mvaInputFileNames_1stLayer_even_[(int)JPA::Category_resolved::k2b0W] = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingAllWJet_even.xml";
  mvaInputFileNames_1stLayer_odd_[(int)JPA::Category_resolved::k2b0W]  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingAllWJet_odd.xml";
  mvaInputVariables_1stLayer_[(int)JPA::Category_resolved::k2b0W]      = {
    "bjet1_ptReg",
    "bjet1_btagCSV",
    "bjet2_ptReg",
    "bjet2_btagCSV",
    "bjet2_qgDiscr",
    "dEta_bjet2_lep",
    "Hbb_massReg",
    "nJet",
    "nBJetMedium"
  };
  mvaInputFileNames_1stLayer_even_[(int)JPA::Category_resolved::k1b2W] = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingBJet_even.xml";
  mvaInputFileNames_1stLayer_odd_[(int)JPA::Category_resolved::k1b2W]  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingBJet_odd.xml";
  mvaInputVariables_1stLayer_[(int)JPA::Category_resolved::k1b2W]      = {
    "bjet1_ptReg",
    "bjet1_btagCSV",
    "wjet1_ptReg",
    "wjet1_btagCSV",
    "wjet2_btagCSV",
    "wjet2_qgDiscr",
    "HadW_mass",
    "dR_HadW_lep",
    "dR_wjet1wjet2",
    "mTop1",
    "nJet",
    "nBJetMedium"
  };
  mvaInputFileNames_1stLayer_even_[(int)JPA::Category_resolved::k1b1W] = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingBJet_missingWJet_even.xml";
  mvaInputFileNames_1stLayer_odd_[(int)JPA::Category_resolved::k1b1W]  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingBJet_missingWJet_odd.xml";
  mvaInputVariables_1stLayer_[(int)JPA::Category_resolved::k1b1W]      = {
    "bjet1_ptReg",
    "bjet1_btagCSV",
    "bjet1_qgDiscr",
    "dEta_bjet1_lep",
    "wjet1_ptReg",
    "wjet1_btagCSV",
    "wjet1_qgDiscr",
    "dEta_wjet1_lep",
    "nJet",
    "nBJetLoose",
    "nBJetMedium",
    "nLep"
  };
  mvaInputFileNames_1stLayer_even_[(int)JPA::Category_resolved::k1b1W] = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingBJet_missingAllWJet_even.xml";
  mvaInputFileNames_1stLayer_odd_[(int)JPA::Category_resolved::k1b1W]  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingBJet_missingAllWJet_odd.xml";
  mvaInputVariables_1stLayer_[(int)JPA::Category_resolved::k1b1W]      = {
    "lepton_pt",
    "bjet1_ptReg",
    "bjet1_btagCSV",
    "bjet1_qgDiscr",
    "dEta_bjet1_lep",
    "nJet",
    "nBJetLoose",
    "nBJetMedium"
  };

  for ( int jpaCategory = (int)JPA::Category_resolved::k2b2W; jpaCategory <= (int)JPA::Category_resolved::k0b0to2W; ++jpaCategory )
  {
    TMVAInterface* mva = new TMVAInterface(
      mvaInputFilePath_ + mvaInputFileNames_1stLayer_even_[jpaCategory], 
      mvaInputFilePath_ + mvaInputFileNames_1stLayer_odd_[jpaCategory], 
      mvaInputVariables_1stLayer_[jpaCategory]);
    mva->enableBDTTransform();
    mvas_1stLayer_[jpaCategory] = mva;
  }

  mvaInputFileNames_2ndLayer_even_[kBoosted]  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_evtCat_boosted_even.xml";
  mvaInputFileNames_2ndLayer_odd_[kBoosted]   = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_evtCat_boosted_odd.xml";
  mvaInputVariables_2ndLayer_[kBoosted]       = { 
    "bdtScore_jpa_4jet",
    "bdtScore_jpa_missingWJet"
  };
  mvaInputFileNames_2ndLayer_even_[kResolved] = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_evtCat_resolved_even.xml";
  mvaInputFileNames_2ndLayer_odd_[kResolved]  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_evtCat_resolved_odd.xml";
  mvaInputVariables_2ndLayer_[kResolved]      = { 
    "bdtScore_jpa_4jet", 
    "bdtScore_jpa_missingWJet", 
    "bdtScore_jpa_missingBJet", 
    "bdtScore_jpa_missingAllWJet", 
    "bdtScore_jpa_missingBJet_missingWJet", 
    "bdtScore_jpa_missingBJet_missingAllWJet" 
  };
  for ( int jpaCategory = kResolved; jpaCategory <= kBoosted; ++jpaCategory ) 
  {
    TMVAInterface* mva = new TMVAInterface(
      mvaInputFilePath_ + mvaInputFileNames_2ndLayer_even_[jpaCategory], 
      mvaInputFilePath_ + mvaInputFileNames_2ndLayer_odd_[jpaCategory], 
      mvaInputVariables_2ndLayer_[jpaCategory]);
    mva->enableBDTTransform();
    mvas_2ndLayer_[jpaCategory] = mva;
  }
}

JPAInterface::~JPAInterface()
{
  for ( std::map<int, TMVAInterface*>::iterator it = mvas_1stLayer_.begin();
        it != mvas_1stLayer_.end(); ++it ) {
    delete it->second;
  }
  for ( std::map<int, TMVAInterface*>::iterator it = mvas_2ndLayer_.begin();
        it != mvas_2ndLayer_.end(); ++it ) {
    delete it->second;
  }
}

namespace
{
  bool isHigherJPAScore(const JPA& JPA1, const JPA& JPA2)
  {
    return JPA1.jpaScore() > JPA2.jpaScore();
  }
}

void
JPAInterface::set(const JPA::LorentzVector& leptonP4, int numLeptons, int numJets, int numBJets_loose, int numBJets_medium, double metPx, double metPy, int event_number)
{
  leptonP4_ = leptonP4;
  numLeptons_ = numLeptons;
  numJets_ = numJets;
  numBJets_loose_ = numBJets_loose;
  numBJets_medium_ = numBJets_medium;
  metPx_ = metPx;
  metPy_ = metPy;
  event_number_ = event_number;
}

JPA
JPAInterface::operator()(const std::vector<JPAJet>& ak4Jets,
                         const JPA::LorentzVector& leptonP4, int numLeptons, int numJets, int numBJets_loose, int numBJets_medium, double metPx, double metPy, 
                         int event_number)
{
  set(leptonP4, numLeptons, numJets, numBJets_loose, numBJets_medium, metPx, metPy, event_number);
  std::vector<const JPAJet*> ak4Jets_ptrs = convert_to_ptrs(ak4Jets);
  for ( int jpaCategory = (int)JPA::Category_resolved::k2b2W; jpaCategory <= (int)JPA::Category_resolved::k0b0to2W; ++jpaCategory )
  {
    jpas_[jpaCategory] = makeJPAs_resolved(ak4Jets_ptrs, jpaCategory);
    std::sort(jpas_[jpaCategory].begin(), jpas_[jpaCategory].end(), isHigherJPAScore);
    if ( jpas_[jpaCategory].size() >= 1 ) mvaOutputs_1stLayer_[jpaCategory] = jpas_[jpaCategory].front().jpaScore();
    else mvaOutputs_1stLayer_[jpaCategory] = -1.; // CV: default value, used during training of the 2nd layer BDT also
  }
  std::map<std::string, double> mvaInputVariables;
  mvaInputVariables["bdtScore_jpa_4jet"] = mvaOutputs_1stLayer_[(int)JPA::Category_resolved::k2b2W];
  mvaInputVariables["bdtScore_jpa_missingWJet"] = mvaOutputs_1stLayer_[(int)JPA::Category_resolved::k2b1W];
  mvaInputVariables["bdtScore_jpa_missingBJet"] = mvaOutputs_1stLayer_[(int)JPA::Category_resolved::k1b2W];
  mvaInputVariables["bdtScore_jpa_missingAllWJet"] = mvaOutputs_1stLayer_[(int)JPA::Category_resolved::k2b0W];
  mvaInputVariables["bdtScore_jpa_missingBJet_missingWJet"] = mvaOutputs_1stLayer_[(int)JPA::Category_resolved::k1b1W];
  mvaInputVariables["bdtScore_jpa_missingBJet_missingAllWJet"] = mvaOutputs_1stLayer_[(int)JPA::Category_resolved::k1b0W];
  int mvaOutput_2ndLayer = TMath::Nint((*mvas_2ndLayer_[kResolved])(mvaInputVariables, event_number_, true));
  int jpaCategory = (int)JPA::Category_resolved::kUndefined;
  if      ( mvaOutput_2ndLayer == 1 ) jpaCategory = (int)JPA::Category_resolved::k2b2W;
  else if ( mvaOutput_2ndLayer == 2 ) jpaCategory = (int)JPA::Category_resolved::k2b1W;
  else if ( mvaOutput_2ndLayer == 3 ) jpaCategory = (int)JPA::Category_resolved::k1b2W;
  else if ( mvaOutput_2ndLayer == 4 ) jpaCategory = (int)JPA::Category_resolved::k2b0W;
  else if ( mvaOutput_2ndLayer == 5 ) jpaCategory = (int)JPA::Category_resolved::k1b1W;
  else if ( mvaOutput_2ndLayer == 6 ) jpaCategory = (int)JPA::Category_resolved::k1b0W;
  else if ( mvaOutput_2ndLayer == 7 ) jpaCategory = (int)JPA::Category_resolved::k0b0to2W;
  else assert(0);
  mvaOutput_2ndLayer_[kResolved] = mvaOutput_2ndLayer;
  if ( jpas_[jpaCategory].size() >= 1 ) return jpas_[jpaCategory].front();
  else return JPA(nullptr, nullptr, nullptr, nullptr, -1., (int)JPA::Category_resolved::kUndefined, false);
}

JPA
JPAInterface::operator()(const std::vector<JPAJet>& ak4Jets, const JPAJet& ak8jet_subjet1, const JPAJet& ak8jet_subjet2,
                         const JPA::LorentzVector& leptonP4, int numLeptons, int numJets, int numBJets_loose, int numBJets_medium, double metPx, double metPy, 
                         int event_number)
{
  set(leptonP4, numLeptons, numJets, numBJets_loose, numBJets_medium, metPx, metPy, event_number);
  std::vector<const JPAJet*> ak4Jets_ptrs = convert_to_ptrs(ak4Jets);
  for ( int jpaCategory = (int)JPA::Category_boosted::k2b2W; jpaCategory <= (int)JPA::Category_boosted::k2b0W; ++jpaCategory )
  {
    jpas_[jpaCategory] = makeJPAs_boosted(ak4Jets_ptrs, &ak8jet_subjet1, &ak8jet_subjet2, jpaCategory);
    std::sort(jpas_[jpaCategory].begin(), jpas_[jpaCategory].end(), isHigherJPAScore);
    if ( jpas_[jpaCategory].size() >= 1 ) mvaOutputs_1stLayer_[jpaCategory] = jpas_[jpaCategory].front().jpaScore();
    else mvaOutputs_1stLayer_[jpaCategory] = -1.; // CV: default value, used during training of the 2nd layer BDT also
  }
  std::map<std::string, double> mvaInputVariables;
  mvaInputVariables["bdtScore_jpa_4jet"] = mvaOutputs_1stLayer_[(int)JPA::Category_boosted::k2b2W];
  mvaInputVariables["bdtScore_jpa_missingWJet"] = mvaOutputs_1stLayer_[(int)JPA::Category_boosted::k2b1W];
  int mvaOutput_2ndLayer = TMath::Nint((*mvas_2ndLayer_[kBoosted])(mvaInputVariables, event_number_, true));
  int jpaCategory = (int)JPA::Category_boosted::kUndefined;
  if      ( mvaOutput_2ndLayer == 1 ) jpaCategory = (int)JPA::Category_boosted::k2b2W;
  else if ( mvaOutput_2ndLayer == 2 ) jpaCategory = (int)JPA::Category_boosted::k2b1W;
  else if ( mvaOutput_2ndLayer == 3 ) jpaCategory = (int)JPA::Category_boosted::k2b0W;
  else assert(0);
  mvaOutput_2ndLayer_[kBoosted] = mvaOutput_2ndLayer;
  if ( jpas_[jpaCategory].size() >= 1 ) return jpas_[jpaCategory].front();
  else return JPA(nullptr, nullptr, nullptr, nullptr, -1., (int)JPA::Category_boosted::kUndefined, true);
}

namespace
{
  double
  compCosTheta(const JPA::LorentzVector& wjet1P4, const JPA::LorentzVector& wjet2P4)
  {
    TLorentzVector wjet1P4_lv, wjet2P4_lv;
    wjet1P4_lv.SetPtEtaPhiM(wjet1P4.pt(), wjet1P4.eta(), wjet1P4.phi(), wjet1P4.mass());
    wjet2P4_lv.SetPtEtaPhiM(wjet2P4.pt(), wjet2P4.eta(), wjet2P4.phi(), wjet2P4.mass());
    TLorentzVector hadWP4_lv = wjet1P4_lv + wjet2P4_lv;
  
    TLorentzVector wjet1Boost, wjet2Boost;
    wjet1Boost = wjet1P4_lv;
    wjet1Boost.Boost(-hadWP4_lv.BoostVector());
    wjet2Boost = wjet2P4_lv;
    wjet2Boost.Boost(-hadWP4_lv.BoostVector());

    double cosTheta = -100;
    if ( wjet1P4_lv.Pt() > wjet2P4_lv.Pt() )
    {
      cosTheta = wjet1Boost.CosTheta();
    }
    else
    {
      cosTheta = wjet2Boost.CosTheta();
    }
    return cosTheta;
  }
}

std::map<std::string, double>
JPAInterface::compMVAInputVariables(const JPAJet* bjet1, const JPAJet* bjet2, const JPAJet* wjet1, const JPAJet* wjet2)
{
  double bjet1_ptReg    = 0.; 
  double bjet2_ptReg    = 0.;
  double wjet1_ptReg    = 0.; 
  double wjet2_ptReg    = 0.;

  // CV: treat jets for which b-tagging discriminator is not available as light-quark jets   
  double bjet1_BtagCSV  = 0.; 
  double bjet2_BtagCSV  = 0.;
  double wjet1_BtagCSV  = 0.; 
  double wjet2_BtagCSV  = 0.; 

  // CV: treat jets for which quark/gluon discriminator is not available as quark jets
  double bjet1_QGDiscr  = 1.;
  double bjet2_QGDiscr  = 1.;
  double wjet1_QGDiscr  = 1.;
  double wjet2_QGDiscr  = 1.;

  double dEta_bjet1_lep = 0.;
  double dEta_bjet2_lep = 0.;
  double dEta_wjet1_lep = 0.;
  double dEta_wjet2_lep = 0.;
  if ( bjet1 )
  {
    bjet1_ptReg    = bjet1->p4_reg().pt();
    bjet1_BtagCSV  = bjet1->BtagCSV();
    bjet1_QGDiscr  = bjet1->QGDiscr();
    dEta_bjet1_lep = TMath::Abs(bjet1->p4().eta() - leptonP4_.eta());
  }
  if ( bjet2 )
  {
    bjet2_ptReg    = bjet2->p4_reg().pt();
    bjet2_BtagCSV  = bjet2->BtagCSV();
    bjet2_QGDiscr  = bjet2->QGDiscr();
    dEta_bjet2_lep = TMath::Abs(bjet2->p4().eta() - leptonP4_.eta());
  }
  if ( wjet1 )
  {
    wjet1_ptReg    = wjet1->p4_reg().pt();
    wjet1_BtagCSV  = wjet1->BtagCSV();
    wjet1_QGDiscr  = wjet1->QGDiscr();
    dEta_wjet1_lep = TMath::Abs(wjet1->p4().eta() - leptonP4_.eta());
  }
  if ( wjet2 )
  {
    wjet2_ptReg    = wjet2->p4_reg().pt();
    wjet2_BtagCSV  = wjet2->BtagCSV();
    wjet2_QGDiscr  = wjet2->QGDiscr();
    dEta_wjet2_lep = TMath::Abs(wjet2->p4().eta() - leptonP4_.eta());
  }

  Particle::LorentzVector hadWP4;
  double hadW_cosTheta = 0.;
  double dR_hadW_lep   = 0.;
  double dR_hadW_bjet1 = 0.;
  double dR_hadW_bjet2 = 0.;
  double dR_wjet1wjet2 = 0.;
  Particle::LorentzVector top1P4;
  Particle::LorentzVector top2P4;
  if ( wjet1 && wjet2 )
  { 
    hadW_cosTheta = compCosTheta(wjet1->p4(), wjet2->p4());
    hadWP4 = wjet1->p4() + wjet2->p4();
    dR_hadW_lep = deltaR(hadWP4, leptonP4_);
    if ( bjet1 )
    {
      dR_hadW_bjet1 = deltaR(hadWP4, bjet1->p4());
      top1P4 = bjet1->p4_reg() + hadWP4;
    }
    if ( bjet2 )
    {
      dR_hadW_bjet2 = deltaR(hadWP4, bjet2->p4());
      top2P4 = bjet2->p4_reg() + hadWP4;
    }
    dR_wjet1wjet2 = deltaR(wjet1->p4(), wjet2->p4());
  }
  double min_dR_hadW_bjet = TMath::Min(dR_hadW_bjet1, dR_hadW_bjet2);
  double max_dR_hadW_bjet = TMath::Max(dR_hadW_bjet1, dR_hadW_bjet2);
  double mTop1 = -1.;
  if ( TMath::Abs(top1P4.mass() - topMass) < TMath::Abs(top2P4.mass() - topMass) )
  {
    mTop1 = top1P4.mass();
  }
  else
  {
    mTop1 = top2P4.mass();
  }
  Particle::LorentzVector HbbP4;
  Particle::LorentzVector HbbP4_reg;
  double dR_bjet1bjet2 = 0.;
  if ( bjet1 && bjet2 )
  { 
    HbbP4 = bjet1->p4() + bjet2->p4();
    HbbP4_reg = bjet1->p4_reg() + bjet2->p4_reg();
    dR_bjet1bjet2 = deltaR(bjet1->p4(), bjet2->p4());
  }
  JPA::LorentzVector HwwP4;
  if ( bjet1 && bjet2 && wjet1 && wjet2 ) 
  {
    JPA::LorentzVector neutrinoP4 = comp_metP4_B2G_18_008(leptonP4_ + wjet1->p4() + wjet2->p4(), metPx_, metPy_, higgsBosonMass);
    JPA::LorentzVector lepWP4 = leptonP4_ + neutrinoP4;
    HwwP4 = lepWP4 + hadWP4;
  }

  std::map<std::string, double> mvaInputVariables = {
    { "lepton_pt",        leptonP4_.pt()                           },
    { "bjet1_ptReg",      bjet1_ptReg                              },
    { "bjet1_btagCSV",    bjet1_BtagCSV                            },
    { "bjet1_qgDiscr",    bjet1_QGDiscr                            },
    { "dEta_bjet1_lep",   dEta_bjet1_lep                           },
    { "bjet2_ptReg",      bjet2_ptReg                              },
    { "bjet2_btagCSV",    bjet2_BtagCSV                            },
    { "bjet2_qgDiscr",    bjet2_QGDiscr                            },
    { "dEta_bjet2_lep",   dEta_bjet2_lep                           },
    { "dR_bjet1bjet2",    dR_bjet1bjet2                            },
    { "maxwjetbtagCSV",   TMath::Max(wjet1_BtagCSV, wjet2_BtagCSV) },    
    { "wjet1_ptReg",      wjet1_ptReg                              },
    { "wjet1_btagCSV",    wjet1_BtagCSV                            },
    { "wjet1_qgDiscr",    wjet1_QGDiscr                            },
    { "dEta_wjet1_lep",   dEta_wjet1_lep                           },
    { "wjet2_ptReg",      wjet2_ptReg                              },
    { "wjet2_btagCSV",    wjet2_BtagCSV                            },
    { "wjet2_qgDiscr",    wjet2_QGDiscr                            },
    { "dEta_wjet2_lep",   dEta_wjet2_lep                           },
    { "dR_wjet1wjet2",    dR_wjet1wjet2                            },
    { "HadW_mass",        hadWP4.mass()                            },
    { "HadW_cosTheta",    hadW_cosTheta                            },
    { "dR_HadW_lep",      dR_hadW_lep                              },
    { "min_dR_HadW_bjet", min_dR_hadW_bjet                         },
    { "max_dR_HadW_bjet", max_dR_hadW_bjet                         },
    { "mTop1",            mTop1                                    },
    { "nJet",             numJets_                                 },
    { "nBJetLoose",       numBJets_loose_                          },
    { "nBJetMedium",      numBJets_medium_                         },
    { "nLep",             numLeptons_                              },
    { "Hbb_pt",           HbbP4.pt()                               },
    { "Hbb_massReg",      HbbP4_reg.mass()                         },
    { "Hww_mass",         HwwP4.mass()                             },
  };
  return mvaInputVariables;
}

std::vector<JPA> 
JPAInterface::makeJPAs_resolved(const std::vector<const JPAJet*>& ak4Jets, int jpaCategory)
{
  std::vector<JPA> jpas;
  std::vector<const JPAJet*> bjets1;
  if ( jpaCategory == (int)JPA::Category_resolved::k2b2W || 
       jpaCategory == (int)JPA::Category_resolved::k2b1W ||
       jpaCategory == (int)JPA::Category_resolved::k2b0W ||
       jpaCategory == (int)JPA::Category_resolved::k1b2W || 
       jpaCategory == (int)JPA::Category_resolved::k1b1W ||
       jpaCategory == (int)JPA::Category_resolved::k1b0W )
    bjets1 = ak4Jets;
  else
    bjets1 = { nullptr };
  std::vector<const JPAJet*> bjets2;
  if ( jpaCategory == (int)JPA::Category_resolved::k2b2W || 
       jpaCategory == (int)JPA::Category_resolved::k2b1W ||
       jpaCategory == (int)JPA::Category_resolved::k2b0W )
    bjets2 = ak4Jets;
  else
    bjets2 = { nullptr };
  std::vector<const JPAJet*> wjets1;
  if ( jpaCategory == (int)JPA::Category_resolved::k2b2W || 
       jpaCategory == (int)JPA::Category_resolved::k2b1W ||
       jpaCategory == (int)JPA::Category_resolved::k1b2W || 
       jpaCategory == (int)JPA::Category_resolved::k1b1W )
    wjets1 = ak4Jets;
  else
    wjets1 = { nullptr };
  std::vector<const JPAJet*> wjets2;
  if ( jpaCategory == (int)JPA::Category_resolved::k2b2W || 
       jpaCategory == (int)JPA::Category_resolved::k1b2W )
    wjets2 = ak4Jets;
  else
    wjets2 = { nullptr };
  for ( std::vector<const JPAJet*>::const_iterator bjet1 = bjets1.begin(); bjet1 != bjets1.end(); ++bjet1 ) 
  {
    for ( std::vector<const JPAJet*>::const_iterator bjet2 = bjets2.begin(); bjet2 != bjets2.end(); ++bjet2 ) 
    {
      if ( (*bjet1) && (*bjet2) && !((*bjet1)->p4().pt() > (*bjet2)->p4().pt()) ) continue;
      assert((*bjet1) != (*bjet2) && !((*bjet1) == nullptr && (*bjet2) != nullptr));
      for ( std::vector<const JPAJet*>::const_iterator wjet1 = wjets1.begin(); wjet1 != wjets1.end(); ++wjet1 ) 
      {
        for ( std::vector<const JPAJet*>::const_iterator wjet2 = wjets2.begin(); wjet2 != wjets2.end(); ++wjet2 ) 
        {
          if ( (*wjet1) && (*wjet2) && !((*wjet1)->p4().pt() > (*wjet2)->p4().pt()) ) continue;
          assert((*wjet1) != (*wjet2) && !((*wjet1) == nullptr && (*wjet2) != nullptr));
          TMVAInterface* mva = mvas_1stLayer_[jpaCategory];
          assert(mva);
          std::map<std::string, double> mvaInputVariables = compMVAInputVariables(*bjet1, *bjet2, *wjet1, *wjet2);
          double jpaScore = (*mva)(mvaInputVariables, event_number_);
          jpas.push_back(JPA(*bjet1, *bjet2, *wjet1, *wjet2, jpaScore, jpaCategory, false));
        }
      }
    }
  }
  return jpas;
}

std::vector<JPA> 
JPAInterface::makeJPAs_boosted(const std::vector<const JPAJet*>& ak4Jets, const JPAJet* ak8jet_subjet1, const JPAJet* ak8jet_subjet2, int jpaCategory)
{
  std::vector<JPA> jpas;
  assert(ak8jet_subjet1 && ak8jet_subjet2);
  const JPAJet* bjet1 = nullptr;
  const JPAJet* bjet2 = nullptr;
  if ( ak8jet_subjet1->p4().pt() > ak8jet_subjet2->p4().pt() )
  {
    bjet1 = ak8jet_subjet1;
    bjet2 = ak8jet_subjet2;
  }
  else
  {
    bjet1 = ak8jet_subjet2;
    bjet2 = ak8jet_subjet1;
  }
  std::vector<const JPAJet*> wjets1;
  if ( jpaCategory == (int)JPA::Category_boosted::k2b2W || 
       jpaCategory == (int)JPA::Category_boosted::k2b1W )
    wjets1 = ak4Jets;
  else
    wjets1 = { nullptr };
  std::vector<const JPAJet*> wjets2;
  if ( jpaCategory == (int)JPA::Category_resolved::k2b2W )
    wjets2 = ak4Jets;
  else
    wjets2 = { nullptr };
  for ( std::vector<const JPAJet*>::const_iterator wjet1 = wjets1.begin(); wjet1 != wjets1.end(); ++wjet1 ) 
  {
    for ( std::vector<const JPAJet*>::const_iterator wjet2 = wjets2.begin(); wjet2 != wjets2.end(); ++wjet2 ) 
    {
      if ( (*wjet1) && (*wjet2) && !((*wjet1)->p4().pt() > (*wjet2)->p4().pt()) ) continue;
      assert((*wjet1) != (*wjet2) && !((*wjet1) == nullptr && (*wjet2) != nullptr));
      TMVAInterface* mva = mvas_1stLayer_[jpaCategory];
      assert(mva);
      std::map<std::string, double> mvaInputVariables = compMVAInputVariables(bjet1, bjet2, *wjet1, *wjet2);
      double jpaScore = (*mva)(mvaInputVariables, event_number_);
      jpas.push_back(JPA(bjet1, bjet2, *wjet1, *wjet2, jpaScore, jpaCategory, true));
    }
  }
  return jpas;
}

double
JPAInterface::jpaScore(int jpaCategory) const
{
  std::map<int, double>::const_iterator jpaScore = mvaOutput_2ndLayer_.find(jpaCategory);
  assert(jpaScore != mvaOutput_2ndLayer_.end());
  return jpaScore->second;
}
