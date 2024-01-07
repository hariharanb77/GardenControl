from gpiozero import LED
import schedule
from config import logger


class TapController:
    resource = ""
    name     = ""
    events   = []
    defaultState = "CLOSED"

    def __init__(self, resourceData):
        self.resource = LED(resourceData['pinNumber'])
        self.resource.on()
        self.name = resourceData['resource']
        self.events = resourceData['events']
        self.defaultState = resourceData['defaultState']

        for event in self.events:
            kwargs = {'newState':event['state']}
            schedule.every().day.at(event['time']).do(self.changeState, **kwargs)


    def changeState(self, newState):
        if (newState == "OPEN"):
            logger.info("Changing state of %s to OPEN" %(self.name))
            self.resource.off()
        elif (newState == "CLOSED"):
            logger.info("Changing state of %s to CLOSED"  %(self.name))
            self.resource.on()

    def cleanUp(self):
        logger.error("abnormal exit cleaning up resource %s" %(self.name))
        self.changeState(self.defaultState)
