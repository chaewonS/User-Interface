import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

StartPin = 5
DestiPin = 17

GPIO.setup(StartPin, GPIO.IN)
GPIO.setup(DestiPin, GPIO.IN)

def detect_start():
    while True:
        if GPIO.input(StartPin) == 0:
            print("시작 버튼 눌림")
            return 1
        else:
            print("point1")
            time.sleep(0.2)

def set_destination():
    while True:
        if GPIO.input(DestiPin) == 0:
            print("목적지 버튼 눌림")
            return 1
        else:
            print("point2")
            time.sleep(0.2)
