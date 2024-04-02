'''
Team: Duces
Ethan - Tafi
James - Santi
Rex - chips
Kaitlyn - Concatakaitlyn
Jack - Ninja
Mason Dalton - Maestro Helper
'''
# A program to take burger orders and display the customers with their total number of burgers

import random

# Order Class 
class Order() :
    def __init__(self) :
        self.burger_count = self.randomBurgers()
        
    def randomBurgers(self):
        return random.randint(1, 20)

# Person Class 
class Person() :
    def __init__(self) :
        self.customer_name = self.randomName()
        
    def randomName(self) :
        self.lstCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Man", "Singing Bush"]
        return random.choice(self.lstCustomers)

# Customer Class, inheriting from person. 
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()

# Declare Queue list variable and customer dictionary variable
lstQueue = []
dictCustomer = {}

# Loop to create a 100 orders 
    # Add customer objects to the Queue.    
for iCount in range(0, 100):
    oCustomer = Customer()
    lstQueue.append(oCustomer)
    
    # Add object key (name) value (burger) to dictionary
    if oCustomer.customer_name in dictCustomer:
        dictCustomer[oCustomer.customer_name] += oCustomer.order.burger_count
    else :
        dictCustomer[oCustomer.customer_name] = oCustomer.order.burger_count

# Now remove each order in queue as if they were processed by FIFO 
for customer in lstQueue :
    lstQueue.pop(0)
    
# Create sorted list from dictionary with Code at bottom of document. 
listSortedCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True)

# Loop through the sorted list and print the values. 
for customer in listSortedCustomers:
    print(customer[0].ljust(19), customer[1])