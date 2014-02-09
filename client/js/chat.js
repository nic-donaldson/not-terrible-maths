var connection;
var port = 9001;

if (document.location.hostname != "") {
    connection = new WebSocket('ws://' + document.location.hostname + ':' + port + '/connect', []);
} else {
    connection = new WebSocket('ws://localhost:' + port + '/connect', []);
}

connection.onopen = function () {
    console.log("Connected to server");
};

connection.onerror = function(error) {
    console.log('WebSocket Error ' + error);
};

connection.onmessage = function (e) {
    console.log('Server: ' + e.data);
    
    var msg = JSON.parse(e.data);

    
}
