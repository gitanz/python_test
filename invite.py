import abc
import json

from file import JsonTextFile
from customer import Customer
from address import Address
from template import InvitationTemplate, InviteNotificationTemplate

class InvitableInterface:

    @abc.abstractclassmethod
    def inviteToOffice(self):
        pass
    
"""
    Attaches customers 
"""
class InviteCustomers(JsonTextFile, InvitableInterface):

    invitables = []

    def __init__(self, fileLocation):
        super().__init__(fileLocation)
    
    def getCustomers(self, withinKm=100):
        for customer in self.readJsonTextLine():
            customer = Customer(customer['user_id'], customer['name'], Address(customer['latitude'], customer['longitude']))
            if customer.distance <= withinKm:
                self.attachCustomers(customer)

    def attachCustomers(self, customer):
        self.invitables.append(customer)

    def sortCustomers(self):
        self.invitables.sort(key = lambda invitable: invitable.id)
        
    def inviteToOffice(self):
        self.sortCustomers()
        # output = open('output.txt', 'a')
        for customer in self.invitables:
            notify = Notification(InviteNotificationTemplate(customer))
            notificationText = notify.notifyToInvite()
            # output.writelines(notificationText+"\n")
        # output.close

    
"""
    Dispatch invite notification
"""
class Notification:

    def __init__(self, template:InvitationTemplate):
        self.template = template
        self.template.writeGreeting()
        self.template.writeInvitationText()
        self.template.writeRegards()

    def notifyToInvite(self):
        text =  self.template.inviteText['text'] 
        print(json.dumps(text))
        return json.dumps(text)

    