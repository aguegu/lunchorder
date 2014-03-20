import requests
import json
import ast
from StringIO import StringIO

url = 'http://127.0.0.1:5000/restaurants/1'

r = requests.get(url)

print 'status_code', r.status_code

print 'headers', r.headers

print 'encoding', r.encoding

print 'text', r.text

print 'json', r.json()

print '%r' % r.json()

#f = StringIO(r.json())
#print json.load(f)

#d = ast.literal_eval(str(r.json()))
#print d
#print d[u'name']

