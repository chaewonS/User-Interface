import RPi.GPIO as GPIO
import time

import TTS
from TTS import txt_reader

# GPIO.setmode(GPIO.BCM)

# pirPin = 23

# GPIO.setup(pirPin, GPIO.IN)

def detecting(pirPin):
    while True:
        if GPIO.input(pirPin):
        # 사람이 2초 이상 감지되면 등으로 조건 추가
        # 민감도가 너무 높음
            txt_reader("ment1")
            return 1
        else:
            print("No motion")
            return 0

# GPIO.cleanup()