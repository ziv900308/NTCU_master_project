class IllustratedBook:
    Npage = list()
    Fpage = list()
    categoryList = list()

    def __init__(self):
        self.categoryList.append("Normal Duck")
        self.categoryList.append("Functional Duck")

        # self.Npage.append(NormalDuckPage("Mallard Duck", 25, 20, 65, 50, 5))
        # self.Npage.append(NormalDuckPage("Redhead Duck", 22, 15, 60, 45, 5))

        # self.Fpage.append(FunctionalDuckPage("Rubber Duck", "Make the duck happy."))
        # self.Fpage.append(FunctionalDuckPage("Decoy Duck", "Attract new ducks."))

    def addNPage(self, page):
        self.Npage.append(page)

    def addFPage(self, page):
        self.Fpage.append(page)

    def read(self):
        print("Choose category:")
        print("1: Normal Duck")
        print("2: Functional Duck")

        inputCategoryNumber = int(input("Input categories ID: "))
        if inputCategoryNumber == 1:
            print("You choose normal Duck category.")
            print("-"*50)

            print("Normal duck pages: ")
            for i in range(len(self.Npage)):
                print("Page {}: {}".format(i, self.Npage[i].duckVariety))

            inputItemNumber = int(input("Input ID to read information of normal duck: "))
            if self.Npage[inputItemNumber - 1] == None:
                print("No this page.")
                print("-"*50)
            
            else:
                Tpage = self.Npage[inputItemNumber - 1]
                print("Duck Variety: " + Tpage.duckVariety)
                print("Preference Temperature Scope: {} ~ {}".format(Tpage.preferenceMinT, Tpage.preferenceMaxT))
                print("Preference Humidity Scope: {} ~ {}".format(Tpage.preferenceMinH, Tpage.preferenceMaxH))
                print("Duck starvation Rate: " + Tpage.starvationRate)

        elif inputCategoryNumber == 2:
            print("You choose functional Duck category.")
            print("-"*50)

            print("Functional Duck pages : ")
            for i in range(len(self.Fpage)):
                print("Page {}: {}".format(i, self.Fpage[i].duckVariety))
            
            inputItemNumber = int(input("Input ID to read information of normal duck: "))
            if self.Fpage[inputItemNumber - 1] == None:
                print("No this page.")
                print("-"*50)
            
            else:
                Tpage = self.Fpage[inputItemNumber - 1]
                print("Duck Variety: " + Tpage.duckVariety)
                print("Function: " + Tpage.commnet)


        else:
            print("No this category...")
            print("Please enter again corrently...")

        print("-"*50)
 