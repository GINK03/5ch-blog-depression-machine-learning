import glob

import MeCab

import pickle

m = MeCab.Tagger('-Ochasen')

tag_feats = {}
for name in glob.glob('courpus/*'):
  for index, line in enumerate(open(name)):
    try:
      tag, line = line.strip().split('\t')
    except Exception as ex:
      print(ex)
      continue
    feat = [x.split('\t').pop(0) for x in filter(lambda x:'名詞-代名詞-一般' in x or '名詞-一般' in x, m.parse(line).strip().split('\n'))]
    if feat == []:
      continue
    if index%5000 == 0:
      print(feat)
      print(line)
    if tag_feats.get(tag) is None:
      tag_feats[tag] = []
    tag_feats[tag].append( feat )

pickle.dump(tag_feats, open(f'wakati/tag_feats.pkl', 'wb'))  
