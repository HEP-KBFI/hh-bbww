#ifndef hhAnalysis_bbww_JPAInterface_h
#define hhAnalysis_bbww_JPAInterface_h

#include <DataFormats/Math/interface/LorentzVector.h> // math::PtEtaPhiMLorentzVector

#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface

#include <vector> // std::vector
#include <string> // std::string
#include <map>    // std::map

class JPAJet;
std::ostream& operator<<(std::ostream&, const JPAJet&);

std::string get_jpaCategory_string(int jpaCategory);
std::vector<std::string> get_jpaInputs(int jpaCategory);

class JPA
{
 public:
  typedef math::PtEtaPhiMLorentzVector LorentzVector;
  enum class Category_resolved { kUndefined = 0, k2b2W = 1, k2b1W = 2, k2b0W = 3, k1b2W = 4, k1b1W = 5, k1b0W = 6, k0b = 7 };
  enum class Category_boosted { kUndefined = 0, k2b2W = 11, k2b1W = 12, k2b0W = 13 };
  enum { kResolved, kBoosted };
  JPA()
    : bjet1_(nullptr)
    , bjet2_(nullptr)
    , wjet1_(nullptr)
    , wjet2_(nullptr)
    , jpaScore_(-1.)
    , jpaCategory_((int)Category_resolved::kUndefined)
    , isBoosted_(false)
  {}
  JPA(const JPAJet* bjet1,
      const JPAJet* bjet2,
      const JPAJet* wjet1,
      const JPAJet* wjet2,
      double jpaScore,
      int jpaCategory,
      bool isBoosted,
      std::map<std::string, double> mvaInputVars)
    : bjet1_(bjet1)
    , bjet2_(bjet2)
    , wjet1_(wjet1)
    , wjet2_(wjet2)
    , jpaScore_(jpaScore)
    , jpaCategory_(jpaCategory)
    , isBoosted_(isBoosted)
    , mvaInputVars_(mvaInputVars)
  {}
  ~JPA() {}

  const JPAJet* bjet1() const { return bjet1_; }
  const JPAJet* bjet2() const { return bjet2_; }
  const JPAJet* wjet1() const { return wjet1_; }
  const JPAJet* wjet2() const { return wjet2_; }

  double jpaScore() const { return jpaScore_; }
  int jpaCategory() const { return jpaCategory_; }
  std::string jpaCategory_string() const 
  { 
    return get_jpaCategory_string(jpaCategory_);
  }
  bool isBoosted() const { return isBoosted_; }
  std::map<std::string, double> mvaInputVars() const { return mvaInputVars_; }

  friend std::ostream&
  operator<<(std::ostream& os, const JPA& jpa)
  {
    os << "bjet1:";
    if ( jpa.bjet1() ) os << " " << (*jpa.bjet1()) << std::endl;
    else os << " N/A" << std::endl;
    os << "bjet2:";
    if ( jpa.bjet2() ) os << " " << (*jpa.bjet2()) << std::endl;
    else os << " N/A" << std::endl;
    os << "wjet1:";
    if ( jpa.wjet1() ) os << " " << (*jpa.wjet1()) << std::endl;
    else os << " N/A" << std::endl;
    os << "wjet2:";
    if ( jpa.wjet2() ) os << " " << (*jpa.wjet2()) << std::endl;
    else os << " N/A" << std::endl;
    os << "category = " << jpa.jpaCategory_string() << ": score = " << jpa.jpaScore() << std::endl;
    return os;
  }
 private:
  const JPAJet* bjet1_;
  const JPAJet* bjet2_;
  const JPAJet* wjet1_;
  const JPAJet* wjet2_;
  double jpaScore_;
  int jpaCategory_;
  bool isBoosted_;
  std::map<std::string, double> mvaInputVars_;
};

class JPAJet
{
 public:
  JPAJet()
    : BtagCSV_(-1.)
    , QGDiscr_(-1.)
  {}
  JPAJet(const JPA::LorentzVector& p4, const JPA::LorentzVector& p4_reg, double BtagCSV, double QGDiscr)
    : p4_(p4)
    , p4_reg_(p4_reg)
    , BtagCSV_(BtagCSV)
    , QGDiscr_(QGDiscr)
  {}
  ~JPAJet() {}

  const JPA::LorentzVector& p4() const { return p4_; }
  const JPA::LorentzVector& p4_reg() const { return p4_reg_; }
  double BtagCSV() const { return BtagCSV_; }
  double QGDiscr() const { return QGDiscr_; }

  friend std::ostream&
  operator<<(std::ostream& os, const JPAJet& jet)
  {
    os << "pT = " << jet.p4().pt() << ", eta = " << jet.p4().eta() << ", phi = " << jet.p4().phi() << "," 
       << " btagCSV = " << jet.BtagCSV() << ", qgDiscr = " << jet.QGDiscr();
    return os;
  }
 private:
  JPA::LorentzVector p4_;
  JPA::LorentzVector p4_reg_;
  double BtagCSV_;
  double QGDiscr_;
};

class JPAInterface
{
 public:
  JPAInterface(const std::string& mvaInputFilePath, const std::string era, bool isDEBUG = false);
  ~JPAInterface();

  JPA
  operator()(const std::vector<JPAJet>& ak4Jets, 
             const JPA::LorentzVector& leptonP4, int numLeptons, int numJets, int numBJets_loose, int numBJets_medium, double metPx, double metPy, 
             int event_number);
  JPA
  operator()(const std::vector<JPAJet>& ak4Jets, const JPAJet& ak8jet_subjet1, const JPAJet& ak8jet_subjet2, 
             const JPA::LorentzVector& leptonP4, int numLeptons, int numJets, int numBJets_loose, int numBJets_medium, double metPx, double metPy, 
             int event_number);

  // CV: auxiliary functions for debugging (and for training of 2ndLayer BDT)
  double 
  mvaOutput_1stLayer(int jpaCategory) const;
  double 
  mvaOutput_2ndLayer(int jpaCategory) const;

  std::map<std::string, double>
  get_mvaInputs_1stLayer(int jpaCategory) const;
  int getevtCat() const;
 private:
  void
  set(const JPA::LorentzVector& leptonP4, int numLeptons, int numJets, int numBJets_loose, int numBJets_medium, double metPx, double metPy, int event_number);
  
  void
  reset_mvaOutputs();

  void
    reset_mva2ndOutput();

  std::map<std::string, double>
  compMVAInputVariables(const JPAJet* bjet1, const JPAJet* bjet2, const JPAJet* wjet1, const JPAJet* wjet2);

  std::vector<JPA>
  makeJPAs_resolved(const std::vector<const JPAJet*>& ak4Jets, int jpaCategory);
  std::vector<JPA>
  makeJPAs_boosted(const std::vector<const JPAJet*>& ak4Jets, const JPAJet* ak8jet_subjet1, const JPAJet* ak8jet_subjet2, int jpaCategory);

  std::map<std::string, double>
  select_mvaInputVariables(const std::map<std::string, double> & mvaInputVariables, int jpaCategory) const;

  std::string mvaInputFilePath_;

  // CV: the JPAInterface class needs to keep an internal copy of the jets passed to JPAInterface::operator(),
  //     in order to prevent the jet pointers stored in the JPA class to become invalid
  //    (which would be the case of the jets passed to JPAInterface::operator() leave scope, 
  //     while the JPA object returned by the call to JPAInterface::operator() is still being used by the analyze_hh_bb1l.cc code)
  std::vector<JPAJet> ak4Jets_;
  JPAJet ak8jet_subjet1_;
  JPAJet ak8jet_subjet2_;

  std::map<int, std::vector<JPA>> jpas_;

  std::map<int, std::string> mvaInputFileNames_1stLayer_even_;
  std::map<int, std::string> mvaInputFileNames_1stLayer_odd_;
  std::map<int, std::vector<std::string>> mvaInputVariables_1stLayer_;
  std::map<int, std::map<std::string, double>> mvaInputVariableValues_1stLayer_;
  std::map<int, TMVAInterface*> mvas_1stLayer_;
  std::map<int, double> mvaOutputs_1stLayer_;

  std::map<int, std::string> mvaInputFileNames_2ndLayer_even_;
  std::map<int, std::string> mvaInputFileNames_2ndLayer_odd_;
  std::map<int, std::vector<std::string>> mvaInputVariables_2ndLayer_;
  std::map<int, TMVAInterface*> mvas_2ndLayer_;
  std::map<int, double> mvaOutputs_2ndLayer_;

  JPA::LorentzVector leptonP4_;
  int numLeptons_;
  int numJets_;
  int numBJets_loose_;
  int numBJets_medium_;
  double metPx_;
  double metPy_;
  int event_number_;

  bool isDEBUG_;
  int mvaOutput_2ndLayer_;
};

#endif
