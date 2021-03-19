import csv
import Destination


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
        global myHash
        self.id = int(id)
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.availableTimeHr = int(availableTimeHr)
        self.availableTimeMin = int(availableTimeMin)
        self.deliverTimeHr = deliverTimeHr
        self.deliverTimeMin = deliverTimeMin
        self.kg = int(kg)
        self.destinationId = Destination.getIdByStreet(self.street)
        self.notes = notes
        availableTime = self.availableTimeHr*60 + self.availableTimeMin
        if (availableTime > 480) or self.destinationId == -1:
            self.status = 'Not Availible'
        else:
            self.status = 'hub'
#        print("Package:" + self.id + " Created.")

    def toString(self) -> object:
        x = "id:" + str(self.id)
        x += " DestinationId:" + str(self.destinationId)
        if not self.deliverTimeHr == 'EOD':
            x += " DeliveryTime:" + str(self.deliverTimeHr) + ':' + str(self.deliverTimeMin)
        x += " Status:" + str(self.status)
        if not self.notes == 'none':
            x += " Notes:" + str(self.notes)
        return x


class ChainingHashTable:

    # Constructor default size is 10.
    def __init__(self, capacity=10):
        self.table = []
        self.itemcount = 0;

        # Creates a list in every bucket
        for i in range(capacity):
            self.table.append([])

    def __len__(self):
        return self.itemcount

    def insert(self, package):
        bucket = hash(package.id) % len(self.table)
        bucketList = self.table[bucket]

        for item in bucketList:
            if item.id == package.id:
                item = package
                return True

        bucketList.append(package)
        self.itemcount += 1
        return True

    def search(self, id):
        bucket = hash(id) % len(self.table)
        bucketList = self.table[bucket]

        for item in bucketList:
            if item.id == id:
                return item
        return None

    def remove(self, package):
        bucket = hash(package.id) % len(self.table)
        bucketList = self.table[bucket]

        for item in bucketList:
            if item.id == package.id:
                bucketList.remove(item)
                self.itemcount -= 1

    def printAll(self):
        index = 1
        count = 0
        while count < len(self):
            if not self.search(index) is None:
                print(self.search(index).toString())
                count += 1
            index += 1

    def printAllAvailible(self):
        index = 1
        count = 0
        while count < len(self):
            if not self.search(index) is None:
                if self.search(index).status == 'hub':
                    print(self.search(index).toString())
                count += 1
            index += 1


global hashTable
hashTable = ChainingHashTable()


def readPackageList():
    global hashTable
    with open('Packages.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            item = Packages(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
            hashTable.insert(item)


def printPackageList():
    global hashTable
    for bucketList in hashTable.table:
        for item in bucketList:
            print(item.toString())

def checkPackageList(currentTime):
    global hashTable
    for bucketList in hashTable.table:
        for item in bucketList:
            # I only want to check on non available packages
            if item.status == 'Not Availible':
                timeAvailible = (item.availableTimeHr * 60) + item.availableTimeMin
                # if current time is past or equal to time availible change status to hub
                if currentTime >= timeAvailible:
                    item.status = 'hub'
                # if item number 9 is past 10:20am then update the address
                if item.id == 9 and currentTime >= 620:
                    item.street = '410 S State St'
                    item.city = 'Salt Lake City'
                    item.state = 'UT'
                    item.Zip = '84111'
                    item.destinationId = 19
                    item.notes = 'Address fixed!'
