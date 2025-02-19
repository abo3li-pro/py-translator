import arabic_reshaper
from bidi.algorithm import get_display
from googletrans import Translator
t = Translator()
#This Function Translate From English To Arabic
#Or From Any Language To Arabic
#And Reshape The Arabic Result To Be Readable
def transhape(translated_text):
    # the name is an abbreviation for translate to arabic
    # and this for translate any text by default language (english) to arabic
    # and reshape this text to be easy for the user to read
    # and this for printing slowly
    reshaped_text = arabic_reshaper.reshape(t.translate(translated_text,dest='ar').text)
    bidi_reshape_text = get_display(reshaped_text)
    print(bidi_reshape_text)
transhape("yes")