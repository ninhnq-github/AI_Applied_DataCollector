import cv2
# 1.creating a video object
video = cv2.VideoCapture(0) 

CardCaptureSignal = []

RecordTimeLine = []

i=1+1

for i in range (CAPFREQ*2):
    check, frame = video.read()
    RecordTimeLine.append(frame)

while True:
    i = i + 1
    # 4.Create a frame object
    check, frame = video.read()
    RecordTimeLine.append(frame)
    # Converting to grayscale
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 5.show the frame!
    cv2.imshow("Capturing",frame)
    # 6.for playing 
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    # 7. image saving
    showPic = cv2.imwrite("%d.jpg"%(a),frame)
    print(showPic)
# 8. shutdown the camera
video.release()
cv2.destroyAllWindows 