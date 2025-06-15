import random

class StatusForm:
    Status = list()
    SatiationScore = 0
    PhysiqueScore = 0
    MoodScore = 0

    SatiationRate = 0
    PhysiqueRate = 0
    MoodRate = 0

    def __init__(self):
        self.Status.append("Health")

    def isHealth(self):
        i = random.randint(0, 100)
        if self.PhysiqueScore > i:
            return False
        else:
            return True
        
    def isHungry(self):
        if self.SatiationScore < 60:
            return True
        else:
            return False

    def UpdateForm(self):
        if self.isHealth():
            self.Status.remove("Sick")
            self.Status.append("Health")
        else:
            self.Status.remove("Health")
            self.Status.append("Sick")

        if self.isHungry():
            self.Status.append("Hungry")
        else:
            self.Status.remove("Hungry")

        self.SatiationScore += self.SatiationRate
        self.PhysiqueScore += self.PhysiqueRate
        self.MoodScore += self.MoodRate

        