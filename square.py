#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

# at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

print 'taking off'
drone.take_off(5.0)

print ' going along the setpoints'

drone.position_set(x=6.5, y=0, z=0, body_frame=True)
drone.position_set(x=0, y=6.5, z=0, body_frame=True)
drone.position_set(x=-6.5, y=0, z=0,body_frame=True)
drone.position_set(x=0, y=-6.5, z=0,body_frame=True)

print 'Landing'
drone.land(async=False)

# shutdown the instance
drone.disconnect()
