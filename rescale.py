import cv2 as cv

# img = cv.imread('images/reference.jpg')
# cv.imshow('Image', img)
# cv.waitKey(0)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimentions = (width, height)

    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)



# Only for LIVE VIDEOS
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4,height)

capture = cv.VideoCapture('videos/test-1.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, .2)
    # cv.imshow('Video', frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

