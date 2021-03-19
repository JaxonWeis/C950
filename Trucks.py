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
#        print("Truck:" + str(self.id) + " Created.")

    def __str__(self):
        hr = math.floor(self.arrivalTime/60)
        min = self.arrivalTime%60
        myStr = 'TruckId:' + str(self.id) +\
                ' Status:' + str(self.status) +\
                ' FinishTime:' + str(hr) +\
                ':' + str(min) +\
                ' Miles:' + str(self.miles) +\
                ' KG:' + str(self.kg)
        myStr += "\n\tRoute Mileage:" + str(calulateMileage(self.packageList))
        for x in self.packageList:
            myStr += "\n\t|-PackageId:" + str(x.id) + " Street:" + str(x.street) + " Status:" + str(x.status)
        return myStr


    def setStatus(self, status):
        self.status = status

    def getStatus(self, status) -> object:
        return self.status

    def getPackageNum(self) -> object:
        return len(self.packageList)

    def isFull(self) -> object:
        return len(self.packageList) >= 16

    def isEmpty(self) -> object:
        return len(self.packageList) == 0

    def loadPackage(self, package):
        if not self.isFull():
            package.status = 'onTruck' + str(self.id)
            self.packageList.append(package)
            self.kg += package.kg

    def isDelivered(self, currentTime):
        if self.status == 'In Transit':
            if currentTime >= self.arrivalTime:
                for x in self.packageList:
                    x.status = x.status.replace("Arrive", "Delivered")
                self.packageList.clear()
                self.status = "Loading"
                self.kg = 0

    def drive(self, currentTime):
        self.setStatus("In Transit")
        self.driver = True
        miles = 0;
        lastId = 0;
        for x in self.packageList:
            miles += Destination.mileageTable[lastId][x.destinationId]
            time = math.ceil(miles/self.speed*60)
            arriveTime = currentTime + time
            arriveHr = math.floor(arriveTime/60)
            arrivemin = arriveTime%60
            if arrivemin < 10:
                x.status = "Arrive @ " + str(arriveHr) + ":0" + str(arrivemin)
            else:
                x.status = "Arrive @ " + str(arriveHr) + ":" + str(arrivemin)
        self.miles += calulateMileage(self.packageList)
        self.arrivalTime = currentTime + math.ceil(calulateMileage(self.packageList)/self.speed*60)
        self.arrivalTimeHr = math.floor(self.arrivalTime / 60)
        self.arrivalTimeMin = self.arrivalTime % 60

    def sortShortestNeighbor(self):
        self.setStatus("Sorted")
        self.algorithm = 'Nearest Neighbor'
        route = []
        shortestNeighbor = 0
        packageList = self.packageList
        while len(packageList) > 0:
            shortestMiles = 900
            for x in packageList:
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
        self.packageList = route

    def sortBruteForce(self):
        self.setStatus("Sorting")
        self.algorithm = 'BruteForce'
        print('Running Brute Force Sort')
        bestRoute = []
        bestRouteMiles = 90000
        packageList = self.packageList
        i = 0
        perm = 1
        num = len(packageList)
        while num > 0:
            perm *= num
            num -= 1
        print("number of perms " + str(perm))
        for x in itertools.permutations(packageList):
            if calulateMileage(x) < bestRouteMiles:
                bestRouteMiles = calulateMileage(x)
                bestRoute = x
            i += 1
            if i % 1000000 == 0:
                print("perm " + str(round((i/perm)*100,2)) + "% complete ")
        self.packageList = bestRoute

global TruckList
TruckList = []

def CreateTrucks(num = 3):
    for i in range(num):
        TruckList.append(Trucks(i + 1))



def calulateMileage(packageList) -> object:
    miles = 0
    lastId = 0
    for x in packageList:
        miles += Destination.mileageTable[lastId][x.destinationId]
        lastId = x.destinationId
    miles += Destination.mileageTable[lastId][0]
    miles = round(miles,2)
    return miles



