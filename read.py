import cv2 as cv

# .......Reading Images........
# img = cv.imread("images/reference.jpg")

# cv.imshow('Image', img)
# cv.waitKey(0)

# .......Reading Videos........
capture = cv.VideoCapture('videos/test-1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
 