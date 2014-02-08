var connection;


if (document.location.hostname != "") {
    connection = new WebSocket('ws://' + document.location.hostname + ':9001/connect', []);
} else {
    connection = new WebSocket('ws://localhost:9001/connect', []);
}

connection.onopen = function () {
    console.log("Connected to server");
};

connection.onerror = function(error) {
    console.log('WebSocket Error ' + error);
};

function getName() {
    return window.prompt("Please enter a username", "");
}

connection.onmessage = function (e) {
    console.log('Server: ' + e.data);
    
    var msg = JSON.parse(e.data);

    if (msg["type"] == "request") {
        if (msg["request"] == "name") {
            var name = getName();
            var response = {
                "type":"response",
                "request":"name",
                "name":name
            }
            connection.send(JSON.stringify(response));
        }
    }
}
