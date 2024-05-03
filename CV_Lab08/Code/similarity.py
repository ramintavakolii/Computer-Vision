import cv2
import numpy as np

I = cv2.imread('./Code/Images/karimi.jpg')

tx = 100
ty = 60

th = 20  # angle of rotation (degrees)
th *= np.pi / 180  # convert to radians

s = 2  # scale factor

M = np.array([[s*np.cos(th), -s*np.sin(th), tx],
              [s*np.sin(th), s*np.cos(th), ty]])

output_size = (int(I.shape[1] * s * 2), int(I.shape[0] * s * 2))
J = cv2.warpAffine(I, M,  output_size)

cv2.imshow('I', I)
cv2.waitKey(0)

cv2.imshow('J', J)
cv2.waitKey(0)
