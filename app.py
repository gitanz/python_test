from invite import InviteCustomers

"""
Main app
    - get customers from file, 
    - filter those who are within 100km 
    - invite them
"""
if __name__ == "__main__":
    process = InviteCustomers('./customers.txt')
    process.getCustomers(withinKm=100)
    process.inviteToOffice()
