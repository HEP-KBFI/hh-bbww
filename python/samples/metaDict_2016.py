from hhAnalysis.bbww.samples.metaDict_2016_hh import meta_dictionary as meta_dictionary_hh
from hhAnalysis.bbww.samples.metaDict_2016_hh_private import meta_dictionary as meta_dictionary_private
from hhAnalysis.bbww.samples.metaDict_2016_hh import sum_events

import itertools, collections

meta_dictionary = collections.OrderedDict(itertools.chain(
  meta_dictionary_hh.items(), meta_dictionary_private.items()
))
