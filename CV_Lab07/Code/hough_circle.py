import numpy as np
import cv2

I = cv2.imread('./Code/Images/samand.jpg')

G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)  # -> Grayscale
G = cv2.GaussianBlur(G, (7, 7), 0)     # Gaussian blur

canny_high_threshold = 200

# minimum no. of votes to be considered as a circle
min_votes = 100

# minimum distance between the centres of detected circles
min_centre_distance = 40

# resolution of parameters (centre, radius) relative to image resolution
resolution = 1

circles = cv2.HoughCircles(G, cv2.HOUGH_GRADIENT, resolution, min_centre_distance,
                           param1=canny_high_threshold,
                           param2=min_votes, minRadius=0, maxRadius=100)

# for opencv 2 use cv2.cv.CV_HOUGH_GRADIENT instead of cv2.HOUGH_GRADIENT

# find the edges
E = cv2.Canny(G, canny_high_threshold/2, canny_high_threshold)

for c in circles[0, :]:
    x = int(c[0])  # x coordinate of the centre
    y = int(c[1])  # y coordinate of the centre
    r = int(c[2])  # radius

    # draw the circle
    cv2.circle(I, (x, y), r, (0, 255, 0), 2)

    # draw the circle center
    cv2.circle(I, (x, y), 2, (0, 0, 255), 2)


cv2.imshow("E", E)
cv2.imshow("I", I)
cv2.waitKey(0)
cv2.destroyAllWindows()
