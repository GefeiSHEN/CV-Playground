import cv2
import numpy as np

sample_image = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/ImageManipulation/testing3.jpg")

h, w = sample_image.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
floodflags = 4
floodflags |= cv2.FLOODFILL_MASK_ONLY
floodflags |= (255 << 8)
starting_point = (w//2, h//2)
lower_diff = (5, 5, 5)
upper_diff = (5, 5, 5)

flood_filled_image = sample_image.copy()
cv2.floodFill(flood_filled_image, mask, starting_point,
              (0, 255, 0), lower_diff, upper_diff, floodflags)

combined_image = np.hstack((flood_filled_image, sample_image))

cv2.imshow("Modified Image", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
