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
    # Setting up trucks O(n)
    Trucks.CreateTrucks(3)
    # Reading Destinations from file O(n)
    Destination.readDestinations()
    # Reading Packages from File O(n)
    Packages.readPackageList()

    # CLI menu for all operations O(infinite)
    while True:
        # Check packages to see if arrived from flight or fixed address O(n)
        Packages.checkPackageList(currentTime)
        # Print out the menu O(1)
        print("\n\nv - View all Packages")
        print("l - Load Packages")
        print("1,2,3 - View Trucks 1,2,3")
        print("s - sort Truck with algorithm")
        print("d - Dispatch Truck to route")
        print("j - Jump to Truck Finished Time")
        print("t - jump to set time")
        # Add mileage from all trucks O(n)
        miles = 0
        for truck in Trucks.TruckList:
            miles += truck.miles
        print("Current Total Mileage: " + str(miles))
        # print out time making sure minutes shows 2 digits O(1)
        if currentTime % 60 < 10:
            print("Current Time is: " + str(math.floor(currentTime / 60)) + ":0" + str(currentTime % 60))
        else:
            print("Current Time is: " + str(math.floor(currentTime / 60)) + ":" + str(currentTime % 60))
        # Get User input of menu items
        userInput = input("\nChoose menu item:")

        ########################################################################################################

        # if user selects v - View all Packages O(n)
        if userInput == 'v':
            # Print time
            if currentTime % 60 < 10:
                print("Current Time is: " + str(math.floor(currentTime / 60)) + ":0" + str(currentTime % 60))
            else:
                print("Current Time is: " + str(math.floor(currentTime / 60)) + ":" + str(currentTime % 60))
            # Print all packages O(n)
            Packages.hashTable.printAll()
            input("Press Enter.")

        # if user selects l - load package
        elif userInput == 'l':
            # Print all available packages O(n)
            Packages.hashTable.printAllAvailible()
            # Ask Which package to load with id number
            packageInput = input("\nThe Package id number to load?")
            # Print all trucks and their package numbers O(n)
            for truck in Trucks.TruckList:
                if not truck.isFull():
                    print("Truck" + str(truck.id) + " has Package Count:" + str(truck.getPackageNum()))
            # Ask Which Truck to load into
            truckInput = input("\nThe Truck id number to load into?")
            # Make sure the package is at the hub available to be loaded
            if Packages.hashTable.search(int(packageInput)).status == 'hub':
                # Make sure the truck is not full
                if not Trucks.TruckList[int(truckInput) - 1].isFull():
                    # Load the package into the truck
                    Trucks.TruckList[int(truckInput) - 1].loadPackage(Packages.hashTable.search(int(packageInput)))
                    input("Package Loaded!\nPress Enter.")
                else:
                    # Truck is full error
                    input("Package NOT Loaded\nTruck is Full\nPress Enter.")
            else:
                # package not available error
                input("Package Not Loaded\nPackage NOT Availible\nPress Enter.")

        # if the user selects a number than lookup that truck and display the trucks information O(n)
        elif userInput.isnumeric():
            if int(userInput) <= len(Trucks.TruckList):
                print(Trucks.TruckList[int(userInput)-1])
                input("\nPress Enter.")

        # if the user selects s - Sort Truck
        elif userInput == 's':
            # Display all the trucks for user
            for truck in Trucks.TruckList:
                if truck.status == "Loading":
                    if not truck.isEmpty():
                        print("Truck" + str(truck.id) + " has Package Count:" + str(truck.getPackageNum()))
                    else:
                        print("Truck" + str(truck.id) + " IS EMPTY")
                else:
                    print("Truck" + str(truck.id) + " IS NOT AT HUB")
            # Ask the user which truck to sort
            truckInput = input("\nChoose which Truck?")
            # Ask the user which algorithm to sort by
            print("\n1 - Shortest Neighbor")
            algorithm = input("\nWhich algorithm?")
            if truckInput.isnumeric():
                truckId = int(truckInput)-1
                if algorithm == '1':
                    # Sort the selected truck by shortest neighbor O(n)
                    Trucks.TruckList[truckId].sortShortestNeighbor()

        # if user selects d - Dispatch
        elif userInput == 'd':
            # Display all trucks for user
            for truck in Trucks.TruckList:
                if truck.status == "Sorted":
                    print("Truck" + str(truck.id) + " has Package Count:" + str(truck.getPackageNum()))
                else:
                    print("Truck" + str(truck.id) + " NOT BEEN SORTED")
            # Ask the user which truck to dispatch
            truckInput = input("\nChoose which Truck?")
            if truckInput.isnumeric():
                # Set the selected truck to drive and display the truck information
                truckId = int(truckInput)-1
                Trucks.TruckList[truckId].drive(currentTime)
                print(Trucks.TruckList[truckId])
                input("Truck Left the Hub!\nPress Enter.")

        # if the user selects j - jump to truck finish time
        elif userInput == 'j':
            # display all trucks and finish times
            for truck in Trucks.TruckList:
                if truck.status == "In Transit":
                    print("Truck" + str(truck.id) + " Finish Time:" + str(truck.arrivalTimeHr) + ":"  + str(truck.arrivalTimeMin))
                else:
                    print("Truck" + str(truck.id) + " TRUCK NOT DISPATCHED!")
            # ask the user which truck
            truckInput = input("Which Truck?")
            # get the finish time for the selected truck and set it as current time
            if truckInput is not None:
                setTime(Trucks.TruckList[int(truckInput)-1].arrivalTime)
                input("Press Enter.")
                for truck in Trucks.TruckList:
                    truck.isDelivered(currentTime)

        # if the user selects t - jump to set time
        elif userInput == 't':
            # ask the user what hour and minute
            hour = int(input("Enter the Hour: "))
            min = int(input ("Enter the Minute: "))
            time = hour * 60
            time += min
            # make sure time is in the future
            if time > currentTime:
                # Set the time that was selected
                setTime(time)
            else:
                print("Time can't go backwards.")
            input("Press Enter.")
