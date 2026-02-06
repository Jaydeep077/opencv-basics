import cv2 as cv

def change_res(vid, width=640, height=480):
    vid.set(cv.CAP_PROP_FRAME_WIDTH, width)
    vid.set(cv.CAP_PROP_FRAME_HEIGHT, height)

vid = cv.VideoCapture(0)

if not vid.isOpened():
    print("Error: Could not open webcam.")
    exit()

change_res(vid, 1280, 720)

actual_width = vid.get(cv.CAP_PROP_FRAME_WIDTH)
actual_height = vid.get(cv.CAP_PROP_FRAME_HEIGHT)
print(f"Webcam resolution: {int(actual_width)} x {int(actual_height)}")

while True:
    isTrue, frame = vid.read()
    if not isTrue:
        break

    cv.imshow('Webcam with Changed Resolution', frame)

    if cv.waitKey(15) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()
