import cv2
import numpy as np

I = cv2.imread('./Code/Images/karimi.jpg', 0)

tx = 20
ty = 30

th = 2  # angle of rotation (degrees)
th *= np.pi / 180  # convert to radians

M = np.array([[np.cos(th), -np.sin(th), tx],
              [np.sin(th), np.cos(th), ty]])

# output image size
output_size = (I.shape[1]+200, I.shape[0]+200)

J = cv2.warpAffine(I, M, output_size)

cv2.imshow('I', I)
cv2.waitKey(0)

cv2.imshow('J', J)
cv2.waitKey(0)
