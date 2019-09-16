#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    # Read video from disk and count frames
    cap = cv2.VideoCapture('test_videos/2.mp4')
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    template = cv2.imread('yellow.PNG',0)
    template1 = cv2.imread('blue.PNG',0)
    template2 = cv2.imread('red.PNG',0)
    
    # for yellow cone
    scale_percent = 20 # percent of original size
    width = int(template.shape[1] * scale_percent / 100)
    height = int(template.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(template, dim, interpolation = cv2.INTER_AREA)

    # for blue cone
    scale_percent = 20 # percent of original size
    width = int(template1.shape[1] * scale_percent / 100)
    height = int(template1.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized1 = cv2.resize(template1, dim, interpolation = cv2.INTER_AREA)
    
    # for red cone
    scale_percent = 20 # percent of original size
    width = int(template2.shape[1] * scale_percent / 100)
    height = int(template2.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized2 = cv2.resize(template2, dim, interpolation = cv2.INTER_AREA)

    count = 0
    while count < frameCount:
        ret, frame = cap.read()
        if ret == True:
            count = count + 1
            img = frame.copy()
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            w, h = resized.shape[::-1] # Yellow cone, width and height
            w1, h1 = resized1.shape[::-1] # blue cone, width and height
            
            res = cv2.matchTemplate(img_gray,resized,cv2.TM_CCOEFF_NORMED)
            res1 = cv2.matchTemplate(img_gray,resized1,cv2.TM_CCOEFF_NORMED)

            threshold = 0.7
            loc = np.where( res >= threshold)
            loc1 = np.where( res1 >= threshold)
            
            # Iterating over yellow cones
            for pt in zip(*loc[::-1]):
                cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,255), 1)
                cv2.putText(frame, 'yellow cone', (int(pt[0]),int(pt[1])-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
            
            # Iterating over blue cones
            for pt in zip(*loc1[::-1]):
                cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (255,0,0), 1)
                cv2.putText(frame, 'blue cone', (int(pt[0]),int(pt[1])-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
            
            cv2.imshow('Original frame', img)
            cv2.imshow('detected framed', frame)

            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()
            
    

    
if __name__ == '__main__':
    main()


# In[ ]:




