import csv

global destinations
global mileageTable
destinations = []
mileageTable = []


def readDestinations():
    with open('Destinations.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            destinations.append({'id': int(row[0]), 'street': row[1], 'zip': int(row[2])})
            mileageTable.append([float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]),
                                 float(row[9]), float(row[10]), float(row[11]), float(row[12]), float(row[13]),
                                 float(row[14]), float(row[15]), float(row[16]), float(row[17]), float(row[18]),
                                 float(row[19]), float(row[20]), float(row[21]), float(row[22]), float(row[23]),
                                 float(row[26]), float(row[25]), float(row[26]), float(row[27]), float(row[28]),
                                 float(row[29])])


def getIdByStreet(street) -> object:
    for x in destinations:
        if x['street'] == street:
            return x['id']
    return -1


