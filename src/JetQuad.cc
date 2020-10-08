#include "hhAnalysis/bbww/interface/JetQuad.h"
#include <TROOT.h>
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // isGenMatched
#include <TROOT.h>
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // isGenMatched
#include "hhAnalysis/bbww/interface/comp_metP4_B2G_18_008.h" // comp_metP4_B2G_18_008

#include <algorithm> // std::sort
#include <TLorentzVector.h> // TLorentzVector
const double topMass = 172.9; // CV: taken from http://pdg.lbl.gov/2019/listings/rpp2019-list-t-quark.pdf ("OUR AVERAGE")
const double higgsBosonMass = 125.;

double
compCosTheta(const Particle::LorentzVector& recWJet1, const Particle::LorentzVector& recWJet2)
{
  TLorentzVector PWj1, PWj2;
  PWj1.SetPtEtaPhiM(recWJet1.pt(), recWJet1.eta(), recWJet1.phi(), recWJet1.mass());
  PWj2.SetPtEtaPhiM(recWJet2.pt(), recWJet2.eta(), recWJet2.phi(), recWJet2.mass());
  TLorentzVector PW = PWj1 + PWj2;
  
  TLorentzVector PWj1boost, PWj2boost;
  PWj1boost = PWj1;
  PWj1boost.Boost(-PW.BoostVector());
  PWj2boost = PWj2;
  PWj2boost.Boost(-PW.BoostVector());

  double cosTheta = -100;
  if ( PWj1.Pt() > PWj2.Pt() )
    {
      cosTheta = PWj1boost.CosTheta();
    }
  else
    {
      cosTheta = PWj2boost.CosTheta();
    }
  return cosTheta;
}

bool
isHigherRankedByBDT(const JetQuadBase& quad1, const JetQuadBase& quad2)
{
  double bdtScore1 = quad1.bdtScore_;
  double bdtScore2 = quad2.bdtScore_;
  return ( bdtScore1 > bdtScore2 );
}

std::vector<JetQuadBase> 
makeJetQuads(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets, const RecoJetAK8* selJetAK8_Hbb)
{
  std::vector<JetQuadBase> jetQuads;
  if ( !selJetAK8_Hbb ) {
    for ( std::vector<const RecoJet*>::const_iterator selBJet1 = selJetsAK4.begin(); selBJet1 != selJetsAK4.end(); ++selBJet1 ) 
    {
      for ( std::vector<const RecoJet*>::const_iterator selBJet2 = selBJet1 + 1; selBJet2 != selJetsAK4.end(); ++selBJet2 )
      {
	for ( std::vector<const RecoJet*>::const_iterator selWJet1 = selJetsAK4.begin(); selWJet1 != selJetsAK4.end(); ++selWJet1 )
	{
	  for ( std::vector<const RecoJet*>::const_iterator selWJet2 = selWJet1 + 1; selWJet2 != selJetsAK4.end(); ++selWJet2 )
	  {
	    if ( deltaR((*selWJet1)->p4(), (*selBJet1)->p4()) <0.1 || deltaR((*selWJet1)->p4(), (*selBJet2)->p4()) <0.1 ) continue;
	    if ( deltaR((*selWJet2)->p4(), (*selBJet1)->p4()) <0.1 || deltaR((*selWJet2)->p4(), (*selBJet2)->p4()) <0.1 ) continue;
	    bool selBJet1_isGenMatched = ( genBJets.size() ) ? isGenMatchedT<GenJet>((*selBJet1)->eta(), (*selBJet1)->phi(), genBJets) : false;
	    bool selBJet2_isGenMatched = ( genBJets.size() ) ? isGenMatchedT<GenJet>((*selBJet2)->eta(), (*selBJet2)->phi(), genBJets) : false;
	    bool selWJet1_isGenMatched = ( genWJets.size() ) ? isGenMatchedT<GenJet>((*selWJet1)->eta(), (*selWJet1)->phi(), genWJets) : false;
	    bool selWJet2_isGenMatched = ( genWJets.size() ) ? isGenMatchedT<GenJet>((*selWJet2)->eta(), (*selWJet2)->phi(), genWJets) : false;
	    JetQuadBase jetQuad(*selBJet1, selBJet1_isGenMatched, *selBJet2, selBJet2_isGenMatched, *selWJet1, selWJet1_isGenMatched, *selWJet2, selWJet2_isGenMatched);
	    jetQuads.push_back(jetQuad); 
	  }
	}
      }
    }
  }
  else
  {
    for ( std::vector<const RecoJet*>::const_iterator selWJet1 = selJetsAK4.begin(); selWJet1 != selJetsAK4.end(); ++selWJet1 )
    {
      for ( std::vector<const RecoJet*>::const_iterator selWJet2 = selWJet1 + 1; selWJet2 != selJetsAK4.end(); ++selWJet2 )
      {
	bool selWJet1_isGenMatched = ( genWJets.size() ) ? isGenMatchedT<GenJet>((*selWJet1)->eta(), (*selWJet1)->phi(), genWJets) : false;
	bool selWJet2_isGenMatched = ( genWJets.size() ) ? isGenMatchedT<GenJet>((*selWJet2)->eta(), (*selWJet2)->phi(), genWJets) : false;
	JetQuadBase jetQuad(selJetAK8_Hbb->subJet1(), false, selJetAK8_Hbb->subJet2(), false, *selWJet1, selWJet1_isGenMatched, *selWJet2, selWJet2_isGenMatched);
	jetQuads.push_back(jetQuad);
      }
    }
  }
  return jetQuads;
}

std::vector<JetQuadBase>
makeJetTripletsMissingBJet(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets)
{
  std::vector<JetQuadBase> jetTriplets;
  for ( std::vector<const RecoJet*>::const_iterator selBJet1 = selJetsAK4.begin(); selBJet1 != selJetsAK4.end(); ++selBJet1 )
    {
      for ( std::vector<const RecoJet*>::const_iterator selWJet1 = selJetsAK4.begin(); selWJet1 != selJetsAK4.end(); ++selWJet1 )
        {
          for ( std::vector<const RecoJet*>::const_iterator selWJet2 = selWJet1 + 1; selWJet2 != selJetsAK4.end(); ++selWJet2 )
            {
              if ( deltaR((*selWJet1)->p4(), (*selBJet1)->p4()) <0.1 ) continue;
              if ( deltaR((*selWJet2)->p4(), (*selBJet1)->p4()) <0.1 ) continue;
              bool selBJet1_isGenMatched = ( genBJets.size() ) ? isGenMatchedT<GenJet>((*selBJet1)->eta(), (*selBJet1)->phi(), genBJets) : false;
              bool selWJet1_isGenMatched = ( genWJets.size() ) ? isGenMatchedT<GenJet>((*selWJet1)->eta(), (*selWJet1)->phi(), genWJets) : false;
              bool selWJet2_isGenMatched = ( genWJets.size() ) ? isGenMatchedT<GenJet>((*selWJet2)->eta(), (*selWJet2)->phi(), genWJets) : false;
              JetQuadBase jetTriplet(*selBJet1, selBJet1_isGenMatched, nullptr, false, *selWJet1, selWJet1_isGenMatched, *selWJet2, selWJet2_isGenMatched);
              jetTriplets.push_back(jetTriplet);
            }
        }
    }
  return jetTriplets;
}

std::vector<JetQuadBase>
makeJetTripletsMissingWJet(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets, const RecoJetAK8* selJetAK8_Hbb)
{
  std::vector<JetQuadBase> jetTriplets;
  if ( !selJetAK8_Hbb ) {
    for ( std::vector<const RecoJet*>::const_iterator selBJet1 = selJetsAK4.begin(); selBJet1 != selJetsAK4.end(); ++selBJet1 )
    {
      for ( std::vector<const RecoJet*>::const_iterator selBJet2 = selBJet1+1; selBJet2 != selJetsAK4.end(); ++selBJet2 )
      {
	for ( std::vector<const RecoJet*>::const_iterator selWJet1 = selJetsAK4.begin(); selWJet1 != selJetsAK4.end(); ++selWJet1 )
        {
	  if ( deltaR((*selWJet1)->p4(), (*selBJet1)->p4()) <0.1 || deltaR((*selWJet1)->p4(), (*selBJet2)->p4()) <0.1 ) continue;
	  bool selBJet1_isGenMatched = ( genBJets.size() ) ? isGenMatchedT<GenJet>((*selBJet1)->eta(), (*selBJet1)->phi(), genBJets) : false;
	  bool selBJet2_isGenMatched = ( genBJets.size() ) ? isGenMatchedT<GenJet>((*selBJet2)->eta(), (*selBJet2)->phi(), genBJets) : false;
	  bool selWJet1_isGenMatched = ( genWJets.size() ) ? isGenMatchedT<GenJet>((*selWJet1)->eta(), (*selWJet1)->phi(), genWJets) : false;
	  JetQuadBase jetTriplet(*selBJet1, selBJet1_isGenMatched, *selBJet2, selBJet2_isGenMatched, *selWJet1, selWJet1_isGenMatched, nullptr, false);
	  jetTriplets.push_back(jetTriplet);
	}
      }
    }
  }
  else 
  {
    for ( std::vector<const RecoJet*>::const_iterator selWJet1 = selJetsAK4.begin(); selWJet1 != selJetsAK4.end(); ++selWJet1 )
    {
      bool selWJet1_isGenMatched = ( genWJets.size() ) ? isGenMatchedT<GenJet>((*selWJet1)->eta(), (*selWJet1)->phi(), genWJets) : false;
      JetQuadBase jetQuad(selJetAK8_Hbb->subJet1(), false, selJetAK8_Hbb->subJet2(), false, *selWJet1, selWJet1_isGenMatched, nullptr, false);
      jetTriplets.push_back(jetQuad);
    }
  }
  return jetTriplets;
}

std::vector<JetQuadBase> 
makeJetDoubletsMissingBJetMissingWJet(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets)
{
  std::vector<JetQuadBase> jetDoublets;
  for ( std::vector<const RecoJet*>::const_iterator selBJet1 = selJetsAK4.begin(); selBJet1 != selJetsAK4.end(); ++selBJet1 )
    {
      for ( std::vector<const RecoJet*>::const_iterator selWJet1 = selJetsAK4.begin(); selWJet1 != selJetsAK4.end(); ++selWJet1 )
	{
	  if ( deltaR((*selWJet1)->p4(), (*selBJet1)->p4()) <0.1 ) continue;
	  bool selBJet1_isGenMatched = ( genBJets.size() ) ? isGenMatchedT<GenJet>((*selBJet1)->eta(), (*selBJet1)->phi(), genBJets) : false;
	  bool selWJet1_isGenMatched = ( genWJets.size() ) ? isGenMatchedT<GenJet>((*selWJet1)->eta(), (*selWJet1)->phi(), genWJets) : false;
	  JetQuadBase jetDoublet(*selBJet1, selBJet1_isGenMatched, nullptr, false, *selWJet1, selWJet1_isGenMatched, nullptr, false);
	  jetDoublets.push_back(jetDoublet);
	}
    }
  return jetDoublets;
}

std::vector<JetQuadBase>
makeJetDoubletsMissingAllWJet(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets)
{
  std::vector<JetQuadBase> jetDoublets;
  for ( std::vector<const RecoJet*>::const_iterator selBJet1 = selJetsAK4.begin(); selBJet1 != selJetsAK4.end(); ++selBJet1 )
    {
      for ( std::vector<const RecoJet*>::const_iterator selBJet2 = selBJet1+1; selBJet2 != selJetsAK4.end(); ++selBJet2 )
        {
          bool selBJet1_isGenMatched = ( genBJets.size() ) ? isGenMatchedT<GenJet>((*selBJet1)->eta(), (*selBJet1)->phi(), genBJets) : false;
          bool selBJet2_isGenMatched = ( genBJets.size() ) ? isGenMatchedT<GenJet>((*selBJet2)->eta(), (*selBJet2)->phi(), genBJets) : false;
          JetQuadBase jetDoublet(*selBJet1, selBJet1_isGenMatched, *selBJet2, selBJet2_isGenMatched, nullptr, false, nullptr, false);
          jetDoublets.push_back(jetDoublet);
        }
    }
  return jetDoublets;
}

std::vector<JetQuadBase>
makeJetSingletsMissingBJetMissingAllWJet(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets)
{
  std::vector<JetQuadBase> jetSinglets;
  for ( std::vector<const RecoJet*>::const_iterator selBJet1 = selJetsAK4.begin(); selBJet1 != selJetsAK4.end(); ++selBJet1 )
    {
      bool selBJet1_isGenMatched = ( genBJets.size() ) ? isGenMatchedT<GenJet>((*selBJet1)->eta(), (*selBJet1)->phi(), genBJets) : false;
      JetQuadBase jetSinglet(*selBJet1, selBJet1_isGenMatched, nullptr, false, nullptr, false, nullptr, false);
      jetSinglets.push_back(jetSinglet);
    }
  return jetSinglets;
}

TMVAInterface initialize_mva_evt_category(bool Hbb_isBoosted)
{
  std::string mvaFileName_jpa_evtCat_even = ( !Hbb_isBoosted ) ? "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_evtCat_resolved_even.xml" : "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_evtCat_boosted_even.xml";
  std::string mvaFileName_jpa_evtCat_odd  = ( !Hbb_isBoosted ) ? "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_evtCat_resolved_odd.xml" : "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_evtCat_boosted_odd.xml";
  std::vector<std::string> mvaInputVariables;
  if ( !Hbb_isBoosted ) {
    mvaInputVariables = {
      "bdtScore_jpa_4jet", "bdtScore_jpa_missingWJet", "bdtScore_jpa_missingBJet", "bdtScore_jpa_missingAllWJet", "bdtScore_jpa_missingBJet_missingWJet", "bdtScore_jpa_missingBJet_missingAllWJet"
    };
  }
  else {
    mvaInputVariables = {
      "bdtScore_jpa_4jet", "bdtScore_jpa_missingWJet"
    };
  }
  TMVAInterface mva_jpa_evtCat(mvaFileName_jpa_evtCat_odd, mvaFileName_jpa_evtCat_even, mvaInputVariables);
  mva_jpa_evtCat.enableBDTTransform();
  return mva_jpa_evtCat;
}

int evt_category(const TMVAInterface& mva, double bdtScore_jpa_4jet, double bdtScore_jpa_missingWJet, double bdtScore_jpa_missingBJet, 
		 double bdtScore_jpa_missingAllWJet, double bdtScore_jpa_missingBJet_missingWJet, double bdtScore_jpa_missingBJet_missingAllWJet,
		 EventInfo eventInfo, const RecoJetAK8* selJetAK8_Hbb) {

  std::map<std::string, double> mvaInputVariables;
  if ( !selJetAK8_Hbb ) {
    mvaInputVariables = {
      {"bdtScore_jpa_4jet",                                 bdtScore_jpa_4jet},
      {"bdtScore_jpa_missingWJet",                          bdtScore_jpa_missingWJet},
      {"bdtScore_jpa_missingBJet",                          bdtScore_jpa_missingBJet},
      {"bdtScore_jpa_missingAllWJet",                       bdtScore_jpa_missingAllWJet},
      {"bdtScore_jpa_missingBJet_missingWJet",              bdtScore_jpa_missingBJet_missingWJet},
      {"bdtScore_jpa_missingBJet_missingAllWJet",           bdtScore_jpa_missingBJet_missingAllWJet},
    };
  }
  else {
    mvaInputVariables = {
      {"bdtScore_jpa_4jet",                                 bdtScore_jpa_4jet},
      {"bdtScore_jpa_missingWJet",                          bdtScore_jpa_missingWJet},
    };
  }
  int output = (int) mva(mvaInputVariables, eventInfo.event, true);
  return (output+1);
}

TMVAInterface initialize_mva_jpa_4jet(bool Hbb_isBoosted)
{
  std::string mvaFileName_even = ( !Hbb_isBoosted ) ? "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_4jet_resolved_even.xml" : "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_4jet_boosted_even.xml";
  std::string mvaFileName_odd  = ( !Hbb_isBoosted ) ? "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_4jet_resolved_odd.xml" : "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_4jet_boosted_odd.xml";
  std::vector<std::string> mvaInputVariables;
  if ( !Hbb_isBoosted ) {
    mvaInputVariables = {
    "bjet1_btagCSV", "bjet2_ptReg", "bjet2_btagCSV", "bjet2_qgDiscr", "maxwjetbtagCSV", "wjet2_ptReg", "wjet2_qgDiscr", "HadW_mass", "dR_HadW_lep", "max_dR_HadW_bjet", "dR_wjet1wjet2", "mTop1", "nBJetMedium", "Hbb_massReg"
  };
  }
  else {
    mvaInputVariables = {
      "wjet1_btagCSV", "wjet1_qgDiscr", "wjet2_btagCSV", "wjet2_qgDiscr", "Hbb_pt", "HadW_mass", "HadW_cosTheta", "dR_HadW_lep", "min_dR_HadW_bjet", "dR_wjet1wjet2", "Hww_mass"
    };
  }
  TMVAInterface mva(mvaFileName_odd, mvaFileName_even, mvaInputVariables);
  mva.enableBDTTransform();
  return mva;
}

TMVAInterface initialize_mva_jpa_missingBJet()
{
  std::string mvaFileName_even = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingBJet_even.xml";
  std::string mvaFileName_odd  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingBJet_odd.xml";
  std::vector<std::string> mvaInputVariables = {
    "bjet1_ptReg", "bjet1_btagCSV", "wjet1_ptReg", "wjet1_btagCSV", "wjet2_btagCSV", "wjet2_qgDiscr", "HadW_mass", "dR_HadW_lep", "dR_wjet1wjet2", "mTop1", "nJet", "nBJetMedium"
  };
  TMVAInterface mva(mvaFileName_odd, mvaFileName_even, mvaInputVariables);
  mva.enableBDTTransform();
  return mva;
}

TMVAInterface initialize_mva_jpa_missingWJet(bool Hbb_isBoosted)
{
  std::string mvaFileName_even = ( !Hbb_isBoosted ) ? "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingWJet_resolved_even.xml" : "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingWJet_boosted_even.xml";
  std::string mvaFileName_odd  = ( !Hbb_isBoosted ) ? "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingWJet_resolved_odd.xml" : "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingWJet_boosted_odd.xml";
  std::vector<std::string> mvaInputVariables;
  if ( !Hbb_isBoosted ) {
    mvaInputVariables = {
    "bjet1_btagCSV", "bjet2_ptReg", "bjet2_btagCSV", "bjet2_qgDiscr", "dEta_bjet2_lep", "wjet1_ptReg", "wjet1_btagCSV", "wjet1_qgDiscr", "dEta_wjet1_lep", "dR_bjet1bjet2", "nJet", "nBJetLoose", "nBJetMedium"
  };
  }
  else {
    mvaInputVariables = {
      "dEta_bjet1_lep", "wjet1_ptReg", "wjet1_btagCSV", "wjet1_qgDiscr", "dR_wjet1_lep", "Hbb_pt", "nBJetMedium"
    };
  }
  TMVAInterface mva(mvaFileName_odd, mvaFileName_even, mvaInputVariables);
  mva.enableBDTTransform();
  return mva;
}

TMVAInterface initialize_mva_jpa_missingBJetmissingWJet()
{
  std::string mvaFileName_even = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingBJet_missingWJet_even.xml";
  std::string mvaFileName_odd  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingBJet_missingWJet_odd.xml";
  std::vector<std::string> mvaInputVariables = {
    "bjet1_ptReg", "bjet1_btagCSV", "bjet1_qgDiscr", "dEta_bjet1_lep", "wjet1_ptReg", "wjet1_btagCSV", "wjet1_qgDiscr", "dEta_wjet1_lep", "nJet", "nBJetLoose", "nBJetMedium", "nLep"
  };
  TMVAInterface mva(mvaFileName_odd, mvaFileName_even, mvaInputVariables);
  mva.enableBDTTransform();
  return mva;
}

TMVAInterface initialize_mva_jpa_missingAllWJet()
{
  std::string mvaFileName_even = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingAllWJet_even.xml";
  std::string mvaFileName_odd  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingAllWJet_odd.xml";
  std::vector<std::string> mvaInputVariables = {
    "bjet1_ptReg", "bjet1_btagCSV", "bjet2_ptReg", "bjet2_btagCSV", "bjet2_qgDiscr", "dEta_bjet2_lep", "Hbb_massReg", "nJet", "nBJetMedium"
  };
  TMVAInterface mva(mvaFileName_odd, mvaFileName_even, mvaInputVariables);
  mva.enableBDTTransform();
  return mva;
}

TMVAInterface initialize_mva_jpa_missingBJetmissingAllWJet()
{
  std::string mvaFileName_even = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingBJet_missingAllWJet_even.xml";
  std::string mvaFileName_odd  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_missingBJet_missingAllWJet_odd.xml";
  std::vector<std::string> mvaInputVariables = {
    "lepton_pt", "bjet1_ptReg", "bjet1_btagCSV", "bjet1_qgDiscr", "dEta_bjet1_lep", "nJet", "nBJetLoose", "nBJetMedium"
  };
  TMVAInterface mva(mvaFileName_odd, mvaFileName_even, mvaInputVariables);
  mva.enableBDTTransform();
  return mva;
}

const RecoJet* getSelJetAK4(const RecoJetBase* jet_) {
  const RecoJet* jet = nullptr;
  if ( dynamic_cast<const RecoJet*>(jet_) )
  {
    jet = dynamic_cast<const RecoJet*>(jet_);
  }
  return jet;
}
void rankJetQuads(std::vector<JetQuadBase>& jetQuads, const RecoLepton& selLepton, 
		  int nBJetMedium, const Particle::LorentzVector& metP4,
		  const TMVAInterface& mva, const EventInfo& eventInfo, const RecoJetAK8* selJetAK8_Hbb) {

  for ( std::vector<JetQuadBase>::iterator jetQuad = jetQuads.begin(); jetQuad != jetQuads.end(); ++jetQuad )
    {
      assert(jetQuad->BJet1_ && jetQuad->BJet2_ && jetQuad->WJet1_ && jetQuad->WJet2_ );

      double selBJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets   
      double selBJet2_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selBJet2_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets
      double selWJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selWJet1_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets
      double selWJet2_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selWJet2_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets     
      
      const RecoJet* selBJet1 = getSelJetAK4(jetQuad->BJet1_);
      Particle::LorentzVector selBJet1_P4 = jetQuad->BJet1_->p4();
      Particle::LorentzVector selBJet1P4_reg;
      if ( selBJet1 )
	{
	  selBJet1_BtagCSV = selBJet1->BtagCSV();
	  selBJet1P4_reg= selBJet1_P4*selBJet1->bRegCorr();
	}

      const RecoJet* selBJet2 = getSelJetAK4(jetQuad->BJet2_);
      Particle::LorentzVector selBJet2_P4 = jetQuad->BJet2_->p4();
      Particle::LorentzVector selBJet2P4_reg;
      if ( selBJet2 )
        {
          selBJet2_BtagCSV = selBJet2->BtagCSV();
	  selBJet2_QGDiscr = selBJet2->QGDiscr();
	  selBJet2P4_reg= selBJet2_P4*selBJet2->bRegCorr();
        }

      const RecoJet* selWJet1 = getSelJetAK4(jetQuad->WJet1_);
      Particle::LorentzVector selWJet1_P4 = jetQuad->WJet1_->p4();
      if ( selWJet1 )
        {
          selWJet1_BtagCSV = selWJet1->BtagCSV();
	  //selWJet1_QGDiscr = selWJet1->QGDiscr();
	}

      const RecoJet* selWJet2 = getSelJetAK4(jetQuad->WJet2_);
      Particle::LorentzVector selWJet2_P4 = jetQuad->WJet2_->p4();
      Particle::LorentzVector selWJet2P4_reg;
      if ( selWJet2 )
        {
          selWJet2_BtagCSV = selWJet2->BtagCSV();
	  selWJet2P4_reg= selWJet2_P4*selWJet2->bRegCorr();
	  selWJet2_BtagCSV = selWJet2->BtagCSV();
	  selWJet2_QGDiscr = selWJet2->QGDiscr();
        }
      Particle::LorentzVector HbbP4_reg = selBJet1P4_reg + selBJet2P4_reg;
      Particle::LorentzVector HadWP4 = selWJet1_P4 + selWJet2_P4;
      double dR_HadW_lep = deltaR(HadWP4, selLepton.p4());
      double  dR_HadW_bjet1 = deltaR(HadWP4, selBJet1_P4);
      double  dR_HadW_bjet2 = deltaR(HadWP4, selBJet2_P4);
      double max_dR_HadW_bjet = TMath::Max(dR_HadW_bjet1, dR_HadW_bjet2);
      double dR_wjet1wjet2 = deltaR(selWJet1_P4, selWJet2_P4);
      Particle::LorentzVector top1P4 = selBJet1P4_reg + HadWP4;
      Particle::LorentzVector top2P4 = selBJet2P4_reg + HadWP4;
      double mTop1(-1);
      if ( TMath::Abs(top1P4.mass() - topMass) < TMath::Abs(top2P4.mass() - topMass) )
	{
	  mTop1 = top1P4.mass();
	}
      else
	{
	  mTop1 = top2P4.mass();
	}

      std::map<std::string, double> mvaInputVariables; 
      if ( !selJetAK8_Hbb ) {
	mvaInputVariables = {
	  {"bjet1_btagCSV", selBJet1_BtagCSV},
	  {"bjet2_ptReg", selBJet2P4_reg.pt()},
	  {"bjet2_btagCSV", selBJet2_BtagCSV},
	  {"bjet2_qgDiscr", selBJet2_QGDiscr},
	  {"maxwjetbtagCSV", TMath::Max(selWJet1_BtagCSV, selWJet2_BtagCSV)},
	  {"wjet2_ptReg", selWJet2P4_reg.pt()},
	  {"wjet2_qgDiscr", selWJet2_QGDiscr},
	  {"HadW_mass", HadWP4.mass()},
	  {"dR_HadW_lep", dR_HadW_lep},
	  {"max_dR_HadW_bjet", max_dR_HadW_bjet},
	  {"dR_wjet1wjet2", dR_wjet1wjet2},
	  {"mTop1", mTop1},
	  {"nBJetMedium", nBJetMedium},
	  {"Hbb_massReg", HbbP4_reg.mass()},
	};
      }
      else {
	Particle::LorentzVector HbbP4 = selBJet1_P4 + selBJet2_P4;
	double HadW_cosTheta = compCosTheta(selWJet1_P4, selWJet2_P4);
	Particle::LorentzVector neutrinoP4_B2G_18_008 = comp_metP4_B2G_18_008(selLepton.p4() + selWJet1_P4 + selWJet2_P4, metP4.px(), metP4.py(), higgsBosonMass);
	Particle::LorentzVector LepWP4= selLepton.p4() + neutrinoP4_B2G_18_008;
	Particle::LorentzVector HwwP4 = LepWP4 + HadWP4;
	double min_dR_HadW_bjet = TMath::Min(dR_HadW_bjet1, dR_HadW_bjet2);
	mvaInputVariables = {
	  {"wjet1_btagCSV",    selWJet1_BtagCSV},
	  {"wjet1_qgDiscr",    selWJet1_QGDiscr},
	  {"wjet2_btagCSV",    selWJet2_BtagCSV},
          {"wjet2_qgDiscr",    selWJet2_QGDiscr},
	  {"Hbb_pt",           HbbP4.pt()},
          {"HadW_mass",        HadWP4.mass()},
	  {"HadW_cosTheta",    HadW_cosTheta},
          {"dR_HadW_lep",      dR_HadW_lep},
	  {"min_dR_HadW_bjet", min_dR_HadW_bjet},
	  {"dR_wjet1wjet2",    dR_wjet1wjet2},
          {"Hww_mass",         HwwP4.mass()},
        };
      }
      double bdtScore = mva(mvaInputVariables, eventInfo.event);
      //if (selJetAK8_Hbb) {std::cout << "**************"<< bdtScore << std::endl;
      //assert(0);}
      jetQuad->bdtScore_ = bdtScore;
    }
  std::sort(jetQuads.begin(), jetQuads.end(), isHigherRankedByBDT);
}

void rankJetTripletsMissingWJet(std::vector<JetQuadBase>& jetTriplets, const RecoLepton& selLepton, int nJet, int nBJetLoose, int nBJetMedium, 
				const TMVAInterface& mva, const EventInfo& eventInfo, const RecoJetAK8* selJetAK8_Hbb) {
  
  for ( std::vector<JetQuadBase>::iterator jetTriplet = jetTriplets.begin(); jetTriplet != jetTriplets.end(); ++jetTriplet )
    {
      assert(jetTriplet->BJet1_ && jetTriplet->BJet2_ && jetTriplet->WJet1_ && !jetTriplet->WJet2_);
      double selBJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selBJet2_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selBJet2_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets
      double selWJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selWJet1_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets

      const RecoJet* selBJet1 = getSelJetAK4(jetTriplet->BJet1_);
      Particle::LorentzVector selBJet1_P4 = jetTriplet->BJet1_->p4();
      Particle::LorentzVector selBJet1P4_reg;
      if ( selBJet1 )
        {
          selBJet1_BtagCSV = selBJet1->BtagCSV();
          selBJet1P4_reg= selBJet1_P4*selBJet1->bRegCorr();
        }

      const RecoJet* selBJet2 = getSelJetAK4(jetTriplet->BJet2_);
      Particle::LorentzVector selBJet2_P4 = jetTriplet->BJet2_->p4();
      Particle::LorentzVector selBJet2P4_reg;
      if ( selBJet2 )
        {
          selBJet2_BtagCSV = selBJet2->BtagCSV();
          selBJet2P4_reg= selBJet2_P4*selBJet2->bRegCorr();
        }

      const RecoJet* selWJet1 = getSelJetAK4(jetTriplet->WJet1_);
      Particle::LorentzVector selWJet1_P4 = jetTriplet->WJet1_->p4();
      Particle::LorentzVector selWJet1P4_reg;
      if ( selWJet1 )
        {
          selWJet1_BtagCSV = selWJet1->BtagCSV();
          selWJet1_QGDiscr = selWJet1->QGDiscr();
          selWJet1P4_reg= selWJet1_P4*selWJet1->bRegCorr();
        }

      double dR_bjet1bjet2 = deltaR(selBJet1_P4, selBJet2_P4);
      double dEta_bjet2_lep = TMath::Abs(selBJet2_P4.eta() - selLepton.eta());
      double dEta_wjet1_lep = TMath::Abs(selWJet1_P4.eta() - selLepton.eta());

      std::map<std::string, double> mvaInputVariables;
      if ( !selJetAK8_Hbb ) {
	mvaInputVariables = {
	  {"bjet1_btagCSV", selBJet1_BtagCSV},
	  {"bjet2_ptReg", selBJet2P4_reg.pt()},
	  {"bjet2_btagCSV", selBJet2_BtagCSV},
	  {"bjet2_qgDiscr", selBJet2_QGDiscr},
	  {"dEta_bjet2_lep", dEta_bjet2_lep},
	  {"wjet1_ptReg", selWJet1P4_reg.pt()},
	  {"wjet1_btagCSV", selWJet1_BtagCSV},
	  {"wjet1_qgDiscr", selWJet1_QGDiscr},
	  {"dEta_wjet1_lep", dEta_wjet1_lep},
	  {"dR_bjet1bjet2", dR_bjet1bjet2},
	  {"nJet", nJet},
	  {"nBJetLoose", nBJetLoose},
	  {"nBJetMedium", nBJetMedium},
	};
      }
      else {
	Particle::LorentzVector HbbP4 = selBJet1_P4 + selBJet2_P4;
	double dEta_bjet1_lep = TMath::Abs(selBJet1_P4.eta() - selLepton.eta());
	double dR_wjet1_lep = deltaR(selWJet1_P4, selLepton.p4());
	mvaInputVariables = {
	  {"dEta_bjet1_lep",      dEta_bjet1_lep},
	  {"wjet1_ptReg",         selWJet1P4_reg.pt()},
	  {"wjet1_btagCSV",       selWJet1_BtagCSV},
	  {"wjet1_qgDiscr",       selWJet1_QGDiscr},
	  {"dR_wjet1_lep",        dR_wjet1_lep},
	  {"Hbb_pt",              HbbP4.pt()},
	  {"nBJetMedium",         nBJetMedium},
	};
      }
      double bdtScore = mva(mvaInputVariables, eventInfo.event);
      //if( selJetAK8_Hbb){std::cout << "*************8wjet= " << bdtScore << std::endl;
      //assert(0);}
      jetTriplet->bdtScore_ = bdtScore;
    }
  std::sort(jetTriplets.begin(), jetTriplets.end(), isHigherRankedByBDT);
}

void rankJetTripletsMissingBJet(std::vector<JetQuadBase>& jetTriplets, const RecoLepton& selLepton, int nJet, int nBJetMedium, const TMVAInterface& mva, const EventInfo& eventInfo) {
  
  for ( std::vector<JetQuadBase>::iterator jetTriplet = jetTriplets.begin(); jetTriplet != jetTriplets.end(); ++jetTriplet )
    {
      assert(jetTriplet->BJet1_ && !jetTriplet->BJet2_ && jetTriplet->WJet1_ && jetTriplet->WJet2_ );

      double selBJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets 
      double selWJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selWJet2_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selWJet2_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets

      const RecoJet* selBJet1 = getSelJetAK4(jetTriplet->BJet1_);
      Particle::LorentzVector selBJet1_P4 = jetTriplet->BJet1_->p4();
      Particle::LorentzVector selBJet1P4_reg;
      if ( selBJet1 )
        {
          selBJet1_BtagCSV = selBJet1->BtagCSV();
          selBJet1P4_reg= selBJet1_P4*selBJet1->bRegCorr();
        }

      const RecoJet* selWJet1 = getSelJetAK4(jetTriplet->WJet1_);
      Particle::LorentzVector selWJet1_P4 = jetTriplet->WJet1_->p4();
      Particle::LorentzVector selWJet1P4_reg;
      if ( selWJet1 )
        {
          selWJet1_BtagCSV = selWJet1->BtagCSV();
          selWJet1P4_reg= selWJet1_P4*selWJet1->bRegCorr();
        }

      const RecoJet* selWJet2 = getSelJetAK4(jetTriplet->WJet2_);
      Particle::LorentzVector selWJet2_P4 = jetTriplet->WJet2_->p4();
      Particle::LorentzVector selWJet2P4_reg;
      if ( selWJet2 )
        {
          selWJet2_BtagCSV = selWJet2->BtagCSV();
          selWJet2_QGDiscr = selWJet2->QGDiscr();
          selWJet2P4_reg= selWJet2_P4*selWJet2->bRegCorr();
        }
      Particle::LorentzVector HadWP4 = selWJet1_P4 + selWJet2_P4;
      double dR_HadW_lep = deltaR(HadWP4, selLepton.p4());
      double dR_wjet1wjet2 = deltaR(selWJet1_P4, selWJet2_P4);
      double mTop1 = (selBJet1P4_reg + HadWP4).mass();

      std::map<std::string, double> mvaInputVariables = {
        {"bjet1_ptReg", selBJet1P4_reg.pt()},
        {"bjet1_btagCSV", selBJet1_BtagCSV},
        {"wjet1_ptReg", selWJet1P4_reg.pt()},
        {"wjet1_btagCSV", selWJet1_BtagCSV},
	{"wjet2_btagCSV", selWJet2_BtagCSV},
        {"wjet2_qgDiscr", selWJet2_QGDiscr},
        {"HadW_mass", HadWP4.mass()},
        {"dR_HadW_lep", dR_HadW_lep},
        {"dR_wjet1wjet2", dR_wjet1wjet2},
        {"mTop1", mTop1},
        {"nJet", nJet},
        {"nBJetMedium", nBJetMedium},
      };
      double bdtScore = mva(mvaInputVariables, eventInfo.event);
      jetTriplet->bdtScore_ = bdtScore;
    }
  std::sort(jetTriplets.begin(), jetTriplets.end(), isHigherRankedByBDT);
}

void rankJetDoubletsMissingBJetMissingWJet(std::vector<JetQuadBase>& jetDoublets, const RecoLepton& selLepton, int nJet, int nBJetLoose, int nBJetMedium, int nLep, 
					  const TMVAInterface& mva, const EventInfo& eventInfo) {

  for ( std::vector<JetQuadBase>::iterator jetDoublet = jetDoublets.begin(); jetDoublet != jetDoublets.end(); ++jetDoublet )
    {
      assert(jetDoublet->BJet1_ && !jetDoublet->BJet2_ && jetDoublet->WJet1_ && !jetDoublet->WJet2_ );
      double selBJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selBJet1_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets
      double selWJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selWJet1_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets
      
      const RecoJet* selBJet1 = getSelJetAK4(jetDoublet->BJet1_);
      Particle::LorentzVector selBJet1_P4 = jetDoublet->BJet1_->p4();
      Particle::LorentzVector selBJet1P4_reg;
      if ( selBJet1 )
        {
          selBJet1_BtagCSV = selBJet1->BtagCSV();
	  selBJet1_QGDiscr = selBJet1->QGDiscr();
          selBJet1P4_reg= selBJet1_P4*selBJet1->bRegCorr();
        }

      const RecoJet* selWJet1 = getSelJetAK4(jetDoublet->WJet1_);
      Particle::LorentzVector selWJet1_P4 = jetDoublet->WJet1_->p4();
      Particle::LorentzVector selWJet1P4_reg;
      if ( selWJet1 )
        {
          selWJet1_BtagCSV = selWJet1->BtagCSV();
          selWJet1P4_reg= selWJet1_P4*selWJet1->bRegCorr();
	  selWJet1_QGDiscr = selWJet1->QGDiscr();
        }
      double dEta_bjet1_lep = TMath::Abs(selBJet1_P4.eta() - selLepton.eta());
      double dEta_wjet1_lep = TMath::Abs(selWJet1_P4.eta() - selLepton.eta());

      std::map<std::string, double> mvaInputVariables = {
        {"bjet1_ptReg", selBJet1P4_reg.pt()},
        {"bjet1_btagCSV", selBJet1_BtagCSV},
	{"bjet1_qgDiscr", selBJet1_QGDiscr},
	{"dEta_bjet1_lep", dEta_bjet1_lep},
        {"wjet1_ptReg", selWJet1P4_reg.pt()},
        {"wjet1_btagCSV", selWJet1_BtagCSV},
	{"wjet1_qgDiscr", selWJet1_QGDiscr},
	{"dEta_wjet1_lep", dEta_wjet1_lep},
        {"nJet", nJet},
	{"nBJetLoose", nBJetLoose},
        {"nBJetMedium", nBJetMedium},
	{"nLep", nLep},
      };
      double bdtScore = mva(mvaInputVariables, eventInfo.event);
      jetDoublet->bdtScore_ = bdtScore;
    }
  std::sort(jetDoublets.begin(), jetDoublets.end(), isHigherRankedByBDT);
}

void rankJetDoubletsMissingAllWJet(std::vector<JetQuadBase>& jetDoublets, const RecoLepton& selLepton, int nJet, int nBJetMedium,
					   const TMVAInterface& mva, const EventInfo& eventInfo) {

  for ( std::vector<JetQuadBase>::iterator jetDoublet = jetDoublets.begin(); jetDoublet != jetDoublets.end(); ++jetDoublet )
    {
      assert(jetDoublet->BJet1_ && jetDoublet->BJet1_ && !jetDoublet->WJet1_ && !jetDoublet->WJet2_  );
      double selBJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selBJet2_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selBJet2_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets

      const RecoJet* selBJet1 = getSelJetAK4(jetDoublet->BJet1_);
      Particle::LorentzVector selBJet1_P4 = jetDoublet->BJet1_->p4();
      Particle::LorentzVector selBJet1P4_reg;
      if ( selBJet1 )
        {
	  selBJet1_BtagCSV = selBJet1->BtagCSV();
          selBJet1P4_reg= selBJet1_P4*selBJet1->bRegCorr();
        }
      const RecoJet* selBJet2 = getSelJetAK4(jetDoublet->BJet2_);
      Particle::LorentzVector selBJet2_P4 = jetDoublet->BJet2_->p4();
      Particle::LorentzVector selBJet2P4_reg;
      if ( selBJet2 )
        {
          selBJet2_BtagCSV = selBJet2->BtagCSV();
          selBJet2P4_reg= selBJet2_P4*selBJet2->bRegCorr();
	  selBJet2_QGDiscr = selBJet2->QGDiscr();
        }
      double dEta_bjet2_lep = TMath::Abs(selBJet2_P4.eta() - selLepton.eta());
      Particle::LorentzVector HbbP4_reg = selBJet1P4_reg + selBJet2P4_reg;

      std::map<std::string, double> mvaInputVariables = {
        {"bjet1_ptReg", selBJet1P4_reg.pt()},
        {"bjet1_btagCSV", selBJet1_BtagCSV},
	{"bjet2_ptReg", selBJet2P4_reg.pt()},
	{"bjet2_btagCSV", selBJet2_BtagCSV},
	{"bjet2_qgDiscr", selBJet2_QGDiscr},
        {"dEta_bjet2_lep", dEta_bjet2_lep},
	{"Hbb_massReg", HbbP4_reg.mass()},
        {"nJet", nJet},
        {"nBJetMedium", nBJetMedium},
      };
      double bdtScore = mva(mvaInputVariables, eventInfo.event);
      jetDoublet->bdtScore_ = bdtScore;
    }
  std::sort(jetDoublets.begin(), jetDoublets.end(), isHigherRankedByBDT);
}

void rankJetSingletsMissingBJetMissingAllWJet(std::vector<JetQuadBase>& jetSinglets, const RecoLepton& selLepton, 
					      int nJet, int nBJetLoose, int nBJetMedium,
					      const TMVAInterface& mva, const EventInfo& eventInfo) {

  for ( std::vector<JetQuadBase>::iterator jetSinglet = jetSinglets.begin(); jetSinglet != jetSinglets.end(); ++jetSinglet )
    {
      assert(jetSinglet->BJet1_ && !jetSinglet->BJet2_ && !jetSinglet->WJet1_ && !jetSinglet->WJet2_  );
      double selBJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selBJet1_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets

      const RecoJet* selBJet1 = getSelJetAK4(jetSinglet->BJet1_);
      Particle::LorentzVector selBJet1_P4 = jetSinglet->BJet1_->p4();
      Particle::LorentzVector selBJet1P4_reg;
      if ( selBJet1 )
        {
          selBJet1_BtagCSV = selBJet1->BtagCSV();
	  selBJet1_QGDiscr = selBJet1->QGDiscr();
          selBJet1P4_reg= selBJet1_P4*selBJet1->bRegCorr();
        }

      double dEta_bjet1_lep = TMath::Abs(selBJet1_P4.eta() - selLepton.eta());

      std::map<std::string, double> mvaInputVariables = {
	{"lepton_pt", selLepton.pt()},
        {"bjet1_ptReg", selBJet1P4_reg.pt()},
	{"bjet1_btagCSV", selBJet1_BtagCSV},
	{"bjet1_qgDiscr", selBJet1_QGDiscr},
        {"dEta_bjet1_lep", dEta_bjet1_lep},
        {"nJet", nJet},
	{"nBJetLoose", nBJetLoose},
        {"nBJetMedium", nBJetMedium},
      };
      double bdtScore = mva(mvaInputVariables, eventInfo.event);
      jetSinglet->bdtScore_ = bdtScore;
    }
  std::sort(jetSinglets.begin(), jetSinglets.end(), isHigherRankedByBDT);
}

JetQuadBase
selectJet_Quad(const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons, const RecoLepton selLepton,
	       int nBJetMedium, const Particle::LorentzVector& metP4, 
	       const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
	       const TMVAInterface& mva, const EventInfo& eventInfo, const RecoJetAK8* selJetAK8_Hbb)
{

  JetQuadBase JetQuadBase_;
  std::vector<JetQuadBase> jetQuadsAK4 = makeJetQuads(cleanedJetsAK4_wrtLeptons, genBJets_ptrs, genWJets_ptrs, selJetAK8_Hbb);
  if( ! jetQuadsAK4.size() ) return JetQuadBase_;
  rankJetQuads(jetQuadsAK4, selLepton, nBJetMedium, metP4, mva, eventInfo, selJetAK8_Hbb);
  return jetQuadsAK4[0];
  
}

JetQuadBase 
selectJet_TripletMissingBJet(const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons, const RecoLepton selLepton,
			     int nJet, int nBJetMedium, const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
			     const TMVAInterface& mva, const EventInfo& eventInfo)
{

  JetQuadBase JetQuadBase_;
  std::vector<JetQuadBase> jetTripletsAK4 = makeJetTripletsMissingBJet(cleanedJetsAK4_wrtLeptons, genBJets_ptrs, genWJets_ptrs);
  if( ! jetTripletsAK4.size() ) return JetQuadBase_;
  rankJetTripletsMissingBJet(jetTripletsAK4, selLepton, nJet, nBJetMedium, mva, eventInfo);
  return jetTripletsAK4[0];
}

JetQuadBase
selectJet_TripletMissingWJet(const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons, const RecoLepton selLepton, 
			     int nJet, int nBJetLoose, int nBJetMedium, const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
			     const TMVAInterface& mva, const EventInfo& eventInfo, const RecoJetAK8* selJetAK8_Hbb)
{
  
  JetQuadBase JetQuadBase_;
  std::vector<JetQuadBase> jetTripletsAK4 = makeJetTripletsMissingWJet(cleanedJetsAK4_wrtLeptons, genBJets_ptrs, genWJets_ptrs, selJetAK8_Hbb);
  if( ! jetTripletsAK4.size() ) return JetQuadBase_;
  rankJetTripletsMissingWJet(jetTripletsAK4, selLepton, nJet, nBJetLoose, nBJetMedium, mva, eventInfo, selJetAK8_Hbb);
  return jetTripletsAK4[0];
}

JetQuadBase
selectJet_DoubletMissingBJetMissingWJet(const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons, const RecoLepton selLepton,
					int nJet, int nBJetLoose, int nBJetMedium, int nLep, 
					const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
					const TMVAInterface& mva, const EventInfo& eventInfo)
{ 
  JetQuadBase JetQuadBase_;
  std::vector<JetQuadBase> jetDoubletsAK4 = makeJetDoubletsMissingBJetMissingWJet(cleanedJetsAK4_wrtLeptons, genBJets_ptrs, genWJets_ptrs);
  if( ! jetDoubletsAK4.size() ) return JetQuadBase_;
  rankJetDoubletsMissingBJetMissingWJet(jetDoubletsAK4, selLepton, nJet, nBJetLoose, nBJetMedium, nLep, mva, eventInfo);
  return jetDoubletsAK4[0];
}

JetQuadBase
selectJet_DoubletMissingAllWJet(const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons, const RecoLepton selLepton,
				int nJet, int nBJetMedium, 
				const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
				const TMVAInterface& mva, const EventInfo& eventInfo)
{
  JetQuadBase JetQuadBase_;
  std::vector<JetQuadBase> jetDoubletsAK4 = makeJetDoubletsMissingAllWJet(cleanedJetsAK4_wrtLeptons, genBJets_ptrs, genWJets_ptrs);
  if( ! jetDoubletsAK4.size() ) return JetQuadBase_;
  rankJetDoubletsMissingAllWJet(jetDoubletsAK4, selLepton, nJet, nBJetMedium, mva, eventInfo);
  return jetDoubletsAK4[0];
}


JetQuadBase 
selectJet_SingletMissingBJetMissingAllWJet(const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons, const RecoLepton selLepton,
												    int nJet, int nBJetLoose, int nBJetMedium,
												    const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
												    const TMVAInterface& mva, const EventInfo& eventInfo)
{
  JetQuadBase JetQuadBase_;
  std::vector<JetQuadBase> jetSingletsAK4 = makeJetSingletsMissingBJetMissingAllWJet(cleanedJetsAK4_wrtLeptons, genBJets_ptrs);
  if( ! jetSingletsAK4.size() ) return JetQuadBase_;
  rankJetSingletsMissingBJetMissingAllWJet(jetSingletsAK4, selLepton, nJet, nBJetLoose, nBJetMedium, mva, eventInfo);
  return jetSingletsAK4[0];
}
