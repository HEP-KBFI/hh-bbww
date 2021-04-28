#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector, math::XYZTLorentzVectorD
#include "DataFormats/Math/interface/deltaR.h" // deltaR
#include "DataFormats/Math/interface/deltaPhi.h" // deltaPhi

#if __has_include (<FWCore/ParameterSetReader/interface/ParameterSetReader.h>)
#  include <FWCore/ParameterSetReader/interface/ParameterSetReader.h> // edm::readPSetsFrom()
#else
#  include <FWCore/PythonParameterSet/interface/MakeParameterSets.h> // edm::readPSetsFrom()
#endif

#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h" // LHEInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEParticleReader.h" // LHEParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEParticle.h" // LHEParticle
#include "tthAnalysis/HiggsToTauTau/interface/PSWeightReader.h" // PSWeightReader
#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/WeightHistManager.h" // WeightHistManager
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoHistManager.h" // LHEInfoHistManager
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h" // format_vstring
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow, fillWithOverFlow2d, divideByBinWidth
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceCouplings.h" // HHWeightInterfaceCouplings
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceLO.h" // HHWeightInterfaceLO
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceNLO.h" // HHWeightInterfaceNLO
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceCouplings.h" // HHWeightInterfaceCouplings
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_cosThetaStar

#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH
#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h" // AnalysisConfig_hh
#include "hhAnalysis/multilepton/interface/HHGenKinematicsHistManager.h" // HHGenKinematicsHistManager

#include "hhAnalysis/bbww/interface/BM_list.h" // BMs
#include "hhAnalysis/bbww/interface/dumpGenParticles.h" // dumpGenParticles
#include "hhAnalysis/bbww/interface/HHatLOvsNLOHistManager.h" // HHatLOvsNLOHistManager

#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TRandom3.h> // TRandom3
#include <TROOT.h> // TROOT
#include <TH1.h>
#include <TH2.h>
#include <TProfile.h>
#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()

#include <iostream> // std::cerr, std::fixed
#include <iomanip> // std::setprecision(), std::setw()
#include <string> // std::string
#include <vector> // std::vector<>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <fstream> // std::ofstream
#include <assert.h> // assert

typedef std::vector<std::string> vstring;
typedef std::vector<double> vdouble;

void save_dXsec(TFileDirectory& subdir, const HHWeightInterfaceNLO* HHWeightNLO_calc, const std::vector<std::string>& bmNames)
{
  assert(HHWeightNLO_calc);
  for ( std::vector<std::string>::const_iterator bmName = bmNames.begin(); bmName != bmNames.end(); ++bmName )
  {
    const TH1D* dXsec_V1_lo = dynamic_cast<const TH1D*>(HHWeightNLO_calc->get_dXsec_V1_lo(*bmName));
    assert(dXsec_V1_lo);
    subdir.make<TH1D>(*dXsec_V1_lo);
    const TH1D* dXsec_V1_nlo = dynamic_cast<const TH1D*>(HHWeightNLO_calc->get_dXsec_V1_nlo(*bmName));
    assert(dXsec_V1_nlo);
    subdir.make<TH1D>(*dXsec_V1_nlo);

    const TH2D* dXsec_V2_lo = dynamic_cast<const TH2D*>(HHWeightNLO_calc->get_dXsec_V2_lo(*bmName));
    assert(dXsec_V2_lo);
    subdir.make<TH2D>(*dXsec_V2_lo);
    const TH2D* dXsec_V2_nlo = dynamic_cast<const TH2D*>(HHWeightNLO_calc->get_dXsec_V2_nlo(*bmName));
    assert(dXsec_V2_nlo);
    subdir.make<TH2D>(*dXsec_V2_nlo);
  }
}

/**
 * @brief Produce datacard and control plots for dilepton category of the HH->bbWW analysis.
 */
int main(int argc, char* argv[])
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- stop ROOT from keeping track of all histograms
  TH1::AddDirectory(false);

//--- parse command-line arguments
  if ( argc < 2 ) {
    std::cout << "Usage: " << argv[0] << " [parameters.py]" << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "<analyze_HHatLOvsNLO>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_HHatLOvsNLO");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_HHatLOvsNLO")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_HHatLOvsNLO");
  AnalysisConfig_hh analysisConfig("HH->bbWW", cfg_analyze);

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  std::string process_string_hh = ( process_string.find("signal_") != std::string::npos ) ? cfg_analyze.getParameter<std::string>("process_hh") : "";
  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  bool isSignal = analysisConfig.isMC_HH();
  std::cout << "isSignal = " << isSignal << std::endl;

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const Era era = get_era(era_string);

  bool hasLHE = cfg_analyze.getParameter<bool>("hasLHE");
  bool hasPS = cfg_analyze.getParameter<bool>("hasPS");
  bool apply_LHE_nom = cfg_analyze.getParameter<bool>("apply_LHE_nom");
  std::string central_or_shift = cfg_analyze.getParameter<std::string>("central_or_shift");
  edm::VParameterSet lumiScale = cfg_analyze.getParameter<edm::VParameterSet>("lumiScale");
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");

  const edm::ParameterSet additionalEvtWeight = cfg_analyze.getParameter<edm::ParameterSet>("evtWeight");
  const bool applyAdditionalEvtWeight = additionalEvtWeight.getParameter<bool>("apply");
  EvtWeightManager * eventWeightManager = nullptr;
  if(applyAdditionalEvtWeight)
  {
    eventWeightManager = new EvtWeightManager(additionalEvtWeight);
    eventWeightManager->set_central_or_shift(central_or_shift);
  }

  bool isDEBUG = cfg_analyze.getParameter<bool>("isDEBUG");

  std::string branchName_genHBosons = cfg_analyze.getParameter<std::string>("branchName_genHBosons");

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)\n";

//--- declare event-level variables
  EventInfo eventInfo(analysisConfig);
  if(isMC)
  {
    const double ref_genWeight = cfg_analyze.getParameter<double>("ref_genWeight");
    eventInfo.set_refGetWeight(ref_genWeight);
  }

//--- HH coupling scan
  const edm::ParameterSet hhWeight_cfg = cfg_analyze.getParameterSet("hhWeight_cfg");
  const HHWeightInterfaceCouplings * couplings = new HHWeightInterfaceCouplings(hhWeight_cfg);
  std::vector<std::string> HHBMNames = couplings->get_bm_names();
  const bool apply_HH_rwgt_lo  = isSignal && analysisConfig.isHH_rwgt_allowed(); // sample is LO HH MC sample
  const bool apply_HH_rwgt_nlo = isSignal;                                       // sample is LO or NLO HH MC sample
  std::cout << "apply_HH_rwgt: LO = " << apply_HH_rwgt_lo << ", NLO = " << apply_HH_rwgt_nlo << std::endl;

  bool save_dXsec_HHWeightInterfaceNLO = cfg_analyze.getParameter<bool>("save_dXsec_HHWeightInterfaceNLO");
  std::cout << "save_dXsec_HHWeightInterfaceNLO = " << save_dXsec_HHWeightInterfaceNLO << std::endl;

  const HHWeightInterfaceCouplings * hhWeight_couplings = nullptr;
  const HHWeightInterfaceLO* HHWeightLO_calc = nullptr;
  const HHWeightInterfaceNLO* HHWeightNLO_calc_woCouplingBugFix = nullptr;
  const HHWeightInterfaceNLO* HHWeightNLO_calc_wCouplingBugFix = nullptr;
  if(apply_HH_rwgt_lo || apply_HH_rwgt_nlo)
  {
    hhWeight_couplings = new HHWeightInterfaceCouplings(hhWeight_cfg);
    //HHWeightNames = hhWeight_couplings->get_weight_names();
    //HHBMNames = hhWeight_couplings->get_bm_names();
    
    if ( apply_HH_rwgt_lo )
    {
      HHWeightLO_calc = new HHWeightInterfaceLO(couplings, hhWeight_cfg);
    }
    if ( apply_HH_rwgt_nlo )
    {
      // CV: applying the NLO weight without applying the LO weight as well
      //     does not make sense for the Run-2 LO HH MC samples,
      //     as the LO weight needs to be applied in order to fix the coupling bug 
      //     present in the LO HH MC samples for 2016, 2017, and 2018        
      HHWeightNLO_calc_woCouplingBugFix = new HHWeightInterfaceNLO(couplings, era, false);
      HHWeightNLO_calc_wCouplingBugFix = new HHWeightInterfaceNLO(couplings, era, true);
    }
  }

  EventInfoReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

//--- declare particle collections
  LHEParticleReader* lheParticleReader = new LHEParticleReader();
  inputTree->registerReader(lheParticleReader);

  GenParticleReader* genHBosonReader = new GenParticleReader(branchName_genHBosons);
  inputTree->registerReader(genHBosonReader);

  LHEInfoReader* lheInfoReader = new LHEInfoReader(hasLHE);
  inputTree->registerReader(lheInfoReader);
  PSWeightReader* psWeightReader = new PSWeightReader(hasPS, apply_LHE_nom);
  inputTree->registerReader(psWeightReader);

//--- declare histograms
  HHGenKinematicsHistManager* genKinematicsHistManager_HH = new HHGenKinematicsHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/genKinematics_HH", histogramDir.data()), era_string, central_or_shift),
    analysisConfig, eventInfo, hhWeight_couplings, HHWeightLO_calc, HHWeightNLO_calc_woCouplingBugFix);
  genKinematicsHistManager_HH->bookHistograms(fs);

  WeightHistManager* weightHistManager = new WeightHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/weights", histogramDir.data()), era_string, central_or_shift));
  weightHistManager->bookHistograms(fs, { "genWeight", "pileupWeight", "HHReweight_lo", "HHReweight_nlo_V1", "HHReweight_nlo_V2" });

  LHEInfoHistManager* lheInfoHistManager = new LHEInfoHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/lheInfo", histogramDir.data()), era_string, central_or_shift));
  lheInfoHistManager->bookHistograms(fs);

  HHatLOvsNLOHistManager* hhHistManager_woLOWeights_woLOtoNLOWeights = new HHatLOvsNLOHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/hh_woLOWeights_woLOtoNLOWeights", histogramDir.data()), era_string, central_or_shift));
  hhHistManager_woLOWeights_woLOtoNLOWeights->bookHistograms(fs);

  struct selHistManagerType
  {  
    HHatLOvsNLOHistManager* wLOWeights_woLOtoNLOWeights_;

    HHatLOvsNLOHistManager* woLOWeights_wLOtoNLOWeights_V1_;
    HHatLOvsNLOHistManager* woLOWeights_wLOtoNLOWeights_V2_;

    HHatLOvsNLOHistManager* wLOWeights_wLOtoNLOWeights_V1_;
    HHatLOvsNLOHistManager* wLOWeights_wLOtoNLOWeights_V2_;

    HHatLOvsNLOHistManager* wNLOtoNLOWeights_V1_;
    HHatLOvsNLOHistManager* wNLOtoNLOWeights_V2_;
  };

  std::map<std::string, selHistManagerType*> hhHistManagers_weighted; // key = bmName;
  for ( std::vector<std::string>::const_iterator HHBMName = HHBMNames.begin(); HHBMName != HHBMNames.end(); ++HHBMName )
  {
    selHistManagerType* hhHistManager_weighted = new selHistManagerType();

    hhHistManager_weighted->wLOWeights_woLOtoNLOWeights_ = new HHatLOvsNLOHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/hh_%s_wLOWeights_woLOtoNLOWeights", histogramDir.data(), HHBMName->data()), era_string, central_or_shift));
    hhHistManager_weighted->wLOWeights_woLOtoNLOWeights_->bookHistograms(fs);

    hhHistManager_weighted->woLOWeights_wLOtoNLOWeights_V1_ = new HHatLOvsNLOHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/hh_%s_woLOWeights_wLOtoNLOWeights_V1", histogramDir.data(), HHBMName->data()), era_string, central_or_shift));   
    hhHistManager_weighted->woLOWeights_wLOtoNLOWeights_V1_->bookHistograms(fs);
    hhHistManager_weighted->woLOWeights_wLOtoNLOWeights_V2_ = new HHatLOvsNLOHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/hh_%s_woLOWeights_wLOtoNLOWeights_V2", histogramDir.data(), HHBMName->data()), era_string, central_or_shift));
    hhHistManager_weighted->woLOWeights_wLOtoNLOWeights_V2_->bookHistograms(fs);

    hhHistManager_weighted->wLOWeights_wLOtoNLOWeights_V1_ = new HHatLOvsNLOHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/hh_%s_wLOWeights_wLOtoNLOWeights_V1", histogramDir.data(), HHBMName->data()), era_string, central_or_shift));
    hhHistManager_weighted->wLOWeights_wLOtoNLOWeights_V1_->bookHistograms(fs);
    hhHistManager_weighted->wLOWeights_wLOtoNLOWeights_V2_ = new HHatLOvsNLOHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/hh_%s_wLOWeights_wLOtoNLOWeights_V2", histogramDir.data(), HHBMName->data()), era_string, central_or_shift));
    hhHistManager_weighted->wLOWeights_wLOtoNLOWeights_V2_->bookHistograms(fs);

    hhHistManager_weighted->wNLOtoNLOWeights_V1_ = new HHatLOvsNLOHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/hh_%s_wNLOtoNLOWeights_V1", histogramDir.data(), HHBMName->data()), era_string, central_or_shift));
    hhHistManager_weighted->wNLOtoNLOWeights_V1_->bookHistograms(fs);
    hhHistManager_weighted->wNLOtoNLOWeights_V2_ = new HHatLOvsNLOHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/hh_%s_wNLOtoNLOWeights_V2", histogramDir.data(), HHBMName->data()), era_string, central_or_shift));
    hhHistManager_weighted->wNLOtoNLOWeights_V2_->bookHistograms(fs);
    hhHistManagers_weighted[*HHBMName] = hhHistManager_weighted;
  }

  TFileDirectory dir = fs.mkdir(histogramDir);

  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  TH1* histogram_analyzedEntries = dir.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1* histogram_selectedEntries = dir.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  while ( inputTree->hasNextEvent() ) 
  {
    if ( inputTree -> canReport(reportEvery) ) 
    {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx()
                << " or " << inputTree -> getCurrentEventIdx() << " entry in #"
                << (inputTree -> getProcessedFileCount() - 1)
                << " (" << eventInfo
                << ") file\n";
    }
    ++analyzedEntries;
    histogram_analyzedEntries->Fill(0.);

    if ( isDEBUG ) 
    {
      std::cout << "processing Entry #" << inputTree->getCumulativeMaxEventCount() << ": " << eventInfo << std::endl;
    }

    EvtWeightRecorderHH evtWeightRecorder({ central_or_shift }, central_or_shift, isMC);

    eventInfo.reset_productionMode();

    if ( isMC )
    {
      if ( apply_genWeight    ) evtWeightRecorder.record_genWeight(eventInfo);
      if ( eventWeightManager ) evtWeightRecorder.record_auxWeight(eventWeightManager);
      lheInfoReader->read();
      psWeightReader->read();
      evtWeightRecorder.record_lheScaleWeight(lheInfoReader);
      evtWeightRecorder.record_psWeight(psWeightReader);
      evtWeightRecorder.record_puWeight(&eventInfo);
      evtWeightRecorder.record_lumiScale(lumiScale);
    }

    double evtWeight = evtWeightRecorder.get(central_or_shift);

    std::vector<GenParticle> genHBosons = genHBosonReader->read();
    if ( genHBosons.size() == 2 )
    {
      std::vector<const GenParticle*> genHBosons_sorted = convert_to_ptrs(genHBosons);
      std::sort(genHBosons_sorted.begin(), genHBosons_sorted.end(), isHigherPt);
      const GenParticle* genHBoson_lead = genHBosons_sorted[0];
      const Particle::LorentzVector genHBosonP4_lead = genHBoson_lead->p4();
      const GenParticle* genHBoson_sublead = genHBosons_sorted[1];
      const Particle::LorentzVector genHBosonP4_sublead = genHBoson_sublead->p4();

      double gen_mHH, gen_cosThetaStar;
      if ( apply_HH_rwgt_lo )
      {
        // sample is LO HH MC sample;
        // take mHH and cos(theta*) values from LHE information
        gen_mHH = eventInfo.gen_mHH;
        gen_cosThetaStar = eventInfo.gen_cosThetaStar;
      }
      else
      {
        // sample is NLO HH MC sample;
        // the mHH and cos(theta*) values are not stored in the LHE information for the NLO HH MC samples,
        // so reconstruct their values from the genParticle information instead
        Particle::LorentzVector genHHP4 = genHBosonP4_lead + genHBosonP4_sublead;
        gen_mHH = genHHP4.mass();
        gen_cosThetaStar = std::fabs(comp_cosThetaStar(genHBosonP4_lead, genHBosonP4_sublead));
      }

      double hhWeight_lo = 1.;

      double hhWeight_lo_to_nlo_woCouplingBugFix_V1 = 1.;
      double hhWeight_lo_to_nlo_woCouplingBugFix_V2 = 1.;

      double hhWeight_lo_to_nlo_wCouplingBugFix_V1 = 1.;
      double hhWeight_lo_to_nlo_wCouplingBugFix_V2 = 1.;
      if ( apply_HH_rwgt_lo )
      {
        hhWeight_lo = HHWeightLO_calc->getWeight("SM", gen_mHH, gen_cosThetaStar, isDEBUG);
      }
      if ( apply_HH_rwgt_nlo )
      {
        hhWeight_lo_to_nlo_woCouplingBugFix_V1 = HHWeightNLO_calc_woCouplingBugFix->getWeight_LOtoNLO_V1("SM", gen_mHH, gen_cosThetaStar, isDEBUG);
        hhWeight_lo_to_nlo_woCouplingBugFix_V2 = HHWeightNLO_calc_woCouplingBugFix->getWeight_LOtoNLO_V2("SM", gen_mHH, gen_cosThetaStar, isDEBUG);

        hhWeight_lo_to_nlo_wCouplingBugFix_V1 = HHWeightNLO_calc_wCouplingBugFix->getWeight_LOtoNLO_V1("SM", gen_mHH, gen_cosThetaStar, isDEBUG);
        hhWeight_lo_to_nlo_wCouplingBugFix_V2 = HHWeightNLO_calc_wCouplingBugFix->getWeight_LOtoNLO_V2("SM", gen_mHH, gen_cosThetaStar, isDEBUG);
      }

      genKinematicsHistManager_HH->fillHistograms(evtWeight*hhWeight_lo*hhWeight_lo_to_nlo_woCouplingBugFix_V2);

      weightHistManager->fillHistograms("genWeight", eventInfo.genWeight);
      weightHistManager->fillHistograms("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift));
      weightHistManager->fillHistograms("HHReweight_lo", hhWeight_lo);
      weightHistManager->fillHistograms("HHReweight_nlo_V1", hhWeight_lo_to_nlo_woCouplingBugFix_V1);
      weightHistManager->fillHistograms("HHReweight_nlo_V2", hhWeight_lo_to_nlo_woCouplingBugFix_V2);

      lheInfoHistManager->fillHistograms(*lheInfoReader, evtWeight*hhWeight_lo*hhWeight_lo_to_nlo_woCouplingBugFix_V2);
    
      hhHistManager_woLOWeights_woLOtoNLOWeights->fillHistograms(genHBosonP4_lead, genHBosonP4_sublead, 
        evtWeight, 1.);

      for ( std::vector<std::string>::const_iterator HHBMName = HHBMNames.begin(); HHBMName != HHBMNames.end(); ++HHBMName )
      {
        double hhReWeight_lo = 1.;

        double hhReWeight_lo_to_nlo_woCouplingBugFix_V1 = 1.;
        double hhReWeight_lo_to_nlo_woCouplingBugFix_V2 = 1.;

        double hhReWeight_lo_to_nlo_wCouplingBugFix_V1 = 1.;
        double hhReWeight_lo_to_nlo_wCouplingBugFix_V2 = 1.;

        double hhWeight_nlo_to_nlo_woCouplingBugFix_V1 = 1.;
        double hhWeight_nlo_to_nlo_woCouplingBugFix_V2 = 1.;
        if ( apply_HH_rwgt_lo )
        {
          hhReWeight_lo = HHWeightLO_calc->getRelativeWeight(*HHBMName, gen_mHH, gen_cosThetaStar, isDEBUG);
        }
        if ( apply_HH_rwgt_nlo )
        {
          hhReWeight_lo_to_nlo_woCouplingBugFix_V1 = HHWeightNLO_calc_woCouplingBugFix->getRelativeWeight_LOtoNLO_V1(*HHBMName, gen_mHH, gen_cosThetaStar, isDEBUG);
          hhReWeight_lo_to_nlo_woCouplingBugFix_V2 = HHWeightNLO_calc_woCouplingBugFix->getRelativeWeight_LOtoNLO_V2(*HHBMName, gen_mHH, gen_cosThetaStar, isDEBUG);

          hhReWeight_lo_to_nlo_wCouplingBugFix_V1 = HHWeightNLO_calc_wCouplingBugFix->getRelativeWeight_LOtoNLO_V1(*HHBMName, gen_mHH, gen_cosThetaStar, isDEBUG);
          hhReWeight_lo_to_nlo_wCouplingBugFix_V2 = HHWeightNLO_calc_wCouplingBugFix->getRelativeWeight_LOtoNLO_V2(*HHBMName, gen_mHH, gen_cosThetaStar, isDEBUG);

          hhWeight_nlo_to_nlo_woCouplingBugFix_V1 = HHWeightNLO_calc_wCouplingBugFix->getRelativeWeight_NLOtoNLO_V1(*HHBMName, gen_mHH, gen_cosThetaStar, isDEBUG);
          hhWeight_nlo_to_nlo_woCouplingBugFix_V2 = HHWeightNLO_calc_wCouplingBugFix->getRelativeWeight_NLOtoNLO_V2(*HHBMName, gen_mHH, gen_cosThetaStar, isDEBUG);
        }

        selHistManagerType* hhHistManager_weighted = hhHistManagers_weighted[*HHBMName];

        hhHistManager_weighted->wLOWeights_woLOtoNLOWeights_->fillHistograms(genHBosonP4_lead, genHBosonP4_sublead, 
          evtWeight, hhWeight_lo*hhReWeight_lo);

        hhHistManager_weighted->woLOWeights_wLOtoNLOWeights_V1_->fillHistograms(genHBosonP4_lead, genHBosonP4_sublead, 
          evtWeight, hhWeight_lo_to_nlo_wCouplingBugFix_V1*hhReWeight_lo_to_nlo_wCouplingBugFix_V1);
        hhHistManager_weighted->woLOWeights_wLOtoNLOWeights_V2_->fillHistograms(genHBosonP4_lead, genHBosonP4_sublead, 
          evtWeight, hhWeight_lo_to_nlo_wCouplingBugFix_V2*hhReWeight_lo_to_nlo_wCouplingBugFix_V2);

        hhHistManager_weighted->wLOWeights_wLOtoNLOWeights_V1_->fillHistograms(genHBosonP4_lead, genHBosonP4_sublead, 
          evtWeight, hhWeight_lo*hhReWeight_lo*hhWeight_lo_to_nlo_woCouplingBugFix_V1*hhReWeight_lo_to_nlo_woCouplingBugFix_V1);
        hhHistManager_weighted->wLOWeights_wLOtoNLOWeights_V2_->fillHistograms(genHBosonP4_lead, genHBosonP4_sublead, 
          evtWeight, hhWeight_lo*hhReWeight_lo*hhWeight_lo_to_nlo_woCouplingBugFix_V2*hhReWeight_lo_to_nlo_woCouplingBugFix_V2);

        hhHistManager_weighted->wNLOtoNLOWeights_V1_->fillHistograms(genHBosonP4_lead, genHBosonP4_sublead, 
          evtWeight, hhWeight_nlo_to_nlo_woCouplingBugFix_V1);
        hhHistManager_weighted->wNLOtoNLOWeights_V2_->fillHistograms(genHBosonP4_lead, genHBosonP4_sublead, 
          evtWeight, hhWeight_nlo_to_nlo_woCouplingBugFix_V2);
      }

      ++selectedEntries;
      selectedEntries_weighted += evtWeight*hhWeight_lo*hhWeight_lo_to_nlo_woCouplingBugFix_V2;
      histogram_selectedEntries->Fill(0.);
    }
  }

  std::cout << "max num. Entries = " << inputTree -> getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree -> getProcessedFileCount() << " file(s) (out of "
            << inputTree -> getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << '\n'
            << " selected = " << selectedEntries << " (weighted = " << selectedEntries_weighted << ")\n";

//--- save histograms of LO and NLO cross sections used for HH reweighting
  if ( save_dXsec_HHWeightInterfaceNLO )
  {
    TFileDirectory subdir_woCouplingBugFix = dir.mkdir("HHWeightInterfaceNLO_woCouplingBugFix");
    save_dXsec(subdir_woCouplingBugFix, HHWeightNLO_calc_woCouplingBugFix, HHBMNames);
    TFileDirectory subdir_wCouplingBugFix = dir.mkdir("HHWeightInterfaceNLO_wCouplingBugFix");
    save_dXsec(subdir_wCouplingBugFix, HHWeightNLO_calc_wCouplingBugFix, HHBMNames);
  }

//--- manually write histograms to output file
  fs.file().cd();
  //histogram_analyzedEntries->Write();
  //histogram_selectedEntries->Write();
  HistManagerBase::writeHistograms();

//--- memory clean-up
  delete lheInfoReader;
  delete psWeightReader;

  delete eventWeightManager;

  delete HHWeightLO_calc;
  delete HHWeightNLO_calc_woCouplingBugFix;
  delete HHWeightNLO_calc_wCouplingBugFix;

  delete inputTree;

  clock.Show("analyze_HHatLOvsNLO");

  return EXIT_SUCCESS;
}
