import RPi.GPIO as GPIO
import time

from find_user import detecting
from TTS import txt_reader
from button import detect_start
from button import set_destination

PIR = 23
VIB = 16
START_BUTT = 5
DESTI_BUTT = 17

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
            if detect_start() == 1:
                txt_reader("ment2")
            if set_destination() == 1:
                txt_reader("ment3")
            perform()
        elif USING == 0:
            print("0")
            USING = detecting(PIR)

def perform():
    print("이제 운행 파트")

if __name__ == "__main__":
    intro()
