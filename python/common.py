import re

NONRESONANT_RE = re.compile(r'signal_ggf_nonresonant_hh_\w+')

def is_nonresonant(sample_category):
  return bool(NONRESONANT_RE.match(sample_category))
