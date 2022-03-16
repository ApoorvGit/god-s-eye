
pip install gTTS
pip install playsound
from playsound import playsound
from gtts import gTTS 
import os 


def voice(myText):

    # Language we want to use 
    language = 'en'

    output = gTTS(text=myText, lang=language, slow=False)

    output.save("output.mp3")
    playsound("D:/ion-thon/output.mp3")


voice("Hello Guys for converting text to speech!")



