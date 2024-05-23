import cv2
import numpy as np

I = cv2.imread('polygons.jpg')
G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

ret, T = cv2.threshold(G, 220, 255, cv2.THRESH_BINARY_INV)

nc1, CC1 = cv2.connectedComponents(T)

for k in range(1, nc1):

    Ck = np.zeros(T.shape, dtype=np.float32)
    Ck[CC1 == k] = 1
    Ck = cv2.GaussianBlur(Ck, (7, 7), 0)
    Ck1 = cv2.cvtColor(Ck, cv2.COLOR_GRAY2BGR)

    # Now, apply corner detection on Ck
    Ck = np.float32(Ck)

    window_size = 5
    soble_kernel_size = 3  # kernel size for gradients
    alpha = 0.02
    H = cv2.cornerHarris(Ck, window_size, soble_kernel_size, alpha)

    # normalize
    H = H / H.max()

    # C[i,j] == 255 if H[i,j] > 0.01, and C[i,j] == 0 otherwise
    C = np.uint8(H > 0.01) * 255

    # to count the number of corners we count the number of nonzero elements of C (wrong way to count corners!)
    n1 = np.count_nonzero(C)
    # Show corners as red pixels in the original image
    Ck1[C != 0] = [0, 0, 255]

    # Create a copy of the image with corners marked in red
    Ck2 = Ck1.copy()

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(Ck2, 'There are %d vertices!' %
                (n1), (20, 30), font, 1, (0, 0, 255), 1)
    cv2.imshow('corners', Ck2)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

    # plot centroids of connected components as corner locations
    nC, CC, stats, centroids = cv2.connectedComponentsWithStats(C)

    # J = Ck1.copy()
    J = Ck.copy()
    
    n2 = nC - 1

    cv2.putText(J, 'There are %d vertices!' %
                (n2), (20, 30), font, 1, (0, 0, 255), 1)
    for i in range(1, nC):
        cv2.circle(J, (int(centroids[i, 0]), int(
            centroids[i, 1])), 4, (0, 0, 255))
    cv2.imshow('corners', J)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
