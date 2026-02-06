import cv2 as cv

def rescale_frame(frame, scale_width=0.5, scale_height=0.5):
    width = int(frame.shape[1] * scale_width)
    height = int(frame.shape[0] * scale_height)
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

img = cv.imread('imgs/img2.jpg')

if img is None:
    print("Error: Could not load image.")
    exit()

cv.imshow('Original Image', img)
resized_img = rescale_frame(img, 0.3, 0.3)
cv.imshow('Rescaled Image', resized_img)

cv.waitKey(5000)
cv.destroyAllWindows()
