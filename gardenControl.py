#!/usr/bin/python3

import config
from tapController import TapController
import json
import schedule
import time

resources = []

def loadResources():
    f = open(config.resourceConfigFile)
    resourceData = json.load(f)

    for resource in resourceData['GardenResources']:
        if (resource['status'] != 'ENABLED'):
            continue
        if (resource['type'] == "Tap"):
            resources.append(TapController(resource))

def do_main_program():
    loadResources()

    while(True):
        schedule.run_pending()
        time.sleep(1)

do_main_program()
    



#output = open(config.logFile, 'w+')
#with daemon.DaemonContext(stdout=output, stderr=output):
#    do_main_program()
