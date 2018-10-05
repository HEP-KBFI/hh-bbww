#ifndef hhAnalysis_bbww_RecoJetCollectionSelectorAK8_bbWW_Wjj_h
#define hhAnalysis_bbww_RecoJetCollectionSelectorAK8_bbWW_Wjj_h

#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionSelector.h" // ParticleCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector

class RecoJetSelectorAK8_bbWW_Wjj
{
public:
  explicit RecoJetSelectorAK8_bbWW_Wjj(int era, int index = -1, bool debug = false);
  ~RecoJetSelectorAK8_bbWW_Wjj() {}

  /**
   * @brief Set cut thresholds
   */
  void set_min_pt(double min_pt);
  void set_max_absEta(double max_absEta);
  void set_min_msoftdrop(double min_msoftdrop);
  void set_max_msoftdrop(double max_msoftdrop);
  void set_max_tau2_div_tau1(double max_tau2_div_tau1);
  void set_max_mD(double max_mD);
  void set_max_dR_lepton(double max_dR_lepton);
  void set_min_subJet1_pt(double min_pt);
  void set_max_subJet1_absEta(double max_absEta);
  void set_min_subJet2_pt(double min_pt);
  void set_max_subJet2_absEta(double max_absEta);
  void set_min_jetId(int min_jetId);

  void set_lepton(const RecoLepton* lepton);
  void set_neutrinoP4(const Particle::LorentzVector& neutrinoP4);

  /**
   * @brief Get cut thresholds
   */
  double get_min_pt() const;
  double get_max_absEta() const;
  double get_min_msoftdrop() const;
  double get_max_msoftdrop() const;
  double get_max_tau2_div_tau1() const;
  double get_max_mD() const;
  double get_max_dR_lepton() const;
  double get_min_subJet1_pt() const;
  double get_max_subJet1_absEta() const;
  double get_min_subJet2_pt() const;
  double get_max_subJet2_absEta() const;
  int get_min_jetId() const;

  /**
   * @brief Check if jet given as function argument passes pT and eta cuts (pT > 25 GeV and |eta| < 2.4, cf. Section 3.1 of AN-2015/321)
   * @return True if jet passes selection; false otherwise
   */
  bool
  operator()(const RecoJetAK8 & jet) const;

protected:
  Double_t min_pt_;                    ///< lower cut threshold on pT of "fat" (AK8) jet
  Double_t max_absEta_;                ///< upper cut threshold on absolute value of eta of "fat" (AK8) jet
  Int_t min_jetId_;                    ///< lower cut threshold on jet ID value 
  Double_t min_msoftdrop_;             ///< lower cut threshold on mass of the two subjets
  Double_t max_msoftdrop_;             ///< upper cut threshold on mass of the two subjets
  Double_t max_tau2_div_tau1_;         ///< upper cut threshold on value of N-subjettiness ratio tau2/tau1
  Double_t max_mD_;                    ///< upper cut threshold on value of mD variable, defined by Eq.(3) in AN-2018/058 (v4)
  Double_t max_dR_lepton_;             ///< upper cut threshold on distance between "fat" (AK8) jet and electron or muon
  Double_t min_subJet1_pt_;            ///< lower cut threshold on pT of first subjet
  Double_t max_subJet1_absEta_;        ///< upper cut threshold on absolute value of eta of first subjet
  Double_t min_subJet2_pt_;            ///< lower cut threshold on pT of second subjet
  Double_t max_subJet2_absEta_;        ///< upper cut threshold on absolute value of eta of second subjet

  const RecoLepton* lepton_;	       ///< pointer to electron or muon produced in H->WW*->jj lnu decay
  Particle::LorentzVector neutrinoP4_; ///< four-vector of neutrino produced in H->WW*->jj lnu decay, reconstructed as described in Section 3.4.2 of AN-2018/058 (v4)
  
  bool debug_;
};

typedef ParticleCollectionSelector<RecoJetAK8, RecoJetSelectorAK8_bbWW_Wjj> RecoJetCollectionSelectorAK8_bbWW_Wjj;

#endif // hhAnalysis_bbww_RecoJetCollectionSelectorAK8_bbWW_Wjj_h
