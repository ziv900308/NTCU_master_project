from statusForm import StatusForm

class Duck:
    ID = 0
    duckVariety = ""
    SF = StatusForm()

    def wavingWing(self):
        print(self.duckVariety + " (ID{}) is flapping its wings".format(self.ID))

    def walk(self):
        print(self.duckVariety + " (ID{}) is walking".format(self.ID))

    def swim(self):
        print(self.duckVariety + " (ID{}) is swimming".format(self.ID))

    def fly(self):
        print(self.duckVariety + " (ID{}) is flying".format(self.ID))

    def eat(self):
        if self.SF.SatiationScore + 10 >= 100:
            self.SF.SatiationScore = 100
            print("{} of index {} is full.".format(self.duckVariety, self.ID))
        else:
            self.SF.SatiationScore = self.SF.SatiationScore + 10
            print("{} of index {} is eating.".format(self.duckVariety, self.ID))

    def showSF(self):
        print("Duck ID : " + self.ID)
        print("duckVariety : " + self.duckVariety)
        print("State : ")
        for i in range(len(self.SF.Status)):
            print(self.SF.Status[i])

        print("Satiation Score : " + self.SF.SatiationScore)
        print("Physique Score : " + self.SF.PhysiqueScore)
        print("Mood Score : " + self.SF.MoodScore)

        print("Satiation Rate : " + self.SF.SatiationRate)
        print("Physique Rate : " + self.SF.PhysiqueRate)
        print("Mood Rate : " + self.SF.MoodRate)


    
    
