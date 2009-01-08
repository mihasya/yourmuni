from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^login$', 'views.login'),
    (r'^logout$', 'views.logout'),
    (r'^addpoint(?:\/)*$', 'views.addPoint'),
    (r'^addstop/(?P<point_name>\w+)(?:\/)*$', 'views.addStop'),
    (r'^addstop/(?P<point_name>\w+)/(?P<route>\w)(?:\/)*$', 'views.addStop'),
    (r'^addstop/(?P<point_name>\w+)/(?P<route>\w)/(?P<direction>\w)(?:\/)*$', 'views.addStop'),
    (r'^addstop/(?P<point_name>\w+)/(?P<route>\w)/(?P<direction>\w)/(?P<stop>\w)(?:\/)*$', 'views.addStop'),
    (r'^catch/(?P<point_name>\w+)(?:\/)*$', 'views.catch'),
    (r'^(?:.*)', 'views.home'),
)
