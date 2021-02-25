from address import Address
class Customer():

    def __init__(self, customer_id, name, address:Address):
        self.id = customer_id
        self.name = name
        self.address = address
        self.distance = self.address.distanceFromOffice()
    
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address
    
    def getDistance(self):
        return self.distance
