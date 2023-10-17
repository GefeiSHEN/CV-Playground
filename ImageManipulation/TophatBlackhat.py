import cv2
import numpy as np

sample_image = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/ImageManipulation/testing2.png")

kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)

tophat_image = cv2.morphologyEx(sample_image, cv2.MORPH_TOPHAT, kernel)
blackhat_image = cv2.morphologyEx(sample_image, cv2.MORPH_BLACKHAT, kernel)

combined_image = np.hstack((sample_image, tophat_image, blackhat_image))

cv2.imshow("Modified Image", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
