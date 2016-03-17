import urllib
import xml.etree.ElementTree as ET
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    url = "http://python-data.dr-chuck.net/comments_231897.xml"  
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved ',len(data),' characters'
    print data
    tree = ET.fromstring(data)
    sum_all_count=0
    for elem in tree.iter('count'):
        print elem.text
        sum_all_count=sum_all_count+ int(elem.text)
    print sum_all_count
    
    
#Reference
#http://pycoders-weekly-chinese.readthedocs.org/en/latest/issue6/processing-xml-in-python-with-element-tree.html
#http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree/
