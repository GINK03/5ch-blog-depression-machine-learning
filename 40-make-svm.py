import os

import glob

import pickle

import json

from collections import Counter
term_index = json.load(fp=open('term_index.json'))

fp = open('data.svm', 'w')
for name in glob.glob('./wakati/*'):
  tag = name.split('/').pop()
  buff = pickle.load(open(name,'rb'))
  for msg in buff:
    msg = dict(Counter(msg))
    msg = {term_index[term]+1:freq for term, freq in msg.items()}
    msg = sorted(msg.items(), key=lambda x:x[0])
    msg = ' '.join([f'{index}:{freq}' for index,freq in msg])

    pn = '0' if tag == 'utu' else '1'

    ctxt = f'{pn} {msg}'
    fp.write( ctxt + '\n' )
    #print(ctxt)
