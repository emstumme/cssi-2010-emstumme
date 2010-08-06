#webstuff

import httplib

conn = httplib.HTTPConnection("localhost:8080")
conn.request("GET", "/")
resp = conn.getresponse()
print resp.status, resp.reason
for x in resp.getheaders(): print x
data = resp.read()
conn.close
