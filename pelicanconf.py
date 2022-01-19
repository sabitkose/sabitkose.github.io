AUTHOR = 'Sabit'
SITENAME = "Sabit's Blog"
SITEURL = "https://sabitkose.github.io"

PATH = 'content'

TIMEZONE = 'Turkey'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', 'https://sabitkose.github.io/'),)

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/sabitkose/'),
          )

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


PLUGIN_PATHS = ['C:\\Users\\skose\\pelican-plugins']
PLUGINS = ['sitemap']

SITEMAP = {
    "format": "txt",
    "exclude": ["tag/", "category/", "author/", "tags.html", "categories.html", "authors.html", "archives.html" ],
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}