from google.appengine.api import users
from django.shortcuts import render_to_response

def render_with_user(tpl, vars={}):
    vars['user'] = users.get_current_user()
    return render_to_response(tpl, vars)
    
def userRequired(fn):
    """decorator for forcing a login"""
    def new(*args, **kws):
        user = users.get_current_user()
        if not (user):
            r = args[0]
            return HttpResponseRedirect(users.create_login_url(
                                            r.build_absolute_uri()))
        else:
            return fn(*args, **kws)
    return new