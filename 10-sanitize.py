import glob

import pickle

import re

import MeCab

me = MeCab.Tagger('-Owakati')
for name in glob.glob('../scraping-designs/logsoku-scrape/messages/*'):
  print(name)
  try:
    obj = pickle.load(open(name, 'rb'))
  except Exception as ex:
    continue
  cat = obj['href'].split('/')[-2]
  mes = obj['messages']
  mes = [re.sub(r'>>\d{1,}','',m) for m in mes]
  mes = [re.sub(r'http.*?\s',' ',m) for m in mes]
  #mes = [me.parse(m).strip() for m in mes]
  print(cat, name)
  with open(f'courpus/{cat}', 'a+') as fp:
    #print(mes)
    for m in mes:
      try:
        fp.write( m + '\n' )
      except Exception as ex:
        continue
