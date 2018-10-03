#ifndef hhAnalysis_bbww_RecoJetCollectionSelectorAK8_bbWW_Hbb_h
#define hhAnalysis_bbww_RecoJetCollectionSelectorAK8_bbWW_Hbb_h

#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionSelector.h" // ParticleCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJet

class RecoJetSelectorAK8_bbWW_Hbb
{
public:
  explicit RecoJetSelectorAK8_bbWW_Hbb(int era,
                           int index = -1,
                           bool debug = false);
  ~RecoJetSelectorAK8_bbWW_Hbb() {}

  /**
   * @brief Set cut thresholds
   */
  void set_min_pt(double min_pt);
  void set_max_absEta(double max_absEta);
  void set_min_msoftdrop(double min_msoftdrop);
  void set_max_msoftdrop(double max_msoftdrop);
  void set_max_tau2_div_tau1(double max_tau2_div_tau1);
  void set_min_subjet1_pt(double min_pt);
  void set_max_subjet1_absEta(double max_absEta);
  void set_min_subjet1_BtagCSV(double min_BtagCSV);
  void set_min_subjet2_pt(double min_pt);
  void set_max_subjet2_absEta(double max_absEta);
  void set_min_subjet2_BtagCSV(double min_BtagCSV);
  void set_min_jetId(int min_jetId);

  /**
   * @brief Get cut thresholds
   */
  double get_min_pt() const;
  double get_max_absEta() const;
  double get_min_msoftdrop() const;
  double get_max_msoftdrop() const;
  double get_max_tau2_div_tau1() const;
  double get_min_subjet1_pt() const;
  double get_max_subjet1_absEta() const;
  double get_min_subjet1_BtagCSV() const;
  double get_min_subjet2_pt() const;
  double get_max_subjet2_absEta() const;
  double get_min_subjet2_BtagCSV() const;
  int get_min_jetId() const;

  /**
   * @brief Check if jet given as function argument passes pT and eta cuts (pT > 25 GeV and |eta| < 2.4, cf. Section 3.1 of AN-2015/321)
   * @return True if jet passes selection; false otherwise
   */
  bool
  operator()(const RecoJetAK8 & jet) const;

protected:
  Double_t min_pt_;              ///< lower cut threshold on pT of "fat" (AK8) jet
  Double_t max_absEta_;          ///< upper cut threshold on absolute value of eta of "fat" (AK8) jet
  Int_t min_jetId_;              ///< lower cut threshold on jet ID value 
  Double_t min_msoftdrop_;       ///< lower cut threshold on mass of the two subjets
  Double_t max_msoftdrop_;       ///< upper cut threshold on mass of the two subjets
  Double_t max_tau2_div_tau1_;   ///< upper cut threshold on value of N-subjettiness ratio tau2/tau1
  Double_t min_subjet1_pt_;      ///< lower cut threshold on pT of first subjet
  Double_t max_subjet1_absEta_;  ///< upper cut threshold on absolute value of eta of first subjet
  Double_t min_subjet1_BtagCSV_; ///< lower cut threshold on CSV b-tagging discriminator value of first subjet
  Double_t min_subjet2_pt_;      ///< lower cut threshold on pT of second subjet
  Double_t max_subjet2_absEta_;  ///< upper cut threshold on absolute value of eta of second subjet
  Double_t min_subjet2_BtagCSV_; ///< lower cut threshold on CSV b-tagging discriminator value of second subjet
  bool debug_;
};

typedef ParticleCollectionSelector<RecoJetAK8, RecoJetSelectorAK8_bbWW_Hbb> RecoJetCollectionSelectorAK8_bbWW_Hbb;

#endif // hhAnalysis_bbww_RecoJetCollectionSelectorAK8_bbWW_Hbb_h
