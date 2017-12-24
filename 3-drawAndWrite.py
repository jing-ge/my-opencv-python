import cv2
import numpy as np
import matplotlib.pyplot as plt

img  = cv2.imread('./images/2.jpg',cv2.IMREAD_COLOR)

#color is bgr
cv2.line(img, (0,0),(150,150), (255,0,0),15)
cv2.rectangle(img, (15,25),(200,150),(0,255,0),5)
cv2.circle(img, (100,63),55,(0,0,255),-1)#-1 means all

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#pts = pts.reshape(-1,1,2)
#这里true or false 表示是否首尾相连
cv2.polylines(img,[pts],False,(0,255,255),4)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'opencv tuts!',(0,130),font,1,(0,0,0),1,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()