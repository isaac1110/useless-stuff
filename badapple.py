import cv2
import numpy as np
import time
import xlwings as xw

since = time.time()
curr = time.time()
cap = cv2.VideoCapture('apple.mp4')#打开相机
i = 0
numimage = 0
wb = xw.Book('test.xlsx')
ws = wb.sheets[0]
while True:
    i = i+1
    ret,frame = cap.read()
    if i%5 !=0:
        continue
    if ret:
        frame1 = frame[:,:,0]
        image1 = cv2.resize(frame1,(72,54))
        image1 = image1/225
        ws.range((1,1),(36,48)).value=image1
        numimage = numimage+1
    else:
        break
    if time.time()<since+0.167*numimage:
        time.sleep(since+0.167*numimage-time.time())
    time_elapsed = time.time() - since
    print(time_elapsed,numimage,time_elapsed/numimage)
    curr = time.time()
