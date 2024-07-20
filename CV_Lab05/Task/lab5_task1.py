import numpy as np
import cv2
from utility_functions import std_filter, zero_crossing

cam_id = 0  # camera id

# for default webcam, cam_id is usually 0
# try out other numbers (1,2,..) if this does not work

cap = cv2.VideoCapture(cam_id)

mode = 'o'  # show the original image at the beginning
thresh = 60
sigma = 5

position = (10, 50)
font_scale = 1.5
font_color = (255, 255, 255)  # White color in BGR format
thickness = 3
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, I = cap.read()
    # I = cv2.imread("agha-bozorg.jpg") # can use this for testing
    I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    Ib = cv2.GaussianBlur(I, (sigma, sigma), 0)  # blur the image

    if mode == 'o':
        # J = the original image
        J = I
        text = "Original Image"
        cv2.putText(J, text, position, font, font_scale, font_color, thickness)
    elif mode == 'x':
        # J = Sobel gradient in x direction
        J = np.abs(cv2.Sobel(Ib, cv2.CV_64F, 1, 0))
        text = "Sobel gradient_x Image"
        cv2.putText(J, text, position, font, font_scale, font_color, thickness)

    elif mode == 'y':
        # J = Sobel gradient in y direction
        J = np.abs(cv2.Sobel(Ib, cv2.CV_64F, 0, 1))
        text = "Sobel gradient_y Image"
        cv2.putText(J, text, position, font, font_scale, font_color, thickness)

    elif mode == 'm':
        # J = magnitude of Sobel gradient
        Jy = np.abs(cv2.Sobel(Ib, cv2.CV_64F, 0, 1))
        Jx = np.abs(cv2.Sobel(Ib, cv2.CV_64F, 1, 0))
        J = np.sqrt(Jx*Jx + Jy*Jy)
        text = "magnitude of Sobel gradient"
        cv2.putText(J, text, position, font, font_scale, font_color, thickness)

    elif mode == 's':
        # J = Sobel + thresholding edge detection
        Jy = np.abs(cv2.Sobel(Ib, cv2.CV_64F, 0, 1))
        Jx = np.abs(cv2.Sobel(Ib, cv2.CV_64F, 1, 0))
        Es = np.sqrt(Jx*Jx + Jy*Jy)
        J = np.uint8(Es > thresh) * 255  # threshold the gradients
        text = "Sobel + thresholding"
        cv2.putText(J, text, position, font, font_scale, font_color, thickness)

    elif mode == 'l':
        # J = Laplacian edges
        El = cv2.Laplacian(Ib, cv2.CV_64F, ksize=5)
        J = zero_crossing(El)
        text = "Laplacian edges"
        cv2.putText(J, text, position, font, font_scale, font_color, thickness)

    elif mode == 'c':
        # J = Canny edges
        lth = 50   # low threshold
        hth = 120  # high threshold
        J = cv2.Canny(Ib, lth, hth)
        text = "Canny edges"
        cv2.putText(J, text, position, font, font_scale, font_color, thickness)


    # we set the image type to float and the maximum value to 1 (for a better illustration) notice that imshow in opencv
    #  does not automatically map the min and max values to black and white.
    J = J.astype("float") / J.max()
    cv2.imshow("my stream", J)

    key = chr(cv2.waitKey(1) & 0xFF)

    if key in ['o', 'x', 'y', 'm', 's', 'c', 'l']:
        mode = key
    if key == '-' and sigma > 1:
        sigma -= 2
        print("sigma = %d" % sigma)
    if key in ['+', '=']:
        sigma += 2
        print("sigma = %d" % sigma)
    elif key == 'q':
        break

cap.release()
cv2.destroyAllWindows()
