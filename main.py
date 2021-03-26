# Jaxon Weis Student ID:#000996862
# For class C950
#
#
# To run this applications you have to load packages manually one at a time.
#   to load a package press 'l' and it will show all packages availible to load
#   enter the package id you want to load and then the truck id to load it on
# Once you have a tuck loaded with packages you need to sort them in a route with 's'
# Once the trucks are sorted dispatch the trucks with 'd'
# Once the trucks are dispatched you can jump to the time when the truck is done with 'j'
#   or enter a time to jump to with 't'
#
#
# 8:00 AM
# 1,13,14,15,16,19,20,21,34,39 -> Truck 1
# 29,7,30,8,37,5,38,40,4 -> Truck 2
# 9:07 AM
# Truck 2 finishes
# 6,25,26,31,32 -> Truck 2
# 10:20 AM
# Truck 1 finishes
# Truck 2 finishes
# 2,3,9,10,11,12,17,18,22,23,24,27,28,33,35,36 -> Truck 2
# 1:08PM
# Truck 2 finishes
# All Packages Delivered
#

import Trucks
import Packages
import Destination
import math

global usrInput
global currentTime
currentTime = 480


# Set The clock O(p)
def setTime(time):
    global currentTime
    # check if time is moving forward
    if time > currentTime:
        currentTime = time
        hr = math.floor(currentTime / 60)
        min = currentTime % 60
        if min < 10:
            print("CurrentTime is " + str(hr) + ":0" + str(min))
        else:
            print("CurrentTime is " + str(hr) + ":" + str(min))
        for truck in Trucks.TruckList:  # check Trucks O(t)
            truck.isDelivered(currentTime)
        Packages.checkPackageList(currentTime)  # check Packages O(p)
    else:
        print("Time can't go backwards")


# Main Worst complexity O(p*d)
if __name__ == '__main__':
    # Setting up trucks O(t) t = trucks
    Trucks.CreateTrucks(3)
    # Reading Destinations from file O(d^2) d = destinations
    Destination.readDestinations()
    # Reading Packages from File O(p*d) p = packages d = destinations
    Packages.readPackageList()

    # CLI menu for all operations infinite
    while True:
        # Print out the menu O(1)
        print("\n\nv - View all Packages")
        print("l - Load Packages")
        print("1,2,3 - View Trucks 1,2,3")
        print("s - sort Truck with algorithm")
        print("d - Dispatch Truck to route")
        print("j - Jump to Truck Finished Time")
        print("t - jump to set time")
        # Add mileage from all trucks O(t) t = trucks
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

        # if user selects v - View all Packages O(p)
        if userInput == 'v':
            # Print time O(1)
            if currentTime % 60 < 10:
                print("Current Time is: " + str(math.floor(currentTime / 60)) + ":0" + str(currentTime % 60))
            else:
                print("Current Time is: " + str(math.floor(currentTime / 60)) + ":" + str(currentTime % 60))
            # Print all packages O(p) p = packages
            Packages.hashTable.printAll()
            input("Press Enter.")

        # if user selects l - load package
        elif userInput == 'l':
            # Print all available packages O(p) p = packages
            Packages.hashTable.printAllAvailible()
            # Ask Which package to load with id number
            packageInput = input("\nThe Package id number to load?")
            # Print all trucks and their package numbers O(t) t = trucks
            for truck in Trucks.TruckList:
                if not truck.isFull():
                    print("Truck" + str(truck.id) + " has Package Count:" + str(truck.getPackageNum()))
            # Ask Which Truck to load into
            truckInput = input("\nThe Truck id number to load into?")
            # Make sure the package is at the hub available to be loaded O(1)
            if Packages.hashTable.search(int(packageInput)).status == 'hub':
                # Make sure the truck is not full O(1)
                if not Trucks.TruckList[int(truckInput) - 1].isFull():
                    # Load the package into the truck O(1)
                    Trucks.TruckList[int(truckInput) - 1].loadPackage(Packages.hashTable.search(int(packageInput)))
                    input("Package Loaded!\nPress Enter.")
                else:
                    # Truck is full error O(1)
                    input("Package NOT Loaded\nTruck is Full\nPress Enter.")
            else:
                # package not available error O(1)
                input("Package Not Loaded\nPackage NOT Availible\nPress Enter.")

        # if the user selects a number than lookup that truck and display the trucks information O(t) t = trucks
        elif userInput.isnumeric():
            if int(userInput) <= len(Trucks.TruckList):
                print(Trucks.TruckList[int(userInput)-1])
                input("\nPress Enter.")

        # if the user selects s - Sort Truck O(m) m = Max packages in Truck
        elif userInput == 's':
            # Display all the trucks for user O(t) t = trucks
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
                    # Sort the selected truck by shortest neighbor O(m^2) m = Max Packages in Truck
                    Trucks.TruckList[truckId].sortShortestNeighbor()

        # if user selects d - Dispatch O(m)
        elif userInput == 'd':
            # Display all trucks for user
            for truck in Trucks.TruckList:  # O(t) t - trucks
                if truck.status == "Sorted":
                    print("Truck" + str(truck.id) + " has Package Count:" + str(truck.getPackageNum()))
                else:
                    print("Truck" + str(truck.id) + " NOT BEEN SORTED")
            # Ask the user which truck to dispatch
            truckInput = input("\nChoose which Truck?")
            if truckInput.isnumeric():
                # Set the selected truck to drive and display the truck information
                truckId = int(truckInput)-1
                Trucks.TruckList[truckId].drive(currentTime)  # O(m) m - packages in truck
                print(Trucks.TruckList[truckId])
                input("Truck Left the Hub!\nPress Enter.")

        # if the user selects j - jump to truck finish time O(t)
        elif userInput == 'j':
            # display all trucks and finish times
            for truck in Trucks.TruckList:  # O(t) t - Trucks
                if truck.status == "In Transit":
                    print("Truck" + str(truck.id) + " Finish Time:" + str(truck.arrivalTimeHr) + ":"  + str(truck.arrivalTimeMin))
                else:
                    print("Truck" + str(truck.id) + " TRUCK NOT DISPATCHED!")
            # ask the user which truck
            truckInput = input("Which Truck?")
            # get the finish time for the selected truck and set it as current time
            if truckInput != "":
                setTime(Trucks.TruckList[int(truckInput)-1].arrivalTime)
                input("Press Enter.")

        # if the user selects t - jump to set time O(1)
        elif userInput == 't':
            # ask the user what hour and minute
            hour = int(input("Enter the Hour: "))
            min = int(input ("Enter the Minute: "))
            time = hour * 60
            time += min
            setTime(time)
            input("Press Enter.")
