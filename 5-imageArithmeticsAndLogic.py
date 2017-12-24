import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/2.jpg', cv2.IMREAD_COLOR)
print(img.shape)