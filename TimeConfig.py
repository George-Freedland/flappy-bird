import datetime

class TimeConfig:

    def __init__(self):
        self.initialTime = datetime.datetime.now()
    
    def timeToMakeEnemy(self):
        if ((datetime.datetime.now() - self.initialTime).seconds > 2):
            self.initialTime = datetime.datetime.now()
            return True
        return False

    def setInitialTime(self, initialTime):
        self.initialTime = initialTime