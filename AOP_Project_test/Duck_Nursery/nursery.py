from duck import Duck
import random

class Nursery:
    # Duck[] DuckArray = new Duck[10]
    # ArrayList<FunctionalDuck> FunctionduckArray = new ArrayList<FunctionalDuck>()

    temperature = 0.0
    huimidity = 0
    hospital = None
    illustratedBook = None
    DuckArray = [None]*10
    FunctionduckArray = list()

    def __init__(self, hospital, illustratedBook):
        self.hospital = hospital
        self.illustratedBook = illustratedBook
        self.temperature = 22.5
        self.huimidity = 50

    def addDuck(self, duck):
        for i in range(len(self.DuckArray)):
            if self.DuckArray[i] == None:
                self.DuckArray[i] = duck
                duck.ID = i + 1
                break

    def adjustTemperature(self):
        print("You can input number with a decimal separator and between 20 to 40.")
        TP = float(input("Set temperature to :"))

        if TP > 40 or TP < 20:
            print("You cannot set the temperature to less than 20 or greater than 40.")
            return
        
        print("Temperature has been set to {}℃".format(TP))
        self.temperature = TP
        print("-"*50)

    def adjustHumidity(self):
        print("You can input an integer from 0 to 100.")
        HD = int(input("Set humidity to :"))

        if HD > 100 or HD < 0:
            print("You cannot set the humidity to less trhan 0 or greater than 100.")
            return
        
        print("Humidity has been set to {}%".format(HD))
        self.huimidity = HD
        print("-"*50)

    def feeding(self):
        for i in range(len(self.DuckArray)):
            if self.DuckArray[i] == None:
                break
            self.DuckArray[i].eat()

        print("-"*50)

    def checkDuckStatus(self):
        print("You currently own the following ducks")

        for i in range(len(self.DuckArray)):
            if self.DuckArray[i] == None:
                break
            print((i + 1) + " : " + self.DuckArray[i].duckVariety)
        
        print()

        number = int(input("Which duck's status do you want to check:"))
        if self.DuckArray[number - 1] == None:
            print("Youy don't have this number of duck")
        else:
            self.DuckArray[number - 1].showSF()
        
        print("-"*50)

    def watchDucks(self):
        randomNum = 0
        print("Observe the nursery...")

        for i in range(len(self.DuckArray)):
            if self.DuckArray[i] == None:
                break
            
            randomNum = random.randint(1, 4)
            if randomNum == 1:
                self.DuckArray[i].wavingWing()
            elif randomNum == 2:
                self.DuckArray[i].walk()
            elif randomNum == 3:
                self.DuckArray[i].swim()
            elif randomNum == 4:
                self.DuckArray[i].fly()
            else:
                print("Not found...")
        
        print("-"*50)

    def readIllustratedBook(self):
        self.illustratedBook.read()
    
    def goHospital(self):
        badDuckId = True
        duckID = 0
        patientDuck = None

        while(badDuckId):
            print("Your nursery have these duck.")
            for i in range(len(self.DuckArray)):
                if self.DuckArray[i] != None:
                    print(self.DuckArray[i].ID + ":" + self.DuckArray[i].duckVariety)

            try:
                duckID = int(input("Input duck ID to take it to hospital:"))
                if duckID < 0 and duckID > 10:
                    print("Please input correct duck ID")
                elif self.DuckArray[duckID - 1] == None:
                    print("You don't have this duck")
                else:
                    patientDuck = self.DuckArray[duckID - 1]
                    badDuckId = False

            except:
                print("You must enter a duck ID number")

        stayhosp = True
        if self.hospital.record[duckID - 1] == None:
            self.hospital.record[duckID - 1] = self.hospital.MedicalCertificate(self.hospital)

        while(stayhosp):
            print("Hosp Items:")
            for i in range(self.hospital.ServiceItems.size()):
                print((i + 1) + ":" + self.hospital.ServiceItems.get(i))
            
            print((self.hospital.ServiceItems.size() + 1) + ":Leave Hospital")
            hospitem = int(input("Input Item number:"))

            if hospitem == 1:
                self.hospital.featherCheck(patientDuck)
            elif hospitem == 2:
                self.hospital.flightTest(patientDuck)
            elif hospitem == 3:
                self.hospital.bodyCheckUp(patientDuck)
            elif hospitem == 4:
                self.hospital.getVaccinated(patientDuck)
            elif hospitem == 5:
                self.hospital.takeMedicine(patientDuck)
            elif hospitem == 6:
                self.hospital.feedingNourishment(patientDuck)
            elif hospitem == 7:
                self.hospital.featherCare(patientDuck)
            elif hospitem == 8:
                self.hospital.recuperate(patientDuck)
            elif hospitem == 9:
                self.hospital.checkMedicalCertificate(patientDuck)
            elif hospitem == 10:
                stayhosp = False
            else:
                print("Please input correct Item number...")
                


# test = Nursery()
# test.addDuck(Duck())
# test.adjustTemperature()

# for i in range(len(test.DuckArray)):
#     if test.DuckArray[i] != None and test.DuckArray[i].ID != None:
#         print(test.DuckArray[i].ID)
#     else:
#         print("This Duck has no ID...")