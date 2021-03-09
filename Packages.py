import csv
import math


def readPackageList() -> object:
    packageHashTable = []
    with open('Packages.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            packageHashTable.append(Packages(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                             row[7], row[8], row[9], row[10]))
    return packageHashTable


def printPackageList(packageList):
    for x in packageList:
        print(x.toString())



def printAvailablePackageList(packageList, currentTime):
    i = 0
    hr = math.floor(currentTime / 60)
    min = currentTime % 60
    print("Package List @" + str(hr) + ":" + str(min))
    for x in packageList:
        if currentTime >= ((x.availableTimeHr * 60) + x.availableTimeMin):
            if x.status == 'hub':
                print("\t-id:" + str(x.id) + " Street:" + str(x.street) + " ", end=' | ')
                if not x.deliverTimeHr == 'EOD':
                    print("DeliveryTime:" + str(x.availableTimeHr) + ":" + str(x.deliverTimeMin), end=' | ')
                if not x.notes == 'none':
                    print("Notes:" + x.notes, end=' | ')
        print("")


def isDeliveryDone(packageList) -> object:
    num = 0
    i = 0
    while len(packageList) > i:
        if 'delivered' not in packageList[i].status:
            return False
        i += 1
    return True


def matchPackagesToDestination(packageList, destinationList):
    for x in packageList:
        for y in destinationList:
            if x.street == 'null':
                x.destinationId = 'null'
            elif x.street == y['street']:
                x.destinationId = y['id']


class Packages:
    global id
    global street
    global city
    global state
    global destinationId
    global zip
    global availableTimeHr
    global availableTimeMin
    global deliverTimeHr
    global deliverTimeMin
    global kg
    global status
    global notes

    def __init__(self, id, street, city, state, zip, availableTimeHr, availableTimeMin, deliverTimeHr, deliverTimeMin, kg, notes):
        self.id = id
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.availableTimeHr = int(availableTimeHr)
        self.availableTimeMin = int(availableTimeMin)
        self.deliverTimeHr = deliverTimeHr
        self.deliverTimeMin = deliverTimeMin
        self.kg = int(kg)
        self.status = 'hub'
        self.destinationId = 0
        self.notes = notes
#        print("Package:" + self.id + " Created.")

    def toString(self) -> object:
        x = "id:" + str(self.id)
        x += " DestinationId:" + str(self.destinationId)
        if not self.deliverTimeHr == 'EOD':
            x += " DeliveryTime:" + str(self.deliverTimeHr) + ':' + str(self.deliverTimeMin)
        if not self.notes == 'none':
            x += " Notes:" + str(self.notes)
        x += " Status:" + str(self.status)
        return x

