import cv2 as cv

def rescale_frame(frame, scale_width=0.6, scale_height=0.6):
    width = int(frame.shape[1] * scale_width)
    height = int(frame.shape[0] * scale_height)
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

vid = cv.VideoCapture(0)

if not vid.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    isTrue, frame = vid.read()
    if not isTrue:
        break

    frame_resized = rescale_frame(frame, 0.6, 0.6)

    cv.imshow('Original Webcam', frame)
    cv.imshow('Rescaled Webcam', frame_resized)

    if cv.waitKey(15) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()
