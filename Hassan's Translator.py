import subprocess
import sys
import os
def install_requirements():
    if os.path.isfile('requirements.txt'):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
install_requirements()
import arabic_reshaper
from bidi.algorithm import get_display
from googletrans import Translator
t = Translator()
#This Function Translate From English To Arabic
#Or From Any Language To Arabic
#And Reshape The Arabic Result To Be Readable
def transhape(translated_text):
    #This Function Translate From English To Arabic
    #Or From Any Language To Arabic
    #And Reshape The Arabic Result To Be Readable
    # the name is an abbreviation for translate to arabic
    # and this for translate any text by default language (english) to arabic
    # and reshape this text to be easy for the user to read
    reshaped_text = arabic_reshaper.reshape(t.translate(translated_text,dest='ar').text)
    bidi_reshape_text = get_display(reshaped_text)
    print(bidi_reshape_text)
transhape("yes")
