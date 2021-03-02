import csv


def readPackageList() -> object:
    packageHashTable = []
    print("Start Reading PackageList...")
    with open('Packages.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            package = {'id': row[0], 'street': row[1], 'city': row[2], 'state': row[3], 'zip': row[4],
                       'availableByTime': row[5], 'deliverByTime': row[6], 'kg': row[7], 'requestedTruck': row[8],
                       'group': row[9], 'status': 'Hub'}
            packageHashTable.append(package)
    print("Done!")
    return packageHashTable
