import MeCab


import glob

import pickle

m = MeCab.Tagger('-Ochasen')

red = set(['わたし', '私', 'オイラ', 'おいら', 'あたしゃ', 'わい', '俺', 'オレ', 'わたくし', 'あたい', 'われ', 'あたし'])
for s in ['negative', 'positive']:
  fp = open(f'{s}.txt', 'w')
  for name in glob.glob(f'{s}/*'):
    obj = pickle.load(open(name, 'rb'))
    cha = m.parse(obj['main']).strip()
    
    targets = []
    for ch in cha.split('\n'):
      if '代名詞' not in ch:
        continue
      #print(ch)
      t = ch.split('\t').pop(0)
      if t in red:
        t = 'self-reflect'
      targets.append(t)
    
    if targets != []:
      fp.write(' '.join(targets) + '\n')
