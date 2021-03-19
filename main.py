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
        print("Current Time is " + str(hr) + ":0" + str(min))
    else:
        print("Current Time is " + str(hr) + ":" + str(min))


def setTime(time):
    global  currentTime
    currentTime = time
    hr = math.floor(currentTime / 60)
    min = currentTime % 60
    if min < 10:
        print("CurrentTime is " + str(hr) + ":0" + str(min))
    else:
        print("CurrentTime is " + str(hr) + ":" + str(min))


def addMinutes(mins):
    global currentTime
    currentTime += mins
    hr = math.floor(currentTime / 60)
    min = currentTime % 60
    if min < 10:
        print("CurrentTime is " + str(hr) + ":0" + str(min))
    else:
        print("CurrentTime is " + str(hr) + ":" + str(min))


if __name__ == '__main__':
    Trucks.CreateTrucks()
    Destination.readDestinations()
    Packages.readPackageList()

    while True:
        Packages.checkPackageList(currentTime)
        print("\n\nv - View all Packages")
        print("l - Load Packages")
        print("1,2,3 - View Trucks 1,2,3")
        print("s - sort Truck with algorithm")
        print("d - Dispatch Truck to route")
        print("j - Jump to Truck Finished Time")
        miles = 0
        for truck in Trucks.TruckList:
            miles += truck.miles
        print("Current Total Mileage: " + str(miles))
        if currentTime % 60 < 10:
            print("Current Time is: " + str(math.floor(currentTime / 60)) + ":0" + str(currentTime % 60))
        else:
            print("Current Time is: " + str(math.floor(currentTime / 60)) + ":" + str(currentTime % 60))
        userInput = input("\nChoose menu item:")

        if userInput == 'v':
            Packages.hashTable.printAll()
            input("Press Enter.")

        elif userInput == 'l':
            Packages.hashTable.printAllAvailible()
            packageInput = input("\nChoose which Package?")
            for truck in Trucks.TruckList:
                if not truck.isFull():
                    print("Truck" + str(truck.id) + " has Package Count:" + str(truck.getPackageNum()))
            truckInput = input("\nChoose which Truck?")
            if Packages.hashTable.search(int(packageInput)).status == 'hub':
                if not Trucks.TruckList[int(truckInput) - 1].isFull():
                    Trucks.TruckList[int(truckInput) - 1].loadPackage(Packages.hashTable.search(int(packageInput)))
                    input("Package Loaded!\nPress Enter.")
                else:
                    input("Package NOT Loaded\nTruck is Full\nPress Enter.")
            else:
                input("Package Not Loaded\nPackage NOT Availible\nPress Enter.")

        elif userInput.isnumeric():
            if int(userInput) <= len(Trucks.TruckList):
                print(Trucks.TruckList[int(userInput)-1])
                input("\nPress Enter.")

        elif userInput == 's':
            for truck in Trucks.TruckList:
                if truck.status == "Loading":
                    if not truck.isEmpty():
                        print("Truck" + str(truck.id) + " has Package Count:" + str(truck.getPackageNum()))
                    else:
                        print("Truck" + str(truck.id) + " IS EMPTY")
                else:
                    print("Truck" + str(truck.id) + " IS NOT AT HUB")

            truckInput = input("\nChoose which Truck?")
            print("\n1 - Shortest Neighbor")
            algorithm = input("\nWhich algorithm?")
            if truckInput.isnumeric():
                truckId = int(truckInput)-1
                if algorithm == '1':
                    Trucks.TruckList[truckId].sortShortestNeighbor()

        elif userInput == 'd':
            for truck in Trucks.TruckList:
                if truck.status == "Sorted":
                    print("Truck" + str(truck.id) + " has Package Count:" + str(truck.getPackageNum()))
                else:
                    print("Truck" + str(truck.id) + " NOT BEEN SORTED")
            truckInput = input("\nChoose which Truck?")
            if truckInput.isnumeric():
                truckId = int(truckInput)-1
                Trucks.TruckList[truckId].drive(currentTime)
                print(Trucks.TruckList[truckId])
                input("Truck Left the Hub!\nPress Enter.")

        elif userInput == 'j':
            for truck in Trucks.TruckList:
                if truck.status == "In Transit":
                    print("Truck" + str(truck.id) + " Finish Time:" + str(truck.arrivalTimeHr) + ":"  + str(truck.arrivalTimeMin))
                else:
                    print("Truck" + str(truck.id) + " TRUCK NOT DISPATCHED!")
            truckInput = input("Which Truck?")
            if truckInput is not None:
                setTime(Trucks.TruckList[int(truckInput)-1].arrivalTime)
                input("Press Enter.")
                for truck in Trucks.TruckList:
                    truck.isDelivered(currentTime)
