from duck import Duck
import random

class RedheadDuck(Duck):
    def __init__(self):
        self.duckVariety = "Redhead Duck"
        self.SF.SatiationScore = random.randint(80, 100)
        self.SF.PhysiqueScore = random.randint(80, 100)
        self.SF.MoodScore = random.randint(80, 100)

        self.SF.SatiationRate = -5
        self.SF.PhysiqueRate = 0
        self.SF.MoodRate = 10