prior = None
pairs = {}

def web_socket_do_extra_handshake(request):
    global prior
    global pairs

    if prior == None:
        prior = request
    else:
        pairs[prior] = request
        pairs[request] = prior
        prior.ws_stream.send_message("1:Connected to another!")
        prior = None

def web_socket_transfer_data(request):
    global prior
    global pairs

    if prior == None:
        request.ws_stream.send_message("2: Connected to another!")

    while True:
        line = request.ws_stream.receive_message()
        if line =="debug":
            print("Prior: " + str(prior))
            print("Pairs: " + str(pairs))
        if line:
            if request in pairs:
                pairs[request].ws_stream.send_message(line)
            else:
                request.ws_stream.send_message("No friend yet, :(")


def web_socket_passive_closing_handshake(request):
    global prior
    global pairs

    if request in pairs:
        pairs[request].ws_stream.send_message("Other has disconnected")
        if prior == None:
            prior = pairs[request]
            del pairs[request]
            del pairs[prior]
        else:
            pairs[pairs[request]] = prior
            pairs[prior] = pairs[request]
            pairs[pairs[request]].ws_stream.send_message("New partner connected")
            pairs[prior].ws_stream.send_message("New partner connected")
            del pairs[request]
            prior = None
    else:
        if prior == request:
            prior = None

    print("Web socket closed, :)")
    print("Prior: " + str(prior))
    print ("Pairs: " + str(pairs))

