import csv


def readPackageList() -> object:
    packageHashTable = []
#    print("Start Reading PackageList...")
    with open('Packages.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            packageHashTable.append(Packages(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                             row[7], row[8], row[9], row[10], row[11]))
#    print("Done!")
    return packageHashTable


class Packages:
    global id
    global street
    global city
    global state
    global zip
    global availableTimeHr
    global availableTimeMin
    global deliverTimeHr
    global deliverTimeMin
    global kg
    global requestedTruck
    global group
    global status

    def __init__(self, id, street, city, state, zip, availableTimeHr, availableTimeMin, deliverTimeHr, deliverTimeMin, kg, requestedTruck, group):
        self.id = id
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.availableTimeHr = availableTimeHr
        self.availableTimeMin = availableTimeMin
        self.deliverTimeHr = deliverTimeHr
        self.deliverTimeMin = deliverTimeMin
        self.kg = kg
        self.requestedTruck = requestedTruck
        self.group = group
        self.status = 'hub'
#        print("Package:" + self.id + " Created.")

    def toString(self) -> object:
        x = "id:" + str(self.id)
        x += " Street:" + str(self.street)
        x += " DeliveryTime:" + str(self.deliverTimeHr) + ':' + str(self.deliverTimeMin)
        x += " RequestedTruck:" + str(self.requestedTruck)
        x += " Group:" + str(self.group)
        x += " Status:" + str(self.status)
        return x
