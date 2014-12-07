var audioPath = "/static/rtc/sounds/";
var manifest = [
    {id:"alarm", src:"alarm.ogg"}
];
createjs.Sound.alternateExtensions = ["mp3"];
createjs.Sound.registerManifest(manifest, audioPath);

var call = function ()
{
  $("#flash").fadeIn(100).fadeOut(100).fadeIn(100).fadeOut(2000).fadeIn(100).fadeOut(100).fadeIn(100).fadeOut(2000).fadeIn(100).fadeOut(100).fadeIn(100).fadeOut(2000);
  createjs.Sound.play("alarm");
}

var CallEngine = function ()
{
    this.server = 'http://www.davidjonas.net:7080/'
    this.socket = io.connect(this.server, {'transports': ['websocket', 'polling'], 'force new connection': true });
    this.socket.on('call', call);
}

CallEngine.prototype.makeCall = function ()
{
  this.socket.emit("call");
}

var ce = new CallEngine();

$('html').click(function () {
  ce.makeCall();
});

var webrtc = new SimpleWebRTC({
    localVideoEl: 'localVideo',
    remoteVideosEl: 'remoteVideos',
    autoRequestMedia: true
});

webrtc.on('readyToCall', function () {
    webrtc.joinRoom(room);
    $("#flash").fadeOut()
});
