# Capture user-drawn shape and process it with Python

A proof-of-concept for capturing a user-drawn shape which can then be
processed using Python's `pillow` library.

* uses [Flask](http://flask.pocoo.org) for the web framework
* [jQuery](https://jquery.com) is served via Cloudflare's CDN

To run, do something like (see Flask docs for details):

    $ export FLASK_APP=app.py
    $ flask run

Built for Zhiyuan at RHUL.