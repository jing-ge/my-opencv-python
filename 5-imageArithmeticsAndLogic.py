import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('./images/2.jpg')
img2 = cv2.imread('./images/4.png')
img2 = cv2.resize(img2,(img1.shape[1]-200,img1.shape[0]-200),interpolation=cv2.INTER_CUBIC)

#three methods of adding
#add = img1 + img2    #直接相加，超过255，就当255
#add = cv2.add(img1,img2)
#add = cv2.addWeighted(img1,0.6,img2,0.4,0)

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret ,mask = cv2.threshold(img2gray, 254,255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
final = cv2.add(img1_bg,img2_fg)

img1[0:rows,0:cols] = final
# cv2.imshow("add",add)
# cv2.imshow('gray',img2gray)
# cv2.imshow("mask",mask)
cv2.imshow("test",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()