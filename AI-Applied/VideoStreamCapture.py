class VideoStreamCapture:
    def __init__(self, stream, capture_interval, max_record_size):
        self.stream = stream
        self.interval = capture_interval
        self.record = []
        self.maxsize = max_record_size


    def captureToRecord(self):
        check, frame = self.video.read()
        Record.append(frame)

    def removeFromRecord(self):
        if len(Record)>20:
            Record.pop(0)







