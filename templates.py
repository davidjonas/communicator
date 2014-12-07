from widgetry.html_generator import Page, Template
from widgets import *

class MainPage(Page):
    def __init__(self, request, title):
        super(MainPage, self).__init__(title, request=request)

        self.addHeadDirective('<link rel="shortcut icon" href="/static/favicon.ico?v=1" />')
        self.addHeadDirective('<meta charset="utf-8">')
        self.addHeadDirective('<meta http-equiv="X-UA-Compatible" content="IE=edge">')
        self.addHeadDirective('<meta name="viewport" content="width=device-width, initial-scale=1">')
        self.addCSSFile('/static/css/base.css')
        self.addCSSFile('/static/css/blocks.css')
        self.addCSSFile('http://fonts.googleapis.com/css?family=Merriweather:700|Open+Sans+Condensed:300|Ruthie')
        self.addJSFile('/static/js/jquery-1.9.1.min.js')

        self.addInlineJS("""
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
            })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

            ga('create', 'UA-11585597-1', 'auto');
            ga('send', 'pageview');
         """)


class RTCTemplate(Template):
    def __init__(self, parent, room):
        super(RTCTemplate, self).__init__(parent)

        self.addJSFile("/static/rtc/latest.js")
        self.addJSFile("https://cdn.socket.io/socket.io-1.2.1.js")
        self.addJSFile("http://code.createjs.com/soundjs-0.5.2.min.js")
        self.addJSFile("/static/rtc/hkuRTC.js")
        self.addCSSFile("/static/rtc/hkuRTC.css")

        self.addInlineJS('var room = "%s"' % room)

        html = """
            <div id="remoteVideos"></div>
            <video id="localVideo"></video>
            <img id="logo" src="/static/images/hku.png"/>
            <div id="flash"></div>
        """ % {'room': room}

        self.add(html)
