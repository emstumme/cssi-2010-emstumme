#webstuff

import httplib

conn = httplib.HTTPConnection("www.google.com")
conn.request("GET", "/")
resp = conn.getresponse()
print resp.status, resp.reason
data = resp.read()
conn.close
