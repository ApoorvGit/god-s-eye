#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install gTTS


# In[3]:


pip install playsound


# In[18]:


from playsound import playsound
from gtts import gTTS 
  
# import Os module to start the audio file
import os 


# In[24]:


def voice(myText):

    # Language we want to use 
    language = 'en'

    output = gTTS(text=myText, lang=language, slow=False)

    output.save("output.mp3")
    playsound("D:/ion-thon/output.mp3")


# In[25]:


voice("Hello Guys for converting text to speech!")


# In[17]:





# In[ ]:




