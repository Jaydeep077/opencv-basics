import cv2 as cv

def rescale_frame(frame, scale_width=0.5, scale_height=0.5):
    width = int(frame.shape[1] * scale_width)
    height = int(frame.shape[0] * scale_height)
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

vid = cv.VideoCapture('vids/15118509_2562_1440_60fps.mp4')

if not vid.isOpened():
    print("Error: Could not open video file.")
    exit()

while True:
    isTrue, frame = vid.read()
    if not isTrue:
        break

    frame_resized = rescale_frame(frame, 0.5, 0.5)

    cv.imshow('Original Video', frame)
    cv.imshow('Rescaled Video', frame_resized)

    if cv.waitKey(15) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()
