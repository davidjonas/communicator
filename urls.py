from django.conf.urls import *

urlpatterns = patterns('communicator.views',
    url(r'^(?P<room>\S*)', 'webrtc'),
)
