#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nick Bettison'
SITENAME = 'LINICKX.com'
SITEURL = 'http://linickx.local:8080'
FEED_DOMAIN = SITEURL

PATH = 'content'

DELETE_OUTPUT_DIRECTORY = False
OUTPUT_PATH = 'output/'

DEFAULT_METADATA = (('generator', 'pelican'),)

EXTRA_PATH_METADATA = {
    'webmaster/robots.txt': {'path': 'robots.txt'},
    'webmaster/humans.txt': {'path': 'humans.txt'},
    'webmaster/favicon.ico': {'path': 'favicon.ico'},
    'webmaster/google79e72bccebf05add.html': {'path': 'google79e72bccebf05add.html'},
    'webmaster/googlehostedservice.html': {'path': 'googlehostedservice.html'},
    'webmaster/BingSiteAuth.xml': {'path': 'BingSiteAuth.xml'},
    'webmaster/LiveSearchSiteAuth.xml': {'path': 'LiveSearchSiteAuth.xml'},
    'webmaster/y_key_36fed1237da329f9.html': {'path': 'y_key_36fed1237da329f9.html'},
    'webmaster/jTMTEjjrFC9vR46tPtaSvPchOwU.txt': {'path': 'jTMTEjjrFC9vR46tPtaSvPchOwU.txt'},
    'webmaster/linickx.com80d2b5324af9e93ab4bf407ac602b69b7f943ef0.txt': {'path': 'linickx.com80d2b5324af9e93ab4bf407ac602b69b7f943ef0.txt'},
    }

STATIC_PATHS = ['images', 'files', 'webmaster']
ARTICLE_EXCLUDES = ['files', 'webmaster']


THEME = 'themes/linickx'
PAGINATED_DIRECT_TEMPLATES = ('index', 'tag', 'archives', 'period_archives',)

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'
DEFAULT_PAGINATION = 10

# Feed generation

FEED_RSS_SAVE_AS = None
FEED_ATOM_SAVE_AS = None
TAG_FEED_RSS_SAVE_AS  = None
TAG_FEED_ATOM_SAVE_AS = None

CATEGORY_FEED_RSS_SAVE_AS  = None
CATEGORY_FEED_ATOM_SAVE_AS = None
FEED_ALL_ATOM_SAVE_AS = None
TRANSLATION_FEED_ATOM_SAVE_AS = None
AUTHOR_FEED_ATOM_SAVE_AS = None
AUTHOR_FEED_RSS_SAVE_AS = None
FEED_MAX_ITEMS = 10


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = '{slug}'
PAGE_URL = '{slug}'
TAG_URL = 'tag/{slug}'
AUTHOR_URL = 'author/{slug}'
CATEGORY_URL = 'category/{slug}'
YEAR_ARCHIVE_URL = "date/{date:%Y}"
MONTH_ARCHIVE_URL = "date/{date:%Y}/{date:%m}"
DAY_ARCHIVE_URL = False

# Settings for S3 or RackSpace Cloud files - If I ever get that far!
# PAGE_SAVE_AS = '{slug}/index.html'
# ARTICLE_SAVE_AS = '{slug}/index.html'
# TAG_SAVE_AS = 'tag/{slug}/index.html'
# AUTHOR_SAVE_AS = False
# CATEGORY_SAVE_AS = False

# Settings for nginx
INDEX_SAVE_AS = 'blog.html'
PAGE_SAVE_AS = 'content/{slug}.html'
ARTICLE_SAVE_AS = 'content/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
ARCHIVES_SAVE_AS = 'content/archives.html'
YEAR_ARCHIVE_SAVE_AS = 'content/date/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS ='content/date/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = False


PAGINATION_PATTERNS = (
    (1, '{name}', 'content/pagination/{name}.html'),
    (2, '{name}/page/{number}/', 'content/pagination/{name}-{number}.html'),
)

# Theme - TAG Cloud.
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 50


# LINICKX Custom Vars
LINICKX_FOOTER = True

PLUGINS=['plugins.assets']
