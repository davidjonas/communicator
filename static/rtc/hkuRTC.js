var webrtc = new SimpleWebRTC({
    // the id of the dom element that will hold the local video
    localVideoEl: 'localVideo',
    // the id of the dom element that will hold remote videos
    remoteVideosEl: 'remoteVideos',
    // immediately ask for camera access
    autoRequestMedia: true
});

// we have to wait until it's ready
webrtc.on('readyToCall', function () {
    webrtc.joinRoom(room);
});

$('html').click(function () {

});
