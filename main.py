import Trucks
import Packages
import Destination
import math


global usrInput
global currentTime
currentTime = 480


def setTime(hr, min):
    global currentTime
    currentTime = (hr*60) + min
    hr = math.floor(currentTime/60)
    min = currentTime % 60
    if min < 10:
        print("CurrentTime is " + str(hr) + ":0" + str(min))
    else:
        print("CurrentTime is " + str(hr) + ":0" + str(min))


def setTime(time):
    global  currentTime
    currentTime = time
    hr = math.floor(currentTime / 60)
    min = currentTime % 60
    if min < 10:
        print("CurrentTime is " + str(hr) + ":0" + str(min))
    else:
        print("CurrentTime is " + str(hr) + ":0" + str(min))


def addMinutes(mins):
    global currentTime
    currentTime += mins
    hr = math.floor(currentTime / 60)
    min = currentTime % 60
    if min < 10:
        print("CurrentTime is " + str(hr) + ":0" + str(min))
    else:
        print("CurrentTime is " + str(hr) + ":0" + str(min))


if __name__ == '__main__':
    truck1 = Trucks.Trucks(1)
    truck2 = Trucks.Trucks(2)
    truck3 = Trucks.Trucks(3)
    truckList = [truck1, truck2, truck3]
    Destination.readDestinations()
    packageHashTable = Packages.readPackageList()
    Packages.matchPackagesToDestination(packageHashTable,Destination.destinations)

    while True:
        if currentTime > 620:
            packageHashTable[8].street = '410 S State St'
            packageHashTable[8].city = 'Salt Lake City'
            packageHashTable[8].state = 'UT'
            packageHashTable[8].Zip = '84111'
            packageHashTable[8].destinationId = 19
            packageHashTable[8].notes = 'Address fixed!'

        Packages.printAvailablePackageList(packageHashTable, currentTime)
        print("l - Load Packages")
        print("1,2,3 - View Trucks 1,2,3")
        print("q,w,e - Send Trucks 1,2,3 to route")
        print("j - Jump to Truck Finished Time")
        print("t - Show Complete Package List")
        print("Current Total Mileage: " + str(truck1.miles + truck2.miles + truck3.miles))
        userInput = input("\nChoose menu item:")
        if userInput == 'l':
            userInputPackage = input("Which package id?")
            userInputTruck = input("Which Truck 1,2,3?")
            print("Loading package id:" + userInputPackage + " onto truck:" + userInputTruck)
            truckList[int(userInputTruck) - 1].loadPackage(packageHashTable[int(userInputPackage) - 1])
            input('Hit Enter to Continue')

        elif userInput == '1':
            print(truck1.toString())
            input('Hit Enter to Continue')

        elif userInput == '2':
            print(truck2.toString())
            input('Hit Enter to Continue')

        elif userInput == '3':
            print(truck3.toString())
            input('Hit Enter to Continue')

        elif userInput == 'q':
            truck1.sortShortestNeighbor()
            truck1.drive(currentTime)
            print(truck1.toString())
            input('Hit Enter to Continue')

        elif userInput == 'w':
            truck2.sortShortestNeighbor()
            truck2.drive(currentTime)
            print(truck2.toString())
            input('Hit Enter to Continue')

        elif userInput == 'e':
            truck3.sortShortestNeighbor()
            truck3.drive(currentTime)
            print(truck3.toString())
            input('Hit Enter to Continue')

        elif userInput == 'j':
            userInput = input("Which Truck 1,2,3?")
            if userInput == '1':
                setTime(truck1.arrivalTime)
            elif userInput == '2':
                setTime(truck2.arrivalTime)
            elif userInput == '3':
                setTime(truck3.arrivalTime)
            truck1.isDelivered(currentTime)
            truck2.isDelivered(currentTime)
            truck3.isDelivered(currentTime)
            input('Hit Enter to Continue')

        elif userInput == 't':
            Packages.printPackageList(packageHashTable)
            input('Hit Enter to Continue')








