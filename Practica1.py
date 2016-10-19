import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

led = 17
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 1)
time.sleep(1)
GPIO.output(led, 0)
time.sleep(1)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 1)
time.sleep(1)
GPIO.output(led, 0)
time.sleep(1)

GPIO.cleanup()
