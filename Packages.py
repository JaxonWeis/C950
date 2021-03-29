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

    # Package Constructor O(d) = destinations
    def __init__(self, id, street, city, state, zip, availableTimeHr, availableTimeMin, deliverTimeHr, deliverTimeMin, kg, notes):
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
        self.destinationId = Destination.getIdByStreet(self.street)  # O(d) d = destinations
        self.notes = notes
        availableTime = self.availableTimeHr*60 + self.availableTimeMin
        if (availableTime > 480) or self.destinationId == -1:
            self.status = 'Not Availible'
        else:
            self.status = 'hub'

    # Converting a Package to string
    def __str__(self):
        x = "id:" + str(self.id)
        x += " DestinationId:" + str(self.destinationId)
        if not self.deliverTimeHr == 'EOD':
            x += " DeliveryTime:" + str(self.deliverTimeHr) + ':' + str(self.deliverTimeMin)
        x += " Status:" + str(self.status)
        if not self.notes == 'none':
            x += " Notes:" + str(self.notes)
        return x

# Hash table class
class ChainingHashTable:

    # Constructor default size is 10.
    def __init__(self, capacity=10):
        self.table = []
        self.itemcount = 0;

        # Creates a list in every bucket
        for i in range(capacity):
            self.table.append([])

    # used to get the number of items in the hash table
    def __len__(self):
        return self.itemcount

    # insert a Package into the hash table with the id as the key O(1)
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

    # finding a package in a hash table with the id as the key O(number of item in bucket)
    def search(self, id):
        bucket = hash(id) % len(self.table)
        bucketList = self.table[bucket]

        for item in bucketList:
            if item.id == id:
                return item
        return None

    # Removing a package from the hash table with the id as a key O(number of item in bucket)
    def remove(self, package):
        bucket = hash(package.id) % len(self.table)
        bucketList = self.table[bucket]

        for item in bucketList:
            if item.id == package.id:
                bucketList.remove(item)
                self.itemcount -= 1

    # Print all packages in hash in order O(p) p = packages
    def printAll(self):
        index = 1
        count = 0
        while count < len(self):
            if not self.search(index) is None:
                print(self.search(index))
                count += 1
            index += 1

    # Print all packages availible O(n)
    def printAllAvailible(self):
        index = 1
        count = 0
        while count < len(self):
            if not self.search(index) is None:
                if self.search(index).status == 'hub':
                    print(self.search(index))
                count += 1
            index += 1


# creating a global hash table
global hashTable
hashTable = ChainingHashTable()


# read the package list O(p*d) p = packages d = destinations
def readPackageList():
    global hashTable
    with open('Packages.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:  # O(p) p = packages
            item = Packages(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])  # O(d) d = destinations
            hashTable.insert(item)  # O(1)


# print all the packages in hash table no order O(n)
def printPackageList():
    global hashTable
    for bucketList in hashTable.table:
        for item in bucketList:
            print(item)


# check the package list for late flight arrivals and updated address O(n)
def checkPackageList(currentTime):
    global hashTable
    for bucketList in hashTable.table:
        for item in bucketList:
            # I only want to check on non available packages
            if item.status == 'Not Availible':
                timeAvailible = (item.availableTimeHr * 60) + item.availableTimeMin
                # if current time is past or equal to time availible change status to hub
                if currentTime >= timeAvailible and not item.destinationId == -1:
                    item.status = 'hub'
                    item.notes = "Arrived on Flight"
                # if item number 9 is past 10:20am then update the address
                if item.id == 9 and currentTime >= 620:
                    item.street = '410 S State St'
                    item.city = 'Salt Lake City'
                    item.state = 'UT'
                    item.Zip = '84111'
                    item.destinationId = 19
                    item.status = 'hub'
                    item.notes = 'Address fixed!'
