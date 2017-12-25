import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)
maozi = cv2.imread('../images/4.png')
middle1 = cv2.imread('../images/4.png')
middle2 = cv2.imread('../images/4.png')
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('./video/output.avi', fourcc, 20.0, (640,480))
for x in range(maozi.shape[0]):
    for y in range(maozi.shape[1]):
        if maozi[x,y,0]==255 and maozi[x,y,1]==255 and maozi[x,y,2]==255:
            middle1[x, y, 0] = 1
            middle1[x, y, 1] = 1
            middle1[x, y, 2] = 1
            middle2[x, y, 0] = 0
            middle2[x, y, 1] = 0
            middle2[x, y, 2] = 0
        else:
            middle1[x, y, 0] = 0
            middle1[x, y, 1] = 0
            middle1[x, y, 2] = 0
            middle2[x, y, 0] = 1
            middle2[x, y, 1] = 1
            middle2[x, y, 2] = 1

while True:
    ret,img = cap.read()
    # out.write(frame)
    face_cascade = cv2.CascadeClassifier(
        'D:\conda\envs\deep\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('D:\conda\envs\deep\Lib\site-packages\cv2\data\haarcascade_eye.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        if w>50 and h>50 and x>10 and y>10:
            newmaozi = cv2.resize(maozi,(w,w),interpolation=cv2.INTER_CUBIC)
            newmid1 = cv2.resize(middle1, (w, w), interpolation=cv2.INTER_CUBIC)
            newmid2 = cv2.resize(middle2, (w, w), interpolation=cv2.INTER_CUBIC)
            try:
                if newmaozi.shape[0]>20 and newmaozi.shape[1]>20 and newmid1.shape[0]>20 and newmid1.shape[1]>20 and newmid2.shape[0]>20 and newmid2.shape[1]>20:
                    img[(y+40 - h):(y+40), (x+20):(x+20 + w)] = img[(y+40 - h):(y+40), (x+20):(x+20 + w)]*newmid1 + newmaozi*newmid2
            except Exception:
                continue
        roi_gray = gray[y:y + w, x:x + w]
        roi_color = img[y:y + w, x:x + w]
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
# out.release()
cv2.destroyAllWindows()