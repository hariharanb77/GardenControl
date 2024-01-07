#!/usr/bin/python3

import config
from tapController import TapController
from config import logger
import json
import schedule
import time
import daemon
import logging
import signal

resources = []

def loadResources():
    f = open(config.resourceConfigFile)
    resourceData = json.load(f)

    for resource in resourceData['GardenResources']:
        if (resource['status'] != 'ENABLED'):
            continue
        if (resource['type'] == "Tap"):
            logger.info("Loading resource %s" %(resource['resource']))
            resources.append(TapController(resource))

def handle_sigterm(sig, frame):
    for resource in resources:
        resource.cleanUp()
    logger.close()
    exit(0)

def do_main_program():
    fhandler = logging.FileHandler(filename=config.logFile, mode='a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
    logger.setLevel(config.logLevel)

    logger.info("Starting garden control service")
    
    loadResources()
    signal.signal(signal.SIGTERM, handle_sigterm)

    while(True):
        logger.debug("garden control waking up to check for events")
        schedule.run_pending()
        time.sleep(60)

with daemon.DaemonContext():
    do_main_program()
