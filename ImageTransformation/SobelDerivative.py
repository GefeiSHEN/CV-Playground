import cv2
import numpy as np

sample_image = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/ImageManipulation/testing3.jpg")

sobelx = cv2.Sobel(sample_image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(sample_image, cv2.CV_64F, 0, 1, ksize=3)

sobel_combined = cv2.magnitude(sobelx, sobely)
sobel_combined = cv2.convertScaleAbs(sobel_combined)

combined_image = np.hstack((sample_image, sobel_combined))

cv2.imshow("Sobel Derivative", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
