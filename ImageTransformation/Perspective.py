import cv2
import numpy as np

sample_image = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/ImageManipulation/testing3.jpg")

src_pts = np.array([[100, 100], [200, 100], [100, 200],
                   [200, 200]], dtype=np.float32)

dst_pts = np.array([[50, 75], [250, 75], [50, 250],
                   [250, 250]], dtype=np.float32)

M = cv2.getPerspectiveTransform(src_pts, dst_pts)
transformed_image = cv2.warpPerspective(
    sample_image, M, (sample_image.shape[1], sample_image.shape[0]))
combined_image = np.hstack((sample_image, transformed_image))

cv2.imshow('Perspective', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
