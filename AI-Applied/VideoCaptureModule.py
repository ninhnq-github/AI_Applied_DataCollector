import cv2
import sched
import threading 
import time

TIME_OF_PIC = 0.2

videoAI, videoAO, videoBI, videoBO, videoCI, videoCO = None, None, None, None, None, None 

RecordAI, RecordAO, RecordBI, RecordBO, RecordCI, RecordCO = [], [], [], [], [], []

def ShortTime():
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%Y%m%d%H%M%S", named_tuple)
    return time_string

def getVideoStream(video, IP, Pass):
    video = cv2.VideoCapture('rtsp://username:'+Pass+'@'+IP)

def initVideoStreamDemo():
    video = cv2.VideoCapture(0) 
    return video

def captureToRecord(video, Record):
    check, frame = video.read()
    Record.append(frame)

def removeFromRecord(Record):
    if len(Record)>20:
        Record.pop(0)

def keepLastPic(Name, Record, Time=0):
    showPic = cv2.imwrite(Name,Record[0])
    print(Name)

def keepCurPic(Name, Record, Time=0):
    showPic = cv2.imwrite(Name,Record[len(Record)-1])
    print(Name)

def keepNextPic(Name, Record, Time=0):
    timer = threading.Timer(Time, keepCurPic, (Name, Record,))
    timer.start()


def captureVideoStream(video, Record):
    captureToRecord(video, Record)
    removeFromRecord(Record)
    #print('Loading...')
    videoCaptureTimer = threading.Timer(0.2, captureVideoStream, (video, Record,))
    videoCaptureTimer.start()

def initProgram():
    #stream input AI
    videoAI = initVideoStreamDemo()
    captureVideoStream(videoAI, RecordAI)
    time.sleep(2)
    
def cardSingal(CardID):
    keepLastPic(str(CardID) + 'IMG_PREV' + ShortTime() + ".png",RecordAI,2)
    keepCurPic(str(CardID) + 'IMG_CURR' + ShortTime() + ".png",RecordAI,2)
    keepNextPic(str(CardID) + 'IMG_NEXT' + ShortTime() + ".png",RecordAI,2)

#videoCaptureTimer = threading.Timer(0.2, captureVideoStream, (videoAI, RecordAI, ))
#videoCaptureTimer.start()

initProgram()

#cardSingal('18110332')
#cardSingal('18110442')
#cardSingal('18110992')
#cardSingal('18111112')
#cardSingal('11144442')
#cardSingal('97126121')

