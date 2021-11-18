#car.py
from _datetime import datetime

class Car:
    def __init__(self, number):
        self.number =number
        self.intime = datetime.now()
        self.outtime = None
        
    def out(self):
        self.outtime = datetime.now()
        
    def gettime(self):
        if self.outtime == None:
            totaltime = datetime.now() - self.intime #현재 주차료 확인
        else:
            totaltime = self.outtime - self.intime #출차 주차료 
        
        return totaltime.seconds  #/ (60*60)
    
    def calprice(self):
        return self.gettime()*1000