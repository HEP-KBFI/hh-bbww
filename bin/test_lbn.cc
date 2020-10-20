#include "tthAnalysis/HiggsToTauTau/interface/TensorFlowInterfaceLBN.h" // TensorFlowInterfaceLBN
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle

int
main()
{
  const std::string pb_file = "hhAnalysis/bbww/data/lbn_test.pb";
  const std::vector<std::string> ll_input_keys = { "bjet1", "bjet2", "wjet1", "wjet2", "lepton" };
  const std::vector<std::string> hl_input_keys = { "met_pt", "met_phi" };
  const std::vector<std::string> classes = { "hh", "tt" };
  const TensorFlowInterfaceLBN tf_iface(pb_file, ll_input_keys, hl_input_keys, classes, "", true);

  const std::map<std::string, Particle> ll_inputs = {
    { "bjet1",  { 276.684,  0.152832, -0.98645, 28.7006   } },
    { "bjet2",  { 169.237,  0.995605 , 1.23096, 20.2758   } },
    { "wjet1",  {  95.2211, 0.350952,  2.66113, 11.43716  } },
    { "wjet2",  {  41.3803, 3.15625,   2.13135,  7.75682  } },
    { "lepton", { 102.122,  0.637329,  2.95996,  0.105713 } },
  };
  std::map<std::string, const Particle *> ll_inputs_ptr;
  for(const auto & kv: ll_inputs)
  {
    ll_inputs_ptr[kv.first] = &kv.second;
  }

  const std::map<std::string, double> hl_inputs = {
    { "met_pt",  383.478   },
    { "met_phi",   2.85488 },
  };
  const std::map<std::string, double> output = tf_iface(ll_inputs_ptr, hl_inputs);

  return EXIT_SUCCESS;
}
