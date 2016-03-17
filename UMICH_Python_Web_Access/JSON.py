import urllib
import json

#url="http://python-data.dr-chuck.net/comments_42.json"
url='http://python-data.dr-chuck.net/comments_231901.json'
print 'Retrieving', url
uh= urllib.urlopen(url)
data=uh.read()
print 'Retrieved',len(data),'characters'

info= json.loads(data)
print 'user count', len(info)
print info['comments']
sum_count=0

for item in info['comments']:
    print 'name ',item['count']
    sum_count=sum_count+int(item['count'])

print sum_count
    
