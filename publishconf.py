#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.linickx.com'
FEED_DOMAIN = SITEURL
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_PATH = 'public_html/'

FEED_RSS_SAVE_AS = 'content/feed/rss.xml'
FEED_RSS_URL = 'feed'
FEED_ATOM_SAVE_AS = 'content/feed/atom.xml'
FEED_ATOM_URL = 'feed/atom'
TAG_FEED_RSS_SAVE_AS  = 'content/feed/%s.rss.xml'
TAG_FEED_RSS_URL  = 'tag/%s/feed'
TAG_FEED_ATOM_SAVE_AS = 'content/feed/%s.atom.xml'
TAG_FEED_ATOM_URL  = 'tag/%s/feed/atom'
CATEGORY_FEED_RSS_SAVE_AS  = None
CATEGORY_FEED_ATOM_SAVE_AS = None
FEED_ALL_ATOM_SAVE_AS = None
TRANSLATION_FEED_ATOM_SAVE_AS = None
AUTHOR_FEED_ATOM_SAVE_AS = None
AUTHOR_FEED_RSS_SAVE_AS = None
FEED_MAX_ITEMS = 10



# Plugins
PLUGINS=['plugins.sitemap', 'plugins.assets', 'minify', 'plugins.gzip_cache']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'weekly',
        'pages': 'yearly'
    }
}

# GA
GOOGLE_ANALYTICS = "UA-76334-1"
