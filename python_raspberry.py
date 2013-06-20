#raspberry pi script 2
#with continues looping
#TODO : Add bluetooth support!

#!/usr/bin/python
# Measure distance using an ultrasonic module
# in a loop.
# -----------------------
# Import required Python libraries GPIO and Sound Modules
# Implemented using PyGame sound library
# -----------------------
import time
import RPi.GPIO as GPIO
from pygame import mixer

# -----------------------
# Define some functions
# -----------------------

def measure():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)	#initialising the Ultrasonic sensor 
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()

  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2
#calculate the distance by using the difference between time #elapsed between start and stopping point. 

  return distance


# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# At the moment, play the sound whenever the distance is less than
# 20 cms. Frequency is preset to 44100, to get max compatibility
try:

  while True:
    mixer.init(frequency=44100)
    s1 = mixer.Sound('rgong2.wav')
    distance = measure()
    if distance < 20 :    
	s1.play()
	time.sleep(2)
	s1.stop()
    print "Distance : %.1f" % distance
    mixer.quit()
    time.sleep(1)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()



