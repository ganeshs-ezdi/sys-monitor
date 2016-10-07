#! /usr/bin/python

import logging
import ConfigParser
import random
import time

config = ConfigParser.ConfigParser()
config.read('config.ini')

useRandom = ('True' == config.get('sleep','random'))
minInMillis = float(config.get('sleep','minInMillis'))
maxInMillis = float(config.get('sleep','maxInMillis'))

messages = [line.strip() for line in open(config.get('messages','filename')).readlines()]
minId = int(config.get('ids', 'minId'))
maxId = int(config.get('ids', 'maxId'))


# Press Ctrl+C to close
def do_logging():
    c,t = random.randint(minId, maxId), random.randint(minId, maxId)
    idx = random.randint(0, len(messages)-1)
    logging.info( 'Corel: %d Trans: %d %s' % (c,t, messages[idx]) )


def do_sleep():
    # delay = random.uniform(minInMillis/1000.0, maxInMillis/1000.0)
    # time.sleep(delay)
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    while True:
        do_logging()
        do_sleep()

