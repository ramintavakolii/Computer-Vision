import cv2
import numpy as np

I = cv2.imread('polygons.jpg')
G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

ret, T = cv2.threshold(G, 232, 255, cv2.THRESH_BINARY_INV)

nc1, CC1 = cv2.connectedComponents(T)

for k in range(1, nc1):

    Ck = np.zeros(T.shape, dtype=np.float32)
    Ck[CC1 == k] = 255
    Ck = cv2.GaussianBlur(Ck, (11, 11), 0)
    Ck1 = cv2.cvtColor(Ck, cv2.COLOR_GRAY2BGR)

    # Now, apply corner detection on Ck
    # Ck = np.float32(Ck)

    window_size = 6
    soble_kernel_size = 7  # kernel size for gradients
    alpha = 0.02
    H = cv2.cornerHarris(Ck, window_size, soble_kernel_size, alpha)

    # normalize
    H = H / H.max()

    H1 = np.zeros(H.shape, dtype=np.float32)
    for i in range(1, H.shape[0]):
        for j in range(1, H.shape[1]):
            if (Ck[i, j] == 0):
                continue
            if (H[i, j] > H[i+1, j]) & (H[i, j] > H[i-1, j]) & (H[i, j] > H[i, j+1]) & (H[i, j] > H[i, j-1]) &\
               (H[i, j] > H[i+1, j+1]) & (H[i, j] > H[i-1, j+1]) & (H[i, j] > H[i+1, j-1]) & (H[i, j] > H[i-1, j-1]):
                H1[i, j] = H[i, j]

    C = np.uint8(H1 > 0.01) * 255
    n1 = np.count_nonzero(C)
    # Show corners as red pixels in the original image
    Ck1[C != 0] = [0, 0, 255]

    # Create a copy of the image with corners marked in red
    Ck2 = Ck1.copy()

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(Ck2, 'There are %d vertices!' %
                (n1), (20, 30), font, 1, (0, 0, 255), 1)

    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            if C[i, j] != 0:
                cv2.circle(Ck2, (j, i), 5, (0, 0, 255), 1)

    cv2.imshow('corners', Ck2)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
