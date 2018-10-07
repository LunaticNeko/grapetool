import urllib2
import json

def url_json(url):
    response = urllib2.urlopen(url)
    data = response.read()
    values = json.loads(data)
    return values

def url_last_updated(url):
    return url_json(url)['updated_at'].strip()

GITHUB_TOKEN = None

try:
    with open('key') as keyfile:
        GITHUB_TOKEN = keyfile.readline()
except:
    GITHUB_TOKEN = None

with open('list') as f:
    for line in f:
        if len(line)<3:
            continue
        authorname, modname = line.strip().split(' ')
        URL = "https://api.github.com/repos/" + authorname + "/" + modname
        if GITHUB_TOKEN is not None:
            URL = URL + "?access_token=" + GITHUB_TOKEN
        lastupdated = url_last_updated(URL)
        print "%s,%s,%s" % (authorname, modname, lastupdated)

