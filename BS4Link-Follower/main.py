import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import collections
collections.Callable = collections.abc.Callable

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Bryn.html"


count = int(input("Enter count: "))
position = int(input("Enter position "))

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    name = tags[position - 1]
    url = name.get("href", None)
    print("Retrieved: ", url)
    count = count - 1
