import bs4


import glob

import gzip

import re

import hashlib

import concurrent.futures

import pickle
def _map(arg):

  key, names = arg

  for name in names:
    html = gzip.decompress(open(name, 'rb').read())
    soup = (bs4.BeautifulSoup(html))
    for script in soup(["script", "style"]):
      script.extract()    # rip it out
    meta = soup.find('meta', {'property':'og:url'})
    
    if meta is None:
      continue
    if 'ameblo' not in meta.get('content'):
      continue
    
    url = meta.get('content')

    ha = hashlib.sha256(bytes(url, 'utf8')).hexdigest()

    main = re.sub(r'\s{1,}', '', soup.find('div',{'id':'main'}).text)
    if 'ã' in main:
      continue
    if '通信エラー' in main:
      continue
    open(f'negative/{ha}', 'wb').write( pickle.dumps({'url':url, 'main':main}) )
    print(meta)
    print(main) 

args = {}
for index, name in enumerate(glob.glob('../../scraping-designs/livedoor-blog-batch-scrape/htmls/*')):
  key = index%16
  if args.get(key) is None:
    args[key] = []
  args[key].append( name )
args = [(key,names) for key,names in args.items()]

with concurrent.futures.ProcessPoolExecutor(max_workers=16) as exe:
  exe.map(_map, args)
