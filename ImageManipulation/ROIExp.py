import cv2
import numpy as np

sample_image = np.zeros((500, 500, 3), dtype=np.uint8)
sample_image[:, :] = [100, 100, 100]

center_x, center_y = 150, 150
width, height = 100, 100

x1 = center_x - width // 2
y1 = center_y - height // 2
x2 = x1 + width
y2 = y1 + height

roi = sample_image[y1:y2, x1:x2]
roi[:, :, 0] = np.clip(roi[:, :, 0] + 150, 0, 255)

sample_image[y1:y2, x1:x2] = roi

sample_image = cv2.flip(sample_image, 2)

cv2.imshow("Modified Image", sample_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
