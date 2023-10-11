import cv2
import numpy as np

sample_image = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/ImageManipulation/TE100.jpg")

kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)
M = cv2.getRotationMatrix2D((kernel_size // 2, kernel_size // 2), 45, 1)
rotated_kernel = cv2.warpAffine(kernel, M, (kernel_size, kernel_size))

kernel_image = cv2.morphologyEx(sample_image, cv2.MORPH_OPEN, kernel)
rotated_image = cv2.morphologyEx(sample_image, cv2.MORPH_OPEN, rotated_kernel)
combined_image = np.hstack((kernel_image, sample_image, rotated_image))

cv2.imshow("Modified Image", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
