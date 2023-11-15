import cv2
import numpy as np

sample_image = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/ImageManipulation/testing3.jpg")

sift = cv2.SIFT_create()
sift_kp = sift.detect(sample_image, None)

mser = cv2.MSER_create()
mser_regions, _ = mser.detectRegions(sample_image)

surf = cv2.xfeatures2d.SURF_create(10000)

sift_img = cv2.drawKeypoints(
    sample_image, sift_kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

mser_img = sample_image.copy()
for p in mser_regions:
    hull = cv2.convexHull(p.reshape(-1, 1, 2))
    cv2.polylines(mser_img, [hull], isClosed=True,
                  color=(0, 255, 0), thickness=1)

surf_kp = surf.detect(sample_image, None)
surf_img = cv2.drawKeypoints(
    sample_image, surf_kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

combined_image = np.hstack((sample_image, sift_img, mser_img, surf_img))

cv2.imshow('SIFT & MSER', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
