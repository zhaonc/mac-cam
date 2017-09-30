#! /usr/bin/env python

"""
This file should be used with applications like uwsgi.

In the uwsgi config, you will need to include the following in the [uwsgi] section.

module = wsgi:router

"""

from app.router import router
