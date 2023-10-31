import cv2
import numpy as np

# Images from https://creativecloud.adobe.com/learn/photoshop/web/photoshop-panorama
sample_image_1 = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/FeatureDetection&Matching/Start Panorama Sample Photos/DSC_2835.jpg")
sample_image_2 = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/FeatureDetection&Matching/Start Panorama Sample Photos/DSC_2836.jpg")

sift = cv2.SIFT_create()

keypoints1, descriptors1 = sift.detectAndCompute(sample_image_1, None)
keypoints2, descriptors2 = sift.detectAndCompute(sample_image_2, None)

bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

bf_matches = bf.match(descriptors1, descriptors2)
flann_matches = flann.knnMatch(descriptors1, descriptors2, k=2)

bf_matches = sorted(bf_matches, key=lambda x: x.distance)
flann_good_matches = []
for m, n in flann_matches:
    if m.distance < 0.4 * n.distance:
        flann_good_matches.append(m)

bf_img = cv2.drawMatches(sample_image_1, keypoints1, sample_image_2, keypoints2,
                         bf_matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
flann_img = cv2.drawMatches(sample_image_1, keypoints1, sample_image_2, keypoints2,
                            flann_good_matches[:20], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

combined_image = np.hstack((bf_img, flann_img))

cv2.imshow('BF & FLANN', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
