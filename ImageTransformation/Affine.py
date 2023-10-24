import cv2
import numpy as np

sample_image = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/ImageManipulation/testing3.jpg")
sample_image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)

# 1. Two sets of points
src_pts = np.float32([[50, 50], [200, 50], [50, 200]])
dst_pts = np.float32([[10, 100], [150, 50], [100, 250]])
matrix = cv2.getAffineTransform(src_pts, dst_pts)
result_affine = cv2.warpAffine(
    sample_image, matrix, (sample_image.shape[1], sample_image.shape[0]))

# 2. 2DRotationMatrix
center = (sample_image.shape[1] // 2, sample_image.shape[0] // 2)
map_matrix = cv2.getRotationMatrix2D(center, -45, 1.5)
result_rotation = cv2.warpAffine(
    sample_image, map_matrix, (sample_image.shape[1], sample_image.shape[0]))

combined_image = np.hstack((sample_image, result_affine, result_rotation))

cv2.imshow("Affine", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
