import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/2.jpg', cv2.IMREAD_COLOR)

#像素点
img[55,55] = [255,255,255]
px = img[55,55]

#reigon
roi = img [100:150,100:150]

watch_face = img[100:250,100:250]
img[0:150, 0:150] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()