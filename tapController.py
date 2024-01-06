from gpiozero import LED
import schedule


class TapController:
    resource = ""
    name     = ""
    events   = []

    def __init__(self, resourceData):
        self.resource = LED(resourceData['pinNumber'])
        self.resource.on()
        self.name = resourceData['resource']
        self.events = resourceData['events']

        for event in self.events:
            kwargs = {'newState':event['state']}
            schedule.every().day.at(event['time']).do(self.changeState, **kwargs)


    def changeState(self, newState):
        if (newState == "OPEN"):
            print("Changing state of %s to OPEN" %(self.name))
            self.resource.off()
        elif (newState == "CLOSED"):
            print("Changing state of %s to CLOSED"  %(self.name))
            self.resource.on()
