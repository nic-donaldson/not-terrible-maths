var connection = new WebSocket('ws://localhost:9001/connect', []);

connection.onopen = function () {
    console.log("Connected to server");
    addMsg('Connected to server');
};

connection.onerror = function(error) {
    console.log('WebSocket Error ' + error);
    addMsg('WebSocket Error ' + error);
};

connection.onmessage = function (e) {
    console.log('Server: ' + e.data);
    if (e.data.startsWith("maths:")) {
        addMsg("Other: " + e.data.substring(6,e.data.length));
        MathJax.Hub.Queue(["Typeset",MathJax.Hub,"messagetable"]);
    } else {
        addMsg("Other: " + e.data);
    }
}


$(document).ready(function() {
    $("#sendbutton").click(function() {
        console.log("Sending message");
        msg = $("#inputfield").val();
        $("#inputfield").val('');
        connection.send(msg);
    });

});

// Delicious!
function addMsg(message) {
    $("#messagetable").append('<tr><td>'+message+'</td></tr>');
}