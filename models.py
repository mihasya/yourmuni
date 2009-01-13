from google.appengine.ext import db

class UserProfile(db.Model):
    user =          db.UserProperty()
    location =      db.StringProperty()

class Bmark(db.Model):
    name =          db.StringProperty()
    desc =          db.StringProperty()
    user =          db.UserProperty()

class Stop(db.Model):
    bmark =         db.ReferenceProperty(Bmark)
    system =        db.StringProperty()
    url =           db.StringProperty()