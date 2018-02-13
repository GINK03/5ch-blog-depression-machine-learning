import glob

import pickle

import re

import MeCab

me = MeCab.Tagger('-Owakati')

bake = '‚'
for index, name in enumerate(glob.glob('../scraping-designs/5ch-scrape/messages/*')):
  #print(name)
  try:
    obj = pickle.load(open(name, 'rb'))
  except Exception as ex:
    continue
  cat = obj['href'].split('/')[-2]
  mes = obj['msg'].replace('\n', '')
  if bake in mes:
    continue
  if index%10 == 0:
    try:
      print(cat, mes)
    except Exception as ex:
      continue
  with open(f'courpus/{cat}', 'a+') as fp:
    #print(mes)
    try:
      fp.write( mes + '\n' )
    except Exception as ex:
      continue
