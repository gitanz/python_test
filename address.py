import json
import random
import abc
import math


class Address:

    def __init__(self, latitude:float, longitude:float):
        self.latitude = latitude
        self.longitude = longitude

    def distanceFromOffice(self)->float:
        return DistanceBetween.method1(self, Address(53.339428, -6.257664))


class DistanceBetween:

    @staticmethod
    def method1(address1:Address, address2:Address):
        long1 = math.radians(float(address1.longitude))
        long2 = math.radians(float(address2.longitude))
        lat1 = math.radians(float(address1.latitude))
        lat2 = math.radians(float(address2.latitude))
        sigma = math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(long1-long2))
        mean_radius = 6371.009
        return mean_radius*sigma
        
    @staticmethod
    def method2(address1:Address, address2:Address):
        return random.randint(1,200)
