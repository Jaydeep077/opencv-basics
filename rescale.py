import cv2 as cv

# ---------- Original Image ----------
img = cv.imread('imgs/img2.jpg')
cv.imshow('Original Image', img)
cv.waitKey(10000)
cv.destroyAllWindows()

# ---------- Original Video ----------
vid = cv.VideoCapture('vids/14806350_2160_3840_30fps.mp4')
while True:
    isTrue, frame = vid.read()
    if not isTrue:
        break
    cv.imshow('Original Video', frame)
    if cv.waitKey(15) & 0xFF == ord('d'):
        break
vid.release()
cv.destroyAllWindows()

# ---------- Rescaling Function ----------
def rescale_frame(frame, scale_width=0.75, scale_height=0.50):
    width = int(frame.shape[1] * scale_width)
    height = int(frame.shape[0] * scale_height)
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

# ---------- Resized Image ----------
resized_image = rescale_frame(img, 0.30)
cv.imshow('Resized Image', resized_image)
cv.waitKey(10000)
cv.destroyAllWindows()

# ---------- Resized Video ----------
vid = cv.VideoCapture('vids/14806350_2160_3840_30fps.mp4')
while True:
    isTrue, frame = vid.read()
    if not isTrue:
        break
    frame_resized = rescale_frame(frame, 0.30, 0.20)
    cv.imshow('Resized Video', frame_resized)
    if cv.waitKey(15) & 0xFF == ord('d'):
        break
vid.release()
cv.destroyAllWindows()
