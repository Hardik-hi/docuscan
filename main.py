import cv2
import numpy as np

img=cv2.imread('lic.jpg',0)
img=cv2.resize(img,(800,450))
img1=cv2.imread('lic.jpg',1)
img1=cv2.resize(img1,(800,450))

#applying contour transformation



#removing noise
#img=cv2.medianBlur(img,3)
img=cv2.GaussianBlur(img,(3,3),0)
#applying thresholding
thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,5)
edges = cv2.Canny(thresh,50,150)

contours,heirarchy=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img1,contours,-1,(0,255,0),3)
print(len(contours))
i=0
max_area=(img.shape[0]*img.shape[1])/3
for cnt in contours:
    epsilon = 0.02*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    area=cv2.contourArea(approx)
    
    if(area>=max_area):
        cv2.drawContours(img1,contours,i,(0,255,255),3)
        #max_area=area
    
    i+=1

#cv2.drawContours(img1,contours,-1,(0,255,255),3)

cv2.imshow('output',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

