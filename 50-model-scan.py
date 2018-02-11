import json

term_index = json.load(open('./term_index.json'))
index_term = {index:term for term,index in term_index.items()}

fp = open('./data.svm.model')

[next(fp) for i in range(6)]

term_weight = {}
for index, weight in enumerate(fp):
  term, weight = (index_term[index], weight.strip())
  term_weight[term] = float(weight)

for term, weight in sorted(term_weight.items(), key=lambda x:x[1]):
  print(term, weight)
