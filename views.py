from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from communicator.templates import *

def webrtc(request, room):
    template = RTCTemplate(MainPage(request, "DJ Communicator"), room)
    return HttpResponse(template.render())
