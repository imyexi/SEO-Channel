import jieba.posseg as pseg
for l in open('words.txt'):
  l = l.rstrip()
  words = pseg.cut(l)
  wl=[]
  for w in words: 
    if 'u' not in w.flag: wl.append(w.word)
  print '|'.join(wl)
