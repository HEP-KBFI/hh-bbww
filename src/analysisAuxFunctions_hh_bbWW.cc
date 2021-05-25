#include "hhAnalysis/bbww/interface/analysisAuxFunctions_hh_bbWW.h"

#include <boost/algorithm/string/replace.hpp> // boost::replace_all_copy()

namespace
{
  std::vector<std::string> BMpoints{"SM", "BM1", "BM2", "BM3", "BM4", "BM5", "BM6", "BM7", "BM8", "BM9", "BM10", "BM11", "BM12", "all"};
  std::vector<std::string> split_spin0points {"low_spin0", "high_spin0"};
  std::vector<std::string> split_spin2points {"low_spin2", "high_spin2"};
  std::vector<std::string> spin0points {"spin0"};
  std::vector<std::string> spin2points {"spin2"};
}

std::map<std::string, TMVAInterface *>
makeTMVAInterfaceMap(const edm::ParameterSet & cfg, const std::string & era, bool is_nonresonant)
{
  std::map<std::string, TMVAInterface *> retVals;
  for ( const std::string & BM: BMpoints) {
    std::string xmlFileName_odd = cfg.getParameter<std::string>("xmlFileName_odd");
    xmlFileName_odd = boost::replace_all_copy(xmlFileName_odd, "era", era);
    xmlFileName_odd = boost::replace_all_copy(xmlFileName_odd, "X", BM);
    std::string xmlFileName_even = cfg.getParameter<std::string>("xmlFileName_even");
    xmlFileName_even = boost::replace_all_copy(xmlFileName_even, "era", era);
    xmlFileName_even = boost::replace_all_copy(xmlFileName_even, "X", BM);
    std::vector<std::string> inputVariables = cfg.getParameter<std::vector<std::string>>("inputVariables");
    //inputVariables.push_back(BM);
    //if ( is_nonresonant )
    //{
    TMVAInterface* retVal = nullptr;
    assert(xmlFileName_even != "" && xmlFileName_odd != "" && inputVariables.size() != 0);
    retVal = new TMVAInterface(xmlFileName_odd, xmlFileName_even, inputVariables);
    //}
    //else
    //{
    //  std::string fitFileName = cfg.getParameter<std::string>("fitFileName");
    //  assert(xmlFileName_odd != "" && xmlFileName_even != "" && fitFileName != "" && inputVariables.size() != 0);
    //  retVal = new TMVAInterface(xmlFileName_odd, xmlFileName_even, inputVariables, fitFileName);
    //}
    retVal->enableBDTTransform();
    retVals[BM] = retVal;
  }
  return retVals;
}

std::vector<TMVAInterface *>
makeTMVAInterface(const edm::ParameterSet & cfg, const std::string & era, bool is_nonresonant)
{
  const std::map<std::string, TMVAInterface *> retValsMap = makeTMVAInterfaceMap(cfg, era, is_nonresonant);
  std::vector<TMVAInterface *> retVals;
  for(const auto & kv: retValsMap)
  {
    retVals.push_back(kv.second);
  }
  return retVals;
}

std::map<std::string, TensorFlowInterfaceLBN *>
makeTensorFlowInterfaceLBNMap(const edm::ParameterSet & cfg, const std::string & era, bool spin0, bool spin2, bool split_resonant_training)
{
  std::map<std::string, TensorFlowInterfaceLBN *> retVals;
  std::vector<std::string> points;
  if ( !(spin0 || spin2) )
  {
    points.insert(points.end(), BMpoints.begin(), BMpoints.end());
  }
  else
  {
    if ( spin0 )
    {
      (!split_resonant_training) ? points.insert(points.end(), spin0points.begin(), spin0points.end()) :
        points.insert(points.end(), split_spin0points.begin(), split_spin0points.end());
    }
    if ( spin2 )
    {
      (!split_resonant_training) ? points.insert(points.end(), spin2points.begin(), spin2points.end()) :
        points.insert(points.end(), split_spin2points.begin(), split_spin2points.end());
    }
  }
  for ( std::string & point: points) 
  {
    std::string pbFileName_odd = cfg.getParameter<std::string>("pbFileName_odd");
    pbFileName_odd = boost::replace_all_copy(pbFileName_odd, "era", era);
    pbFileName_odd = boost::replace_all_copy(pbFileName_odd, "X", point);
    std::string pbFileName_even = cfg.getParameter<std::string>("pbFileName_even");
    pbFileName_even = boost::replace_all_copy(pbFileName_even, "era", era);
    pbFileName_even = boost::replace_all_copy(pbFileName_even, "X", point);
    std::vector<std::string> ll_inputVariables = cfg.getParameter<std::vector<std::string>>("ll_inputVariables");
    std::vector<std::string> hl_inputVariables = cfg.getParameter<std::vector<std::string>>("hl_inputVariables");
    std::vector<std::string> classes = cfg.getParameter<std::vector<std::string>>("classes");
    assert(pbFileName_even != "" && pbFileName_odd != "" && ll_inputVariables.size() != 0 && hl_inputVariables.size() != 0 && classes.size() != 0);
    TensorFlowInterfaceLBN * retVal = new TensorFlowInterfaceLBN(pbFileName_odd, ll_inputVariables, hl_inputVariables, classes, pbFileName_even);
    retVals[point] = retVal;
  }
  return retVals;
}
std::vector<TensorFlowInterfaceLBN *>
makeTensorFlowInterfaceLBN(const edm::ParameterSet & cfg, const std::string & era, bool spin0, bool spin2, bool split_resonant_training)
{
  const std::map<std::string, TensorFlowInterfaceLBN *> retValsMap = makeTensorFlowInterfaceLBNMap(cfg, era, spin0, spin2, split_resonant_training);
  std::vector<TensorFlowInterfaceLBN *> retVals;
  for(const auto & kv: retValsMap)
  {
    retVals.push_back(kv.second);
  }
  return retVals;
}

void printHbb(const std::vector<const RecoJetAK8*>& jets_ak8, const RecoJetCollectionSelectorAK8_hh_bbWW_Hbb& jetSelectorAK8_Hbb,
	      const std::vector<GenParticle>& genBJets)
{
  std::cout << "<printHbb>:" << std::endl;
  std::cout << "#genBJets = " << genBJets.size() << std::endl;
  for ( size_t idxBJet = 0; idxBJet < genBJets.size(); ++idxBJet ) {
    const GenParticle& genBJet = genBJets[idxBJet];
    std::cout << " genBJet #" << idxBJet << ": pT = " << genBJet.pt() << ", eta = " << genBJet.eta() << ", phi = " << genBJet.phi() << std::endl;
  }
  if ( genBJets.size() == 2 ) {
    bool isMatched = false;
    Particle::LorentzVector genHbbP4 = genBJets[0].p4() + genBJets[1].p4();
    std::cout << "genHbb: pT = " << genHbbP4.pt() << ", eta = " << genHbbP4.eta() << ", phi = " << genHbbP4.phi() << std::endl;
    for ( std::vector<const RecoJetAK8*>::const_iterator jet_ak8 = jets_ak8.begin();
	  jet_ak8 != jets_ak8.end(); ++jet_ak8 ) {
      double dR = deltaR(genHbbP4, (*jet_ak8)->p4());
      if ( dR < 0.8 ) {
	std::cout << "matches reconstructed AK8 jet: pT = " << (*jet_ak8)->pt() << ", eta = " << (*jet_ak8)->eta() << ", phi = " << (*jet_ak8)->phi() << ", which ";
	if ( jetSelectorAK8_Hbb.getSelector()(**jet_ak8) ) {
	  std::cout << "PASSES";
	  isMatched = true;
	} else {
	  std::cout << "FAILS";
	}
	std::cout << " the H->bb jet selection." << std::endl;
      }
    }
    if ( genHbbP4.pt() > 100. && !isMatched ) std::cout << "--> DEBUG (Hbb) !!" << std::endl;
  }
}

void printWjj(const std::vector<const RecoJetAK8*>& jets_ak8, const RecoJetCollectionSelectorAK8_hh_Wjj& jetSelectorAK8_Wjj,
	      const std::vector<GenParticle>& genWBosons, const std::vector<GenParticle>& genWJets)
{
  std::cout << "<printWjj>:" << std::endl;
  std::cout << "#genWBosons = " << genWBosons.size() << std::endl;
  for ( size_t idxWBoson = 0; idxWBoson < genWBosons.size(); ++idxWBoson ) {
    const GenParticle& genWBoson = genWBosons[idxWBoson];
    std::cout << " genWBoson #" << idxWBoson << ": pT = " << genWBoson.pt() << ", eta = " << genWBoson.eta() << ", phi = " << genWBoson.phi() << std::endl;
  }
  std::cout << "#genWJets = " << genWJets.size() << std::endl;
  for ( size_t idxWJet = 0; idxWJet < genWJets.size(); ++idxWJet ) {
    const GenParticle& genWJet = genWJets[idxWJet];
    std::cout << " genWJet #" << idxWJet << ": pT = " << genWJet.pt() << ", eta = " << genWJet.eta() << ", phi = " << genWJet.phi() << std::endl;
  }
  if ( genWBosons.size() == 1 ) {
    bool isMatched = false;
    Particle::LorentzVector genWjjP4 = genWBosons[0].p4();
    std::cout << "genWjj: pT = " << genWjjP4.pt() << ", eta = " << genWjjP4.eta() << ", phi = " << genWjjP4.phi() << std::endl;
    for ( std::vector<const RecoJetAK8*>::const_iterator jet_ak8 = jets_ak8.begin();
	  jet_ak8 != jets_ak8.end(); ++jet_ak8 ) {
      double dR = deltaR(genWjjP4, (*jet_ak8)->p4());
      if ( dR < 0.8 ) {
	std::cout << "matches reconstructed AK8 jet: pT = " << (*jet_ak8)->pt() << ", eta = " << (*jet_ak8)->eta() << ", phi = " << (*jet_ak8)->phi() << ","
		  << " msoftdrop = " << (*jet_ak8)->msoftdrop() << ", tau21 = " << (*jet_ak8)->tau2()/(*jet_ak8)->tau1() << ", which ";
	if ( jetSelectorAK8_Wjj.getSelector()(**jet_ak8) ) {
	  std::cout << "PASSES";
	  isMatched = true;
	} else {
	  std::cout << "FAILS";
	}
	std::cout << " the W->jj jet selection." << std::endl;
	std::cout << "generator-level subjets:" << std::endl;
	for ( std::vector<GenParticle>::const_iterator genWJet1 = genWJets.begin();
	      genWJet1 != genWJets.end(); ++genWJet1 ) {
	  for ( std::vector<GenParticle>::const_iterator genWJet2 = genWJet1 + 1;
		genWJet2 != genWJets.end(); ++genWJet2 ) {
	    if ( deltaR(genWJet1->p4() + genWJet2->p4(), genWjjP4) < 1.e-1 && std::fabs((genWJet1->p4() + genWJet2->p4()).mass() - genWjjP4.mass()) < 1.e+1 ) {
	      std::cout << " genWJet #1: pT = " << genWJet1->pt() << ", eta = " << genWJet1->eta() << ", phi = " << genWJet1->phi() << std::endl;
	      std::cout << " genWJet #2: pT = " << genWJet2->pt() << ", eta = " << genWJet2->eta() << ", phi = " << genWJet2->phi() << std::endl;
	    }
	  }
	}
	std::cout << "reconstructed subjets:" << std::endl;
	const RecoSubjetAK8* subjet1 = (*jet_ak8)->subJet1();
	if ( subjet1 ) std::cout << " subjet #1: pT = " << subjet1->pt() << ", eta = " << subjet1->eta() << ", phi = " << subjet1->phi() << std::endl;
	const RecoSubjetAK8* subjet2 = (*jet_ak8)->subJet2();
	if ( subjet2 ) std::cout << " subjet #2: pT = " << subjet2->pt() << ", eta = " << subjet2->eta() << ", phi = " << subjet2->phi() << std::endl;
      }
    }
    if ( genWjjP4.pt() > 100. && !isMatched ) std::cout << "--> DEBUG (Wjj) !!" << std::endl;
  }
}
