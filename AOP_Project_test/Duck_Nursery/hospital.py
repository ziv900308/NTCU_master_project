class Hospital:
    record = [None]*10
    ServiceItems = list()

    def __init__(self):
        self.ServiceItems.append("Feather Check")
        self.ServiceItems.append("Flight Test")
        
        self.ServiceItems.append("Body Check Up")
        self.ServiceItems.append("Get Vaccinated")
        self.ServiceItems.append("Take Medicine")

        self.ServiceItems.append("Feeding Nourishment")
        self.ServiceItems.append("Feather Care")
        self.ServiceItems.append("Recuperate")

        self.ServiceItems.append("Check MedicalCertificate")
        self.record[0] = MedicalCertificate()

    def checkMedicalCertificate(self, duck):
        print("Duck Variety : {} (ID : {})".format(duck.duckVariety, duck.ID))

        if self.record[duck.ID - 1].hospItem.get("featherCheck") == True:
            print("Feather check : Yes")
        else:
            print(print("Feather check : No"))

        if self.record[duck.ID - 1].hospItem.get("flightTest") == True:
            print("Flight test : Yes")
        else:
            print(print("Flight test : No"))

        if self.record[duck.ID - 1].hospItem.get("bodyCheckUp") == True:
            print("Body check up : Yes")
        else:
            print(print("Body check up : No"))

        if self.record[duck.ID - 1].hospItem.get("getVaccinated") == True:
            print("Get vaccinated : Yes")
        else:
            print(print("Get vaccinated : No"))

        if self.record[duck.ID - 1].hospItem.get("featherCare") == True:
            print("Feather care : Yes")
        else:
            print(print("Feather care : No"))

        if self.record[duck.ID - 1].hospItem.get("feedingNourishment") == True:
            print("Feeding nourishment : Yes")
        else:
            print(print("Feeding nourishment : No"))

        if self.record[duck.ID - 1].hospItem.get("takeMedicine") == True:
            print("Take medicine : Yes")
        else:
            print(print("Take medicine : No"))

        if self.record[duck.ID - 1].hospItem.get("recuperate") == True:
            print("Recuperate : Yes")
        else:
            print(print("Recuperate : No"))

    def check(self, duck):
        if self.record[duck.ID - 1].hospItem.get("getVaccinated") and self.record[duck.ID - 1].hospItem.get("flightTest") and self.record[duck.ID - 1].hospItem.get("bodyCheckUp"):
            print("{} (ID {}) has completed health checked".format(duck.duckVariety, duck.ID))
            self.record[duck.ID - 1].hospItem["featherCheck"] = False
            self.record[duck.ID - 1].hospItem["flightTest"] = False
            self.record[duck.ID - 1].hospItem["bodyCheckUp"] = False

        if self.record[duck.ID - 1].hospItem.get("getVaccinated") and self.record[duck.ID - 1].hospItem.get("featherCare") and self.record[duck.ID - 1].hospItem.get("feedingNourishment"):
            print("{} (ID {}) has been maintained".format(duck.duckVariety, duck.ID))
            self.record[duck.ID - 1].hospItem["getVaccinated"] = False
            self.record[duck.ID - 1].hospItem["featherCare"] = False
            self.record[duck.ID - 1].hospItem["feedingNourishment"] = False

        if self.record[duck.ID - 1].hospItem.get("takeMedicine") and self.record[duck.ID - 1].hospItem.get("recuperate"):
            print("{} (ID {}) has been recovered".format(duck.duckVariety, duck.ID))
            self.record[duck.ID - 1].hospItem["takeMedicine"] = False
            self.record[duck.ID - 1].hospItem["recuperate"] = False

    def featherCheck(self, duck):
        print("{} (ID {}) has completed the feather checking item".format(duck.duckVariety, duck.ID))
        self.record[duck.ID - 1].hospItem["featherCheck"] = True
        self.check(duck)
        print()

    def flightTest(self, duck):
        print("{} (ID {}) has completed the flight testing item".format(duck.duckVariety, duck.ID))
        self.record[duck.ID - 1].hospItem["flightTest"] = True
        self.check(duck)
        print()

    def flightTest(self, duck):
        print("{} (ID {}) has completed the body checking up item".format(duck.duckVariety, duck.ID))
        self.record[duck.ID - 1].hospItem["bodyCheckUp"] = True
        self.check(duck)
        print()

    def getVaccinated(self, duck):
        print("{} (ID {}) has getted vaccinated item".format(duck.duckVariety, duck.ID))
        self.record[duck.ID - 1].hospItem["getVaccinated"] = True
        self.check(duck)
        print()

    def featherCare(self, duck):
        print("{} (ID {}) has completed feather caring item".format(duck.duckVariety, duck.ID))
        self.record[duck.ID - 1].hospItem["featherCare"] = True
        self.check(duck)
        print()
    
    def feedingNourishment(self, duck):
        print("{} (ID {}) has completed feeding nourishment item".format(duck.duckVariety, duck.ID))
        self.record[duck.ID - 1].hospItem["feedingNourishment"] = True
        self.check(duck)
        print()

    def takeMedicine(self, duck):
        print("{} (ID {}) has completed taking medicine item".format(duck.duckVariety, duck.ID))
        self.record[duck.ID - 1].hospItem["takeMedicine"] = True
        self.check(duck)
        print()

    def recuperate(self, duck):
        print("{} (ID {}) has completed recuperating item".format(duck.duckVariety, duck.ID))
        self.record[duck.ID - 1].hospItem["recuperate"] = True
        self.check(duck)
        print()

class MedicalCertificate:
    hospItem = {}

    def __init__(self):
        self.hospItem["featherCheck"] = False
        self.hospItem["flightTest"] = False
        self.hospItem["bodyCheckUp"] = False

        self.hospItem["getVaccinated"] = False
        self.hospItem["featherCare"] = False
        self.hospItem["feedingNourishment"] = False

        self.hospItem["takeMedicine"] = False
        self.hospItem["recuperate"] = False
    
# test = MedicalCertificate()
# print(test.hospItem)
# print(test.hospItem.get("featherCheck"))