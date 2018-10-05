import urllib2
import json

def url_json(url):
    response = urllib2.urlopen(url)
    data = response.read()
    values = json.loads(data)
    return values

def url_last_updated(url):
    return url_json(url)['updated_at'].strip()

URL = "https://api.github.com/repos/FluffierThanThou/WorkTab"

status = url_json("https://api.github.com/rate_limit")
print status

with open('list') as f:
    for line in f:
        if len(line)<3:
            continue
        authorname, modname = line.strip().split(' ')
        URL = "https://api.github.com/repos/" + authorname + "/" + modname
        lastupdated = url_last_updated(URL)
        print "%s,%s,%s" % (authorname, modname, lastupdated)

