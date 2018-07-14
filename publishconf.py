#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.arteteco.com'
RELATIVE_URLS = False
OUTPUT_RETENTION = [".git", "CNAME"]
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/%s.atom.xml'


DELETE_OUTPUT_DIRECTORY = True

I18N_SUBSITES = {
    'it': {
        'SITENAME': 'Arteteco',
        }
    }



# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
