import cv2
import numpy as np

I = cv2.imread('square.jpg')
G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

print(I.shape)
print(G.shape)

G = np.float32(G)

window_size = 2
soble_kernel_size = 3  # kernel size for gradients
alpha = 0.04
H = cv2.cornerHarris(G, window_size, soble_kernel_size, alpha)

# normalize C so that the maximum value is 1
print(H.shape)
H = H / H.max()

# C[i,j] == 255 if H[i,j] > 0.01, and C[i,j] == 0 otherwise
C = np.uint8(H > 0.005) * 255

# to count the number of corners we count the number of nonzero elements of C (wrong way to count corners!)
n1 = np.count_nonzero(C)

# Show corners as red pixels in the original image
I[C != 0] = [0, 0, 255]

# Create a copy of the image with corners marked in red
I1 = I.copy()

cv2.imshow('corners', C)
cv2.waitKey(0)  # press any key

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(I1, 'There are %d corners!' %
            n1, (20, 40), font, 1, (0, 0, 255), 2)

cv2.imshow('corners', I1)
cv2.waitKey(0)  # press any key

# cv2.destroyAllWindows()

# --------------------------------------------- Using connected components -------------------------------------------------

nc, CC = cv2.connectedComponents(C)

Ck = np.zeros(G.shape, dtype=G.dtype)
for k in range(nc):
    # show the k-th connected component
    k += 1
    print(k)
    Ck[CC == k] = 255


# to count the number of corners we count the number of connected components except background
n2 = nc - 1

# Create another copy of the original image to display the new text
I2 = I.copy()

# Show corners as red pixels in the original image
I2[CC != 0] = [0, 0, 255]

cv2.imshow('corners', np.uint8(Ck))
cv2.waitKey(0)  # press any key

cv2.putText(I2, 'There are %d corners!' %
            n2, (20, 40), font, 1, (0, 0, 255), 2)
cv2.imshow('corners', I2)
cv2.waitKey(0)  # press any key

cv2.destroyAllWindows()
