import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./data/0_000000000_000000000_000000000.00000_-00000001_-00000001.jpg',0)

# cv2.imshow('image',img)
# cv2.waitKey(0)

# print error if image not loaded
if img is None:
    print('Error: Image not loaded')

# drawing a rectangle
start_point = (50, 50)
end_point = (200, 200)

# draw a green rectangle
img = cv2.rectangle(img, start_point, end_point, (0, 255, 0), 3)

# display the image
cv2.imshow('image', img)
cv2.waitKey(0)