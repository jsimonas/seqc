__author__ = 'ambrose'

import logging
from datetime import datetime


def setup_logger():
    """create a simple log file in the cwd to track progress and any errors"""
    logging.basicConfig(filename='seqc.log', level=logging.DEBUG)


def info(message):
    """print a timestamped update for the user"""
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ':' + message)


def exception():
    logging.exception(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ':main:')
