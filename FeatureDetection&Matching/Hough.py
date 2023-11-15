import cv2
import numpy as np

sample_image = cv2.imread(
    "/Users/gefeishen/Developer/Research/Playground/CV-Playground/ImageManipulation/TE100.jpg")
gray_image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray_image, 140, 400, apertureSize=7)
lines = cv2.HoughLines(edges, 1, np.pi / 360, 200)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(sample_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the result
cv2.imshow('Hough', sample_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
