#!/usr/bin/env python

from tthAnalysis.HiggsToTauTau.safe_root import ROOT
from tthAnalysis.HiggsToTauTau.common import logging, SmartFormatter

import argparse
import enum
import math
import collections
import prettytable
import os

class Hbb(enum.Enum):
  undefined = 0
  resolved = 1
  boosted = 2

class VBF(enum.Enum):
  undefined = 0
  nottagged = 1
  tagged = 2

class LeptonPair(enum.Enum):
  dilepton = 0
  dielectron = 1
  dimuon = 2

class categoryEntryType(object):
  def __init__(self, num_electrons, num_muons, num_bjets_medium, num_bjets_loose, min_num_jets, max_num_jets, type_Hbb, type_vbf):
    self.num_electrons    = num_electrons
    self.num_muons        = num_muons
    self.num_bjets_medium = num_bjets_medium
    self.num_bjets_loose  = num_bjets_loose
    self.min_num_jets     = min_num_jets
    self.max_num_jets     = max_num_jets
    self.type_Hbb         = type_Hbb
    self.type_vbf         = type_vbf

    self.name = "hh_bbWW_"
    self.label = ""
    if   self.num_bjets_medium >= 2:
      self.name += "2bM"
      self.label = "2bM"
    elif self.num_bjets_medium >= 1 and self.num_bjets_loose >= 2:
      self.name += "1bM2bL"
      self.label = "1bM2bL"
    elif self.num_bjets_medium >= 1:
      self.name += "1bM"
      self.label = "1bM"
    elif                                self.num_bjets_loose >= 2:
      self.name += "2bL"
      self.label = "2bL"
    elif                                self.num_bjets_loose >= 1:
      self.name += "1bL"
      self.label = "1bL"

    if self.min_num_jets == -1 and self.max_num_jets == -1:
      pass
    elif self.min_num_jets == self.max_num_jets:
      self.name += "%ij" % self.min_num_jets
      label = "%i jets" % self.min_num_jets
      if self.label:
        self.label += ", " + label
      else:
        self.label = label
    elif self.min_num_jets == -1:
      self.name += "le%ij" % self.max_num_jets
      label = "<= %i jets" % self.max_num_jets
      if self.label:
        self.label += ", " + label
      else:
        self.label = label
    elif self.max_num_jets == -1:
      self.name += "ge%ij" % self.min_num_jets
      label = ">= %i jets" % self.min_num_jets
      if self.label:
        self.label += ", " + label
      else:
        self.label = label
    elif self.max_num_jets > self.min_num_jets:
      self.name += "%ito%ij" % (self.min_num_jets, self.max_num_jets)
      label = "%i to %i jets" % (self.min_num_jets, self.max_num_jets)
      if self.label:
        self.label += ", " + label
      else:
        self.label = label
    else:
      assert(False)

    if self.num_electrons >= 2:
      self.name += "2e"
      label = "2e"
      if self.label:
        self.label += ", " + label
      else:
        self.label = label
    elif self.num_muons >= 2:
      self.name += "2mu"
      label = "2mu"
      if self.label:
        self.label += ", " + label
      else:
        self.label = label
    else:
      self.name += "2l"
      label = "2l"
      if self.label:
        self.label += ", " + label
      else:
        self.label = label

    self.name += "_DYctrl"
    if self.type_Hbb == Hbb.resolved:
      self.name += "_resolvedHbb"
    elif self.type_Hbb == Hbb.boosted:
      self.name += "_boostedHbb"
      label = "boostedHbb"
      if self.label:
        self.label += ", " + label
      else:
        self.label = label
    if self.type_vbf == VBF.tagged:
      self.name += "_vbf"
      label = "vbf"
      if self.label:
        self.label += ", " + label
      else:
        self.label = label
    elif self.type_vbf == VBF.nottagged:
      self.name += "_nonvbf"

    self.name += "_OS_Tight"

  def __str__(self):
    return self.label

def is_higher_priority(category):
  return (
    category.num_bjets_medium,
    category.num_bjets_loose,
    category.max_num_jets if category.max_num_jets > 0 else +999,
    category.min_num_jets,
    category.type_Hbb,
    category.type_vbf,
    category.num_muons,
    category.num_electrons,
  )

def load_histogram(input_file, histogram_name):
  histogram = input_file.Get(histogram_name)
  if not histogram_name:
    return None
  if not histogram.GetSumw2N():
    histogram.Sumw2()
  return histogram

def comp_integral(histogram,
                  include_underflow_bin = False,
                  include_overflow_bin = False):
  if histogram:
    nof_bins = histogram.GetNbinsX()
    first_bin = 0 if include_underflow_bin else 1
    last_bin = (nof_bins + 1) if include_overflow_bin else nof_bins
    return sum(histogram.GetBinContent(i_bin) for i_bin in range(first_bin, last_bin + 1))
  else:
    return -1.

def comp_integral_err(histogram,
                      include_underflow_bin = False,
                      include_overflow_bin = False):
  if histogram:
    nof_bins = histogram.GetNbinsX()
    first_bin = 0 if include_underflow_bin else 1
    last_bin = (nof_bins + 1) if include_overflow_bin else nof_bins
    return math.sqrt(sum(histogram.GetBinError(i_bin)**2 for i_bin in range(first_bin, last_bin + 1)))
  else:
    return -1.

def get_content_sum(input_file, category, processes):
  num_events_sum = 0.
  num_events_err2_sum = 0.
  for process in processes:
    histogram_name = "%s/sel/evt/%s/EventCounter" % (category.name, process)
    histogram = load_histogram(input_file, histogram_name)
    assert(histogram)
    integral = comp_integral(histogram)
    integral_err = comp_integral_err(histogram)
    num_events_sum += integral
    num_events_err2_sum += integral_err**2
  return num_events_sum, math.sqrt(num_events_err2_sum)

def compute_error(results, results_key, lepton_key):
  v1 = results[results_key][lepton_key]['sf']
  e1 = results[results_key][lepton_key]['sf_err']
  v2 = results['inclusive'][lepton_key]['sf']
  e2 = results['inclusive'][lepton_key]['sf_err']
  return v1 / v2 * math.sqrt((e1 / v1)**2 + (e2 / v2)**2)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    formatter_class = lambda prog: SmartFormatter(prog, max_help_position = 35)
  )
  parser.add_argument('-i', '--input',
    type = str, dest = 'input', metavar = 'file', required = True, default = '',
    help = 'R|Path to hadd stage2 file',
  )
  parser.add_argument('-v', '--verbose',
    dest = 'verbose', action = 'store_true', default = False,
    help = 'R|Enable verbose output',
  )
  args = parser.parse_args()
  logging.getLogger().setLevel(logging.DEBUG if args.verbose else logging.INFO)
  input_file_name = args.input

  if not os.path.isfile(input_file_name):
    raise ValueError("No such file: %s" % input_file_name)

  categories = []
  for type_lepton in range(LeptonPair.dielectron.value, LeptonPair.dimuon.value + 1):
    type_lepton_enum = LeptonPair(type_lepton)
    num_electrons = 2 if type_lepton_enum == LeptonPair.dielectron else -1
    num_muons     = 2 if type_lepton_enum == LeptonPair.dimuon     else -1
    # AN, add categories for inclusive 2e, 2mu
    categories.append(categoryEntryType(num_electrons, num_muons, -1, -1, -1, -1, Hbb.undefined, VBF.undefined))
    # CV: add categories for "resolved" b-jets without VBF jet selection
    # categories.append(categoryEntryType(num_electrons, num_muons,  2, -1, -1, -1, Hbb.resolved,  VBF.undefined))
    categories.append(categoryEntryType(num_electrons, num_muons,  2, -1,  2,  2, Hbb.resolved, VBF.undefined))
    categories.append(categoryEntryType(num_electrons, num_muons,  2, -1,  3,  3, Hbb.resolved, VBF.undefined))
    categories.append(categoryEntryType(num_electrons, num_muons,  2, -1,  4, -1, Hbb.resolved, VBF.undefined))
    # categories.append(categoryEntryType(num_electrons, num_muons,  1,  1, -1, -1, Hbb.resolved,  VBF.undefined))
    categories.append(categoryEntryType(num_electrons, num_muons,  1,  2,  2,  2, Hbb.resolved, VBF.undefined))
    categories.append(categoryEntryType(num_electrons, num_muons,  1,  2,  3,  3, Hbb.resolved, VBF.undefined))
    categories.append(categoryEntryType(num_electrons, num_muons,  1,  2,  4, -1, Hbb.resolved, VBF.undefined))
    # categories.append(categoryEntryType(num_electrons, num_muons,  1, -1, -1, -1, Hbb.resolved,  VBF.undefined))
    categories.append(categoryEntryType(num_electrons, num_muons,  1, -1,  2,  2, Hbb.resolved, VBF.undefined))
    categories.append(categoryEntryType(num_electrons, num_muons,  1, -1,  3,  3, Hbb.resolved, VBF.undefined))
    categories.append(categoryEntryType(num_electrons, num_muons,  1, -1,  4, -1, Hbb.resolved, VBF.undefined))
    # categories.append(categoryEntryType(num_electrons, num_muons,  1,  2, -1, -1, Hbb.resolved,  VBF.undefined))
    categories.append(categoryEntryType(num_electrons, num_muons, -1,  2,  2,  2, Hbb.resolved, VBF.undefined))
    categories.append(categoryEntryType(num_electrons, num_muons, -1,  2,  3,  3, Hbb.resolved, VBF.undefined))
    categories.append(categoryEntryType(num_electrons, num_muons, -1,  2,  4, -1, Hbb.resolved, VBF.undefined))
    # CV: add categories for "resolved" b-jets with VBF jet selection
    # categories.append(categoryEntryType(num_electrons, num_muons,  2, -1, -1, -1, Hbb.resolved, VBF.tagged))
    # categories.append(categoryEntryType(num_electrons, num_muons,  1,  1, -1, -1, Hbb.resolved, VBF.tagged))
    # categories.append(categoryEntryType(num_electrons, num_muons,  1, -1, -1, -1, Hbb.resolved, VBF.tagged))
    # categories.append(categoryEntryType(num_electrons, num_muons, -1,  2, -1, -1, Hbb.resolved, VBF.tagged))
    # CV: add categories for "boosted" b-jets (no VBF jet selection)
    # categories.append(categoryEntryType(num_electrons, num_muons,  2, -1, -1, -1, Hbb.boosted, VBF.undefined))
    # categories.append(categoryEntryType(num_electrons, num_muons,  1,  1, -1, -1, Hbb.boosted, VBF.undefined))
    # categories.append(categoryEntryType(num_electrons, num_muons,  1, -1, -1, -1, Hbb.boosted, VBF.undefined))

  categories = list(sorted(categories, key = is_higher_priority, reverse = True))
  signal_processes = [ "DY", "DY_Convs", "DY_fake" ]
  background_processes = [ "TT", "TTW", "TTWW", "TTZ", "TH", "TTH", "WZ", "ZZ", "W", "VH" ] # exclude: "Convs", "data_fakes", "fakes_mc"

  input_file = ROOT.TFile.Open(input_file_name, 'read')
  if not input_file:
    raise RuntimeError("Unable to open file: %s" % input_file_name)

  results = collections.OrderedDict()
  for category in categories:
    num_events_signal_sum, num_events_err_signal_sum = get_content_sum(input_file, category, signal_processes)
    num_events_background_sum, num_events_err_background_sum = get_content_sum(input_file, category, background_processes)
    num_events_data, num_events_err_data = get_content_sum(input_file, category, [ "data_obs" ])
    num_events_data_minus_background = num_events_data - num_events_background_sum
    num_events_err_data_minus_background = math.sqrt(num_events_err_data**2 + num_events_err_background_sum**2)
    sf = num_events_data_minus_background / num_events_signal_sum
    sf_err = sf * math.sqrt(
      (num_events_err_data_minus_background / num_events_data_minus_background)**2 +
      (num_events_err_signal_sum            / num_events_signal_sum)**2
    )
    logging.debug(
      "category = {}: DY = {:.2f} +/- {:.3f}, data - background = {:.2f} +/- {:.3f} --> SF = {:.6f} +/- {:.6f}".format(
        category,
        num_events_signal_sum, num_events_err_signal_sum,
        num_events_data_minus_background, num_events_err_data_minus_background,
        sf, sf_err
      )
    )
    results_key = category.name
    assert(any(key in results_key for key in [ '2e_', '2mu_' ]))
    results_key = results_key.replace('2e_', '').replace('2mu_', '')
    if '2e' in category.name:
      key_lepton = '2e'
    elif '2mu' in category.name:
      key_lepton = '2mu'
    else:
      assert(False)

    label = category.label.replace(', {}'.format(key_lepton), '').replace(key_lepton, '')
    if not label:
      results_key = 'inclusive'
      label = 'inclusive'
    if results_key not in results:
      results[results_key] = { 'label' : label }
    assert(key_lepton not in results[results_key])
    results[results_key][key_lepton] = {
      'sf'     : sf,
      'sf_err' : sf_err,
    }
  input_file.Close()

  header = [
    "Category",
    "SF (2mu)",
    "SF err (2mu)",
    "SF (2e)",
    "SF err (2e)",
    "SF (2mu - 2e)",
    "SF err (total)",
    "SF (up)",
    "SF (down)",
  ]
  rows = []
  for results_key in results:
    if results_key == 'inclusive':
      continue
    sf_2mu = results[results_key]['2mu']['sf'] / results['inclusive']['2mu']['sf']
    sf_2e  = results[results_key]['2e']['sf']  / results['inclusive']['2e']['sf']
    sf_2mu_err = compute_error(results, results_key, '2mu')
    sf_2e_err = compute_error(results, results_key, '2e')
    emdiff = sf_2mu - sf_2e
    sf_err = math.sqrt(sf_2mu_err**2 + emdiff**2)
    sf_err_up = sf_2mu + sf_err
    sf_err_down = sf_2mu - sf_err
    rows.append([
      results[results_key]['label'],
      '{:.3f}'.format(sf_2mu),
      '{:.3f}'.format(sf_2mu_err),
      '{:.3f}'.format(sf_2e),
      '{:.3f}'.format(sf_2e_err),
      '{:.3f}'.format(emdiff),
      '{:.3f}'.format(sf_err),
      '{:.3f}'.format(sf_err_up),
      '{:.3f}'.format(sf_err_down),
    ])
  table = prettytable.PrettyTable(header)
  for row in rows:
    table.add_row(row)
  print(table)
