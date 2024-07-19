import numpy as np
import cv2

I1 = cv2.imread('scene1.jpg')
I2 = cv2.imread('scene2.jpg')
# print(I1)
# print(I2)
''' We se two images has different value in same pixle'''
print(I1.dtype)
print(I2.dtype)

cv2.imshow('Image 1 (background)', I1)
cv2.waitKey(0)

cv2.imshow('Image 2', I2)
cv2.waitKey(0)

K = np.abs(np.int16(I2)-np.int16(I1)) # take the (signed int) differnce
print(K.shape)
K = K.max(axis=2) # choose the maximum value over color channels
print(K)
K = np.uint8(K)
cv2.imshow('The difference image', K)
cv2.waitKey(0)

threshold = 33
ret, T = cv2.threshold(K,threshold,255,cv2.THRESH_BINARY)
cv2.imshow('Thresholded', T)
cv2.waitKey(0)

# opening
kernel = np.ones((3,3),np.uint8)
T = cv2.morphologyEx(T, cv2.MORPH_OPEN, kernel)
cv2.imshow('After Openning', T)
cv2.waitKey(0)

# closing
kernel = np.ones((15,15),np.uint8)
T = cv2.morphologyEx(T, cv2.MORPH_CLOSE, kernel)
cv2.imshow('After Closing', T)
cv2.waitKey(0)

n,C = cv2.connectedComponents(T);

J = I2.copy()
J[T != 0] = [255,255,255]
font = cv2.FONT_HERSHEY_SIMPLEX 
cv2.putText(J,'There are %d toys!'%(n-1),(20,40), font, 1,(0,0,255),2)
cv2.imshow('Number', J)
cv2.waitKey()

# connected components with statistics
n,C,stats, centroids = cv2.connectedComponentsWithStats(T);

max = 0
for i in range(n):
    print("-"*20)
    print("Connected Component: ", i)
    print("center= %.2f,%.2f"%(centroids[i][0], centroids[i][1]))
    print("left= ", stats[i][0])
    print("top=  ",  stats[i][1])
    print("width=  ", stats[i][2])
    print("height= ", stats[i][3])
    print("area= ", stats[i][4])
    if (stats[i][4] > max) and (stats[i][0] > 0) :
        max = stats[i][4]
        j = i

# j = n-1 # j: index of largest connected component (change this line)
J[C == j] = [0,0,255] # Paint largest connected component in RED
cv2.imshow('Largest Toy in red', J)
cv2.waitKey()

