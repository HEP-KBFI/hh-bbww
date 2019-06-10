#include "hhAnalysis/bbww/interface/HHWeightInterface.h"
#include "tthAnalysis/HiggsToTauTau/interface/LocalFileInPath.h" // LocalFileInPath
#include <FWCore/Utilities/interface/Exception.h> // cms::Exception

#include <boost/filesystem.hpp> // boost::filesystem::

#include <fstream> // std::ifstream
#include <streambuf> // std::istreambuf_iterator<>()
#include <iostream> // std::cerr, std::fixed

#include "tthAnalysis/HiggsToTauTau/interface/TFileOpenWrapper.h" // TFileOpenWrapper::
#include <TFile.h> // TH1
#include <TH2.h> // TH2

double comp_cosThetaS(const LorentzVector& hadTauP4_lead, const LorentzVector& hadTauP4_sublead)
{
  TLorentzVector hadTauP4tlv_lead;
  hadTauP4tlv_lead.SetPtEtaPhiM(hadTauP4_lead.pt(), hadTauP4_lead.eta(), hadTauP4_lead.phi(), hadTauP4_lead.mass());
  TLorentzVector hadTauP4tlv_sublead;
  hadTauP4tlv_sublead.SetPtEtaPhiM(hadTauP4_sublead.pt(), hadTauP4_sublead.eta(), hadTauP4_sublead.phi(), hadTauP4_sublead.mass());
  TLorentzVector hadTauBoost = hadTauP4tlv_lead + hadTauP4tlv_sublead;
  hadTauP4tlv_lead.Boost(-hadTauBoost.BoostVector());
  return std::fabs(hadTauP4tlv_lead.CosTheta());
}

HHWeightInterface::HHWeightInterface(
  std::vector<double> & BM_klScan, // for the case we want to use to chose an specific BDT
  int & Nscan,
  std::string era,
  bool do_scan,
  bool isDEBUG
)
{
  // AC: limit number of threads running in python to one
  setenv("OMP_NUM_THREADS", "1", 0);
  std::cout << "Entered CX interface " << '\n';

  // read the python file that we're about to execute
  const std::string applicationLoadPath = (
    boost::filesystem::path(std::getenv("CMSSW_BASE")) /
    boost::filesystem::path("src/hhAnalysis/bbww/python/do_weight.py")
  ).string();
  std::ifstream applicationLoadFile(applicationLoadPath);
  std::string applicationLoadStr;

  applicationLoadFile.seekg(0, std::ios::end);
  applicationLoadStr.reserve(applicationLoadFile.tellg());
  applicationLoadFile.seekg(0, std::ios::beg);
  applicationLoadStr.assign(std::istreambuf_iterator<char>(applicationLoadFile), std::istreambuf_iterator<char>());

  // https://ubuntuforums.org/archive/index.php/t-324544.html
  // https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-a-python-script
  // https://gist.github.com/rjzak/5681680
  Py_SetProgramName(const_cast<char *>("do_weight"));
  moduleMainString_ = PyString_FromString("__main__");
  moduleMain_ = PyImport_Import(moduleMainString_);
  PyRun_SimpleString(applicationLoadStr.c_str());

  /////////////////////////////////////////////////////////
  // General: Load the class with the functions to calculate the different parts of the weights
  cms_base = PyString_FromString(std::getenv("CMSSW_BASE"));
  PyObject* func_load = PyObject_GetAttrString(moduleMain_, "load");
  PyObject* args_load = PyTuple_Pack(1, cms_base);
  modeldata_ = PyObject_CallObject(func_load, args_load);
  // function to calculate and return parts of the weights
  func_Weight_ = PyObject_GetAttrString(moduleMain_, "evaluate_weight");
  // This histogram is adapted to our input events -- it is going to be used event-by-event
  // calculated on macros/make_nonres_norm.py
  std::string denominator_hist = "/src/hhAnalysis/bbww/data/denominator_reweighting_bbvv_";
  denominator_hist += era;
  denominator_hist += ".root";
  const std::string FileDenominator = (
    boost::filesystem::path(std::getenv("CMSSW_BASE")) /
    boost::filesystem::path(denominator_hist)
  ).string();
  fileHH = TFileOpenWrapper::Open(FileDenominator.c_str(), "READ");
  if(! fileHH) throw cms::Exception("HHWeightInterface")
    << "Could not open file " << FileDenominator<< " !!\n";
  if(fileHH -> IsZombie()) throw cms::Exception("HHWeightInterface")
    << "The file '" << FileDenominator << "' appears to be a zombie";
  sumEvt = static_cast<TH2 *>(fileHH -> Get(histtitle_.c_str()));
  if(! sumEvt) throw cms::Exception("HHWeightInterface")
    << "The file '" << fileHH << "' does not have a TTree named " << sumEvt;

  ///////////////////////////////////////////////////////////////////
  // Load a file with an specific scan, that we can decide at later stage on the analysis
  // save the closest shape BM to use this value on the evaluation of a BDT
  if ( do_scan )
  {
    std::string applicationLoadPath_klScan = (
      boost::filesystem::path(std::getenv("CMSSW_BASE")) /
      boost::filesystem::path("src/hhAnalysis/bbww/data/kl_scan.dat")
    ).string();

    std::ifstream inFile_kl_scan;
    inFile_kl_scan.open(applicationLoadPath_klScan);
    if (!inFile_kl_scan) throw cms::Exception("HHWeightInterface")
      << "Error opening file for kl scan !!\n";
    double value1;
    int count = 0;
    while (inFile_kl_scan >> value1)
    {
      if ( isDEBUG ) std::cout << " ====================== \n";
      if ( count == 0 ) kl_scan.push_back(value1);
      if ( count == 1 ) kt_scan.push_back(value1);
      //if ( count == 2 ) c2_scan.push_back(value1);
      //if ( count == 3 ) cg_scan.push_back(value1);
      //if ( count == 4 ) c2g_scan.push_back(value1);
      if ( count == 5 ) BM_klScan.push_back(value1); // the closest BM is hardcoded in the scan file intead of calculated in situ

      if ( count == 6 )
      {
        Norm_klScan.push_back(value1);
        count = 0;
      } // the normalization is hardcoded in the scan file intead of calculated in situ
      else {++count;}
    }
    Nscan = Norm_klScan.size();
    if ( isDEBUG )  for (unsigned int bm_list = 0; bm_list < Norm_klScan.size(); bm_list++)
                        {std::cout << "line = "<< bm_list << " kl = " << kl_scan[bm_list] << " ; Norm = " << Norm_klScan[bm_list] << "\n ";}
  }

  Py_XDECREF(func_load);
  Py_XDECREF(args_load);
}

HHWeightInterface::~HHWeightInterface()
{
  Py_XDECREF(modeldata_);
  Py_XDECREF(moduleMainString_);
  Py_XDECREF(moduleMain_);
  Py_XDECREF(moduleMain_);
  Py_XDECREF(func_Weight_);
}

void
HHWeightInterface::operator()(
  const double & mhh_gen,
  const double & costSgen_gen,
  //
  std::vector<double> & WeightBM,
  std::vector<double> & Weight_klScan,
  bool isDEBUG
) const
{
  setenv("OMP_NUM_THREADS", "1", 0);
  // this info could also be on the post-production stage
  double denominator = sumEvt->GetBinContent(sumEvt->GetXaxis()->FindBin(mhh_gen), sumEvt->GetYaxis()->FindBin(std::abs(costSgen_gen)));

  /////////////////////////////////////////////////////////
  // This can be calculated at post-production stage
  for (unsigned int bm_list = 0; bm_list < 13; bm_list++){
    PyObject* args_BM_list = PyTuple_Pack(10,
      PyFloat_FromDouble(static_cast<double>(klJHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(ktJHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(c2JHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(cgJHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(c2gJHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(mhh_gen)),
      PyFloat_FromDouble(static_cast<double>(costSgen_gen)),
      PyFloat_FromDouble(static_cast<double>(normJHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(denominator)),
      modeldata_);
    WeightBM.push_back(
      PyFloat_AsDouble(PyObject_CallObject(func_Weight_, args_BM_list))
    );
    Py_XDECREF(args_BM_list);
  }
  if ( isDEBUG ) for (unsigned int bm_list = 0; bm_list < WeightBM.size(); bm_list++)
  {std::cout << bm_list << " " <<  WeightBM[bm_list] << " " << denominator << "\n";}

  ///////////////////////////////////////////////////////////////////
  // This part is for any scan that we can decide at later stage on the analysis
  for (unsigned int scan_list = 0; scan_list < Norm_klScan.size(); scan_list++)
  {
      PyObject* args_kl_scan_list = PyTuple_Pack(10,
        PyFloat_FromDouble(static_cast<double>(kl_scan[scan_list])),
        PyFloat_FromDouble(static_cast<double>(kt_scan[scan_list])),
        PyFloat_FromDouble(static_cast<double>(0.0)),
        PyFloat_FromDouble(static_cast<double>(0.0)),
        PyFloat_FromDouble(static_cast<double>(0.0)),
        PyFloat_FromDouble(static_cast<double>(mhh_gen)),
        PyFloat_FromDouble(static_cast<double>(costSgen_gen)),
        PyFloat_FromDouble(static_cast<double>(Norm_klScan[scan_list])),
        PyFloat_FromDouble(static_cast<double>(denominator)),
        modeldata_);
      Weight_klScan.push_back(
        PyFloat_AsDouble(PyObject_CallObject(func_Weight_, args_kl_scan_list))
      );
      Py_XDECREF(args_kl_scan_list);
  }

}
