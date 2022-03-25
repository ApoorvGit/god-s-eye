from PIL import Image
import pytesseract
import cv2
import numpy as np
import sys
sys.path.append('../Module-1')
from voice import *

def textRecognition(filename):
  img1 = np.array(Image.open(filename))
  text = pytesseract.image_to_string(img1)
  l=''.join(text)
  l=l.split('\n')
  li=[]
  for s in l:
    s1="".join(c for c in s if c.isalpha() or c.isdigit() or c==" " or c in "!@#$%&*.?':;_" )
    if s1!="":
      li.append(s1) 
  temp=" ".join(li)
  temp=temp.split('.')
  return temp
  
def ocr(img):
  cv2.imwrite("frame.jpg", img)
  sentences=textRecognition("frame.jpg")
  for s in sentences:
    voice(s)
