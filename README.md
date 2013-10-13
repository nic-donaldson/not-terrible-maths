not-terrible-maths
==================

Little side project to try and stop me from crying when I want to communicate maths over the internet.

Installation
============

This project (currently) requires mod_pywebsocket.

    pip install mod_pywebsocket
    
Once that is done, symlink and make executable the standalone.py file from the mod_pywebsocket package.
For me that went something like this (using virtualenv):

    ln --symbolic ../lib/python2.7/site-packages/mod_pywebsocket/standalone.py standalone.py
    sudo chmod ug+x standalone.py


Running
=======

Try:

    ./run_server.sh <port>
   
At the moment port should be 9001 as that is the hardcoded value in the client. (sloppy, I know)
The latest version expects the static files to be served from a web server now, as it tries to connect to the websockets server on the same domain. You can use Python's built in web server module to do this:

    python2 -m SimpleHTTPServer

or

    python -m SimpleHTTPServer

from the client directory, depending on how your system is set up.

To-do
=====

* Figure out why the server throws an error occasionally on connects/disconnects
* Prettify the client
* Define a protocol for messages
* Start messing around with image transfer/canvas trickery
* Set mathjax to only render new messages
* Add link autorecognition in chat
* Implement image sharing
* Add description of project to readme!
