import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1724038.json"

test = urllib.request.urlopen(url, context=ctx)
data = test.read()
data.decode()
info = json.loads(data)
numbers = 0
for item in info["comments"]:
    numbers += int((item["count"]))
print(numbers)
