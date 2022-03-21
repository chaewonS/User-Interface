import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

pin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

# # while True:
# GPIO.output(pin, True)
# time.sleep(1)
# GPIO.output(pin, False)



# PWM
myPwm = GPIO.PWM(pin, 1000) # pin, frequency
myPwm.start(50)

GPIO.output(pin, True)

# 출력값 변경 (0~100%)
# myPwm.ChangeDutyCycle(75)
# time.sleep(2)

# Frequency  변경 (Hz)
# myPwm.ChangeFrequency(1500)

for i in range(100):
	myPwm.ChangeDutyCycle(i)
	time.sleep(0.02)
	
#swPWM 정지
myPwm.stop()

GPIO.output(pin, False)