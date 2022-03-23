import RPi.GPIO as GPIO
import time

from find_user import *
from TTS import *
from button import *

PIR = 23
VIB = 16
START_BUTT = 5
DESTI_BUTT = 17
DEST = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(VIB, GPIO.OUT)
GPIO.setup(START_BUTT, GPIO.IN)
GPIO.setup(DESTI_BUTT, GPIO.IN)

def intro():
    USING = 0   # 사용 - 1 / 대기 - 0

    while True:
        if USING == 1:
            print("1")
            # 스레딩 처리하기. 음성 듣는 중에도 버튼 누르면 동작하도록
            
            # 목적지 버튼 여러개, 파라미터 사용
            DEST = set_destination()        # 목적지 정보 획득
            perform(DEST)

        elif USING == 0:
            print("0")
            USING = detecting(PIR)

def perform(DEST):
    while True:
        print("이제 운행 파트:",DEST)
        time.sleep(0.2)

if __name__ == "__main__":
    intro()
    GPIO.cleanup()
