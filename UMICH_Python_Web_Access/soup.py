import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = "http://python-data.dr-chuck.net/comments_231900.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
sum_up=0
for tag in tags:
    #print tag.contents[0]
    sum_up=sum_up+int(tag.contents[0])
print sum_up
