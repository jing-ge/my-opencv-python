import cv2
import numpy as np

img = cv2.imread('./images/3.jpg', 0)
retval,threshold1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
retval,threshold2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
retval,threshold3 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
retval,threshold4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
retval,threshold5 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

autoadapt_GAUSSIAN = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
autoadapt_MEAN = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 1)


cv2.imshow('original',img)
cv2.imshow('htreshold1',threshold1)
cv2.imshow('htreshold2',threshold2)
cv2.imshow('htreshold3',threshold3)
cv2.imshow('htreshold4',threshold4)
cv2.imshow('htreshold5',threshold5)
cv2.imshow('autoadapt_GAUSSIAN', autoadapt_GAUSSIAN)
cv2.imshow('autoadapt_MEAN', autoadapt_MEAN)

cv2.waitKey(0)
cv2.destroyAllWindows()
