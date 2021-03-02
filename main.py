from Trucks import*
import Packages


if __name__ == '__main__':
    truck1 = Trucks(1)
    truck2 = Trucks(2)
    truck3 = Trucks(3)
    truckList = [truck1, truck2, truck3]
    packageHashTable = Packages.readPackageList()
    truck1.loadPackage(packageHashTable[0])
#    truck1.packageList[0]['status'] = 'onTruck' + str(truck1.id)
    print(packageHashTable[0])
