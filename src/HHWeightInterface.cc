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
  TLorentzVector hadTauBoost = hadTauP4tlv_lead;
  return std::fabs(hadTauBoost.CosTheta());
}

HHWeightInterface::HHWeightInterface(
  std::vector<double> & BM_klScan, // for the case we want to use to chose an specific BDT
  int & Nscan,
  const int era,
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

  // Load the class
  cms_base = PyString_FromString(std::getenv("CMSSW_BASE"));
  PyObject* func_load = PyObject_GetAttrString(moduleMain_, "load");
  PyObject* args_load = PyTuple_Pack(1, cms_base);
  modeldata_ = PyObject_CallObject(func_load, args_load);

  PyObject * kl_py = PyFloat_FromDouble(static_cast<double>(kl));
  PyObject * kt_py = PyFloat_FromDouble(static_cast<double>(kt));
  PyObject * c2_py = PyFloat_FromDouble(static_cast<double>(c2));
  PyObject * cg_py = PyFloat_FromDouble(static_cast<double>(cg));
  PyObject * c2g_py = PyFloat_FromDouble(static_cast<double>(c2g));

  // calculate and return normalization
  PyObject* args_Norm = PyTuple_Pack(7,  kl_py, kt_py, c2_py, cg_py, c2g_py, modeldata_, cms_base);
  PyObject* func_Norm = PyObject_GetAttrString(moduleMain_, "getNorm");
  Norm   = PyFloat_AsDouble(PyObject_CallObject(func_Norm, args_Norm));

  for (unsigned int bm_list = 0; bm_list < 13; bm_list++){
    PyObject* args_BM_list = PyTuple_Pack(7,
      PyFloat_FromDouble(static_cast<double>(klJHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(ktJHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(c2JHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(cgJHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(c2gJHEP[bm_list])),
      modeldata_, cms_base);
    NormBM.push_back(PyFloat_AsDouble(PyObject_CallObject(func_Norm, args_BM_list)));
    Py_XDECREF(args_BM_list);
  }

  applicationLoadPath_klScan = (
    boost::filesystem::path(std::getenv("CMSSW_BASE")) /
    boost::filesystem::path("src/hhAnalysis/bbww/data/kl_scan.dat")
  ).string();

  std::ifstream inFile_kl_scan;
  inFile_kl_scan.open(applicationLoadPath_klScan);
  if (!inFile_kl_scan) throw cms::Exception("HHWeightInterface")
    << "Error opening file for kl scan !!\n";
  double value1;
  int count = 0;
  double kl_scan = 1.0;
  double kt_scan = 1.0;
  double c2_scan = 1.0;
  double cg_scan = 1.0;
  double c2g_scan = 1.0;
  while (inFile_kl_scan >> value1)
  {
    if ( isDEBUG ) std::cout << " " << value1;
    if ( count == 0 ) kl_scan = value1;
    if ( count == 1 ) kt_scan = value1;
    if ( count == 2 ) c2_scan = value1;
    if ( count == 3 ) cg_scan = value1;
    if ( count == 4 ) c2g_scan = value1;
    if ( count == 5 )
    {
      BM_klScan.push_back(value1);
      PyObject* args_norm_kl = PyTuple_Pack(7,
        PyFloat_FromDouble(static_cast<double>(kl_scan)),
        PyFloat_FromDouble(static_cast<double>(kt_scan)),
        PyFloat_FromDouble(static_cast<double>(c2_scan)),
        PyFloat_FromDouble(static_cast<double>(cg_scan)),
        PyFloat_FromDouble(static_cast<double>(c2g_scan)),
        modeldata_, cms_base);
      if ( isDEBUG ) std::cout << " (kl = "<< kl_scan << ")\n";
      Norm_klScan.push_back(PyFloat_AsDouble(PyObject_CallObject(func_Norm, args_norm_kl)));
      count = 0;
      Py_XDECREF(args_norm_kl);
    }
    else {++count;}
  }
  Nscan = Norm_klScan.size();

  // this histogram bellow should be adapted to our input events
  std::string denominator_hist = "/src/hhAnalysis/bbww/data/denominator_reweighting_";
  denominator_hist += std::to_string(era);
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

  Py_XDECREF(args_Norm);
  Py_XDECREF(func_Norm);

  Py_XDECREF(kl_py);
  Py_XDECREF(kt_py);
  Py_XDECREF(c2_py);
  Py_XDECREF(cg_py);
  Py_XDECREF(c2g_py);

  Py_XDECREF(func_load);
  Py_XDECREF(args_load);
}

HHWeightInterface::~HHWeightInterface()
{
  Py_XDECREF(modeldata_);
  Py_XDECREF(moduleMainString_);
  Py_XDECREF(moduleMain_);
}

double
HHWeightInterface::operator()(
  const double & mhh_gen,
  const double & costSgen_gen,
  //
  std::vector<double> & WeightBM,
  std::vector<double> & Weight_klScan
) const
{

  double denominator = sumEvt->GetBinContent(sumEvt->GetXaxis()->FindBin(mhh_gen), sumEvt->GetYaxis()->FindBin(std::abs(costSgen_gen)));

  PyObject* func_Weight = PyObject_GetAttrString(moduleMain_, "evaluate_weight");
  PyObject* args_Weight = PyTuple_Pack(11,
    PyFloat_FromDouble(static_cast<double>(kl)),
    PyFloat_FromDouble(static_cast<double>(kt)),
    PyFloat_FromDouble(static_cast<double>(c2)),
    PyFloat_FromDouble(static_cast<double>(cg)),
    PyFloat_FromDouble(static_cast<double>(c2g)),
    PyFloat_FromDouble(static_cast<double>(mhh_gen)),
    PyFloat_FromDouble(static_cast<double>(costSgen_gen)),
    PyFloat_FromDouble(static_cast<double>(Norm)),
    PyFloat_FromDouble(static_cast<double>(denominator)),
    cms_base, modeldata_
  );
  PyObject* Weightpy = PyObject_CallObject(func_Weight, args_Weight);
  double HHWeight   = PyFloat_AsDouble(Weightpy);

  for (unsigned int bm_list = 0; bm_list < 13; bm_list++){
    PyObject* args_BM_list = PyTuple_Pack(10,
      PyFloat_FromDouble(static_cast<double>(klJHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(ktJHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(c2JHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(cgJHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(c2gJHEP[bm_list])),
      PyFloat_FromDouble(static_cast<double>(mhh_gen)),
      PyFloat_FromDouble(static_cast<double>(costSgen_gen)),
      PyFloat_FromDouble(static_cast<double>(NormBM[bm_list])),
      cms_base, modeldata_);
    WeightBM.push_back(
      PyFloat_AsDouble(PyObject_CallObject(func_Weight, args_BM_list))
    );
    Py_XDECREF(args_BM_list);
  }

  std::ifstream inFile_kl_scan;
  inFile_kl_scan.open(applicationLoadPath_klScan);
  if (!inFile_kl_scan) throw cms::Exception("HHWeightInterface")
    << "Error opening file for kl scan !!\n";
  double value1;
  int count = 0;
  int countNorm = 0;
  double kl_scan = 1.0;
  while (inFile_kl_scan >> value1)
  {
    if ( count == 0 ) kl_scan = value1;
    if ( count == 5 )
    {
      PyObject* args_kl_scan_list = PyTuple_Pack(10,
        PyFloat_FromDouble(static_cast<double>(kl_scan)),
        PyFloat_FromDouble(static_cast<double>(1.0)),
        PyFloat_FromDouble(static_cast<double>(0.0)),
        PyFloat_FromDouble(static_cast<double>(0.0)),
        PyFloat_FromDouble(static_cast<double>(0.0)),
        PyFloat_FromDouble(static_cast<double>(mhh_gen)),
        PyFloat_FromDouble(static_cast<double>(costSgen_gen)),
        PyFloat_FromDouble(static_cast<double>(Norm_klScan[countNorm])),
        cms_base, modeldata_);
      Weight_klScan.push_back(
        PyFloat_AsDouble(PyObject_CallObject(func_Weight, args_kl_scan_list))
      );
      Py_XDECREF(args_kl_scan_list);
      count = 0;
    }
    else {++count;}
    ++countNorm;
  }

  return HHWeight;
}
