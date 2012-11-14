def poplist(l, ids):
        offset = 0
        for id_ in ids:
                l.pop(id_ + offset)
                offset -= 1
        return l

def intersect(a, b):
        return list(set(a) & set(b))

f = open('uniq.txt', 'w')
datas = []
results = []

for line in open('solr.txt'):
        line = line.rstrip()
        if len(line)==0:
                continue
        ids = line.split(',')
        datas.append(ids)

c = 0
while 1:
        c += 1
        print c
        try:
                ids = datas.pop()
        except:
                break

        rm = []
        for i, current in enumerate(datas[:]):
                if len(intersect(ids, current))>5:
                        rm.append(i)
        datas = poplist(datas, rm)
        results.append(ids)

for ids in results:
        f.write(','.join(ids) + '\n')

f.close()