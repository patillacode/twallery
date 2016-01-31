
/*
    Node.js server script
    Required node packages: express, redis, socket.io
*/
var PORT = 3000;
var HOST = 'localhost';

var express = require('express'),
    http = require('http'),
    server = http.createServer(app);

var app = express();

var redis = require('redis');
var client = redis.createClient();

var io = require('socket.io');

if (!module.parent) {
    server.listen(PORT, HOST);
    var socket  = io.listen(server);

    socket.on('connection', function(client) {
        var subscribe = redis.createClient();
        subscribe.subscribe('realtime');

        subscribe.on("message", function(channel, message) {
            client.send(message);
        });

        client.on('message', function(msg) {
        });

        client.on('disconnect', function() {
            subscribe.quit();
        });
    });
}

