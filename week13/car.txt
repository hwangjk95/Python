from datetime import datetime

class Car:
    def __init__(self, number):
        self.number = number
        self.intime = datetime.now()
        self.outtime = None

    def out(self):
        self.outtime = datetime.now()

    def gettime(self):
        if self.outtime == None:
            return (datetime.now() - self.intime).seconds
        else:
            return (self.outtime - self.intime).seconds

    def calprice(self):
        return self.gettime() * 1000
