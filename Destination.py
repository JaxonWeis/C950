import csv

global destinations
global mileageTable
destinations = []
mileageTable = []


# Read the package list O(d^2) d = destinations
def readDestinations():
    with open('Destinations.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:  # O(d) d = destinations
            destinations.append({'id': int(row[0]), 'street': row[1], 'zip': int(row[2])})  # O(1)
            miles = []
            i = 3
            while i < len(row):  # O(d) d = destinations
                miles.append(float(row[i]))  # O(1)
                i += 1
            mileageTable.append(miles)  # O(1)


# get the id number by street address O(d) d = destinations
def getIdByStreet(street) -> object:
    for x in destinations:
        if x['street'] == street:
            return x['id']
    return -1


