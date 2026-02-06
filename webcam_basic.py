import cv2 as cv

vid = cv.VideoCapture(0)

if not vid.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    isTrue, frame = vid.read()
    if not isTrue:
        break

    cv.imshow('Webcam Feed', frame)

    if cv.waitKey(15) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()
