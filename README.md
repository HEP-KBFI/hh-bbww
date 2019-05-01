# hh-bbww
repository for HH->bbWW analysis

### Setup

```bash
git clone -b master102x https://github.com/HEP-KBFI/hh-bbww               $CMSSW_BASE/src/hhAnalysis/bbww
git clone -b master102x https://github.com/HEP-KBFI/hh-bbww-mem.git       $CMSSW_BASE/src/hhAnalysis/bbwwMEM
git clone -b master102x https://github.com/HEP-KBFI/hh-multilepton        $CMSSW_BASE/src/hhAnalysis/multilepton
git clone               https://github.com/tahuang1991/HeavyMassEstimator $CMSSW_BASE/src/hhAnalysis/Heavymassestimator
git clone -b master102x https://github.com/HEP-KBFI/tth-htt               $CMSSW_BASE/src/tthAnalysis/HiggsToTauTau
git clone               https://github.com/SVfit/ClassicSVfit4tau         $CMSSW_BASE/src/TauAnalysis/ClassicSVfit4tau
git clone               https://github.com/SVfit/ClassicSVfit             $CMSSW_BASE/src/TauAnalysis/ClassicSVfit
git clone               https://github.com/SVfit/SVfitTF                  $CMSSW_BASE/src/TauAnalysis/SVfitTF

curl -s https://raw.githubusercontent.com/cms-hh/HHStatAnalysis/master/install_ana_models.sh | bash -s (in $CMSSW_BASE/src/)
git clone https://github.com/cms-hh/Support.git $CMSSW_BASE/src/Support
```
