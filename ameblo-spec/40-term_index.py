
import json
term_index = {}
for s in ['./negative.txt', './positive.txt']:
  for line in open('negative.txt'):
    line = line.strip()
    terms = line.split()
    for term in terms:
      if term_index.get(term) is None:
        term_index[term] = len(term_index)
json.dump(term_index, fp=open('term_index.json', 'w'), ensure_ascii=False, indent=2)
