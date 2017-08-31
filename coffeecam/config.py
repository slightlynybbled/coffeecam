"""
Parses the supplied configuration file
"""

import sys
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# defaults if the element is not specified
SHOW_STATS = True
HOST_NAME = 'coffeeCam'
FRAME_RATE = 2
RESOLUTION = '640x480'
CAMERA = 'pi'
USE_CLIENT_TIME = False


def parse_config():
    global SHOW_STATS, HOST_NAME, FRAME_RATE, RESOLUTION, CAMERA

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

    logger.debug('config: {}'.format(config))

    # load each parameter from the config file (if present)
    if config.get('stats'):
        SHOW_STATS = config.get('stats')

    if config.get('host'):
        HOST_NAME = config.get('host')

    if config.get('framerate'):
        FRAME_RATE = int(config.get('framerate'))

    if config.get('resolution'):
        RESOLUTION = config.get('resolution')

    if config.get('camera'):
        CAMERA = config.get('camera')

    if config.get('client time'):
        CAMERA = config.get('client time')

    logger.debug('SHOW_STATS: {}'.format(SHOW_STATS))
    logger.debug('HOST_NAME: {}'.format(HOST_NAME))
    logger.debug('FRAME_RATE: {}'.format(FRAME_RATE))
    logger.debug('RESOLUTION: {}'.format(RESOLUTION))
    logger.debug('CAMERA: {}'.format(CAMERA))
    logger.debug('USE_CLIENT_TIME: {}'.format(USE_CLIENT_TIME))

    return
