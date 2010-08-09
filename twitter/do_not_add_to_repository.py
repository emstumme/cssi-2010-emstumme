# twitter authentication

import base64

def getauth():
    """get authorization for my account"""
    print 'getting auth info'
    username = "estum1"
    password = "skvfh1"
    auth = username + ':' + password
    return base64.encodestring(auth) # magic- see twitter api reference
