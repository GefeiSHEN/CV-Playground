import cv2
import numpy as np

sample_image = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/FeatureDetection&Matching/bear.jpg")
gray = cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

cv2.imshow('Watershed Segmentation', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
sure_bg = cv2.dilate(opening, kernel, iterations=3)

cv2.imshow('Watershed Segmentation', sure_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

cv2.imshow('Watershed Segmentation', sure_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Marker labelling
_, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown == 255] = 0

# Apply the Watershed algorithm
cv2.watershed(sample_image, markers)
sample_image[markers == -1] = [255, 0, 0]

# Display the result
cv2.imshow('Watershed Segmentation', sample_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
