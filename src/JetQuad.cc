#include "hhAnalysis/bbww/interface/JetQuad.h"
#include <TROOT.h>
#include "hhAnalysis/bbww/interface/genMatchingAuxFunctions.h" // isGenMatched

#include <algorithm> // std::sort
const double topMass = 172.9; // CV: taken from http://pdg.lbl.gov/2019/listings/rpp2019-list-t-quark.pdf ("OUR AVERAGE")

bool
isHigherRankedByBDT(const JetQuad& quad1, const JetQuad& quad2)
{
  double bdtScore1 = quad1.bdtScore_;
  double bdtScore2 = quad2.bdtScore_;
  return ( bdtScore1 > bdtScore2 );
}

std::vector<JetQuad> 
makeJetQuads(const std::vector<const RecoJet*>& selJetsAK4, const std::vector<const GenJet*>& genBJets, const std::vector<const GenJet*>& genWJets)
{
  std::vector<JetQuad> jetQuads;
  for ( std::vector<const RecoJet*>::const_iterator selBJet1 = selJetsAK4.begin(); selBJet1 != selJetsAK4.end(); ++selBJet1 ) 
  {
    for ( std::vector<const RecoJet*>::const_iterator selBJet2 = selBJet1 + 1; selBJet2 != selJetsAK4.end(); ++selBJet2 )
      {
	for ( std::vector<const RecoJet*>::const_iterator selWJet1 = selJetsAK4.begin(); selWJet1 != selJetsAK4.end(); ++selWJet1 )
	{
	  for ( std::vector<const RecoJet*>::const_iterator selWJet2 = selWJet1 + 1; selWJet2 != selJetsAK4.end(); ++selWJet2 )
	    {
	      //	      if ( deltaR((*selWJet1)->p4(), (*selBJet1)->p4()) < 0.8 || deltaR((*selWJet1)->p4(), (*selBJet2)->p4()) < 0.8 ) continue;
              //if ( deltaR((*selWJet2)->p4(), (*selBJet1)->p4()) < 0.8 || deltaR((*selWJet2)->p4(), (*selBJet2)->p4()) < 0.8 ) continue;
	      if ( ((*selWJet1)->eta() == (*selBJet1)->eta() && (*selWJet1)->phi() == (*selBJet1)->phi()) || ((*selWJet1)->eta() == (*selBJet2)->eta() && (*selWJet1)->phi() == (*selBJet2)->phi()) ) continue;
	      if ( ((*selWJet2)->eta() == (*selBJet1)->eta() && (*selWJet2)->phi() == (*selBJet1)->phi()) || ((*selWJet2)->eta() == (*selBJet2)->eta() && (*selWJet2)->phi() == (*selBJet2)->phi()) ) continue;
	      bool selBJet1_isGenMatched = ( genBJets.size() ) ? isGenMatchedT<GenJet>((*selBJet1)->eta(), (*selBJet1)->phi(), genBJets) : false;
	      bool selBJet2_isGenMatched = ( genBJets.size() ) ? isGenMatchedT<GenJet>((*selBJet2)->eta(), (*selBJet2)->phi(), genBJets) : false;
	      bool selWJet1_isGenMatched = ( genWJets.size() ) ? isGenMatchedT<GenJet>((*selWJet1)->eta(), (*selWJet1)->phi(), genWJets) : false;
	      bool selWJet2_isGenMatched = ( genWJets.size() ) ? isGenMatchedT<GenJet>((*selWJet2)->eta(), (*selWJet2)->phi(), genWJets) : false;
	      JetQuad jetQuad(*selBJet1, selBJet1_isGenMatched, *selBJet2, selBJet2_isGenMatched, *selWJet1, selWJet1_isGenMatched, *selWJet2, selWJet2_isGenMatched);
	      //if ( selBJet1_isGenMatched && selBJet2_isGenMatched && (selWJet1_isGenMatched && selWJet2_isGenMatched) ) std::cout  << "matched" << std::endl;
	      jetQuads.push_back(jetQuad); 
	    }
	}
    }
  }
  return jetQuads;
}

TMVAInterface initialize_mva_jpa()
{
  std::string mvaFileName_jpa_even = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_even.pkl.xml";
  std::string mvaFileName_jpa_odd  = "hhAnalysis/bbww/data/BDT_hh_bb1l/bb1l_jpa_odd.pkl.xml";
  std::vector<std::string> mvaInputVariables_jpa = {
    "bjet1_btagCSV", "bjet2_ptReg", "bjet2_btagCSV", "bjet2_qgDiscr", "maxwjetbtagCSV", "wjet2_ptReg", "wjet2_qgDiscr", "HadW_mass", "dR_HadW_lep", "max_dR_HadW_bjet", "dR_wjet1wjet2", "mTop1", "nBJetMedium"
  };
  TMVAInterface mva_jpa(mvaFileName_jpa_odd, mvaFileName_jpa_even, mvaInputVariables_jpa);
  mva_jpa.enableBDTTransform();
  return mva_jpa;
}

const RecoJet* getSelJetAK4(const RecoJetBase* jet_) {
  const RecoJet* jet = nullptr;
  if ( dynamic_cast<const RecoJet*>(jet_) )
  {
    jet = dynamic_cast<const RecoJet*>(jet_);
  }
  return jet;
}
void rankJetQuads(std::vector<JetQuad>& jetQuads, const RecoLepton& selLepton, int nBJetMedium, const TMVAInterface& mva_jpa, const EventInfo& eventInfo) {

  for ( std::vector<JetQuad>::iterator jetQuad = jetQuads.begin(); jetQuad != jetQuads.end(); ++jetQuad )
    {
      assert(jetQuad->BJet1_ && jetQuad->BJet2_ && jetQuad->WJet1_ && jetQuad->WJet2_ );

      double selBJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets   
      double selBJet2_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
      double selBJet2_QGDiscr = 1.; // CV: treat jets for which quark/gluon discriminator is not available as quark jets
      double selWJet1_BtagCSV = 0.; // CV: treat jets for which b-tagging discriminator is not available as light-quark jets
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
	}

      const RecoJet* selWJet2 = getSelJetAK4(jetQuad->WJet2_);
      Particle::LorentzVector selWJet2_P4 = jetQuad->WJet2_->p4();
      Particle::LorentzVector selWJet2P4_reg;
      if ( selWJet2 )
        {
          selWJet2_BtagCSV = selWJet2->BtagCSV();
	  selWJet2P4_reg= selWJet2_P4*selWJet2->bRegCorr();
	  selWJet2_BtagCSV = selWJet2->BtagCSV();
        }
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

      std::map<std::string, double> mvaInputVariables_jpa = {
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
      };
      double bdtScore = mva_jpa(mvaInputVariables_jpa, eventInfo.event);
      jetQuad->bdtScore_ = bdtScore;
    }
  std::sort(jetQuads.begin(), jetQuads.end(), isHigherRankedByBDT);
}

std::vector<const RecoJet*> selectJet_Quad(const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons, const RecoLepton selLepton,
					   int nBJetMedium, const std::vector<const GenJet*>& genBJets_ptrs, const std::vector<const GenJet*>& genWJets_ptrs,
					   const TMVAInterface& mva_jpa, const EventInfo& eventInfo)
{

  std::vector<const RecoJet*> jetquad_collection;
  std::vector<JetQuad> jetQuadsAK4 = makeJetQuads(cleanedJetsAK4_wrtLeptons, genBJets_ptrs, genWJets_ptrs);
  if( ! jetQuadsAK4.size() ) return jetquad_collection; 
  rankJetQuads(jetQuadsAK4, selLepton, nBJetMedium, mva_jpa, eventInfo);
  //  if( !(jetQuadsAK4[0].BJet1_isGenMatched_ && jetQuadsAK4[0].BJet2_isGenMatched_  && jetQuadsAK4[0].WJet1_isGenMatched_ && jetQuadsAK4[0].WJet2_isGenMatched_) ) return jetquad_collection;
  const RecoJet* bjet1 =  jetQuadsAK4[0].BJet1_;
  const RecoJet* bjet2 =  jetQuadsAK4[0].BJet2_;
  const RecoJet* wjet1 =  jetQuadsAK4[0].WJet1_;
  const RecoJet* wjet2 =  jetQuadsAK4[0].WJet2_;
  
  jetquad_collection.push_back(bjet1);
  jetquad_collection.push_back(bjet2);
  jetquad_collection.push_back(wjet1);
  jetquad_collection.push_back(wjet2);
  return jetquad_collection;
  
}
