# myapp.py

import chart

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

#---------------------------
# Utility Functions

def get_user(page):
    """return a user or None (and do a redirect)"""
    user = users.User("emstumme@gmail.com")
    # users.get_current_user()
    if user: return user
    page.redirect(users.create_login_url(
        self.request.uri))
    return None

#vote.celebrity
#vote.user
#  d = { 'ladygaga' : 4, 'justin' :3, 'guido' : 2 }
def count_votes(votes):
    """return a dictionary with number of votes per celebrity"""
    # input [CelebrityVote(user0, celeb0), CV(user1, c1)]

    d = {}
    for vote in votes:
        if vote.celebrity in d:
            d[vote.celebrity] = d[vote.celebrity] +1
        else:
            d[vote.celebrity] = 1
    return d 


#---------------------------
# DATASTORE OBJECTS

class CelebrityVote(db.Model):
    user = db.UserProperty()
    celebrity = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)

def add_vote(user, celebrity):
    vote = CelebrityVote()
    vote.user = user
    vote.celebrity = celebrity
    vote.put() # store vote in datastore

def get_votes():
    """return a list of CelebrityVote"""
    votes = db.GqlQuery("SELECT * FROM CelebrityVote")
    return votes
#-------------------------
# WEBPAGE DEFINITIONS

class MainPage(webapp.RequestHandler):
    def get(self):
        user = get_user(self)
        if not user: return
        self.response.out.write("""
<html><body>
<img src="/images/google.png"/>
<h1> My Awesome Website</h1>

<img src="http://www.google.com/intl/en_ALL/images/srpr/logo1w.png">
Hello <b>%s</b>!
<p/>
Take my <ahref="/quiz'>quiz</a>!
</body></html>
""" % user.nickname())
         #  'Hello,' + user.nickname())

class QuizPage(webapp.RequestHandler):
    def get(self):
        user = get_user(self)
        if not user: return
        self.response.out.write("""
<html>
<head><title> My Awesome Quiz</title></head>
<body>
<form action="/answer" method=post>
Who is your favorite celebrity?<p>
<input type=radio name= "celebrity" value = "justin">
    Justin Bieber<br>

<input type=radio name= "celebrity" value = "ladygaga">
    Lady Gaga<br>

<input type=radio name= "celebrity" value = "guido">
    guido<p>'

<input type=submit value="answer">
</form>
</body>
</html>""")

class AnswerPage(webapp.RequestHandler):
    def post(self):
        user = get_user(self)
        if not user: return
        celebrity = self.request.get("celebrity")
        add_vote(user, celebrity)
        self.response.out.write("""
     
<html><body>
You chose <b>%s</b>.
See all <a href="/results"> the results</a>
</body></html>""" % celebrity)

class ResultsPage(webapp.RequestHandler):
    def get(self):
        user = get_user(self)
        if not user: return
        votes = get_votes() # list of CelebrityVote
        d = count_votes(votes)
        #vote.celebrity
        #vote.user
        #d = { 'ladygaga' : 4, 'justin' :3, 'guido' : 2 }
        charturl = chart.dictionary_chart(d)
        self.response.out.write("""
<html><body>
Here are the votes:<p>
<img src="%s"/>
</body></html>
""" %charturl)
            
class BeatlesPage(webapp.RequestHandler):
    def get(self):
        user = get_user(self)
        if not user: return
        self.response.headers['content-type'] = 'text/plain'
        self.response.out.write('hello, goodbye\n' + 'i am the walrus')

application = webapp.WSGIApplication(
    [ ("/", MainPage),
    ('/beatles', BeatlesPage),
    ("/quiz", QuizPage),
    ("/answer", AnswerPage),
    ("/results", ResultsPage)],

    debug = False)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
