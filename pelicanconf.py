#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
# import extended_sitemap

AUTHOR = u'Bagas Abisena Swastanto'
SITENAME = u'abisena.me'
SITEURL = ''

PATH = 'content'

# PLUGINS
<<<<<<< HEAD
PLUGIN_PATHS = ['~/dev/github/pelican-plugins']
PLUGINS = ['extended_sitemap']
=======
PLUGIN_PATHS = ['/Users/bagas/dev/github/pelican-plugins/']
PLUGINS = ['extended_sitemap', 'pelican-flickr']
>>>>>>> gallery

# DATE TIME CONFIGURATION
TIMEZONE = 'Europe/Amsterdam'
CURRENT_DATE = datetime.now().isoformat()

DEFAULT_LANG = u'en'

# static files
<<<<<<< HEAD
STATIC_PATHS = ['images', 'js', 'data', 'extra/CNAME', 'extra/robots.txt']
=======
STATIC_PATHS = ['images', 'js', 'data', 'lightbox', 'raw', 'extra/CNAME', 'extra/robots.txt']
>>>>>>> gallery
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/robots.txt': {'path': 'robots.txt'}}

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
          ('Github', 'http://www.github.com/bagasabisena'),
          ('Instagram', 'http://www.instagram.com/bagasabisena'),)

DISPLAY_TAGS_INLINE = True

# Github
GITHUB_USER = 'bagasabisena'
GITHUB_SKIP_FORK = True

DISPLAY_ARTICLE_INFO_ON_INDEX = True

# ABOUT ME
ABOUT_ME = 'Master student Computer Science in TU Delft, NL.'
AVATAR = 'images/bagas2.jpg'
GRAVATAR_IMAGE = 'http://www.gravatar.com/avatar/f7b09b54c898a2db1bc7a20c74827bb6.png'

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

<<<<<<< HEAD
=======
# THUMBNAILER SETTING
IMAGE_PATH = 'gallery'
THUMBNAIL_DIR = 'thumbnails'

# Flickr Plugin
FLICKR_API_KEY = '8f4133f9de401e93cadfc9fc5ea17ed5'
FLICKR_API_SECRET = 'd8430ac165f59da0'
FLICKR_USER = '128667897@N04'
FLICKR_OUTPUT_DIRNAME = 'flickr'
FLICKR_UPDATE = True

>>>>>>> gallery
# SITEMAP
# EXTENDED_SITEMAP_PLUGIN = {
#     'priorities': {
#         'index': 1.0,
#         'articles': 0.8,
#         'pages': 0.5,
#         'others': 0.4
#     },
#     'changefrequencies': {
#         'index': 'daily',
#         'articles': 'weekly',
#         'pages': 'monthly',
#         'others': 'monthly',
#     }
# }
