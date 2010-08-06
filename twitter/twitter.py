# twitter
#
# Make an update to twitter.

import urllib
import httplib
import ignore_off as auth

twitterhost = 'twitter.com'
twitterurl = '/statuses/update.xml?'

def twitterupdate(status):
    """update my twitter account with the status"""
    urlquery  = urllib.urlencode(
        { 'status' : status})
    url = twitterurl + urlquery
    conn = httplib.HTTPConnection(twitterhost)
    conn.putrequest('POST',url)
    conn.putheader(
        'Authorization',
        'Basic ' + auth.getauth())
    conn.endheaders()

    resp = conn.getresponse()
    print resp.status, resp.reason
    for x in resp.getheaders():
        print x
    print resp.read()
    

    
