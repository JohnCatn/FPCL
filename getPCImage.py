
import requests
import urllib
from lxml import html

pageContent=requests.get('https://freepostcodelottery.com/?reminder=492ce018-e02c-11e6-a05e-00163e6ac872')
tree = html.fromstring(pageContent.content)
xhtml = html.document_fromstring(pageContent.content)
imageUrl = tree.xpath('//img[@alt="The current winning postcode"]/@src')[0]


urllib.urlretrieve("https://freepostcodelottery.com" + imageUrl, "postcode.gif")
print "https://freepostcodelottery.com" + imageUrl + " downloaded"
