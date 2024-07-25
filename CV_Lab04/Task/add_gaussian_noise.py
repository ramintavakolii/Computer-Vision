# Introduction to Computer Vision (Undergrad)
# School of Computer Engineering
# K.N. Toosi University of Technology

import numpy as np
import cv2

I = cv2.imread('isfahan.jpg');
print(I.dtype) # unit8

# convert I to floating point from unsigned integer
# Note: For displaying floating point images the maximum intensity has to be 1 instead of 255
I = I.astype('float32') / 255
print(I.dtype) # float64
print('Shape(I) =', I.shape)
# print(I)

# create the noise image
sigma = 0.4 # notice maximum intensity is 1
N = np.random.randn(*I.shape) * sigma
print('Shape(N) =', N.shape)

# add noise to the original image
J = I+N; # or use cv2.add(I,N);

cv2.imshow('original',I)
cv2.waitKey(0) # press any key to exit

cv2.imshow('noisy image',J)
cv2.waitKey(0) # press any key to exit

cv2.destroyAllWindows()

