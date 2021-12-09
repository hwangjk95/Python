#car.py
from datetime import datetime
import common as cm

class Car:
    def __init__(self, number, intime = datetime.now()):
        self.number = number
        self.intime = intime
        self.outtime = None

    def out(self):
        self.outtime = datetime.now()

    def gettime(self):
        if self.outtime == None:
            parkingtime = (datetime.now() - self.intime).seconds
        else:
            parkingtime = (self.outtime - self.intime).seconds
        return int(parkingtime/60)

    def calprice(self):
        return self.gettime() * 1000 #분당 10000원
    
    def filecontent(self):
        data = self.number
        data += '\n'
        data += datetime.strftime(self.intime, cm.datetimeformat) #strftime 활용!!!
        data += '\n'
        return data