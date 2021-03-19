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
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_cosThetaStar
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow, fillWithOverFlow2d, divideByBinWidth
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterface2.h" // HHWeightInterface2
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceLOtoNLO.h" // HHWeightInterfaceLOtoNLO

#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH
#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h" // AnalysisConfig_hh
#include "hhAnalysis/multilepton/interface/HHGenKinematicsHistManager.h"

#include "hhAnalysis/bbww/interface/BM_list.h" // BMS
#include "hhAnalysis/bbww/interface/dumpGenParticles.h" // dumpGenParticles

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
  clock.Start("analyze_hh_bb1l");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_HHatLOvsNLO")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_HHatLOvsNLO");
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

  //std::string branchName_genHBosons = cfg_analyze.getParameter<std::string>("branchName_genHBosons");
  std::string branchName_genHBosons;
  if (cfg_analyze.exists("branchName_genHBosons"))
  {
    branchName_genHBosons = cfg_analyze.getParameter<std::string>("branchName_genHBosons");
  }
  else if (cfg_analyze.exists("branchName_genHiggses"))
  {
    branchName_genHBosons = cfg_analyze.getParameter<std::string>("branchName_genHiggses");
  }
  
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
  std::vector<std::string> HHWeightNames;
  std::vector<std::string> HHBMNames;
  const edm::ParameterSet hhWeight_cfg = cfg_analyze.getParameterSet("hhWeight_cfg");
  const bool apply_HH_rwgt = analysisConfig.isHH_rwgt_allowed() && hhWeight_cfg.getParameter<bool>("apply_rwgt");
  const HHWeightInterface2* HHWeight_calc = nullptr;
  if(apply_HH_rwgt)
  {
    HHWeight_calc = new HHWeightInterface2(hhWeight_cfg);
    HHWeightNames = HHWeight_calc->get_weight_names();
    HHBMNames = HHWeight_calc->get_bm_names();
  }
  const bool apply_HH_rwgt_LOtoNLO = analysisConfig.isHH_rwgt_allowed() && hhWeight_cfg.getParameter<bool>("apply_rwgt_LOtoNLO");
  const bool apply_HH_coupling_fix_CMS = hhWeight_cfg.getParameter<bool>("apply_coupling_fix_Run2");
  const HHWeightInterfaceLOtoNLO* HHWeight_calc_LOtoNLO = nullptr;
  if(apply_HH_rwgt_LOtoNLO)
  {
    HHWeight_calc_LOtoNLO = new HHWeightInterfaceLOtoNLO(era, apply_HH_coupling_fix_CMS, 10., isDEBUG);
  }
  std::cout << "apply_HH_rwgt: " << apply_HH_rwgt
	    << ", apply_HH_rwgt_LOtoNLO: " << apply_HH_rwgt_LOtoNLO
	    << ", apply_HH_coupling_fix_CMS: " << apply_HH_coupling_fix_CMS
	    << "\n";

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
  struct selHistManagerType
  {  
    HHGenKinematicsHistManager* genKinematics_HH_;
    WeightHistManager* weights_;
  };

  selHistManagerType* selHistManager = new selHistManagerType();
  selHistManager->genKinematics_HH_ = new HHGenKinematicsHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/genKinematics_HH", histogramDir.data()), era_string, central_or_shift),
    analysisConfig, eventInfo, HHWeight_calc, HHWeight_calc_LOtoNLO);
  selHistManager->genKinematics_HH_->bookHistograms(fs);
  selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/weights", histogramDir.data()), era_string, central_or_shift));
  selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight", "HHReweight", "HHReweight_LOtoNLO_V1", "HHReweight_LOtoNLO_V2" });

  LHEInfoHistManager* lheInfoHistManager = new LHEInfoHistManager(makeHistManager_cfg(process_string,
    Form("%s/sel/lheInfo", histogramDir.data()), era_string, central_or_shift));
  lheInfoHistManager->bookHistograms(fs);

  TFileDirectory dir = fs.mkdir(histogramDir);
  TFileDirectory dir1 = fs.mkdir(Form("%s/sel/evt/%s", histogramDir.data(),process_string.data()));

  TH1* histogram_genHBoson_lead_pt = dir1.make<TH1D>("genHBoson_lead_pt", "genHBoson_lead_pt", 50, 0., 500.);
  TH1* histogram_genHBoson_lead_eta = dir1.make<TH1D>("genHBoson_lead_eta", "genHBoson_lead_eta", 100, -5.0, +5.0);
  TH1* histogram_genHBoson_sublead_pt = dir1.make<TH1D>("genHBoson_sublead_pt", "genHBoson_sublead_pt", 50, 0., 500.);
  TH1* histogram_genHBoson_sublead_eta = dir1.make<TH1D>("genHBoson_sublead_eta", "genHBoson_sublead_eta", 100, -5.0, +5.0);
  int numBins_genHH_mass = 36;
  double binning_genHH_mass[] = {
     250,  270,  290,  310,  330,  350,  370, 390,  410,  430, 
     450,  470,  490,  510,  530,  550,  570, 590,  610,  630, 
     650,  670,  700,  750,  800,  850,  900, 950, 1000, 1100, 
    1200, 1300, 1400, 1500, 1750, 2000, 5000
  };
  //TH1* histogram_genHH_mass = dir1.make<TH1D>("genHH_mass", "genHH_mass", 500, 0., 5000.);
  TH1* histogram_genHH_mass_unweighted = dir1.make<TH1D>("genHH_mass_unweighted", "genHH_mass_unweighted", numBins_genHH_mass, binning_genHH_mass);
  TH1* histogram_genHH_mass_reweighted_V1 = dir1.make<TH1D>("genHH_mass_reweighted_V1", "genHH_mass_reweighted_V1", numBins_genHH_mass, binning_genHH_mass);
  TH1* histogram_genHH_mass_reweighted_V2 = dir1.make<TH1D>("genHH_mass_reweighted_V2", "genHH_mass_reweighted_V2", numBins_genHH_mass, binning_genHH_mass);
  TH1* histogram_genHH_pt = dir1.make<TH1D>("genHH_pt", "genHH_pt", 50, 0., 500.);
  TH1* histogram_genHH_absCosThetaStar = dir1.make<TH1D>("genHBoson_sublead_eta", "genHBoson_sublead_eta", 10, 0., +1.);  
  TH2* histogram_HHReweight_V1_vs_genHH_mass = dir1.make<TH2D>("HHReweight_V1_vs_genHH_mass", "HHReweight_V1_vs_genHH_mass", numBins_genHH_mass, binning_genHH_mass, 200, 0., 2.);
  TH2* histogram_HHReweight_V2_vs_genHH_mass = dir1.make<TH2D>("HHReweight_V2_vs_genHH_mass", "HHReweight_V2_vs_genHH_mass", numBins_genHH_mass, binning_genHH_mass, 200, 0., 2.);


  TFileDirectory subD1 = dir1;
  TH1* hgen_mHH_0 = subD1.make<TH1D>("gen_mHH_0", "gen_mHH_0",  400, 0, 1200);
  TH1* hgen_mHH_HHrwgt_0 = subD1.make<TH1D>("gen_mHH_HHrwgt_0", "gen_mHH_HHrwgt_0",  400, 0, 1200);
  TH1* hgen_mHH_LOtoNLOrwgt_0 = subD1.make<TH1D>("gen_mHH_LOtoNLOrwgt_0", "gen_mHH_LOtoNLOrwgt_0",  400, 0, 1200);
  TH1* hgen_mHH_HHrwgt_LOtoNLOrwgt_0 = subD1.make<TH1D>("gen_mHH_HHrwgt_LOtoNLOrwgt_0", "gen_mHH_HHrwgt_LOtoNLOrwgt_0",  400, 0, 1200);


  TH1* hgen_mHH_1 = subD1.make<TH1D>("gen_mHH_1", "gen_mHH_1",  numBins_genHH_mass, binning_genHH_mass);
  TH1* hgen_mHH_HHrwgt_1 = subD1.make<TH1D>("gen_mHH_HHrwgt_1", "gen_mHH_HHrwgt_1",  numBins_genHH_mass, binning_genHH_mass);
  TH1* hgen_mHH_LOtoNLOrwgt_1 = subD1.make<TH1D>("gen_mHH_LOtoNLOrwgt_1", "gen_mHH_LOtoNLOrwgt_1",  numBins_genHH_mass, binning_genHH_mass);
  TH1* hgen_mHH_HHrwgt_LOtoNLOrwgt_1 = subD1.make<TH1D>("gen_mHH_HHrwgt_LOtoNLOrwgt_1", "gen_mHH_HHrwgt_LOtoNLOrwgt_1",  numBins_genHH_mass, binning_genHH_mass);


  TH1* hgen_mHH_2 = subD1.make<TH1D>("gen_mHH_2", "gen_mHH_2",  numBins_genHH_mass, binning_genHH_mass);
  TH1* hgen_mHH_HHrwgt_2 = subD1.make<TH1D>("gen_mHH_HHrwgt_2", "gen_mHH_HHrwgt_2",  numBins_genHH_mass, binning_genHH_mass);
  TH1* hgen_mHH_LOtoNLOrwgt_2 = subD1.make<TH1D>("gen_mHH_LOtoNLOrwgt_2", "gen_mHH_LOtoNLOrwgt_2",  numBins_genHH_mass, binning_genHH_mass);
  TH1* hgen_mHH_HHrwgt_LOtoNLOrwgt_2 = subD1.make<TH1D>("gen_mHH_HHrwgt_LOtoNLOrwgt_2", "gen_mHH_HHrwgt_LOtoNLOrwgt_2",  numBins_genHH_mass, binning_genHH_mass);




  
  int analyzedEntries = 0;
  double analyzedEntries_weighted = 0.;
  TH1* histogram_analyzedEntries = dir.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
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

    if ( isDEBUG ) 
    {
      std::cout << "processing Entry #" << inputTree->getCumulativeMaxEventCount() << ": " << eventInfo << std::endl;
    }

    EvtWeightRecorderHH evtWeightRecorder({ central_or_shift }, central_or_shift, isMC);

    std::vector<GenParticle> genHBosons = genHBosonReader->read();

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

    double HHReweight = 1.;
    double HHReweight_V1 = 1.;
    double HHReweight_V2 = 1.;    
    if ( apply_HH_rwgt )
    {
      assert(HHWeight_calc);
      HHReweight = HHWeight_calc->getWeight("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG);
      HHReweight_V1 = HHReweight;
      HHReweight_V2 = HHReweight;
    }
    double HHReweight_LOtoNLO_V1 = 1.;
    double HHReweight_LOtoNLO_V2 = 1.;
    if ( apply_HH_rwgt_LOtoNLO )
    {
      assert(HHWeight_calc_LOtoNLO);
      HHReweight_LOtoNLO_V1 = HHWeight_calc_LOtoNLO->getReWeight("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG);
      HHReweight_LOtoNLO_V2 = HHWeight_calc_LOtoNLO->getReWeight_V2("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG);
    }

    HHReweight *= HHReweight_LOtoNLO_V2;
    HHReweight_V1 *= HHReweight_LOtoNLO_V1;
    HHReweight_V2 *= HHReweight_LOtoNLO_V2;

    if ( genHBosons.size() == 2 )
    {
      std::vector<const GenParticle*> genHBosons_sorted = convert_to_ptrs(genHBosons);
      std::sort(genHBosons_sorted.begin(), genHBosons_sorted.end(), isHigherPt);
      const GenParticle* genHBoson_lead = genHBosons_sorted[0];
      const GenParticle* genHBoson_sublead = genHBosons_sorted[1];
      Particle::LorentzVector genHHP4 = genHBoson_lead->p4() + genHBoson_sublead->p4();
      double genHH_mass = genHHP4.mass();
      double genHH_pt = genHHP4.pt();
      double genHH_cosThetaStar = std::fabs(comp_cosThetaStar(genHBoson_lead->p4(), genHBoson_sublead->p4()));
      fillWithOverFlow(histogram_genHBoson_lead_pt, genHBoson_lead->pt(), evtWeight*HHReweight);
      fillWithOverFlow(histogram_genHBoson_lead_eta, genHBoson_lead->eta(), evtWeight*HHReweight);
      fillWithOverFlow(histogram_genHBoson_sublead_pt, genHBoson_sublead->pt(), evtWeight*HHReweight);
      fillWithOverFlow(histogram_genHBoson_sublead_eta, genHBoson_sublead->eta(), evtWeight*HHReweight);
      fillWithOverFlow(histogram_genHH_mass_unweighted, genHH_mass, evtWeight);
      fillWithOverFlow(histogram_genHH_mass_reweighted_V1, genHH_mass, evtWeight*HHReweight_V1);
      fillWithOverFlow(histogram_genHH_mass_reweighted_V2, genHH_mass, evtWeight*HHReweight_V2);
      fillWithOverFlow(histogram_genHH_pt, genHH_pt, evtWeight*HHReweight);
      fillWithOverFlow(histogram_genHH_absCosThetaStar, genHH_cosThetaStar, evtWeight*HHReweight);
      fillWithOverFlow2d(histogram_HHReweight_V1_vs_genHH_mass, genHH_mass, HHReweight_LOtoNLO_V1, evtWeight);
      fillWithOverFlow2d(histogram_HHReweight_V2_vs_genHH_mass, genHH_mass, HHReweight_LOtoNLO_V2, evtWeight);

      fillWithOverFlow(hgen_mHH_0, genHH_mass, evtWeight);
      if ( apply_HH_rwgt_LOtoNLO )
	fillWithOverFlow(hgen_mHH_LOtoNLOrwgt_0, genHH_mass,
		       evtWeight *
		       HHWeight_calc_LOtoNLO->getReWeight_V2("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG));
      if ( apply_HH_rwgt )
	fillWithOverFlow(hgen_mHH_HHrwgt_0, genHH_mass,
		       evtWeight *
		       HHWeight_calc->getWeight("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG));
      if ( apply_HH_rwgt && apply_HH_rwgt_LOtoNLO )
	fillWithOverFlow(hgen_mHH_HHrwgt_LOtoNLOrwgt_0, genHH_mass,
		       evtWeight *
		       HHWeight_calc->getWeight("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG) *
		       HHWeight_calc_LOtoNLO->getReWeight_V2("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG));


 
      fillWithOverFlow(hgen_mHH_1, genHH_mass, evtWeight);
      if ( apply_HH_rwgt_LOtoNLO )
	fillWithOverFlow(hgen_mHH_LOtoNLOrwgt_1, genHH_mass,
		       evtWeight *
		       HHWeight_calc_LOtoNLO->getReWeight_V2("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG));
      if ( apply_HH_rwgt )
	fillWithOverFlow(hgen_mHH_HHrwgt_1, genHH_mass,
		       evtWeight *
		       HHWeight_calc->getWeight("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG));
      if ( apply_HH_rwgt && apply_HH_rwgt_LOtoNLO )
	fillWithOverFlow(hgen_mHH_HHrwgt_LOtoNLOrwgt_1, genHH_mass,
		       evtWeight *
		       HHWeight_calc->getWeight("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG) *
		       HHWeight_calc_LOtoNLO->getReWeight_V2("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG));


 
      fillWithOverFlow(hgen_mHH_2, genHH_mass, evtWeight);
      if ( apply_HH_rwgt_LOtoNLO )
	fillWithOverFlow(hgen_mHH_LOtoNLOrwgt_2, genHH_mass,
		       evtWeight *
		       HHWeight_calc_LOtoNLO->getReWeight_V2("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG));
      if ( apply_HH_rwgt )
	fillWithOverFlow(hgen_mHH_HHrwgt_2, genHH_mass,
		       evtWeight *
		       HHWeight_calc->getReWeight("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG));
      if ( apply_HH_rwgt && apply_HH_rwgt_LOtoNLO )
	fillWithOverFlow(hgen_mHH_HHrwgt_LOtoNLOrwgt_2, genHH_mass,
		       evtWeight *
		       HHWeight_calc->getReWeight("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG) *
		       HHWeight_calc_LOtoNLO->getReWeight_V2("SM", eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG));


      
    }
    
    selHistManager->genKinematics_HH_->fillHistograms(evtWeight*HHReweight);

    selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
    selHistManager->weights_->fillHistograms("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift));
    selHistManager->weights_->fillHistograms("HHReweight_LOtoNLO_V1", HHReweight_LOtoNLO_V1);
    selHistManager->weights_->fillHistograms("HHReweight_LOtoNLO_V2", HHReweight_LOtoNLO_V2);

    lheInfoHistManager->fillHistograms(*lheInfoReader, evtWeight*HHReweight);

    ++analyzedEntries;
    analyzedEntries_weighted += evtWeight*HHReweight;
    histogram_analyzedEntries->Fill(0.); 
  }

  std::cout << "max num. Entries = " << inputTree -> getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree -> getProcessedFileCount() << " file(s) (out of "
            << inputTree -> getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << " (weighted = " << analyzedEntries_weighted << ")\n";

  //divideByBinWidth(histogram_genHH_mass_unweighted);
  //divideByBinWidth(histogram_genHH_mass_reweighted_V1);
  //divideByBinWidth(histogram_genHH_mass_reweighted_V2);

//--- manually write histograms to output file
  fs.file().cd();
  //histogram_analyzedEntries->Write();
  HistManagerBase::writeHistograms();

//--- memory clean-up
  delete lheInfoReader;
  delete psWeightReader;

  delete eventWeightManager;

  delete HHWeight_calc;
  delete HHWeight_calc_LOtoNLO;

  delete inputTree;

  clock.Show("analyze_HHatLOvsNLO");

  return EXIT_SUCCESS;
}
