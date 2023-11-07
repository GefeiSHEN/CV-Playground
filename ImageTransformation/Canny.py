import cv2
import numpy as np

sample_image = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/ImageManipulation/testing3.jpg")
sample_image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)

threshold1 = 150
threshold2 = 400
aperture = 3

edges = cv2.Canny(sample_image, threshold1, threshold2,
                  apertureSize=aperture, L2gradient=True)

combined_image = np.hstack((sample_image, edges))

cv2.imshow("Modified Image", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
