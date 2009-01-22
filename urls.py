from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^login$', 'views.login'),
    (r'^logout$', 'views.logout'),
    (r'^addbmark(?:\/)*$', 'views.addBmark'),

    (r'^addstop/nb/(?P<bmark>[\w|-]+?)(?:\/)*$', 'nextbus.views.addStop'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)/_dflt(?:\/)*$', 'nextbus.views.addStopDflt'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)(?:\/)*$', 'nextbus.views.addStop'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)(?:\/)*$', 'nextbus.views.addStop'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)(?:\/)*$', 'nextbus.views.addStop'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)/(?P<direction>[\w|-]+?)(?:\/)*$', 'nextbus.views.addStop'),
    (r'^addstop/nb/(?P<bmark>[\w|-]+?)/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)/(?P<direction>[\w|-]+?)/(?P<stop>[\w|-]+?)(?:\/)*$', 'nextbus.views.addStop'),

    (r'^nb/catchstop(?:\/)*$', 'nextbus.views.catchStop'),
    (r'^catchstop/nb/_dflt(?:\/)*$', 'nextbus.views.catchStopDflt'),
    (r'^catchstop/nb/(?P<re>[\w|-]+?)(?:\/)*$', 'nextbus.views.catchStop'),
    (r'^catchstop/nb/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)(?:\/)*$', 'nextbus.views.catchStop'),
    (r'^catchstop/nb/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)(?:\/)*$', 'nextbus.views.catchStop'),
    (r'^catchstop/nb/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)/(?P<direction>[\w|-]+?)(?:\/)*$', 'nextbus.views.catchStop'),
    (r'^catchstop/nb/(?P<re>[\w|-]+?)/(?P<agency>[\w|-]+?)/(?P<route>[\w|-]+?)/(?P<direction>[\w|-]+?)/(?P<stop>[\w|-]+?)(?:\/)*$', 'nextbus.views.catchStop'),

    (r'^catch/(?P<bmark>[\w|-]+)(?:\/)*$', 'views.catch'),

    (r'^delete/bmark/(?P<bmark>[\w|-]+)(?:\/)*(?P<confirm>[\w|-]*)$', 'views.deleteBmark'),

    (r'^clear-cache$', 'views.clearCache'),

    (r'^(?:.*)', 'views.home'),
)
