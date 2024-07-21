import cv2 as cv
from tkinter import filedialog
import numpy as np
filename=filedialog.askopenfilename(initialdir="c:/",title="Select Image",filetypes=[("Image Files","*.jpg;*.png")])
img=cv.imread(filename)
img_copy=img.copy()
if img.shape[0]>=1000 or img.shape[1]>=1000:
    img=cv.resize(img,None,fx=0.2,fy=0.2)
    img_copy=cv.resize(img_copy,None,fx=0.2,fy=0.2)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
haar_cascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml")#read the xml file code and store it in a variable
face_rect=haar_cascade.detectMultiScale(gray,1.1,minNeighbors=3)# returns [x,y,w,h]
#haar_cascade classifier is too sensitive to noise in an image
print(face_rect)
print(len(face_rect))
for x,y,w,h in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    roi=img_copy[y:y+h,x:x+w]
    blurroi=cv.blur(roi,(20,20),cv.BORDER_DEFAULT)
    img_copy[y:y+h,x:x+w]=blurroi
cv.imshow("Detected face",img_copy)
cv.waitKey(0)

