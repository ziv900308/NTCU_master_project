from hospital import Hospital
from illustratedBook import IllustratedBook
from nursery import Nursery
from clock import Clock
from backgroundProcess import BackgroundProcess


end = False
action = 0

Hosp = Hospital()
IB = IllustratedBook()

nursery = Nursery(Hosp, IB)
clock = Clock()
BgP = BackgroundProcess(clock, nursery)
BgP.start()

print("Welcome to Duck Nursery Game...")
print()

while not end:
    print("You can do the following things: ")
    print()
    print("1: Watch what your duck is doing...")
    print("2: Check the status of the duck...")
    print("3: Adjust the temperature of the nursery...")
    print("4: Adjust the humidity of the nursery...")
    print("5: Feed duck...")
    print("6: Read illustrated book...")
    print("7: Go hospital...")
    print("8: End game...")

    try:
        actionID = int(input("Input action number: "))
    except ValueError:
        print("You must enter an action index.")
    
    print()
    if actionID == 1:
        nursery.watchDucks()
    elif actionID == 2:
        nursery.checkDuckStatus()
    elif actionID == 3:
        nursery.adjustTemperature()
    elif actionID == 4:
        nursery.adjustHumidity()
    elif actionID == 5:
        print("You fed the ducks...")
        nursery.feeding()
    elif actionID == 6:
        nursery.readIllustratedBook()
    elif actionID == 7:
        nursery.goHospital()
    elif actionID == 8:
        end = True
        BgP.playing = False
        BgP.stop()
        BgP.join()
        print("See you next time...")
        
    else:
        print("No this action number...")
        