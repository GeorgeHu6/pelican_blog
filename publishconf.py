import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = ""
RELATIVE_URLS = False


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'pymdownx.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
