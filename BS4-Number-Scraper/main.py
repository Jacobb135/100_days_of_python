import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import collections
collections.Callable = collections.abc.Callable

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1724035.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup("span")
total = 0
for tag in tags:
    number = int(tag.contents[0])
    total += number
print(total)


