#!/usr/bin/env python

from tthAnalysis.HiggsToTauTau.safe_root import ROOT
from tthAnalysis.HiggsToTauTau.common import SmartFormatter, logging
from tthAnalysis.HiggsToTauTau.analysisSettings import lumi_2016, lumi_2017, lumi_2018

import os
import collections
import numpy as np
import prettytable
import jinja2
import datetime
import itertools
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
import io
import argparse
import xml.etree.ElementTree as ET
import subprocess

ROOT.gROOT.SetBatch(True)

CSS_COMMON = """
.list {
  list-style-type: circle;
  font-size: 0.9em;
  font-family: "Courier New", Courier, monospace;
  line-height: 1.5em;
}

.multicol {
  column-count: 4;
  column-gap: 0px;
}

div {
  float: left;
}

.selected, tbody.selected {
  background-color: #dbd21f;
}

a {

  font-family: Arial, Helvetica, sans-serif;
  color: #0060B6;
  text-decoration: none;
}

a:hover {
  color:#00A0C6;
  text-decoration:none;
  cursor:pointer;
}

a.title {
  font-size: 1.5em;
  margin: 10px;
}

table {
  border-collapse: collapse;
  margin: 2px 0;
  font-size: 0.9em;
  font-family: "Courier New", Courier, monospace;
  min-width: 400px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
  float: left;
  margin-right: 10px;
}

table th,
table td {
  padding: 2px 5px;
}

table tbody tr {
  border-bottom: 1px solid #dddddd;
}

table tbody tr:nth-of-type(even) {
  background-color: #d4d4d4;
}

.selected, table tbody tr.selected:nth-of-type(even) {
  background-color: #dbd21f;
}

table tr:hover td {
  background-color: #a3a3a3;
}
"""

CSS_TEMPLATE = """
table.{{ cat }} thead tr {
  background-color: {{ color }};
  color: #ffffff;
  text-align: left;
}

table.{{ cat }} tbody tr:last-of-type {
  border-bottom: 2px solid {{ color }};
}
"""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>

<script>
function toggleClass(el, className) {
  if (el.className.indexOf(className) >= 0) {
      el.className = el.className.replace(className,"");
  }
  else {
    el.className  += className;
  }
}
</script>

<style>
{{ css }}
</style>

</head>
<body>

<p><em>File generated at {{ today }} with <a href="{{ url }}">this script</a>
from ROOT files stored in the following directories:</em>

<ul class="list">{% for dirname in dirnames %}
  <li>{{ dirname }}</li>
{% endfor %}
</ul>

In <em>ERA_1st vs ERA_2nd</em> columns, the relative differences are computed wrt
<tt>ERA_2nd</tt>: <tt>(ERA_1st - ERA_2nd) / ERA_2nd</tt>.<br />
All event counts are normalized to 1/fb.

<ul class="list multicol">
{% for link in toc %}
<li>{{ link }}</li>
{% endfor %}
</ul>

</p>

{{ tables }}
</body>
</html>
"""

# in /fb
LUMIS = {
  2016 : lumi_2016 / 1e3,
  2017 : lumi_2017 / 1e3,
  2018 : lumi_2018 / 1e3,
}

HIGGS_PROCESSES = [ 'ggH', 'qqH', 'WH', 'ZH', 'tHq', 'tHW', 'TTH', 'signal' ]
BKG_PROCESSES = [ 'data_fakes', 'Convs', 'DY', 'ST', 'TT', 'TTW', 'TTWW', 'TTZ', 'VV', 'VVV', 'W', 'Other' ]
PROCESSES = [ 'data_obs', 'fakes_mc' ] + BKG_PROCESSES

CATEGORIES = [
  'TT_resolved',
  'TT_boosted',
  'HH_resolved_1b',
  'HH_resolved_2b',
  'HH_boosted',
  'H_resolved_1b',
  'H_resolved_2b',
  'H_boosted',
  'W_resolved',
  'W_boosted',
  'Other',
]
COLORS = [
  '#009879', '#540098', '#009098', '#986d00', '#980000',
  '#980081', '#00981e', '#980051', '#6f9800', '#000d98',
  '#983f00',
]

BASEDIRS = {
  2016 : '/home/snandan/hhAnalysis/2016/final_bb1l_LBN_resonant_sigweight1_wfullsyst_moretopsyst/datacards/hh_bb1l/addSystFakeRates',
  2017 : '/home/snandan/hhAnalysis/2017/final_bb1l_LBN_resonant_sigweight1_wfullsyst/datacards/hh_bb1l/addSystFakeRates',
  2018 : '/home/snandan/hhAnalysis/2018/final_bb1l_LBN_resonant_sigweight1_wfullsyst_moretopsyst/datacards/hh_bb1l/addSystFakeRates',
}

SPINS = [ 0, 2 ]
MASSES = [ 250, 260, 270, 280, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 1000 ]
ERAS = list(LUMIS.keys())

def get_link():
  repo_path = os.path.join(os.getenv('CMSSW_BASE'), 'src', 'hhAnalysis', 'bbww')
  assert(os.path.isdir(repo_path))
  cmd_str = 'git -C {} rev-parse HEAD'.format(repo_path)
  cmd = subprocess.Popen(cmd_str.split(), stdout = subprocess.PIPE, stderr = None, shell = False)
  stdout, stderr = cmd.communicate()
  commit_hash = stdout.strip()
  this_file = os.path.basename(__file__)
  url = 'https://github.com/HEP-KBFI/hh-bbww/blob/{}/scripts/{}'.format(commit_hash, this_file)
  return url

def read_evsums(basedirs, cat, mass, spin, era):

  fn_base = 'addSystFakeRates_hh_bb1l_LBN_{}_MVAOutput_{}_spin{}.root'.format(cat, mass, spin)
  fn = os.path.join(basedirs[era], fn_base)
  logging.debug('Reading {}'.format(fn))
  if not os.path.isfile(fn):
    raise RuntimeError("No such file: %s" % fn)
  f = ROOT.TFile.Open(fn, 'read')

  evsums = {}
  for k in f.GetListOfKeys():
    kn = k.GetName()
    if 'CMS' in kn or kn.endswith(('Up', 'Down')):
      continue
    higgs_key = [ higgs_proc for higgs_proc in HIGGS_PROCESSES if kn.startswith(higgs_proc) ]
    proc_key = ''
    if higgs_key:
      proc_key = higgs_key[0]
    elif kn in PROCESSES:
      proc_key = kn
    else:
      raise RuntimeError("Unexpected histogram name: %s" % kn)
    assert(proc_key)
    if proc_key not in evsums:
      evsums[proc_key] = 0.
    h = f.Get(kn)
    evsums[proc_key] += h.Integral() / LUMIS[era]
  f.Close()

  evsums_ordered = collections.OrderedDict()
  evsums_ordered['data_obs'] = evsums['data_obs']
  evsums_ordered['bkg_sum'] = sum(evsums[bkg_proc] for bkg_proc in BKG_PROCESSES + HIGGS_PROCESSES if bkg_proc != 'signal')
  for bkg_proc in [ 'TT', 'ST', 'W', 'DY' ]:
    evsums_ordered[bkg_proc] = evsums[bkg_proc]
  evsums_ordered['VV+VVV'] = sum(evsums[bkg_proc] for bkg_proc in [ 'VV', 'VVV' ])
  evsums_ordered['TTV'] = sum(evsums[bkg_proc] for bkg_proc in [ 'TTZ', 'TTW', 'TTWW' ])
  evsums_ordered['singleH'] = sum(evsums[bkg_proc] for bkg_proc in HIGGS_PROCESSES if bkg_proc != 'signal')
  for bkg_proc in [ 'Other', 'Convs' ]:
    evsums_ordered[bkg_proc] = evsums[bkg_proc]
  evsums_ordered['signal'] = evsums['signal']
  for bkg_proc in [ 'data_fakes', 'fakes_mc' ]:
    evsums_ordered[bkg_proc] = evsums[bkg_proc]

  evsums_ordered['data_fakes / fakes_mc'] = evsums_ordered['data_fakes'] / evsums_ordered['fakes_mc']
  for numerator in [ 'data_obs', 'TT', 'ST', 'W', 'DY', 'VV+VVV', 'TTV', 'singleH', 'Other', 'Convs', 'data_fakes' ]:
    evsums_ordered['{} / bkg_sum'.format(numerator)] = evsums_ordered[numerator] / evsums_ordered['bkg_sum']
  evsums_ordered['signal / sqrt(bkg_sum)'] = evsums_ordered['signal'] / np.sqrt(evsums_ordered['bkg_sum'])

  return evsums_ordered

def get_era_combination_str(*era_combination):
  return '{} vs {}'.format(*era_combination)

def add_images(era_tables, alt_text):
  html = ''
  for era_combination_str in era_tables:
    era_table = era_tables[era_combination_str]
    procs = list(era_table.keys())
    cats = list(era_table[procs[0]].keys())
    data = []
    for cat in cats:
      data.append([ era_table[proc][cat] for proc in procs ])
    data = np.asarray(data)

    vmin = max(np.amin(data), -100)
    vmax = min(np.amax(data), +100)
    vcolor_switch = (vmax - vmin) / 2 + vmin

    plt.figure(figsize = (10, 8), dpi = 100)
    plt.gca().imshow(data, vmin = vmin, vmax = vmax)
    plt.gca().set_xticks(np.arange(len(procs)))
    plt.gca().set_xticklabels(procs, rotation = 45, fontsize = 12)
    plt.gca().set_yticks(np.arange(len(cats)))
    plt.gca().set_yticklabels(labels = cats, fontsize = 12)

    for i in range(len(cats)):
      for j in range(len(procs)):
        val = data[i, j]
        text = plt.gca().text(j, i, '{:.2f}'.format(val),
                      ha = 'center', va = 'center', color = 'white' if val < vcolor_switch else 'black')

    title = ', '.join([ alt_text, era_combination_str ])
    plt.title('{} [%]'.format(title))
    plt.tight_layout()
    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes,  format = 'png')
    pic_IObytes.seek(0)
    pic_hash = base64.b64encode(pic_IObytes.read())
    plt.close()
    pic_hash_str = pic_hash.decode('utf-8') if type(pic_hash) == bytes else pic_hash
    html += '<div><img src="data:image/png;base64, {}" alt="{}"/></div>'.format(pic_hash_str, title)
  return html

def generate_html(spins, masses, eras, basedirs, output):

  era_combinations = list(itertools.combinations(eras, 2))
  era_combination_strs = [ get_era_combination_str(*era_combination) for era_combination in era_combinations ]

  css = CSS_COMMON
  for cat_idx, cat in enumerate(CATEGORIES):
    css += jinja2.Template(CSS_TEMPLATE).render(cat = cat, color = COLORS[cat_idx])

  tables = ''
  toc = []

  for spin in spins:
    for mass in masses:
      anchor = 'spin{spin}_{mass}'.format(spin = spin, mass = mass)
      anchor_name = 'Spin-{spin} {mass}'.format(spin = spin, mass = mass)
      tables += '<div><p><a class="title" href="#{anchor}" name="{anchor}">{anchor_name}</a></p>'.format(
        anchor = anchor,
        anchor_name = anchor_name,
      )
      toc.append('<a href="#{}">{}</a>'.format(anchor, anchor_name))

      era_tables = collections.OrderedDict()
      for era_combination_str in era_combination_strs:
        era_tables[era_combination_str] = collections.OrderedDict()

      for cat_idx, cat in enumerate(CATEGORIES):
        evsums = {}
        for era in eras:
          evsums[era] = read_evsums(basedirs, cat, mass, spin, era)

        table = prettytable.PrettyTable()
        table.field_names = [ cat ] + list(map(str, eras)) + era_combination_strs

        for row_key in evsums[eras[0]]:
          row = [ row_key ]
          for era in eras:
            nr = evsums[era][row_key]
            if nr > 1e4:
              nr_fmt = '{:.0f}'.format(nr)
            elif nr > 1e3:
              nr_fmt = '{:.1f}'.format(nr)
            elif nr > 1e2:
              nr_fmt = '{:.2f}'.format(nr)
            elif nr < 0.1:
              nr_fmt = '{:.2e}'.format(nr)
            else:
              nr_fmt = '{:.3f}'.format(nr)
            assert(nr_fmt)
            row.append(nr_fmt)

          for era_combination in era_combinations:
            era_1st = era_combination[0]
            era_2nd = era_combination[1]
            nr_1st = evsums[era_1st][row_key]
            nr_2nd = evsums[era_2nd][row_key]
            diff = (nr_1st - nr_2nd) * 100. / nr_2nd
            diff_fmt = '{:+.2f}%'.format(diff)
            row.append(diff_fmt)

            if '/' in row_key:
              continue
            era_combination_str = get_era_combination_str(era_1st, era_2nd)
            if row_key not in era_tables[era_combination_str]:
              era_tables[era_combination_str][row_key] = collections.OrderedDict()
            era_tables[era_combination_str][row_key][cat] = diff

          table.add_row(row)
        table_str = table.get_html_string(attributes = {"class" : cat}).replace('<tr>', "<tr onmousedown=\"toggleClass(this,'selected');\">")
        if '<thead>' not in table_str:
          # we're dealing with an old version of prettytable
          root = ET.fromstring(table_str)
          head_el = ET.tostring(root[0])
          body_els = ''.join(ET.tostring(el) for el in root[1:])
          table_str = '<table class="{}"><thead>{}</thead><tbody>{}</tbody></table>'.format(cat, head_el, body_els)

        tables += table_str

      tables += '</div><br>'
      tables += add_images(era_tables, 'Spin-{}, {}'.format(spin, mass))

  output = 'yields.html'
  with open(output, 'w') as f:
    html = jinja2.Template(HTML_TEMPLATE).render(
      css = css,
      tables = tables,
      today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S%z"),
      dirnames = basedirs.values(),
      toc = toc,
      url = get_link(),
    )
    f.write(html)
  logging.debug('Saved HTML file to: {}'.format(output))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(formatter_class = lambda prog: SmartFormatter(prog, max_help_position = 35))
  parser.add_argument('-e', '--era', dest = 'eras', metavar = 'era', required = False, type = int, choices = ERAS,
                      default = ERAS, nargs = '+',
                      help = 'R|Eras')
  parser.add_argument('-m', '--mass', dest = 'masses', metavar = 'mass', required = False, type = int, choices = MASSES,
                      default = MASSES, nargs = '+',
                      help = 'R|Masses')
  parser.add_argument('-s', '--spin', dest = 'spins', metavar = 'spin', required = False, type = int, choices = SPINS,
                      default = SPINS, nargs = '+',
                      help = 'R|Spins')
  for era in ERAS:
    parser.add_argument('--dir-{}'.format(era), dest = 'dir_{}'.format(era), metavar = 'path', required = False, type = str,
                        default = BASEDIRS[era],
                        help = 'R|Directory to {} datacards'.format(era))
  parser.add_argument('-o', '--output', dest = 'output', metavar = 'file', required = False, type = str, default = 'yields.html',
                      help = 'R|Output HTML file')
  parser.add_argument('-v', '--verbose', dest = 'verbose', action = 'store_true', default = False,
                      help = 'R|Enable verbose printout')
  args = parser.parse_args()

  if args.verbose:
    logging.getLogger().setLevel(logging.DEBUG)

  basedirs = collections.OrderedDict([ (era, getattr(args, 'dir_{}'.format(era))) for era in ERAS ])
  generate_html(args.spins, args.masses, args.eras, basedirs, args.output)
