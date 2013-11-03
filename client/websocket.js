var connection;
var messagecontainer;
var maths_prefix = "m:";

if (document.location.hostname != "") {
    connection = new WebSocket('ws://' + document.location.hostname + ':9001/connect', []);
} else {
    connection = new WebSocket('ws://localhost:9001/connect', []);
}

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
    if (e.data.indexOf(maths_prefix) === 0) {
        addMsg("Them: " + e.data.substring(6,e.data.length));
        MathJax.Hub.Queue(["Typeset",MathJax.Hub,$("#messagebox div:last")[0]]);
    } else {
        addMsg("Them: " + e.data);
    }
}


$(document).ready(function() {

    $("#inputfield").keypress(function(event) {
        if (event.which == 13 && !event.shiftKey) {
            event.preventDefault();

            console.log("Sending message");
            msg = $("#inputfield").val();
            $("#inputfield").val('');
            connection.send(msg);
            addMsg("You: " + msg);

            if (msg.indexOf(maths_prefix) === 0) {
                MathJax.Hub.Queue(["Typeset",MathJax.Hub,$("#messagebox div:last")[0]]);
            }
        }
    });

    messagecontainer = document.getElementById("messagecontainer");

});

// Delicious!
function addMsg(message) {
    // If message container already at bottom or not overflowing, set to bottom
    //-- at bottom or not overflowing => scrollheight - scrolltop == height
    if(messagecontainer.scrollHeight - messagecontainer.scrollTop == $(messagecontainer).height()) {
        $("#messagebox").append('<div class="message">' + message + '</div>');
        messagecontainer.scrollTop = messagecontainer.scrollHeight - $(messagecontainer).height();
    } else {
        $("#messagebox").append('<div class="message">' + message + '</div>');
    }
}
