import unittest
import json

from address import Address
from address import DistanceBetween
from file import File
from file import JsonTextFile
from customer import Customer
from invite import InviteCustomers

class Tests(unittest.TestCase):

    def testDistanceEqual(self):
        self.assertAlmostEqual(
            DistanceBetween.method1(
                Address(53.34831474023537, -6.40492946137835), Address(53.34823148079508, -6.404414477252805)
            ), 0.0354, 2,"Should be almost 0.035")
    
    def testDistanceFromOffice(self):
        address = Address(52.986375, -6.043701)
        self.assertAlmostEqual(address.distanceFromOffice(), 41.768, 2, 'should be 41816')

    def testTextFile(self):
        file = File('./test.txt')
        lineGenerator = file.readLine()
        self.assertEqual(next(lineGenerator).strip(), 'test')
        self.assertEqual(next(lineGenerator).strip(), 'test2')
        self.assertIsNone(next(lineGenerator))

    def testReadJsonTextLine(self):
        file = JsonTextFile('./testJson.txt')
        lineGenerator = file.readJsonTextLine()
        self.assertEqual(next(lineGenerator)['name'], 'hello')

    def testCustomerCreation(self):
        customer = Customer(12, "Christina McArdle", Address(52.986375, -6.043701))
        self.assertEqual(customer.id, 12)
        self.assertAlmostEqual(customer.distance, 41.768, 2, 'should be 41.768')

    def testInvitedCustomersAreWithinRange(self):
        inviteCustomer = InviteCustomers('./customers.txt')
        inviteCustomer.getCustomers()
        invalidCustomers = [ invitable for invitable in inviteCustomer.invitables if invitable.distance > 100]
        self.assertListEqual(invalidCustomers, [])

    def testInvitedCustomersSort(self):
        inviteCustomer = InviteCustomers('./customers.txt')
        inviteCustomer.getCustomers()
        inviteCustomer.sortCustomers()
        self.assertTrue(all( inviteCustomer.invitables[i] < inviteCustomer.invitables[i+1] for i in range(len(inviteCustomer.invitables) - 1)))

if __name__ == "__main__":
    unittest.main()
