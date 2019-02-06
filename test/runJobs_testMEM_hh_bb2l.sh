#!/bin/bash

rm -rf testMEM_hh_bb2l_signal_genMatchOpt1_cfg.py
sed 's/$PROCESS/signal/ ; s/$GENMATCHINGOPTION/1/' templates/testMEM_hh_bb2l_cfg.py > testMEM_hh_bb2l_signal_genMatchOpt1_cfg.py
rm -rf testMEM_hh_bb2l_signal_genMatchOpt2_cfg.py
sed 's/$PROCESS/signal/ ; s/$GENMATCHINGOPTION/2/' templates/testMEM_hh_bb2l_cfg.py > testMEM_hh_bb2l_signal_genMatchOpt2_cfg.py
rm -rf testMEM_hh_bb2l_signal_genMatchOpt3_cfg.py
sed 's/$PROCESS/signal/ ; s/$GENMATCHINGOPTION/3/' templates/testMEM_hh_bb2l_cfg.py > testMEM_hh_bb2l_signal_genMatchOpt3_cfg.py

rm -rf testMEM_hh_bb2l_background_genMatchOpt1_cfg.py
sed 's/$PROCESS/background/ ; s/$GENMATCHINGOPTION/1/' templates/testMEM_hh_bb2l_cfg.py > testMEM_hh_bb2l_background_genMatchOpt1_cfg.py
rm -rf testMEM_hh_bb2l_background_genMatchOpt2_cfg.py
sed 's/$PROCESS/background/ ; s/$GENMATCHINGOPTION/2/' templates/testMEM_hh_bb2l_cfg.py > testMEM_hh_bb2l_background_genMatchOpt2_cfg.py
rm -rf testMEM_hh_bb2l_background_genMatchOpt3_cfg.py
sed 's/$PROCESS/background/ ; s/$GENMATCHINGOPTION/3/' templates/testMEM_hh_bb2l_cfg.py > testMEM_hh_bb2l_background_genMatchOpt3_cfg.py

#rm -rf testMEM_hh_bb2l_signal_genMatchOpt1.log
#testMEM_hh_bb2l testMEM_hh_bb2l_signal_genMatchOpt1_cfg.py &> testMEM_hh_bb2l_signal_genMatchOpt1.log &
#rm -rf testMEM_hh_bb2l_signal_genMatchOpt2.log
#testMEM_hh_bb2l testMEM_hh_bb2l_signal_genMatchOpt2_cfg.py &> testMEM_hh_bb2l_signal_genMatchOpt2.log &
rm -rf testMEM_hh_bb2l_signal_genMatchOpt3.log
testMEM_hh_bb2l testMEM_hh_bb2l_signal_genMatchOpt3_cfg.py &> testMEM_hh_bb2l_signal_genMatchOpt3.log &

#rm -rf testMEM_hh_bb2l_background_genMatchOpt1.log
#testMEM_hh_bb2l testMEM_hh_bb2l_background_genMatchOpt1_cfg.py &> testMEM_hh_bb2l_background_genMatchOpt1.log &
#rm -rf testMEM_hh_bb2l_background_genMatchOpt2.log
#testMEM_hh_bb2l testMEM_hh_bb2l_background_genMatchOpt2_cfg.py &> testMEM_hh_bb2l_background_genMatchOpt2.log &
rm -rf testMEM_hh_bb2l_background_genMatchOpt3.log
testMEM_hh_bb2l testMEM_hh_bb2l_background_genMatchOpt3_cfg.py &> testMEM_hh_bb2l_background_genMatchOpt3.log &

#rm -rf testMEM_hh_bb2l_all.root
#hadd testMEM_hh_bb2l_all.root testMEM_hh_bb2l_signal_genMatchOpt1.root testMEM_hh_bb2l_signal_genMatchOpt2.root testMEM_hh_bb2l_signal_genMatchOpt3.root testMEM_hh_bb2l_background_genMatchOpt1.root testMEM_hh_bb2l_background_genMatchOpt2.root testMEM_hh_bb2l_background_genMatchOpt3.root

