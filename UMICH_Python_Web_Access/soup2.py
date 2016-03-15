import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
#url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
pos = raw_input('Enter Position ')
count = raw_input('Enter count ')
pos=int(pos)
count=int(count)
print url
for i in xrange(count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    att=list()
    for tag in tags:
        att.append(tag.attrs)
    real_pos=pos-1
    [(a,b)]=att[real_pos]
    url=str(b)
    print str(b)
