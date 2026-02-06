import cv2 as cv

vid = cv.VideoCapture('vids/14806350_2160_3840_30fps.mp4')

if not vid.isOpened():
    print("Error: Could not open video file.")
    exit()

while True:
    isTrue, frame = vid.read()
    if not isTrue:
        break

    cv.imshow('Original Video', frame)

    if cv.waitKey(15) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()
