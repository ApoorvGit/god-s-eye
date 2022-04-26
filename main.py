import cv2
import sys
sys.path.append('Module-2')
from OCR import *

sys.path.append('../Module-3')
from Image_Captioning import *

sys.path.append('../Module-4')
from main import *

sys.path.append('../')
mode=1
def cam():
    # Load Camera
    cap = cv2.VideoCapture(0)
    counter=0
    while True:
        if(counter%5!=0):
            continue
        ret, frame = cap.read()
        if(mode==1) output_caption_stream(frame)
        elif(mode==2) recognise(frame)
        elif(mode==3) ocr(frame)
        key = cv2.waitKey(1)
        if key == 1:
            mode=1
        elif key == 2:
            mode=2
        elif key == 3:
            mode=3
        elif key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
cam()
