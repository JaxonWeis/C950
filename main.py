# Jaxon Weis Student ID:#000996862
# For class C950
# Passed on 3rd attempt

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
        printTime()
        for truck in Trucks.TruckList:  # check Trucks O(t)
            truck.isDelivered(currentTime)
        Packages.checkPackageList(currentTime)  # check Packages O(p)
    else:
        print("Time can't go backwards")


def printTime():
    global currentTime
    if currentTime % 60 < 10:
        print("Current Time is: " + str(math.floor(currentTime / 60)) + ":0" + str(currentTime % 60))
    else:
        print("Current Time is: " + str(math.floor(currentTime / 60)) + ":" + str(currentTime % 60))


# Main Worst complexity O(p*d)
if __name__ == '__main__':
    # Setting up trucks O(t) t = trucks
    Trucks.CreateTrucks(3)
    truck1 = Trucks.TruckList[0]
    truck2 = Trucks.TruckList[1]
    # Reading Destinations from file O(d^2) d = destinations
    Destination.readDestinations()
    # Reading Packages from File O(p*d) p = packages d = destinations
    Packages.readPackageList()

    # HardCoded Loading
    # 8:00 Loading #####################################################################################################
    printTime()

    print("\nLoading Packages 1,13,14,15,16,19,20,21,34,39 -> Truck 1")
    # 1,13,14,15,16,19,20,21,34,39 -> Truck 1
    truck1.loadPackage(Packages.hashTable.search(1))  # O(1)
    truck1.loadPackage(Packages.hashTable.search(13))  # O(1)
    truck1.loadPackage(Packages.hashTable.search(14))  # O(1)
    truck1.loadPackage(Packages.hashTable.search(15))  # O(1)
    truck1.loadPackage(Packages.hashTable.search(16))  # O(1)
    truck1.loadPackage(Packages.hashTable.search(19))  # O(1)
    truck1.loadPackage(Packages.hashTable.search(20))  # O(1)
    truck1.loadPackage(Packages.hashTable.search(21))  # O(1)
    truck1.loadPackage(Packages.hashTable.search(34))  # O(1)
    truck1.loadPackage(Packages.hashTable.search(39))  # O(1)
    truck1.sortShortestNeighbor()  # O(m^2) m = loaded packages
    truck1.drive(currentTime)  # O(m) m = loaded packages
    print(truck1)
    input("Press enter")

    print("\nLoading Packages 4,5,7,8,29,30,37,38,40 -> Truck 2")
    # 4,5,7,8,29,30,37,38,40 -> Truck 2
    truck2.loadPackage(Packages.hashTable.search(4))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(5))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(7))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(8))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(29))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(30))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(37))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(38))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(40))  # O(1)
    truck2.sortShortestNeighbor()  # O(m^2) m = loaded packages
    truck2.drive(currentTime)  # O(m) m = loaded packages
    print(truck2)
    input("Press enter")

    print("\n")
    printTime()  # O(1)
    Packages.hashTable.printAll()  # O(p) p = packages
    input("Press enter")

    # 9:07 Loading #####################################################################################################
    setTime(547)  # O(1)
    print("Truck 2 is Finished")

    print("\nLoading Packages 6,25,26,31,32 -> Truck 2")
    # 6,25,26,31,32 -> Truck 2
    truck2.loadPackage(Packages.hashTable.search(6))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(25))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(26))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(31))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(32))  # O(1)
    truck2.sortShortestNeighbor()  # O(m^2) m = loaded packages
    truck2.drive(currentTime)  # O(m) m = loaded package
    print(truck2)
    input("Press enter")

    print("\n")
    printTime()  # O(1)
    Packages.hashTable.printAll()  # O(p) p = packages
    input("Press enter")

    # 10:20 Loading ####################################################################################################
    setTime(620)  # O(1)
    print("Truck 1 is Finished")
    print("Truck 2 is Finished")

    print("\nLoading Packages 2,3,9,10,11,12,17,18,22,23,24,27,28,33,35,36 -> Truck 2")
    # 2,3,9,10,11,12,17,18,22,23,24,27,28,33,35,36 -> Truck 2
    truck2.loadPackage(Packages.hashTable.search(2))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(3))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(9))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(10))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(11))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(12))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(17))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(18))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(22))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(23))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(24))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(27))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(28))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(33))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(35))  # O(1)
    truck2.loadPackage(Packages.hashTable.search(36))  # O(1)
    truck2.sortShortestNeighbor()  # O(m^2) m = loaded packages
    truck2.drive(currentTime)  # O(m) m = loaded package
    print(truck2)
    input("Press enter")

    print("\n")
    printTime()  # O(1)
    Packages.hashTable.printAll()  # O(p) p = packages
    input("Press enter")

    # 13:08 All Deliveries Done ########################################################################################
    setTime(788)  # O(1)

    print("\n")
    printTime()  # O(1)
    Packages.hashTable.printAll()  # O(p) p = packages
    print("\nAll Packages Delivered")
    printTime()  # O(1)
    # Add mileage from all trucks O(t) t = trucks
    miles = 0
    for truck in Trucks.TruckList:
        miles += truck.miles
    print("Current Total Mileage: " + str(miles))
    input("Press enter")
