import RPi.GPIO as GPIO
import time
from TTS import txt_reader

from find_user import *
from TTS import *
from button import *
from ultrasound import *
from vibration import *

PIR = 23
VIB = 16
START_BUTT = 5
DESTI_BUTT = 17
DEST = 0
OUT = 25
RANGE = 8
LEFT = 16
RIGHT = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(VIB, GPIO.OUT)
GPIO.setup(START_BUTT, GPIO.IN)
GPIO.setup(DESTI_BUTT, GPIO.IN)
GPIO.setup(OUT, GPIO.IN)
GPIO.setup(RANGE, GPIO.OUT)
GPIO.setup(LEFT, GPIO.OUT)
GPIO.setup(RIGHT, GPIO.OUT)

GPIO.output(RANGE, False)

queue = []      # 진행 경로가 들어있는 큐

def intro():
    # 사용 - 1 / 대기 - 0
    USING = 0

    while True:
        if USING == 1:
            print("1")
            # 스레딩 처리하기. 음성 듣는 중에도 버튼 누르면 동작하도록
            
            DEST = set_destination()        # 목적지 정보 획득
            perform(DEST)

        elif USING == 0:
            print("0")
            USING = detecting_people(PIR)

def perform(DEST):
    while True:
        # print("이제 운행 파트:",DEST)
        if ultrasound_sensing() == 0:       # 초음파 1m 이내에 장애물 감지 되면
            obstacle()

        while queue:
            node = queue.pop(1)


if __name__ == "__main__":
    # proc1 = Thread(target=ultrasound_sensing, args=())
    # proc2 = Thread(target=obstacle, args=())
    # proc3 = Thread(target=txt_reader, args=())
    # proc1.start()
    # proc2.start()
    # proc3.start()
    intro()        
    GPIO.cleanup()
