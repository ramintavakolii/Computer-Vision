import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread("pasargadae.jpg", cv2.IMREAD_GRAYSCALE)
flattened_img = I.flatten()
H, W = I.shape
print('w =',W)
print('h =',H)
levels = 256

# calculating histogram
def calc_hist(I, levels):
    hist = np.zeros(levels)
    H, W = I.shape

    for i in range(H):
        for j in range(W):
            intensity = int(I[i, j])

            hist[intensity] += 1
    return hist


# calculating CDF
def calc_cdf(hist, levels):
    cdf = np.zeros_like(hist)
    intensity = 0
    for i in range(levels):
        intensity = hist[i] + intensity
        cdf[i] = intensity
    return cdf


hist = calc_hist(I, levels)
cdf = calc_cdf(hist, levels)

# normalize CDF
# cdf = (cdf * levels) / (H*W)
normalized_cdf = (cdf - cdf.min()) / (cdf.max() - cdf.min())

# mapping
mapping = normalized_cdf * (levels-1)

# replace intensity
img_new = mapping[flattened_img]

# --------------------------------------- testing ---------------------------------------
# print(mapping.shape)
# print(flattened_img.shape)
# print(flattened_img)
# print(img_new)
# print(img_new.shape)
# ---------------------------------------------------------------------------------------

equalized_image =  np.reshape(img_new, I.shape)

equalized_image_hist = calc_hist(equalized_image, levels)
equalized_image_cdf = calc_cdf(equalized_image_hist, levels)

fig = plt.figure(figsize=(16, 8))
fig.add_subplot(2, 3, 1)
plt.imshow(I, cmap='gray')
plt.title('pasargadae')
plt.axis('off')

fig.add_subplot(2, 3, 2)
plt.plot(hist)
plt.title('Source histogram')

fig.add_subplot(2, 3, 3)
plt.plot(normalized_cdf)
plt.title('Source CDF')

fig.add_subplot(2, 3, 4)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized image')
plt.axis('off')

fig.add_subplot(2, 3, 5)
plt.plot(equalized_image_hist)
plt.title('Equalized histogram')


fig.add_subplot(2, 3, 6)
plt.plot(equalized_image_cdf)
plt.title('Equalized CDF')

plt.show()
