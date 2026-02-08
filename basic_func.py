import cv2 as cv
import numpy as np

# ------------------------------------
# Read and display original image
# ------------------------------------
img = cv.imread('imgs/img3.jpg')
cv.imshow('Original Image', img)

# ------------------------------------
# Convert to Grayscale
# ------------------------------------
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray)

# ------------------------------------
# Apply Gaussian Blur (Noise Reduction)
# ------------------------------------
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blurred Image', blur)

# ------------------------------------
# Edge Detection using Canny
# ------------------------------------
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ------------------------------------
# Dilate edges (Thickens edges)
# ------------------------------------
dilated = cv.dilate(canny, (5, 5), iterations=1)
cv.imshow('Dilated Edges', dilated)

# ------------------------------------
# Erode edges (Thins edges)
# ------------------------------------
eroded = cv.erode(dilated, (5, 5), iterations=1)
cv.imshow('Eroded Edges', eroded)

# ------------------------------------
# Resize Image
# ------------------------------------
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Image', resized)

# ------------------------------------
# Crop Image using NumPy slicing
# ------------------------------------
cropped = img[50:400, 100:400]
cv.imshow('Cropped Image', cropped)

"""
OpenCV Image Coordinate System (NumPy slicing)

Origin (0, 0) is at the TOP-LEFT corner

(0,0) ----------------------------------------------------> X (width)
  |
  |
  |        x = 100                     x = 400
  |          |-----------------------------|
  |          |     CROPPED REGION          |
  | y = 50   |                             |
  |          |                             |   height = 400 - 50 = 350 px
  |          |                             |
  | y = 400  |-----------------------------|
  |
  v
Y (height)

Cropping syntax:
    cropped = img[y1:y2, x1:x2]

Meaning:
    img[rows , columns]
"""

# ------------------------------------
# Wait & Close all windows
# ------------------------------------
cv.waitKey(0)
cv.destroyAllWindows()
