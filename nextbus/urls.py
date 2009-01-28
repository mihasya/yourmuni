from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^addstop/(?P<bmark>[\w|-]+?)(?:\/)*$', 'nextbus.views.addStop'),
    (r'^addstop/(?P<bmark>[\w|-]+?)/_dflt(?:\/)*$', 'nextbus.views.addStopDflt'),
    (r'^addstop/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)(?:\/)*$', 'nextbus.views.addStop'),
    (r'^addstop/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)(?:\/)*$', 'nextbus.views.addStop'),
    (r'^addstop/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)(?:\/)*$', 'nextbus.views.addStop'),
    (r'^addstop/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)/(?P<direction>[\w|-]+?)(?:\/)*$', 'nextbus.views.addStop'),
    (r'^addstop/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)/(?P<direction>[\w|-]+?)/(?P<stop>[\w|-]+?)(?:\/)*$', 'nextbus.views.addStop'),

    (r'^catchstop(?:\/)*$', 'nextbus.views.catchStopDflt'),
    (r'^catchstop/_dflt(?:\/)*$', 'nextbus.views.catchStopDflt'),
    (r'^catchstop/(?P<re>[\w|-]+?)(?:\/)*$', 'nextbus.views.catchStop'),
    (r'^catchstop/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)(?:\/)*$', 'nextbus.views.catchStop'),
    (r'^catchstop/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)(?:\/)*$', 'nextbus.views.catchStop'),
    (r'^catchstop/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)/(?P<direction>[\w|-]+?)(?:\/)*$', 'nextbus.views.catchStop'),
    (r'^catchstop/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)/(?P<direction>[\w|-]+?)/(?P<stop>[\w|-]+?)(?:\/)*$', 'nextbus.views.catchStop'),
)