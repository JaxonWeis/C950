from Trucks import*
import Packages
import Destination


global usrInput
global currentTimeHr
global currentTimeMin
currentTimeHr = 8
currentTimeMin = 0


def setTime(hr, min):
    global currentTimeHr
    global currentTimeMin
    currentTimeHr = hr
    currentTimeMin = min
    while min >= 60:
        min -= 60
        hr += 1


if __name__ == '__main__':
    truck1 = Trucks(1)
    truck2 = Trucks(2)
    truck3 = Trucks(3)
    truckList = [truck1, truck2, truck3]
    packageHashTable = Packages.readPackageList()
    Destination.readDestinations()
    setTime(8,0)

    print("throwing packages 1-5 on truck 1")
    i = 0
    while not truck1.isFull():
        if i == 8:
            i += 1
        truck1.loadPackage(packageHashTable[i])
        i += 1

    while len(truck1.packageList) > 0:
        print(truck1.toString())
        truck1.driveShortestDistance(currentTimeHr,currentTimeMin)
        setTime(truck1.arrivalTimeHr,truck1.arrivalTimeMin)
        print(truck1.atDestination(currentTimeHr,currentTimeMin))
        i = 0
        while i < 0:
            packageHashTable[i].toString()
            i += 1
    truck1.setDestination(0,currentTimeHr,currentTimeMin)
    setTime(truck1.arrivalTimeHr,truck1.arrivalTimeMin)
    truck1.atDestination(currentTimeHr,currentTimeMin)
    print(truck1.toString())






    while False:
        print("\n\nOptions:\nLoad truck - L\nView Truck1,2,3 - 1,2,3\nExit - exit")
        usrInput = input()

        if usrInput == 'L':
            for x in packageHashTable:
                if x.status == 'hub':
                    print(x.toString())
            print("Which Package ID?")
            userInputPackageID = int(input())-1
            for x in truckList:
                print("Truck Id:" + str(x.id) + " Packages:" + str(x.getPackageNum()))
            print("Which Truck?")
            userInputTruckID = int(input())-1
            truckList[userInputTruckID].loadPackage(packageHashTable[userInputPackageID])

        if usrInput == '1' or usrInput == '2' or usrInput == '3':
            usrInput = int(usrInput)-1
            print("truck id:" + str(truckList[usrInput].id))
            for x in truckList[usrInput].packageList:
                print(x.toString())

        if usrInput == 'exit':
            break


