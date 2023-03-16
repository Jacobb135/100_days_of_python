import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1724037.xml"

test = urllib.request.urlopen(url, context=ctx)

data = test.read()
data.decode()
tree = ET.fromstring(data)

numbers = tree.findall('comments/comment')
total = 0
for number in numbers:
    counter = int(number.find('count').text)
    total += counter
print(total)
