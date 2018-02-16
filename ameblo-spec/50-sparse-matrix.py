import json
from collections import Counter
import math
term_index = json.load(open('term_index.json'))

fp = open('data.svm', 'w')
for fl, s in [(0, './negative.txt'), (1, './positive.txt')]:
  for line in open(s):
    line = line.strip()
    terms = line.split()
    obj = dict(Counter(terms))
    
    try:
      c = [f'{term_index[term]+1}:{math.log(freq+1)}'for term, freq in sorted(obj.items(),key=lambda x:term_index[x[0]])]
    except KeyError as ex:
      continue
    c = f'{fl} {" ".join(c)}'
    fp.write( c + '\n')
