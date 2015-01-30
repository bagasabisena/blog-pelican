#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bagas Abisena Swastanto'
SITENAME = u'abisena.me'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

# static files
STATIC_PATHS = ['images', 'js', 'data', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'http://www.twitter.com/bagasabisena'),
          ('Flickr', 'http://www.flickr.com/bagasabisena'),
          ('Github', 'http://www.github.com/bagasabisena'),)

DISPLAY_TAGS_INLINE = True

# Github
GITHUB_USER = 'bagasabisena'
GITHUB_SKIP_FORK = True

DISPLAY_ARTICLE_INFO_ON_INDEX = True

# ABOUT ME
ABOUT_ME = 'Master student Computer Science in TU Delft, NL.'
AVATAR = 'images/bagas2.jpg'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME
THEME = '../template/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
HIDE_SITENAME = False
SITELOGO = False
BANNER = 'theme/images/banner4.jpg'
BANNER_SUBTITLE = 'A view from the afternoon'

# FAVICON
FAVICON = 'theme/images/kribo.ico'
