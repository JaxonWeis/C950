import Destination
import math


class Trucks:
    global maxPackages
    global packageList
    global driver
    global speed
    global id
    global miles
    global status
    global currentLocation
    global currentDestination
    global arrivalTimeHr
    global arrivalTimeMin
    global currentHr
    global currentMin

    def __init__(self, id):
        self.maxPackages = 16
        self.packageList = []
        self.driver = False
        self.speed = 18
        self.id = id
        self.miles = 0;
        self.status = 'loading'
        self.currentLocation = 0;
        self.currentDestination = 0;
        self.arrivalTimeHr = 8;
        self.arrivalTimeMin = 0;
        self.currentHr = 8;
        self.currentMin = 0;
#        print("Truck:" + str(self.id) + " Created.")

    def toString(self) -> object:
        myStr = 'TruckId:' + str(self.id) + ' Status:' + str(self.status) + ' ArrivalTime:' + str(self.arrivalTimeHr) +\
                ':' + str(self.arrivalTimeMin) + ' Miles:' + str(self.miles)
        for x in self.packageList:
            myStr += "\n\t|_PackageId:" + str(x.id) + " Status:" + str(x.status) + " Street:" + str(x.street)
        return myStr

    def setStatus(self, status):
        self.status = status

    def getStatus(self, status) -> object:
        return self.status

    def getPackageNum(self) -> object:
        return len(self.packageList)

    def isFull(self) -> object:
        return len(self.packageList) >= 16

    def setArrivalTime(self, hr, min):
        self.arrivalTimeHr = hr
        self.arrivalTimeMin = min
        while self.arrivalTimeMin >= 60:
            self.arrivalTimeMin = self.arrivalTimeMin - 60
            self.arrivalTimeHr = self.arrivalTimeHr + 1

    def loadPackage(self, package):
        if not self.isFull():
            package.status = 'onTruck' + str(self.id)
            self.packageList.append(package)

    def setDestination(self, destination, currentHr, currentMin):
        miles = Destination.mileageTable[self.currentLocation][destination]
        min = math.ceil((miles / self.speed)*60)
        self.setArrivalTime(self.arrivalTimeHr, self.arrivalTimeMin+min)
        self.currentDestination = destination
        self.status = 'inTransit'
        self.miles += miles

    def atDestination(self, currentHr, currentMin) -> object:
        if currentHr >= self.arrivalTimeHr and currentMin >= self.arrivalTimeMin:
            self.status = 'arrived'
            for x in self.packageList:
                if x.street == Destination.destinations[self.currentDestination]['street']:
                    x.status = 'delivered at: ' + str(self.arrivalTimeHr) + ":" + str(self.arrivalTimeMin)
                    self.packageList.remove(x)
            if self.currentDestination == 0:
                self.setStatus('loading')
            return True
        return False

    def driveShortestDistance(self, currentHr, currentMin):
        self.setStatus("inTransit")
        self.currentHr = currentHr
        self.currentMin = currentMin
        print("running shortest Neighbor")
        set = []
        for x in self.packageList:
            set.append(x.street)
        print("Comparing " + str(len(set)) + " packages")
        shortestMiles = 1000000
        shortestNeighbor = 0
        for x in set:
            for y in Destination.destinations:
                if y['street'] == x:
                    x = y['id']
            if int(Destination.mileageTable[self.currentLocation][x]) < shortestMiles:
                shortestMiles = Destination.mileageTable[self.currentLocation][int(x)]
                shortestNeighbor = x
        print("Shortest Neighbor is " + str(shortestNeighbor) + " " + Destination.destinations[shortestNeighbor]['street'])
        self.setDestination(shortestNeighbor, self.currentHr, self.currentMin)