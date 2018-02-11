import glob

import pickle

import json
term_index = {}
for name in glob.glob('wakati/*'):
  buff = pickle.load(open(name,'rb'))
  for msg in buff:
    for term in msg:
      if term_index.get(term) is None:
        term_index[term] = len(term_index)
        print(term)
json.dump(term_index, fp=open('term_index.json', 'w'), ensure_ascii=False, indent=2)

    
