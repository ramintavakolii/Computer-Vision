import cv2
import numpy as np
from matplotlib import pyplot as plt

fname = 'terrain.jpg'
# fname = 'office.jpg'

I = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
print('shape(I) = ', I.shape)
print('shape(I.ravel) = ', I.ravel().shape)

f, axes = plt.subplots(2, 3, figsize=(10, 7))

# ---------------------------- Visualize Image I and it's Histogram ------------------------------
axes[0, 0].imshow(I, 'gray', vmin=0, vmax=255)
axes[0, 0].axis('off')
# Hist = np.hist(I.ravel(), 255, [0, 256])
# Hist = cv2.calcHist(I,[0], None, [256], [0, 256])
# HistCumSum = np.cumsum(Hist)
axes[1, 0].hist(I.ravel(), 256, [0, 256])
'''
256: number of bins in the histogram. In this case, there are 256 bins.
'''
# -------------------------------- automatically obtaining a and  --------------------------------


def implement_ab(image, percent = 2):

    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    max_index = np.where(hist == np.max(hist))[0][0]
    print(max_index)
    print(np.max(hist))

    for i in range(max_index):
        if hist[max_index-i] <= ((np.max(hist) * percent) / 100):
            a = max_index-i
            print('a =', a)
            break
    for i in range(max_index):
        if hist[max_index+i] <= ((np.max(hist) * percent) / 100):
            b = max_index + i
            print('b =', b)
            break
    return a, b


# b = 240
# a = 135
a, b = implement_ab(I)

# ------------------------------------ Constructing Image J --------------------------------------

J = (I-a) * 255.0 / (b-a)
J[J < 0] = 0
J[J > 255] = 255
J = J.astype(np.uint8)
print('shape(J) = ', J.shape)
print('shape(J.ravel) = ', J.ravel().shape)

# ---------------------------- Visualize Image J and it's Histogram ------------------------------
axes[0, 1].imshow(J, 'gray', vmin=0, vmax=255)
axes[0, 1].axis('off')
axes[1, 1].hist(J.ravel(), 255, [0, 256])


# --------------------------- Constructing histogram equalization of I -------------------------

K = cv2.equalizeHist(I)


# ---------------------------- Visualize  histogram equalization of I  -------------------------

axes[0, 2].imshow(K, 'gray', vmin=0, vmax=255)
axes[0, 2].axis('off')

axes[1, 2].hist(K.ravel(), 255, [0, 256])


# axes[1, 1].hist(I[1], 256, [0, 256])
# axes[1, 1].hist(I, 256, [0, 256])


plt.show()
