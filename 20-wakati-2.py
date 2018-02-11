import glob

import MeCab

import pickle

m = MeCab.Tagger('-Ochasen')

for name in glob.glob('./courpus/*'):
  tag = name.split('/').pop()
  
  buff = []
  for index, line in enumerate(open(name)):
    line = line.strip()
    feat = [x.split('\t').pop(0) for x in filter(lambda x:'名詞-代名詞-一般' in x, m.parse(line).strip().split('\n'))]
    if feat == []:
      continue
    if index%5000 == 0:
      print(feat)
      print(line)
    buff.append(feat)

  pickle.dump(buff, open(f'wakati/{tag}', 'wb'))  
