from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^login$', 'views.login'),
    (r'^logout$', 'views.logout'),
    (r'^addbmark(?:\/)*$', 'views.addBmark'),

    (r'^nb/', include('nextbus.urls') ),
    
    (r'^catch/(?P<bmark>[\w|-]+)(?:\/)*$', 'views.catch'),

    (r'^delete/bmark/(?P<bmark>[\w|-]+)(?:\/)*(?P<confirm>[\w|-]*)$', 'views.deleteBmark'),

    (r'^clear-cache$', 'views.clearCache'),

    (r'^(?:.*)', 'views.home'),
)
