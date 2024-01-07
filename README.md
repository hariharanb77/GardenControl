# GardenControl

## About the project
This software is used to automate events like watering plants using raspberry pi. This code 
uses the GPIO pin of the raspberry pi to drive a solenoid valve that controls the water flow
to the garden.

## Starting the service

To start this service as part of startup, upsate the <path> value in **gardenControl.service**
file and place the file in /etc/systemd/system folder. Once this is done, you can start/stop
the service with the following commands

```
> sudo systemctl start gardenControl
> sudo systemctl stop gardenControl
```

To start the service as part of system startup automatically, use the following command
'''
> sudo systemctl enable gardenControl
'''

Use the following command to check the status of the service
'''
> sudo systemctl status gardenControl
'''

## Configuration
Update the **resourceConfiguratoin.json** file to control when to change the status of your resource.
In this example, one tap resource is used which is opened and closed daily at a specified time.

Update the **config.py** file to control the location of the log file and log level. The file path 
of the **resourceConfig.json** file has to be updated to reflect the actual path.



