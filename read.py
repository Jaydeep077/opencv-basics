import cv2 as cv

###reading and displaying image
img=cv.imread('imgs/img1.jpg')
cv.imshow('tiger',img)
cv.waitKey(10000)
print(img.shape)
print(type(img))

###capturing video   

capture=cv.VideoCapture(0)
while True:
    isTrue,frame=capture.read()
    print(isTrue)
    if not isTrue:
        break
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()




