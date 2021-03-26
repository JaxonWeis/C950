import Destination
import itertools
import math


class Trucks:
    global maxPackages
    global packageList
    global driver
    global algorithm
    global speed
    global id
    global miles
    global status
    global arrivalTimeHr
    global arrivalTimeMin
    global kg

    # Truck Constructor O(1)
    def __init__(self, id):
        self.maxPackages = 16
        self.packageList = []
        self.driver = False
        self.algorithm = 'none'
        self.speed = 18
        self.id = id
        self.miles = 0;
        self.status = 'Loading'
        self.arrivalTime = 480;
        self.arrivalTimeHr = 8;
        self.arrivalTimeMin = 0
        self.kg = 0

    # The return string of a Truck O(1)
    def __str__(self):
        hr = math.floor(self.arrivalTime/60)
        min = self.arrivalTime%60
        myStr = 'TruckId:' + str(self.id) +\
                ' Status:' + str(self.status) +\
                ' FinishTime:' + str(hr) +\
                ':' + str(min) +\
                ' Miles:' + str(self.miles) +\
                ' KG:' + str(self.kg)
        myStr += "\n\tRoute Mileage:" + str(calculateMileage(self.packageList))
        # prints the package list of a Truck O(n)
        for x in self.packageList:
            myStr += "\n\t|-PackageId:" + str(x.id) + " Street:" + str(x.street) + " Status:" + str(x.status)
        return myStr

    # Set the status of a truck O(1)
    def setStatus(self, status):
        self.status = status

    # get the status of a truck O(1)
    def getStatus(self, status) -> object:
        return self.status

    # get the package number of a truck O(1)
    def getPackageNum(self) -> object:
        return len(self.packageList)

    # return true if truck is full (package num vs max packages) O(1)
    def isFull(self) -> object:
        return self.getPackageNum() >= self.maxPackages

    # return true if package list is empty O(0)
    def isEmpty(self) -> object:
        return self.getPackageNum() == 0

    # add package to package list if truck isnt full O(1)
    def loadPackage(self, package):
        if not self.isFull():
            package.status = 'onTruck' + str(self.id)
            self.packageList.append(package)
            self.kg += package.kg

    # check if all packages are delivered O(m) m = packages in truck
    def isDelivered(self, currentTime):
        if self.status == 'In Transit':
            if currentTime >= self.arrivalTime:
                for x in self.packageList:  # O(m) m = packages in truck
                    x.status = x.status.replace("Arrive", "Delivered")
                self.packageList.clear()
                self.status = "Loading"
                self.kg = 0

    # Set the truck to drive O(m)
    def drive(self, currentTime):
        self.setStatus("In Transit")
        self.driver = True
        miles = 0;
        lastId = 0;
        # Set the arrival times for all packages in the truck
        for x in self.packageList:  # O(m) m = packages in truck
            miles += Destination.mileageTable[lastId][x.destinationId]
            lastId = x.destinationId
            time = math.ceil(miles/self.speed*60)
            arriveTime = currentTime + time
            arriveHr = math.floor(arriveTime/60)
            arrivemin = arriveTime%60
            if arrivemin < 10:
                x.status = "Arrive @ " + str(arriveHr) + ":0" + str(arrivemin)
            else:
                x.status = "Arrive @ " + str(arriveHr) + ":" + str(arrivemin)
        miles += Destination.mileageTable[lastId][0]
        # Add miles to the mileage of the truck
        self.miles += miles
        # calculate the drive time for the round trip
        self.arrivalTime = currentTime + math.ceil(miles / self.speed * 60)
        self.arrivalTimeHr = math.floor(self.arrivalTime / 60)
        self.arrivalTimeMin = self.arrivalTime % 60

    # Sort the package list in shortest neighbor O(m^2)
    def sortShortestNeighbor(self):
        self.setStatus("Sorted")
        self.algorithm = 'Nearest Neighbor'
        route = []
        shortestNeighbor = 0
        packageList = self.packageList
        # So I guess I made a bubble sort algorithm for this. O(m^2)
        while len(packageList) > 0:  # loop through package list and remove 1 item each round O(m) m = packages in truck
            shortestMiles = 900
            for x in packageList:  # for each item in the package list get the mileage and find the shortest 0(m)
                if len(route) == 0:
                    if Destination.mileageTable[0][x.destinationId] < shortestMiles:
                        shortestMiles = Destination.mileageTable[0][x.destinationId]
                        shortestNeighbor = x
                else:
                    if Destination.mileageTable[route[-1].destinationId][x.destinationId] < shortestMiles:
                        shortestMiles = Destination.mileageTable[route[-1].destinationId][x.destinationId]
                        shortestNeighbor = x
            route.append(shortestNeighbor)
            packageList.remove(shortestNeighbor)
        # reWrite package list with package list in order of shortest route
        self.packageList = route

    # Brute force the route !!!O(n!)!!! takes too long for packagelist > 10
    def sortBruteForce(self):
        self.setStatus("Sorted")
        self.algorithm = 'BruteForce'
        print('Running Brute Force Sort')
        bestRoute = []
        bestRouteMiles = 90000
        packageList = self.packageList
        i = 0
        perm = math.perm(len(packageList))
        print("number of perms " + str(perm))
        for x in itertools.permutations(packageList):
            if calculateMileage(x) < bestRouteMiles:
                bestRouteMiles = calculateMileage(x)
                bestRoute = x
            i += 1
            if i % 1000000 == 0:
                print("perm " + str(round((i/perm)*100,2)) + "% complete ")
        self.packageList = bestRoute


global TruckList
TruckList = []


# Creates Trucks Default 3 O(t) t = trucks
def CreateTrucks(num = 3):
    for i in range(num):
        TruckList.append(Trucks(i + 1))


# Calculate the mileage based on the package list O(m) m = packages in trucks
def calculateMileage(packageList) -> object:
    miles = 0
    lastId = 0
    for x in packageList:
        miles += Destination.mileageTable[lastId][x.destinationId]
        lastId = x.destinationId
    miles += Destination.mileageTable[lastId][0]
    miles = round(miles,2)
    return miles



