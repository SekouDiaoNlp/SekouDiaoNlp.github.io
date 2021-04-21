#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'SekouDiaoNlp'
SITENAME = "Python, Natural Language Processing and AI technologies"
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['articles', ]

# Defines the landing page
LANDING_PAGE_TITLE = "I use Python to develop Computational Linguistics and AI technologies."

COMMENTBOX_PROJECT = '5690486803136512-proj'

PROJECTS = [{
    'name': 'mlconjug3',
    'url': 'https://github.com/SekouDiaoNlp/mlconjug3',
    'description': 'A Python library to conjugate verbs in French, English, Spanish, Italian, Portuguese and Romanian '
                   '(more soon) using Machine Learning techniques.'},
    {'name': 'lyricsmaster3',
     'url': 'https://github.com/SekouDiaoNlp/lyricsmaster3',
     'description': 'LyricsMaster is a library for downloading lyrics from multiple lyrics providers.'},
    {'name': 'potranslator3',
     'url': 'https://github.com/SekouDiaoNlp/potranslator3',
     'description': 'A package to easily translate po and pot files in any language supported by Google Translate.'},
]

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['C:/Users/user/Documents/Pelican_Plugins']
PLUGINS = ['extract_toc', 'neighbors']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.toc': {}
    }
}

# MARKDOWN = (['toc'])

# Blogroll
LINKS = (('GitHub Profile', 'https://github.com/SekouDiaoNlp'),
         ('Python Packages on PyPi', 'https://pypi.org/user/SekouDiaoNlp/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/SekouDiaoNlp', 'My Github repositories'),
          )

DEFAULT_PAGINATION = 10

THEME = 'C:/Users/user/Documents/Pelican_Themes/elegant-master'

APPLAUSE_BUTTON = True

ARTICLE_ORDER_BY = 'reversed-date'
PAGE_ORDER_BY = 'order'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
