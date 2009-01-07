from google.appengine.ext import db

class user(db.Model):
    user =          db.UserProperty()
    location =      db.StringProperty()

class point(db.Model):
    name =          db.StringProperty()
    desc =          db.StringProperty()
    user =          db.UserProperty()

class stop(db.Model):
    point =         db.ReferenceProperty(point)
    system =        db.StringProperty()
    route =         db.StringProperty()
    direction =     db.StringProperty()
    stop_id =       db.StringProperty()