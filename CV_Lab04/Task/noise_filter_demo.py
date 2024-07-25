import numpy as np
import cv2

I = cv2.imread('isfahan.jpg').astype(np.float64) / 255

noise_sigma = 0.04  # initial standard deviation of noise

m = 1  # initial filter size,

gm = 3  # gaussian filter size

size = 9  # bilateral filter size
sigmaColor = 0.3
sigmaSpace = 75

# with m = 1 the input image will not change
filter = 'b'  # box filter

while True:

    # add noise to image
    N = np.random.rand(*I.shape) * noise_sigma
    J = I + N

    if filter == 'b':
        # filter with a box filter
        K = cv2.boxFilter(J, -1, (m, m), normalize=True)
    elif filter == 'g':
        # filter with a Gaussian filter
        K = cv2.GaussianBlur(J, (gm, gm), 0)
    elif filter == 'l':
        # filter with a bilateral filter
        J = J.astype("float32")
        # print(J.dtype)
        K = cv2.bilateralFilter(J, size, sigmaColor, sigmaSpace)
        

    # filtered image

    cv2.imshow('img', K)
    key = cv2.waitKey(30) & 0xFF

    if key == ord('b'):
        J.astype("float64")
        filter = 'b'  # box filter
        print('Box filter')

    elif key == ord('g'):
        J = J.astype("float64")
        filter = 'g'  # filter with a Gaussian filter
        print('Gaussian filter')

    elif key == ord('l'):
        filter = 'l'  # filter with a bilateral filter
        print('Bilateral filter')

    elif key == ord('+'):
        # increase m (initial filter size)
        m = m + 2
        print('m=', m)

    elif key == ord('-'):
        # decrease m (initial filter size)
        if m >= 3:
            m = m - 2
        print('m=', m)
    elif key == ord('u'):
        # increase noise intensity
        noise_sigma = noise_sigma + 0.02
        print('noise_sigma =', noise_sigma)
    elif key == ord('d'):
        # decrease noise intensity
        noise_sigma = noise_sigma - 0.02
        print('noise_sigma =', noise_sigma)
    elif key == ord('p'):
        # increase gm (gaussian filter size)
        gm = gm + 2
        print('gm=', gm)
    elif key == ord('n'):
        # decrease gm (gaussian filter size)
        gm = gm - 2
        print('gm=', gm)
    elif key == ord('>'):
        # increase size
        size += 1
        print('size=', size)
    elif key == ord('<'):
        # decrease size
        size -= 1
        print('size=', size)
    elif key == ord('c'):
        # increase sigmaColor or sigmaSpace
        sigmaColor = sigmaColor + 0.1
        print('sigmaColor=', sigmaColor)
    elif key == ord('z'):
        # decrease sigmaColor or sigmaSpace
        sigmaColor = sigmaColor - 0.1
        print('sigmaColor=', sigmaColor)
    
    elif key == ord('q'):
        break  # quit

cv2.destroyAllWindows()
