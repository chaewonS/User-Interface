import RPi.GPIO as GPIO
import time

pin = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

# # while True:
# GPIO.output(pin, True)
# time.sleep(1)
# GPIO.output(pin, False)

def once():
	GPIO.output(pin, True)
	time.sleep(3)
	GPIO.output(pin, False)

# PWM
myPwm = GPIO.PWM(pin, 1000) # pin, frequency
myPwm.start(50)

GPIO.output(pin, True)

for i in range(100):
	myPwm.ChangeDutyCycle(i)	#0~100%
	time.sleep(0.02)
	
myPwm.stop()

GPIO.output(pin, False)
GPIO.cleanup()

# Frequency  변경 (Hz)
# myPwm.ChangeFrequency(1500)