import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pirPin = 23

GPIO.setup(pirPin, GPIO.IN)


while True:
    if GPIO.input(pirPin):
        print("Motion detected!")

    else:
        print("No motion")

    time.sleep(0.2)