from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^login$', 'views.login'),
    (r'^logout$', 'views.logout'),
    (r'^addbmark(?:\/)*$', 'views.addBmark'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)(?:\/)*$', 'nextbus.addStop'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)/_dflt(?:\/)*$', 'nextbus.addStopDflt'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)(?:\/)*$', 'nextbus.addStop'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)(?:\/)*$', 'nextbus.addStop'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)(?:\/)*$', 'nextbus.addStop'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)/(?P<direction>[\w|-]+?)(?:\/)*$', 'nextbus.addStop'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)/(?P<direction>[\w|-]+?)/(?P<stop>[\w|-]+?)(?:\/)*$', 'nextbus.addStop'),
    (r'^catch/(?P<bmark>[\w|-]+)(?:\/)*$', 'views.catch'),
    (r'^clear-cache$', 'views.clearCache'),
    (r'^(?:.*)', 'views.home'),
)
