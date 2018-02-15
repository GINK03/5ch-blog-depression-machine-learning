import glob

import pickle

import re

import MeCab

import concurrent.futures

bake = '‚'

def _map(arg):
  me = MeCab.Tagger('-Owakati')
  key, names = arg

  fp = open(f'courpus/{key:09d}', 'w')
  for name in names:
    try:
      obj = pickle.load(open(name, 'rb'))
    except Exception as ex:
      continue
    cat = obj['href'].split('/')[-2]
    mes = obj['msg'].replace('\n', '')
    if bake in mes:
      continue
    if index%1 == 0:
      try:
        print(cat, mes)
      except Exception as ex:
        continue
      try:
        fp.write( f'{cat}\t{mes}\n' )
      except Exception as ex:
        print(ex)
        continue

args = {}
for index, name in enumerate(glob.glob('../scraping-designs/5ch-scrape/messages/*')):
  key = index%12
  if args.get(key) is None:
    args[key] = []
  args[key].append(name)
args = [(key,names) for key, names in args.items()]
#_map(args[0])
with concurrent.futures.ProcessPoolExecutor(max_workers=12) as exe:
  exe.map(_map, args)
