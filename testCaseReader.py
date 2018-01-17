import requests,bs4
s=requests.get("http://codeforces.com/problemset/problem/910/B")
try:
	s.raise_for_status()
except Exception as exc:
	print('There was a problem %s' % exc)

b=bs4.BeautifulSoup(s.text,"lxml")
f=open('in.in','w')
ele=b.select('div[class="input"] pre')
f.write(str(len(ele)))
f.write('\n')
for i in ele:
	for j in i:
		if len(j)!=0 :
			f.write(j+'\n')
f.close()
f=open('out.out','w')
ele=b.select('div[class="output"] pre')
#f.write(str(len(ele)))
#f.write('\n')
for i in ele:
	for j in i:
		if len(j)!=0 :
			f.write(j+'\n')
f.close()


