#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Veronica Brandt'
SITENAME = u'Brandt Lab'
SITEURL = ''

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = u'en'

THEME = "./theme/mybuiltexts"

# Where to look for plugins
PLUGIN_PATH = '../pelican-plugins'
# Which plugins to enable
PLUGINS = ['better_figures_and_images']
# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True
#PLUGINS = [u"pelican.plugins.disqus_static"]

DISQUS_SITENAME = u'brandtlab'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Peter', 'http://peterbrandt.com.au/'),
#          ('Veronica', 'http://veromarybrrr.wordpress.com'),
#          ('windpower', 'http://diy.org/windpower'),
#          ('M Loki', 'http://diy.org/mischiefloki'),
#          ('H Hunter', 'http://diy.org/huskyhunter'),
#          ('M Swoop', 'http://diy.org/misterswoop'))

# Social widget
#SOCIAL = (('facebook', 'http://www.facebook.com/veromarybrrr'),
#          ('twitter', 'http://twitter.com/veromarybrrr'),
#          ('github', 'http://veromary.github.com'),
#          ('google-plus', 'https://plus.google.com/u/0/103892341173448817529/'))
#EMAIL = 'allofus@brandt.id.au'

DEFAULT_PAGINATION = 10

COLOPHON = True
COLOPHON_TITLE = 'The Brandts'
COLOPHON_CONTENT = 'are a family of seven living in the Blue Mountains near Sydney, Australia. <a href="http://peterbrandt.com.au">Peter Brandt</a>'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'pdf']

