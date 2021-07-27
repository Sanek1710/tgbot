import logging
import os

LOG_FILE = os.getenv('LOG_FILE', 'log.txt')

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename=LOG_FILE)

LOG = logging.getLogger()