# coding=utf-8
import urllib2,re,time
f = open('test.txt')
r = file('result.txt','a')
regextuniu='<a class=\"total\" href=\"http://www.tuniu.com/[^>]*>([^<]*)</a>'
regexmfw='<a class=\"total\" href=\"http://www.mafengwo.cn/[^>]*>([^<]*)</a>'
regextab='<li class="tab-item active">([^<]*?)</li>'
for line in f:
	res = []
	res.append(line.rstrip())
	url = 'http://www.so.com/s?q=' + line
	req = urllib2.urlopen(url)
	html = req.read()
	if html.find("cmpid=mkt_01026001") != -1:
		res.append('1')
		if html.find('<ul class="tabs">') != -1:
			res.append('1')
			act = re.findall(regextab,html)
			numtuniu = re.findall(regextuniu,html)
			nummfw = re.findall(regexmfw,html)
			num1 = '|'.join(numtuniu)
			num2 = '|'.join(nummfw)
			res.append(act[0])
			res.append(num1)
			res.append(num2)
		else:
			res.append('0')
			
	else:
		res.append('0')
	req.close()
	result="\t".join(res)
	r.write(result)
	r.write("\n")
	time.sleep(1)
f.close()
r.close()
