import cv2 as cv

# Load image
img = cv.imread('imgs/img1.jpg')

if img is None:
    print("Error: Could not load image.")
    exit()

# Show image
cv.imshow('Original Image', img)
cv.waitKey(3000)  # Wait 3 seconds
cv.destroyAllWindows()
