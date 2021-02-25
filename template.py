import abc
class InvitationTemplate:

    @abc.abstractmethod
    def writeGreeting(self):
        pass

    @abc.abstractmethod
    def writeInvitationText(self):
        pass
    
    @abc.abstractmethod
    def writeRegards(self):
        pass


class InviteNotificationTemplate(InvitationTemplate):

    inviteText = {}

    def __init__(self, inviatable):
        self.inviatable = inviatable

    def writeGreeting(self):
        self.inviteText['greeting'] = 'Hello, '
    
    def writeInvitationText(self):
        self.inviteText['text'] =    { "name": self.inviatable.name,\
                                    "id": str(self.inviatable.id),\
                                    "distance": str(round(self.inviatable.distance, 2)) + "km" }

    def writeRegards(self):
        self.inviteText['regards'] = " Regards \n"
