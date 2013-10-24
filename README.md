not-terrible-maths
==================

Little side project to try and stop me from crying when I want to communicate maths over the internet.

Installation
============

This project requires tornado or mod_pywebsocket (no longer supported, check out older versions).

    pip install tornado
    
Is all you should need.

Running
=======

    python server/tornado_server.py

Will start a server on port 9001.

The latest version expects the static files to be served from a web server now, as it tries to connect to the websockets server on the same domain. You can use Python's built in web server module to do this:

    python2 -m SimpleHTTPServer

or

    python -m SimpleHTTPServer

from the client directory, depending on how your system is set up.

To-do
=====

* Add web serving stuff to tornado server as well
* Prettify the client
* Define a protocol for messages
* Start messing around with image transfer/canvas trickery
* Set mathjax to only render new messages
* Add link autorecognition in chat
* Implement image sharing
* Add description of project to readme!
