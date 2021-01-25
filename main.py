import cv2
import numpy as np

img=cv2.imread('newsclip.jpg',0)
edges = cv2.Canny(img,100,200)
#applying contour transformation



#removing noise
img=cv2.medianBlur(img,3)

#applying thresholding
thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,5)
cv2.imshow('output',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

