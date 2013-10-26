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

Will start a server on port 9001. Then head to localhost:9001 in your browser and hopefully it will work!

To-do
=====

* Prettify the client
* Define a protocol for messages
* Start messing around with image transfer/canvas trickery
* Set mathjax to only render new messages
* Add link autorecognition in chat
* Implement image sharing
* Add description of project to readme!
* Make static file serving less lame