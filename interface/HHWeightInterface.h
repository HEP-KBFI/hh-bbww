#ifndef hhAnalysis_bbww_HHWeightInterface_h
#define hhAnalysis_bbww_HHWeightInterface_h

#include <Python.h> // PyObject
#include <vector> // std::vector<>
#include <string> // std::string
#include <map> // std::map<,>

#include <Math/LorentzVector.h>
#include <Math/PtEtaPhiM4D.h>
typedef ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<double> > LorentzVector;
#include <TLorentzVector.h> // TLorentzVector
#include <fstream> // std::ifstream

#include <TFile.h> // TH1
#include <TH2.h> // TH2

double comp_cosThetaS(const LorentzVector& hadTauP4_lead, const LorentzVector& hadTauP4_sublead);

class HHWeightInterface
{
public:
  HHWeightInterface(
              std::vector<double> & BM_klScan,
              int & Nscan,
              std::string era,
              bool isDEBUG
             );
  ~HHWeightInterface();

  /**
   * @brief Calculates MVA output.
   * @param mvaInputs Values of MVA input variables (stored in std::map with key = MVA input variable name)
   * @return          MVA output
   */
  void
  operator()(
    const double & mhh_gen,
    const double & costSgen_gen,
    //
    std::vector<double> & WeightBM,
    std::vector<double> & WeightBMp,
    std::vector<double> & Weight_klScan,
    bool isDEBUG
  ) const;

private:
  //std::string mvaFileName_;

  //std::vector<std::string> mvaInputVariables_; // list of MVA input variables
  PyObject* modeldata_;
  PyObject* moduleMainString_;
  PyObject* moduleMain_;
  PyObject* func_Weight_;
  PyObject* cms_base;

  // any point can be chosen here
  const double kl = 1.0;
  const double kt = 1.0;
  const double c2 = 0.0;
  const double cg = 0.0;
  const double c2g = 0.0;

  const double klJHEP[13]  = {1.0,  7.5,  1.0,  1.0,  -3.5, 1.0, 2.4, 5.0, 15.0, 1.0, 10.0, 2.4, 15.0};
  const double ktJHEP[13]  = {1.0,  1.0,  1.0,  1.0,  1.5,  1.0, 1.0, 1.0, 1.0,  1.0, 1.5,  1.0, 1.0};
  const double c2JHEP[13]  = {0.0,  -1.0, 0.5, -1.5, -3.0,  0.0, 0.0, 0.0, 0.0,  1.0, -1.0, 0.0, 1.0};
  const double cgJHEP[13]  = {0.0,  0.0, -0.8,  0.0, 0.0,   0.8, 0.2, 0.2, -1.0, -0.6, 0.0, 1.0, 0.0};
  const double c2gJHEP[13] = {0.0, 0.0, 0.6, -0.8, 0.0, -1.0, -0.2,-0.2,  1.0,  0.6, 0.0, -1.0, 0.0};
  const double normJHEP[13] = {0.99997, 0.94266, 0.71436, 0.95608, 0.97897, 0.87823, 0.95781, 1.00669, 0.92494, 0.86083, 1.00658, 0.95096, 1.00063};
  const double norm_2017MC_BM[13] = {0.96923, 0.92239, 0.81805, 0.96286, 0.97893, 0.96260, 0.92272, 0.97476, 0.92495, 0.82462, 0.99226, 0.92999, 1.00169};

  std::vector<double> Norm_klScan;
  std::vector<double> kl_scan;
  std::vector<double> kt_scan;
  std::vector<double> c2_scan;
  std::vector<double> cg_scan;
  std::vector<double> c2g_scan;

  TFile * fileHH;
  TH2 * sumEvt;
  const std::string histtitle_ = "denominator_reweighting";

};

#endif // HHWeightInterface_h
