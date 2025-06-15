from page import Page

class NormalDuckPage(Page):
    preferenceMaxT = 0.0
    preferenceMinT = 0.0
    preferenceMaxH = 0
    preferenceMinH = 0
    starvationRate = 0

    def __init__(self, duckVariety, preferenceMaxT=0.0, preferenceMinT=0.0, preferenceMaxH=0, preferenceMinH=0, starVationRate=0):
        self.category = "Normal Duck"
        self.duckVariety = duckVariety
        self.preferenceMaxT = preferenceMaxT
        self.preferenceMinT = preferenceMinT
        self.preferenceMaxH = preferenceMaxH
        self.preferenceMinH = preferenceMinH
        self.starvationRate = starVationRate 
        