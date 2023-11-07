import cv2
import numpy as np

sample_image = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/ImageManipulation/TE100.jpg", cv2.IMREAD_GRAYSCALE)
# https://people.math.sc.edu/Burkardt/c_src/image_denoise/image_denoise.html
# sample_image = cv2.imread(
#     "/Users/gefeishen/Developer/Research/Playground/CV-Playground/FeatureDetection&Matching/balloons_noisy.png", cv2.IMREAD_GRAYSCALE)

small_kernel_size = (3, 3)
large_kernel_size = (9, 9)

gaussian_small = cv2.GaussianBlur(sample_image, small_kernel_size, 0)
gaussian_large = cv2.GaussianBlur(sample_image, large_kernel_size, 0)

DoG = cv2.subtract(sample_image, gaussian_large)

sign = np.sign(DoG)

combined_image = np.hstack((gaussian_small, gaussian_large, DoG))

cv2.imshow('DoG', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
