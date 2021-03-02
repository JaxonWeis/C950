class Trucks:
    global maxPackages
    global packageList
    global driver
    global speed
    global id

    def __init__(self, id):
        self.maxPackages = 16
        self.packageList = []
        self.driver = False
        self.speed = 18
        self.id = id
        print("Truck:" + str(self.id) + " Created.")

    def getPackageNum(self) -> object:
        return len(self.packageList)

    def addPackage(self, package):
        self.packageList.append(package)

    def isFull(self) -> object:
        return len(self.packageList) >= 16

    def loadPackage(self, package):
        if not self.isFull():
            package['status'] = 'onTruck' + str(self.id)
            self.packageList.append(package)
