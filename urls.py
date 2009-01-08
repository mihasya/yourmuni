from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^login$', 'views.login'),
    (r'^logout$', 'views.logout'),
    (r'^addpoint(?:\/)*$', 'views.addPoint'),
    (r'^addstop/nb/(?P<point_name>\w+)(?:\/)*$', 'nextbus.addStop'),
    (r'^addstop/nb/(?P<point_name>\w+)/(?P<re>\w)(?:\/)*$', 'nextbus.addStop'),
    (r'^addstop/nb/(?P<point_name>\w+)/(?P<re>\w)/(?P<agency>\w)(?:\/)*$', 'nextbus.addStop'),
    (r'^addstop/nb/(?P<point_name>\w+)/(?P<re>\w)/(?P<agency>\w)/(?P<route>\w)(?:\/)*$', 'nextbus.addStop'),
    (r'^addstop/nb/(?P<point_name>\w+)/(?P<re>\w)/(?P<agency>\w)/(?P<route>\w)/(?P<direction>\w)(?:\/)*$', 'nextbus.addStop'),
    (r'^addstop/nb/(?P<point_name>\w+)/(?P<re>\w)/(?P<agency>\w)/(?P<route>\w)/(?P<direction>\w)/(?P<stop>\w)(?:\/)*$', 'nextbus.addStop'),
    (r'^catch/(?P<point_name>\w+)(?:\/)*$', 'views.catch'),
    (r'^(?:.*)', 'views.home'),
)
