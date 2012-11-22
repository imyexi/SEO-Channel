def intersact(a,b):
  return list(set(a) & set(b))
f =open('uniq2.txt','w')
data=[]
result=[]
for line in open('solr.txt'):
  line = line.rstrip()
  ids=line.split(',')
  data.append(ids)
result.append(data[0])
num=0
for each in data[1:]:
  flag=0
  for res in result:
    flag+=1
    if len(intersact(each,res))>5:
      break
    if flag==len(result):
      flag=1
  if flag==1:result.append(each)
for ids in result:
  f.write(','.join(ids) + '\n')
