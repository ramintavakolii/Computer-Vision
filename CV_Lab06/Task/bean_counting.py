import numpy as np
import cv2

I = cv2.imread('beans.jpg')
G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
# G = cv2.imread('beans.jpg', cv2.IMREAD_GRAYSCALE)
# print(np.unique(G))

ret, T = cv2.threshold(G,127,255,cv2.THRESH_BINARY)
print(np.unique(T))
# print(T)
# print(ret)

cv2.imshow('Thresholded', T)
cv2.waitKey(0) # press any key to continue...

# erosion 
kernel = np.ones((25,25),np.uint8)
T = cv2.erode(T,kernel)
cv2.imshow('After Erosion', T)
cv2.waitKey(0) # press any key to continue...

# dilatoin
kernel = np.ones((20,20),np.uint8)
T = cv2.dilate(T, kernel)
cv2.imshow('After dilatoin', T)
cv2.waitKey(0) # press any key to continue...

n,C = cv2.connectedComponents(T);

font = cv2.FONT_HERSHEY_SIMPLEX 
cv2.putText(T,'There are %d beans!'%(n-1),(20,40), font, 1, 255,2)
cv2.imshow('Num', T)
cv2.waitKey(0)

