# twitter
#
# Make an update to twitter.

import urllib
import base64
import httplib

twitterhost = 'twitter.com'
twitterurl = '/statuses/update.xml?'

username = "username"
password = "password"

def getauth():
    """get authorization for my account"""
    username = "username"
    password = "password"
    auth = username + ':' + password
    return base64.encodestring(auth) # magic- see twitter api reference


def twitterupdate(status):
    """update my twitter account with the status"""
    urlquery  = urllib.urlencode(
        { 'status' : status})
    url = twitterurl + urlquery
    conn = httplib.HTTPConnection(twitterhost)
    conn.putrequest('POST',url)
    conn.putheader('Authorization', 'Basic' + 'getauth()')
    conn.endheaders()
    resp = conn.getresponse()
    print resp.status, resp.reason
    for x in resp.getheaders():
        print x
    print resp.read()
    

    
