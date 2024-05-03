import cv2
import numpy as np

I1 = cv2.imread('./Code/Images/farshchian1.jpg')
I2 = cv2.imread('./Code/Images/farshchian2.jpg')

points1 = np.array([(82, 14),
                    (242, 17),
                    (241, 207),
                    (81, 206)]).astype(np.float32)

points2 = np.array([(46, 75),
                    (196, 61),
                    (220, 227),
                    (76, 251)]).astype(np.float32)

for i in range(4):
    cv2.circle(I1, (int(points1[i, 0]), int(points1[i, 1])), 3, [0, 0, 255], 2)
    cv2.circle(I2, (int(points2[i, 0]), int(points2[i, 1])), 3, [0, 0, 255], 2)

# compute homography from point correspondences
H = cv2.getPerspectiveTransform(points1, points2)

# Transform I2 to match the perspective of I1
output_size = (I2.shape[1], I2.shape[0])
J = cv2.warpPerspective(I1, H,  output_size)

# Optionally, blend images
J1 = cv2.multiply(J, I2)
J1 = cv2.multiply(J, 100)
I3 = cv2.add(I2, J1)
J = J + I3


cv2.imshow('I1', I1)
cv2.waitKey(0)

cv2.imshow('I2', I2)
cv2.waitKey(0)

cv2.imshow('J', J)
cv2.waitKey(0)

# cv2.imshow('Blended Image', blended_image)
cv2.waitKey(0)
