#ifndef hhAnalysis_bbww_JPAInterface_h
#define hhAnalysis_bbww_JPAInterface_h

#include <DataFormats/Math/interface/LorentzVector.h> // math::PtEtaPhiMLorentzVector

#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface

#include <vector> // std::vector
#include <string> // std::string
#include <map>    // std::map

class JPAJet;

class JPA
{
 public:
  typedef math::PtEtaPhiMLorentzVector LorentzVector;
  enum class Category_resolved { kUndefined = 0, k2b2W = 1, k2b1W = 2, k2b0W = 3, k1b2W = 4, k1b1W = 5, k1b0W = 6, k0b0to2W = 7 };
  enum class Category_boosted { kUndefined = 0, k2b2W = 11, k2b1W = 12, k2b0W = 13 };
  JPA(const JPAJet* bjet1, const JPAJet* bjet2, const JPAJet* wjet1, const JPAJet* wjet2, double jpaScore, int jpaCategory, bool isBoosted)
    : bjet1_(bjet1)
    , bjet2_(bjet2)
    , wjet1_(bjet1)
    , wjet2_(bjet2)
    , jpaScore_(jpaScore)
    , jpaCategory_(jpaCategory)
    , isBoosted_(isBoosted)
  {}
  ~JPA() {}
  const JPAJet* bjet1() const { return bjet1_; }
  const JPAJet* bjet2() const { return bjet2_; }
  const JPAJet* wjet1() const { return wjet1_; }
  const JPAJet* wjet2() const { return wjet2_; }
  double jpaScore() const { return jpaScore_; }
  int jpaCategory() const { return jpaCategory_; }
 private:
  const JPAJet* bjet1_;
  const JPAJet* bjet2_;
  const JPAJet* wjet1_;
  const JPAJet* wjet2_;
  double jpaScore_;
  int jpaCategory_;
  bool isBoosted_;
};

class JPAJet
{
 public:
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
 private:
  JPA::LorentzVector p4_;
  JPA::LorentzVector p4_reg_;
  double BtagCSV_;
  double QGDiscr_;
};

class JPAInterface
{
 public:
  JPAInterface(const std::string& mvaInputFilePath);
  ~JPAInterface();

  JPA
  operator()(const std::vector<JPAJet>& ak4Jets, 
             const JPA::LorentzVector& leptonP4, int numLeptons, int numJets, int numBJets_loose, int numBJets_medium, double metPx, double metPy, 
             int event_number);
  JPA
  operator()(const std::vector<JPAJet>& ak4Jets, const JPAJet& ak8jet_subjet1, const JPAJet& ak8jet_subjet2, 
             const JPA::LorentzVector& leptonP4, int numLeptons, int numJets, int numBJets_loose, int numBJets_medium, double metPx, double metPy, 
             int event_number);

  double jpaScore(int jpaCategory) const;
 private:
  void
  set(const JPA::LorentzVector& leptonP4, int numLeptons, int numJets, int numBJets_loose, int numBJets_medium, double metPx, double metPy, int event_number);
  
  std::map<std::string, double>
  compMVAInputVariables(const JPAJet* bjet1, const JPAJet* bjet2, const JPAJet* wjet1, const JPAJet* wjet2);

  std::vector<JPA> 
  makeJPAs_resolved(const std::vector<const JPAJet*>& ak4Jets, int jpaCategory);
  std::vector<JPA> 
  makeJPAs_boosted(const std::vector<const JPAJet*>& ak4Jets, const JPAJet* ak8jet_subjet1, const JPAJet* ak8jet_subjet2, int jpaCategory);

  std::string mvaInputFilePath_;

  std::map<int, std::vector<JPA>> jpas_;

  std::map<int, std::string> mvaInputFileNames_1stLayer_even_;
  std::map<int, std::string> mvaInputFileNames_1stLayer_odd_;
  std::map<int, std::vector<std::string>> mvaInputVariables_1stLayer_;
  std::map<int, TMVAInterface*> mvas_1stLayer_;
  std::map<int, double> mvaOutputs_1stLayer_;

  enum { kResolved, kBoosted };
  std::map<int, std::string> mvaInputFileNames_2ndLayer_even_;
  std::map<int, std::string> mvaInputFileNames_2ndLayer_odd_;
  std::map<int, std::vector<std::string>> mvaInputVariables_2ndLayer_;
  std::map<int, TMVAInterface*> mvas_2ndLayer_;
  std::map<int, double> mvaOutput_2ndLayer_;

  JPA::LorentzVector leptonP4_;
  int numLeptons_;
  int numJets_;
  int numBJets_loose_;
  int numBJets_medium_;
  double metPx_;
  double metPy_;
  int event_number_;
};

#endif
