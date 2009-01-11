from google.appengine.ext import db

class UserProfile(db.Model):
    user =          db.UserProperty()
    location =      db.StringProperty()

class Point(db.Model):
    name =          db.StringProperty()
    desc =          db.StringProperty()
    user =          db.UserProperty()

class Stop(db.Model):
    point =         db.ReferenceProperty(Point)
    system =        db.StringProperty()
    url =           db.StringProperty()