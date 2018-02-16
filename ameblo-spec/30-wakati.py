import MeCab


import glob

import pickle

m = MeCab.Tagger('-Owakati')

for s in ['negative', 'positive']:
  fp = open(f'{s}.txt', 'w')
  for name in glob.glob(f'{s}/*'):
    obj = pickle.load(open(name, 'rb'))
    wa = m.parse(obj['main']).strip()
    fp.write(wa + '\n')
