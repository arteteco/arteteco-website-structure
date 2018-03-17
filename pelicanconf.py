#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals



### WEBSITE

AUTHOR = u'Arteteco'
SITENAME = u'Arteteco'
SITEURL = ''
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = u'en'
RELATIVE_URLS = True

## PATHS

PATH = 'content'
STATIC_PATHS = ['images']
LOAD_CONTENT_CACHE = False
IMAGE_PATH='content/images/'
PAGE_PATHS = ['pages']
PATH = 'content'

### THEME & APPARANCE

THEME = 'pelican-bootstrap3'
DISPLAY_PAGES_ON_MENU=False
DISPLAY_CATEGORIES_ON_MENU=False
HIDE_SIDEBAR=True
CC_LICENSE="CC-BY-SA"
MENUITEMS = (('<i class="fa fa-flask" style="font-size:18px"></i> Projects', '/pages/projects.html'),
			 ('<i class="fa fa-pencil" style="font-size:18px"></i> Articles', '/pages/articles.html'),)
DEFAULT_PAGINATION = 10
SHOW_ARTICLE_AUTHOR=False
SHOW_ARTICLE_CATEGORY=True
SHOW_DATE_MODIFIED=True

### PLUGINS

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'tipue_search', 'tag_cloud']

# i18n_subsites
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# tipue_search
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# tag_cloud
TAG_CLOUD_STEPS = 1
TAG_CLOUD_SORTING = 'alphabetically'
TAG_CLOUD_BADGE = True




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
