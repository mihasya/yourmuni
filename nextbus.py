from views import userRequired, render_with_user

@userRequired 
def addStop(r, point_name, route=None, direction=None, stop=None):
    params = {}
    return render_with_user('user/addstop.html', params)
    