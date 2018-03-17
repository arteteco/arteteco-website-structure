#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals



### WEBSITE

AUTHOR = u'Arteteco'
SITENAME = u'Arteteco'
SITEURL = ''
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = u'en'

## PATHS

PATH = 'content'
STATIC_PATHS = ['images']
LOAD_CONTENT_CACHE = False
IMAGE_PATH='content/images/'
PAGE_PATHS = ['pages']
PATH = 'content'

### THEME

THEME = 'pelican-bootstrap3'
DISPLAY_PAGES_ON_MENU=False
DISPLAY_CATEGORIES_ON_MENU=False
HIDE_SIDEBAR=True
CC_LICENSE="CC-BY-SA"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
