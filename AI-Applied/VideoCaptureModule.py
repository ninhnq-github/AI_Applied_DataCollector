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

def getVideoStream(IP):
    cap = cv2.VideoCapture()
    #video = cv2.VideoCapture('rtsp://admin:hd543211@192.168.1.121:8000')
    cap.open('rtsp://admin:hd543211@@'+IP+':554/Streaming/Channels/1/')
    #video = cv2.VideoCapture('rtsp://'+IP+'/h264_ulaw.sdp')
    return cap

def initVideoStreamDemo():
    video = cv2.VideoCapture(0) 
    return video

def captureToRecord(video, Record):
    check, frame = video.read()
    Record.append(frame)

def removeFromRecord(Record):
    if len(Record)>60:
        Record.pop(0)

def keepLastPic(Name, Record, Time=0):
    showPic = cv2.imwrite(Name,Record[0])
    print(Name)

def keepCurPic(Name, Record, Time=0):
    showPic = cv2.imwrite(Name,Record[len(Record)//2-1])
    print(Name)

def keepNextPic(Name, Record, Time=0):
    timer = threading.Timer(Time, keepCurPic, (Name, Record,))
    timer.start()


def CaptureStreamInput(video):
    ret, frame = video.read()
    timer = threading.Timer(0.1, CaptureStreamInput, (video,))
    timer.start()
    

def captureVideoStream(video, Record):
    captureToRecord(video, Record)
    removeFromRecord(Record)
    videoCaptureTimer = threading.Timer(0.01, captureVideoStream, (video, Record,))
    videoCaptureTimer.start()

def initProgram():
    #stream input AI
    videoAI = getVideoStream('192.168.1.113')
    #CaptureStreamInput(videoAI)
    captureVideoStream(videoAI, RecordAI)
    time.sleep(2)

    #stream input BI
    videoBI = getVideoStream('192.168.1.112')
    #CaptureStreamInput(videoBI)
    captureVideoStream(videoBI, RecordBI)
    time.sleep(2)


    
def cardSingal(CardID):
    keepLastPic('A' + ShortTime() + str(CardID) + 'IMG_PREV' + ".png",RecordAI,1)
    keepCurPic('A' + ShortTime() + str(CardID) + 'IMG_CURR' + ".png",RecordAI,1)
    keepNextPic('A' + ShortTime() + str(CardID) + 'IMG_NEXT' + ".png",RecordAI,1)

    keepLastPic('B' + ShortTime() + str(CardID) + 'IMG_PREV' + ".png",RecordBI,1)
    keepCurPic('B' + ShortTime() + str(CardID) + 'IMG_CURR' + ".png",RecordBI,1)
    keepNextPic('B' + ShortTime() + str(CardID) + 'IMG_NEXT' + ".png",RecordBI,1)
#videoCaptureTimer = threading.Timer(0.2, captureVideoStream, (videoAI, RecordAI, ))
#videoCaptureTimer.start()

initProgram()

#cardSingal('18110332')
#cardSingal('18110442')
#cardSingal('18110992')
#cardSingal('18111112')
#cardSingal('11144442')
#cardSingal('97126121')

cardSingal('18110332')
