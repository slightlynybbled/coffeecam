"""
Parses the supplied configuration file
"""

import sys
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


if '-c' not in sys.argv and '--config' not in sys.argv:
    logger.error('!!! configuration not found !!!')
    sys.exit(1)

if '-c' in sys.argv:
    index_of_config = sys.argv.index('-c') + 1
elif '--config' in sys.argv:
    index_of_config = sys.argv.index('--config') + 1

logging.debug('config index: {} ({})'.format(index_of_config, sys.argv[index_of_config]))

with open(sys.argv[index_of_config], 'r') as f:
    config = json.loads(f.read())

MEDIA_URL = config.get('web').get('media url')

if not MEDIA_URL.startswith('/'):
    MEDIA_URL = '/' + MEDIA_URL
if not MEDIA_URL.endswith('/'):
    MEDIA_URL = MEDIA_URL + '/'

MEDIA_DIR = config.get('local').get('directory')

if not MEDIA_DIR.startswith('/'):
    MEDIA_DIR = '/' + MEDIA_DIR
if not MEDIA_DIR.endswith('/'):
    MEDIA_DIR = MEDIA_DIR + '/'

MEDIA_NAME = config.get('local').get('name')

HOST_NAME = config.get('web').get('host')
if HOST_NAME is None:
    HOST_NAME = 'coffeecam on flask, humanize, watress, and python'

SHOW_STATS = config.get('web').get('stats')
SHOW_STATS = True if SHOW_STATS else False
