"""
Parses the supplied configuration file
"""

import sys
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

SHOW_STATS = True
HOST_NAME = 'coffeeCam'


def parse_config():
    global SHOW_STATS, HOST_NAME

    if '-c' not in sys.argv and '--config' not in sys.argv:
        logger.error('configuration not found, using defaults')
        return

    if '-c' in sys.argv:
        index_of_config = sys.argv.index('-c') + 1
    elif '--config' in sys.argv:
        index_of_config = sys.argv.index('--config') + 1

    logging.debug('config index: {} ({})'.format(index_of_config, sys.argv[index_of_config]))

    with open(sys.argv[index_of_config], 'r') as f:
        config = json.loads(f.read())

    if config.get('stats'):
        SHOW_STATS = config.get('stats')

    if config.get('host'):
        HOST_NAME = config.get('host')

    return
