from gtts import gTTS
import os
import time

os.system('gtts-cli "안녕하세요. 저는 gTTS 입니다." --lang ko | mpg123 -')
