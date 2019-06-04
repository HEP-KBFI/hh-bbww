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
  double
  operator()(
    const double & mhh_gen,
    const double & costSgen_gen,
    //
    std::vector<double> & WeightBM,
    std::vector<double> & Weight_klScan
  ) const;

private:
  //std::string mvaFileName_;

  //std::vector<std::string> mvaInputVariables_; // list of MVA input variables
  PyObject* modeldata_;
  PyObject* moduleMainString_;
  PyObject* moduleMain_;
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

  std::string applicationLoadPath_klScan;

  std::vector<double> NormBM;
  std::vector<double> Norm_klScan;
  double Norm = 1.0;

  TFile * fileHH;
  TH2 * sumEvt;
  const std::string histtitle_ = "denominator_reweighting";

};

#endif // HHWeightInterface_h
