import numpy as np
import cv2

I = cv2.imread('isfahan.jpg').astype("float32") / 255

size = 9            # bilateral filter size (diameter)
sigma_color = 0.5
sigma_space = 1

Jl = cv2.bilateralFilter(I,size, sigma_color, sigma_space)
I = I.astype("float64")
print(I.dtype)
cv2.imshow('original',I)
cv2.waitKey()

cv2.imshow('blurred_Gaussian',Jl)
cv2.waitKey()

cv2.destroyAllWindows()
