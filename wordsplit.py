#! /usr/bin/python
import jieba.posseg as pseg
import sys
reload(sys)
sys.setdefaultencoding('utf8')
f = open('words-split.txt','a')
for l in open('words.txt'):
  l = l.rstrip()
  words = pseg.cut(l)
  wl=[]
  for w in words: 
    if 'u' not in w.flag: wl.append(w.word)
  f.write('|'.join(wl))
  f.write('\n')
