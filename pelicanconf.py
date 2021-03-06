#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals



### GENERAL

AUTHOR = u'Arteteco'
SITENAME = u'Arteteco'
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = u'en'
RELATIVE_URLS = True
AUTHORS_SAVE_AS = ''
DEFAULT_DATE_FORMATS='%dd/%mm/%yyyy'

# feed
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

### PUBLISHING

OUTPUT_RETENTION = [".git", "CNAME"]
DELETE_OUTPUT_DIRECTORY = False
DEFAULT_CATEGORY = 'misc'


## PATHS

PATH = 'content'
STATIC_PATHS = ['images']
LOAD_CONTENT_CACHE = False
IMAGE_PATH='content/images/'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'


#PAGE_PATHS = ['pages']

### THEME & APPARANCE

THEME = 'pelican-bootstrap3'
DISPLAY_PAGES_ON_MENU=True
DISPLAY_CATEGORIES_ON_MENU=False
HIDE_SIDEBAR=True
CC_LICENSE="CC-BY-SA"
DEFAULT_PAGINATION = 10
SHOW_ARTICLE_AUTHOR=False
SHOW_ARTICLE_CATEGORY=True
SHOW_DATE_MODIFIED=True
DISPLAY_ARTICLE_INFO_ON_INDEX=False

### PLUGINS

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'tipue_search', 'tag_cloud', 'series']


# i18n_subsites
# required by pelican-bootstrap3

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_SUBSITES = {
    'it': {
        'SITENAME': 'Arteteco',
        'STATIC_PATHS': ['../images']
        }
    }



# tipue_search
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# tag_cloud
TAG_CLOUD_STEPS = 1
TAG_CLOUD_SORTING = 'alphabetically'
TAG_CLOUD_BADGE = True
DISPLAY_TAGS_ON_SIDEBAR=False

# photos
# with translation it creates double folder, waiting to fix to activate translation
"""
PHOTO_LIBRARY = "content/galleries"
PHOTO_GALLERY = (4096, 4096, 100)
PHOTO_ARTICLE = (768, 768, 80)
PHOTO_THUMB = (512, 512, 60)
PHOTO_RESIZE_JOBS = 5
PHOTO_EXIF_COPYRIGHT = 'CC-BY-SA'
"""


# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
