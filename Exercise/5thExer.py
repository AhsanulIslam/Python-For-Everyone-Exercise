import json
import urllib.request
count = 0

url = "http://py4e-data.dr-chuck.net/comments_590392.json"

data= urllib.request.urlopen(url).read()

info = json.loads(data)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	count = count + number
print (count)
