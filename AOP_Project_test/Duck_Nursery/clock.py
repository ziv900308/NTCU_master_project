from datetime import datetime
import time

class Clock:
    originalDate = None
    currentDate = None
    originanTime = 0
    currentTime = 0
    Day = 0
    hour = 0

    def __init__(self):
        self.originalDate = datetime.now()
        self.originanTime = int(time.time() * 1000)

    def updateTime(self):
        self.currentDate = datetime.now()
        self.currentTime = int(datetime.now().timestamp() * 1000)

        self.Day = (self.currentTime - self.originanTime) / (1000*60*60*24/2000)
        self.hour = (self.currentTime - self.originanTime) / (1000*60*60/2000)%24

    def displayTime(self):
        self.updateTime()
        print("Elapsed time : {} Day & {} hour".format(self.Day, self.hour))