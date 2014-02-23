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

You will need to write a config file before using the server. A sample config file is included in sample_config.ini . Save the new config file to config.ini . Then:


    python3.3 server/tornado_server.py

Will start a server on the port specified in config.ini. Then head to localhost:port in your browser and hopefully it will work!

To-do
=====

* Make autoscroll work with maths
* Prettify the client
* Define a protocol for messages
* Start messing around with image transfer/canvas trickery
* Add link autorecognition in chat
* Implement image sharing
* Add description of project to readme!
* Make static file serving less lame
