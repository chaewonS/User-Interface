from gtts import gTTS
import os

def txt_reader(ment):
    f = open("./"+ment+".txt", 'r')
    f = f.read()
    os.system('gtts-cli \"'+f+'\" --lang ko | mpg123 -')
# distance = "20"
# os.system('gtts-cli "%s 미터 앞에서 우회전입니다." --lang ko | mpg123 -' %distance)

txt_reader("ment2")

