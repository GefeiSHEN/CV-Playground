import cv2
import numpy as np

sample_image = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/ImageManipulation/TE100.jpg")

gaussian_blur = cv2.GaussianBlur(sample_image, (15, 15), 0)
bilateral_filter = cv2.bilateralFilter(sample_image, 15, 50, 50)
combined_image = np.hstack((gaussian_blur, sample_image, bilateral_filter))

cv2.imshow("Modified Image", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
