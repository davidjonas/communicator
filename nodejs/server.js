var server = require('http').createServer(),
        io = require('socket.io')(server, {'transports': ['websocket', 'htmlfile', 'xhr-polling', 'jsonp-polling', 'polling']});

//port to listen can be set through command line argument by running 'node server.js [port]' (it defaults to 8080)
var port = (process.argv.length >= 3) ? process.argv[2] : 8080;

//Server starting
server.listen(port);
console.log("Server listening on port " + port);

io.sockets.on('connection', function(socket) {
    //User connected through socket
    console.log("Incomming connection...");

    socket.on('call', function ()
    {
        io.sockets.emit('call');
    });

});
